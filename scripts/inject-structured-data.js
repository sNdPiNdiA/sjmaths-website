// inject-structured-data.js
//
// Injects JSON-LD structured data (schema.org) into HTML pages:
//   1. FAQPage schema for maths chapter pages (from chapter JSON Q&A data)
//   2. BreadcrumbList schema for all indexable pages
//   3. Course/LearningResource schema for educational content
//
// Usage: node scripts/inject-structured-data.js [--dry-run]

const fs = require('fs');
const path = require('path');
const { isHighConfidenceIndexPath, normalizePath, toUrl, DOMAIN } = require('./seo-policy');

const ROOT_DIR = path.resolve(__dirname, '..');
const DRY_RUN = process.argv.includes('--dry-run');

const SD_START = '<!-- STRUCTURED_DATA_START -->';
const SD_END = '<!-- STRUCTURED_DATA_END -->';

const stats = { processed: 0, injected: 0, skipped: 0, errors: 0 };

// ─── Utility ────────────────────────────────────────────────────

function stripHtml(html) {
  return html
    .replace(/<[^>]+>/g, ' ')
    .replace(/&nbsp;/gi, ' ')
    .replace(/&amp;/gi, '&')
    .replace(/&lt;/gi, '<')
    .replace(/&gt;/gi, '>')
    .replace(/&quot;/gi, '"')
    .replace(/&#39;/gi, "'")
    .replace(/\*\*/g, '')
    .replace(/\s+/g, ' ')
    .trim();
}

function stripOldStructuredData(html) {
  const startIdx = html.indexOf(SD_START);
  const endIdx = html.indexOf(SD_END);
  if (startIdx === -1 || endIdx === -1) return html;
  return html.slice(0, startIdx) + html.slice(endIdx + SD_END.length);
}

function readJsonSafe(filePath) {
  try {
    return JSON.parse(fs.readFileSync(filePath, 'utf8'));
  } catch {
    return null;
  }
}

function extractTitle(html) {
  const match = html.match(/<title>\s*([^<]+?)\s*<\/title>/i);
  return match ? match[1].replace(/\s+/g, ' ').trim() : '';
}

function extractDescription(html) {
  const match = html.match(/<meta[^>]+name=["']description["'][^>]+content=["']([^"']+)["']/i);
  return match ? match[1].trim() : '';
}

// ─── Schema Builders ────────────────────────────────────────────

function buildBreadcrumbSchema(relativePath) {
  const parts = relativePath.replace(/\/index\.html$/, '').replace(/\.html$/, '').split('/');
  const items = [{ name: 'Home', url: DOMAIN + '/' }];

  let accumulated = '';
  for (let i = 0; i < parts.length; i++) {
    accumulated += '/' + parts[i];
    const name = parts[i]
      .replace(/-/g, ' ')
      .replace(/_/g, ' ')
      .replace(/\b\w/g, c => c.toUpperCase());
    const url = DOMAIN + accumulated + (i < parts.length - 1 || relativePath.endsWith('index.html') ? '/' : '.html');
    items.push({ name, url });
  }

  return {
    '@context': 'https://schema.org',
    '@type': 'BreadcrumbList',
    'itemListElement': items.map((item, idx) => ({
      '@type': 'ListItem',
      'position': idx + 1,
      'name': item.name,
      'item': item.url,
    })),
  };
}

function buildFaqSchema(data) {
  const faqItems = [];

  if (!data.concepts) return null;

  for (const concept of data.concepts) {
    // Use practice questions as FAQ items
    if (concept.practice) {
      for (const q of concept.practice.slice(0, 3)) {
        const question = stripHtml(q.question);
        const answer = q.options?.[q.correctIndex] || '';
        const solution = q.solution ? ' ' + stripHtml(q.solution) : '';
        if (question && answer) {
          faqItems.push({
            '@type': 'Question',
            'name': question,
            'acceptedAnswer': {
              '@type': 'Answer',
              'text': answer + '.' + solution,
            },
          });
        }
      }
    }
  }

  if (faqItems.length === 0) return null;

  return {
    '@context': 'https://schema.org',
    '@type': 'FAQPage',
    'mainEntity': faqItems.slice(0, 10), // Max 10 FAQ items
  };
}

function buildCourseSchema(title, description, url) {
  return {
    '@context': 'https://schema.org',
    '@type': 'Course',
    'name': title,
    'description': description,
    'provider': {
      '@type': 'Organization',
      'name': 'SJMaths',
      'sameAs': DOMAIN,
    },
    'url': url,
    'isAccessibleForFree': true,
    'inLanguage': 'en',
  };
}

function buildLearningResourceSchema(title, description, url) {
  return {
    '@context': 'https://schema.org',
    '@type': 'LearningResource',
    'name': title,
    'description': description,
    'provider': {
      '@type': 'Organization',
      'name': 'SJMaths',
      'sameAs': DOMAIN,
    },
    'url': url,
    'isAccessibleForFree': true,
    'inLanguage': 'en',
    'educationalLevel': 'intermediate',
  };
}

// ─── Processing ─────────────────────────────────────────────────

function injectSchemas(htmlPath, schemas) {
  let html = fs.readFileSync(htmlPath, 'utf8');
  html = stripOldStructuredData(html);

  const scriptTags = schemas
    .filter(Boolean)
    .map(schema => `<script type="application/ld+json">\n${JSON.stringify(schema, null, 2)}\n</script>`)
    .join('\n');

  if (!scriptTags) return false;

  const block = `${SD_START}\n${scriptTags}\n${SD_END}`;

  // Insert before </head>
  const headClose = html.indexOf('</head>');
  if (headClose === -1) return false;

  html = html.slice(0, headClose) + block + '\n' + html.slice(headClose);

  if (!DRY_RUN) {
    fs.writeFileSync(htmlPath, html, 'utf8');
  }
  return true;
}

function processChapterPages() {
  const classPattern = /^class-(?:9|10|11|12)-maths$/;
  const dirs = fs.readdirSync(ROOT_DIR).filter(d =>
    classPattern.test(d) && fs.statSync(path.join(ROOT_DIR, d)).isDirectory()
  );

  for (const classDir of dirs) {
    const classPath = path.join(ROOT_DIR, classDir);
    const files = fs.readdirSync(classPath);

    for (const file of files) {
      if (!/^chapter-\d+-.*\.html$/.test(file)) continue;

      const htmlPath = path.join(classPath, file);
      const relativePath = normalizePath(htmlPath, ROOT_DIR);
      const chapterNum = file.match(/chapter-(\d+)/)?.[1];
      if (!chapterNum) continue;

      stats.processed++;

      const html = fs.readFileSync(htmlPath, 'utf8');
      const title = extractTitle(html);
      const description = extractDescription(html);
      const url = toUrl(relativePath);

      const schemas = [buildBreadcrumbSchema(relativePath)];

      // Try to load chapter JSON for FAQ schema
      const jsonPath = path.join(classPath, `chapter-${chapterNum}-data.json`);
      if (fs.existsSync(jsonPath)) {
        const data = readJsonSafe(jsonPath);
        if (data) {
          const faqSchema = buildFaqSchema(data);
          if (faqSchema) schemas.push(faqSchema);
        }
      }

      // Course schema
      if (title) {
        schemas.push(buildCourseSchema(title, description || title, url));
      }

      if (injectSchemas(htmlPath, schemas)) {
        stats.injected++;
        console.log(`✅ ${relativePath}`);
      } else {
        stats.skipped++;
      }
    }
  }
}

function processTopicPages(baseDir, sectionLabel) {
  if (!fs.existsSync(baseDir)) return;

  function walk(dir, depth) {
    const entries = fs.readdirSync(dir, { withFileTypes: true });
    for (const entry of entries) {
      if (entry.isDirectory() && entry.name !== 'hi' && entry.name !== 'node_modules' && !entry.name.startsWith('.')) {
        walk(path.join(dir, entry.name), depth + 1);
      }
    }

    if (depth < 2) return;

    const indexPath = path.join(dir, 'index.html');
    if (!fs.existsSync(indexPath)) return;

    const relativePath = normalizePath(indexPath, ROOT_DIR);
    if (!isHighConfidenceIndexPath(relativePath)) return;

    stats.processed++;

    const html = fs.readFileSync(indexPath, 'utf8');
    const title = extractTitle(html);
    const description = extractDescription(html);
    const url = toUrl(relativePath);

    const schemas = [
      buildBreadcrumbSchema(relativePath),
      title ? buildLearningResourceSchema(title, description || title, url) : null,
    ];

    if (injectSchemas(indexPath, schemas)) {
      stats.injected++;
    } else {
      stats.skipped++;
    }
  }

  console.log(`\n=== ${sectionLabel} ===`);
  walk(baseDir, 0);
  console.log(`  Processed topic pages in ${sectionLabel}`);
}

// ─── Main ───────────────────────────────────────────────────────

function main() {
  console.log(`${DRY_RUN ? '[dry-run] ' : ''}Injecting structured data...\n`);

  console.log('=== Maths Chapter Pages ===');
  processChapterPages();

  processTopicPages(path.join(ROOT_DIR, 'ahc-ro-aro'), 'AHC RO ARO');
  processTopicPages(path.join(ROOT_DIR, 'upsc'), 'UPSC');

  console.log('\n─── Summary ───');
  console.table(stats);
}

main();
