const fs = require('fs');
const path = require('path');

const ROOT_DIR = path.join(__dirname, '..');
const CLASS11_DIR = path.join(ROOT_DIR, 'class-11-maths');

const targetSubdirs = [
  path.join(CLASS11_DIR, 'ncert-exercise-practice'),
  path.join(CLASS11_DIR, 'ncert-exemplar-practice'),
  path.join(CLASS11_DIR, 'worksheets'),
  path.join(CLASS11_DIR, 'tests'),
  path.join(CLASS11_DIR, 'sample-papers')
];

function getHtmlFiles(dir, fileList = []) {
  if (!fs.existsSync(dir)) return fileList;
  const files = fs.readdirSync(dir);
  for (const file of files) {
    const filePath = path.join(dir, file);
    const stat = fs.statSync(filePath);
    if (stat.isDirectory()) {
      getHtmlFiles(filePath, fileList);
    } else if (file.endsWith('.html') && file !== 'index.html') {
      fileList.push(filePath);
    }
  }
  return fileList;
}

let unlockedFiles = [];
for (const sub of targetSubdirs) {
  unlockedFiles = getHtmlFiles(sub, unlockedFiles);
}

console.log(`Found ${unlockedFiles.length} Class 11 target pages to unlock for indexing.`);

let count = 0;

