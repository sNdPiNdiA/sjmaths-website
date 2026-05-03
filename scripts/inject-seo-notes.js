/**
 * inject-seo-notes.js
 * 
 * Injects OG tags, Twitter Card meta, JSON-LD (BreadcrumbList + Article),
 * and author meta into all chapter-wise-notes pages that are missing them.
 * 
 * Usage: node scripts/inject-seo-notes.js
 *        node scripts/inject-seo-notes.js --dry-run   (preview only)
 */

const fs = require('fs');
const path = require('path');

const ROOT_DIR = path.resolve(__dirname, '..');
const DOMAIN = 'https://sjmaths.com';
const DRY_RUN = process.argv.includes('--dry-run');

// Map of class directories to their display names and educational levels
const CLASS_CONFIG = {
  'class-9-maths': { label: 'Class 9', level: 'Class 9' },
  'class-10-maths': { label: 'Class 10', level: 'Class 10' },
  'class-11-maths': { label: 'Class 11', level: 'Class 11' },
  'class-12-maths': { label: 'Class 12', level: 'Class 12' },
};

function extractTitle(html) {
  const match = html.match(/<title>([^<]+)<\/title>/i);
  return match ? match[1].trim() : '';
}

function extractDescription(html) {
  const match = html.match(/<meta\s+name="description"\s+content="([^"]+)"/i);
  return match ? match[1].trim() : '';
}

function extractCanonical(html) {
  const match = html.match(/<link\s+rel="canonical"\s+href="([^"]+)"/i);
  return match ? match[1].trim() : '';
}

function hasOGTags(html) {
  return /property="og:title"/.test(html);
}

function hasTwitterCard(html) {
  return /name="twitter:card"/.test(html);
}

function hasJSONLD(html) {
  return /application\/ld\+json/.test(html);
}

function buildChapterName(dirName) {
  // e.g., "chapter-6-perimeter-and-area" → "Perimeter and Area"
  const parts = dirName.replace(/^chapter-\d+-/, '');
  return parts
    .split('-')
    .map(w => w.charAt(0).toUpperCase() + w.slice(1))
    .join(' ');
}

function buildChapterNumber(dirName) {
  const match = dirName.match(/^chapter-(\d+)/);
  return match ? parseInt(match[1], 10) : 0;
}

function buildSEOBlock(title, description, canonicalUrl, classKey, chapterDir) {
  const config = CLASS_CONFIG[classKey];
  const chapterName = buildChapterName(chapterDir);
  const today = new Date().toISOString().slice(0, 10);

  const ogBlock = `
    <!-- Open Graph -->
    <meta property="og:title" content="${escapeAttr(title)}">
    <meta property="og:description" content="${escapeAttr(description)}">
    <meta property="og:type" content="article">
    <meta property="og:url" content="${canonicalUrl}">
    <meta property="og:image" content="${DOMAIN}/assets/icons/icon-512x512.png">
    <meta property="og:site_name" content="SJMaths">`;

  const twitterBlock = `
    <!-- Twitter Card -->
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="${escapeAttr(title)}">
    <meta name="twitter:description" content="${escapeAttr(description)}">
    <meta name="twitter:image" content="${DOMAIN}/assets/icons/icon-512x512.png">`;

  const authorBlock = `
    <meta name="author" content="SJMaths – Sandeep Jaiswal (PGT Maths)">
    <meta name="robots" content="index, follow">`;

  const jsonLD = `
    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@graph": [
        {
          "@type": "BreadcrumbList",
          "itemListElement": [
            {"@type":"ListItem","position":1,"name":"Home","item":"${DOMAIN}/"},
            {"@type":"ListItem","position":2,"name":"${config.label}","item":"${DOMAIN}/${classKey}/"},
            {"@type":"ListItem","position":3,"name":"Chapter Notes","item":"${DOMAIN}/${classKey}/chapter-wise-notes/"},
            {"@type":"ListItem","position":4,"name":"${escapeJSON(chapterName)}","item":"${canonicalUrl}"}
          ]
        },
        {
          "@type": "Article",
          "headline": "${escapeJSON(title)}",
          "description": "${escapeJSON(description)}",
          "author": {"@type":"Person","name":"Sandeep Jaiswal"},
          "publisher": {"@type":"Organization","name":"SJMaths","url":"${DOMAIN}"},
          "datePublished": "${today}",
          "educationalLevel": "${config.level}",
          "inLanguage": "en",
          "isAccessibleForFree": true,
          "url": "${canonicalUrl}"
        }
      ]
    }
    </script>`;

  return ogBlock + twitterBlock + authorBlock + jsonLD;
}

function escapeAttr(str) {
  return str.replace(/&/g, '&amp;').replace(/"/g, '&quot;');
}

function escapeJSON(str) {
  return str.replace(/\\/g, '\\\\').replace(/"/g, '\\"');
}

function processFile(filePath, classKey, chapterDir) {
  let html = fs.readFileSync(filePath, 'utf8');

  // Skip if already has OG tags
  if (hasOGTags(html)) {
    console.log(`  ⏭ Already has OG tags: ${chapterDir}`);
    return false;
  }

  const title = extractTitle(html);
  const description = extractDescription(html);
  const canonical = extractCanonical(html);

  if (!title || !description || !canonical) {
    console.log(`  ⚠ Missing title/description/canonical: ${chapterDir}`);
    return false;
  }

  const seoBlock = buildSEOBlock(title, description, canonical, classKey, chapterDir);

  // Insert before </head>
  const insertPoint = html.lastIndexOf('</head>');
  if (insertPoint === -1) {
    console.log(`  ⚠ No </head> found: ${chapterDir}`);
    return false;
  }

  html = html.slice(0, insertPoint) + seoBlock + '\n' + html.slice(insertPoint);

  if (DRY_RUN) {
    console.log(`  🔍 [DRY RUN] Would update: ${chapterDir}`);
  } else {
    fs.writeFileSync(filePath, html, 'utf8');
    console.log(`  ✅ Updated: ${chapterDir}`);
  }

  return true;
}

function main() {
  console.log(`\n🔧 SEO Injection for Chapter Notes Pages${DRY_RUN ? ' (DRY RUN)' : ''}\n`);

  let totalUpdated = 0;
  let totalSkipped = 0;

  for (const [classKey, config] of Object.entries(CLASS_CONFIG)) {
    const notesDir = path.join(ROOT_DIR, classKey, 'chapter-wise-notes');

    if (!fs.existsSync(notesDir)) {
      console.log(`📁 ${config.label}: No chapter-wise-notes directory found`);
      continue;
    }

    console.log(`📁 ${config.label}:`);

    const chapters = fs.readdirSync(notesDir, { withFileTypes: true })
      .filter(d => d.isDirectory() && d.name.startsWith('chapter-'))
      .sort((a, b) => {
        const numA = buildChapterNumber(a.name);
        const numB = buildChapterNumber(b.name);
        return numA - numB;
      });

    for (const chapter of chapters) {
      const indexPath = path.join(notesDir, chapter.name, 'index.html');
      if (!fs.existsSync(indexPath)) {
        console.log(`  ⚠ No index.html: ${chapter.name}`);
        totalSkipped++;
        continue;
      }

      const updated = processFile(indexPath, classKey, chapter.name);
      if (updated) totalUpdated++;
      else totalSkipped++;
    }

    console.log('');
  }

  console.log(`\n📊 Summary: ${totalUpdated} updated, ${totalSkipped} skipped`);
  if (DRY_RUN) {
    console.log('💡 Run without --dry-run to apply changes.');
  }
}

main();