for (const filePath of unlockedFiles) {
  let html = fs.readFileSync(filePath, 'utf8');
  let modified = false;

  const relPath = path.relative(ROOT_DIR, filePath).replace(/\\/g, '/');
  const canonical = `https://sjmaths.com/${relPath}`;

  // 1. Remove noindex and set to index, follow
  if (/<meta\s+name=["']robots["']\s+content=["'][^"']*noindex/i.test(html)) {
    html = html.replace(
      /<meta\s+name=["']robots["']\s+content=["'][^"']*noindex[^"']*["']/i,
      '<meta name="robots" content="index, follow, max-image-preview:large">'
    );
    modified = true;
  } else if (!/<meta\s+name=["']robots["']/i.test(html)) {
    if (html.includes('</head>')) {
      html = html.replace('</head>', '    <meta name="robots" content="index, follow, max-image-preview:large">\n</head>');
      modified = true;
    }
  }

  // 2. Ensure canonical tag exists
  if (!/<link\s+rel=["']canonical["']/i.test(html)) {
    if (html.includes('</head>')) {
      html = html.replace('</head>', `    <link rel="canonical" href="${canonical}">\n</head>`);
      modified = true;
    }
  } else {
    html = html.replace(/<link\s+rel=["']canonical["']\s+href=["'](.*?)["']/i, `<link rel="canonical" href="${canonical}">`);
    modified = true;
  }

  // 3. Title Optimization
  let titleM = html.match(/<title[^>]*>(.*?)<\/title>/i);
  let title = titleM ? titleM[1].trim() : '';

  const filename = path.basename(filePath, '.html');
  const dirParts = relPath.split('/');
  const chapName = dirParts[dirParts.length - 2]
    .replace(/^chapter-\d+-?/, '')
    .replace(/-/g, ' ')
    .replace(/\b\w/g, c => c.toUpperCase());

  if (!title || title.length < 25 || title.includes('Updating')) {
    let cleanTitle = '';
    if (relPath.includes('ncert-exercise-practice')) {
      const exNum = filename.replace('exercise-', '').replace('-', '.');
      cleanTitle = `Class 11 Maths Chapter ${chapName} Exercise ${exNum} NCERT Solutions | SJMaths`;
    } else if (relPath.includes('ncert-exemplar-practice')) {
      const topicName = filename.replace(/-/g, ' ').replace(/\b\w/g, c => c.toUpperCase());
      cleanTitle = `Class 11 ${chapName} ${topicName} NCERT Exemplar Solutions | SJMaths`;
    } else if (relPath.includes('worksheets')) {
      const type = filename.replace(/-/g, ' ').replace(/\b\w/g, c => c.toUpperCase());
      cleanTitle = `Class 11 ${chapName} ${type} Worksheet Solutions | SJMaths`;
    } else if (relPath.includes('tests') || relPath.includes('sample-papers')) {
      const testName = filename.replace(/-/g, ' ').replace(/\b\w/g, c => c.toUpperCase());
      cleanTitle = `Class 11 ${chapName} ${testName} Online Test | SJMaths`;
    }

    if (cleanTitle) {
      if (titleM) {
        html = html.replace(/<title[^>]*>(.*?)<\/title>/i, `<title>${cleanTitle}</title>`);
      } else {
        html = html.replace('</head>', `    <title>${cleanTitle}</title>\n</head>`);
      }
      title = cleanTitle;
      modified = true;
    }
  }

  // 4. Meta Description Optimization
  let descM = html.match(/<meta\s+name=["']description["']\s+content=["'](.*?)["']/i);
  let desc = descM ? descM[1].trim() : '';

  if (!desc || desc.length < 50 || desc.length > 170) {
    const topicText = title.replace(/\s*\|\s*SJMaths/i, '');
    desc = `Practice ${topicText} for Class 11 CBSE Board exam preparation. Access step-by-step solutions, key formulas, and expert revision notes on SJMaths.`;
    if (descM) {
      html = html.replace(/<meta\s+name=["']description["']\s+content=["'](.*?)["']/i, `<meta name="description" content="${desc}">`);
    } else {
      html = html.replace('</head>', `    <meta name="description" content="${desc}">\n</head>`);
    }
    modified = true;
  }

  // 5. Open Graph Meta Tags
  if (!/<meta\s+property=["']og:title["']/i.test(html)) {
    const ogBlock = `\n    <!-- Open Graph Social Meta -->\n` +
      `    <meta property="og:title" content="${title}">\n` +
      `    <meta property="og:description" content="${desc}">\n` +
      `    <meta property="og:type" content="article">\n` +
      `    <meta property="og:url" content="${canonical}">\n` +
      `    <meta property="og:image" content="https://sjmaths.com/assets/icons/icon-512x512.png">\n`;
    html = html.replace('</head>', `${ogBlock}</head>`);
    modified = true;
  }

  // 6. Twitter Card Meta Tags
  if (!/<meta\s+name=["']twitter:card["']/i.test(html)) {
    const twBlock = `\n    <!-- Twitter Card Meta -->\n` +
      `    <meta name="twitter:card" content="summary_large_image">\n` +
      `    <meta name="twitter:title" content="${title}">\n` +
      `    <meta name="twitter:description" content="${desc}">\n` +
      `    <meta name="twitter:image" content="https://sjmaths.com/assets/icons/icon-512x512.png">\n`;
    html = html.replace('</head>', `${twBlock}</head>`);
    modified = true;
  }

  // 7. JSON-LD Schema
  if (!html.includes('"BreadcrumbList"')) {
    const breadcrumbItems = [
      { "@type": "ListItem", "position": 1, "name": "Home", "item": "https://sjmaths.com/" },
      { "@type": "ListItem", "position": 2, "name": "Class 11 Maths", "item": "https://sjmaths.com/class-11-maths/" },
      { "@type": "ListItem", "position": 3, "name": title.replace(/\s*\|\s*SJMaths/i, ''), "item": canonical }
    ];

    const schemaGraph = [
      {
        "@type": "BreadcrumbList",
        "itemListElement": breadcrumbItems
      },
      {
        "@type": "LearningResource",
        "name": title.replace(/\s*\|\s*SJMaths/i, ''),
        "description": desc,
        "learningResourceType": relPath.includes('tests') ? "Quiz" : "Practice Problem / Study Material",
        "educationalLevel": "Class 11 CBSE",
        "url": canonical
      }
    ];

    const fullSchema = {
      "@context": "https://schema.org",
      "@graph": schemaGraph
    };

    const scriptBlock = `\n    <!-- Structured Data (JSON-LD) -->\n    <script type="application/ld+json">\n${JSON.stringify(fullSchema, null, 2)}\n    </script>\n`;
    html = html.replace('</head>', `${scriptBlock}</head>`);
    modified = true;
  }

  // 8. Image lazy loading
  if (html.includes('<img') && !html.includes('loading="lazy"')) {
    html = html.replace(/<img(?![^>]*loading=)/gi, '<img loading="lazy"');
    modified = true;
  }

  if (modified) {
    fs.writeFileSync(filePath, html, 'utf8');
    count++;
  }
}

console.log(`🎉 Unlocked and SEO-optimized ${count} Class 11 pages for search indexation.`);
