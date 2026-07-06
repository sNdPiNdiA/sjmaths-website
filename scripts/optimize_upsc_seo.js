const fs = require('fs');
const path = require('path');

const ROOT_DIR = path.join(__dirname, '..');
const UPSC_DIR = path.join(ROOT_DIR, 'upsc');

function getHtmlFiles(dir, fileList = []) {
  if (!fs.existsSync(dir)) return fileList;
  const files = fs.readdirSync(dir);
  for (const file of files) {
    const filePath = path.join(dir, file);
    const stat = fs.statSync(filePath);
    if (stat.isDirectory()) {
      getHtmlFiles(filePath, fileList);
    } else if (file.endsWith('.html')) {
      fileList.push(filePath);
    }
  }
  return fileList;
}

const allHtmlFiles = getHtmlFiles(UPSC_DIR);
console.log(`Found ${allHtmlFiles.length} UPSC HTML files to process.`);

let processedCount = 0;

for (const filePath of allHtmlFiles) {
  let html = fs.readFileSync(filePath, 'utf8');
  let modified = false;

  const relPath = path.relative(ROOT_DIR, filePath).replace(/\\/g, '/');
  const canonical = `https://sjmaths.com/${relPath}`;

  const isHindi = relPath.includes('/hi/') || relPath.endsWith('/hi/index.html');
  const dirParts = relPath.split('/');
  const subjectSlug = dirParts[1] || 'general_studies';
  const subjectName = subjectSlug.replace(/_/g, ' ').replace(/\b\w/g, c => c.toUpperCase());

  let topicName = '';
  const titleM = html.match(/<title[^>]*>(.*?)<\/title>/i);
  if (titleM) {
    topicName = titleM[1]
      .replace(/\s*-\s*UPSC.*$/i, '')
      .replace(/\s*\|\s*SJMaths/i, '')
      .trim();
  }

  if (!topicName || topicName.length < 3) {
    const folderName = dirParts[dirParts.length - 2] || 'notes';
    topicName = folderName.replace(/-/g, ' ').replace(/_/g, ' ').replace(/\b\w/g, c => c.toUpperCase());
  }

  const cleanTitle = isHindi
    ? `${topicName} - UPSC ${subjectName} नोट्स | SJMaths`
    : `${topicName} - UPSC ${subjectName} Study Notes | SJMaths`;

  // 1. Title Tag
  if (!titleM || titleM[1].length < 15 || titleM[1].includes('Updating')) {
    if (titleM) {
      html = html.replace(/<title[^>]*>(.*?)<\/title>/i, `<title>${cleanTitle}</title>`);
    } else if (html.includes('</head>')) {
      html = html.replace('</head>', `    <title>${cleanTitle}</title>\n</head>`);
    }
    modified = true;
  }

  // 2. Meta Description
  let descM = html.match(/<meta\s+name=["']description["']\s+content=["'](.*?)["']/i);
  let desc = descM ? descM[1].trim() : '';

  if (!desc || desc.length < 40 || desc.length > 170) {
    desc = isHindi
      ? `UPSC सिविल सेवा ${subjectName} परीक्षा की तैयारी के लिए ${topicName} के इंटरैक्टिव माइंडमैप्स और रिवीजन नोट्स SJMaths पर पढ़ें।`
      : `Explore interactive mindmaps, revision notes, and key facts for ${topicName} in UPSC Civil Services ${subjectName} preparation on SJMaths.`;

    if (descM) {
      html = html.replace(/<meta\s+name=["']description["']\s+content=["'](.*?)["']/i, `<meta name="description" content="${desc}">`);
    } else if (html.includes('</head>')) {
      html = html.replace('</head>', `    <meta name="description" content="${desc}">\n</head>`);
    }
    modified = true;
  }

  // 3. Robots Meta Tag
  if (!/<meta\s+name=["']robots["']/i.test(html)) {
    if (html.includes('</head>')) {
      html = html.replace('</head>', '    <meta name="robots" content="index, follow, max-image-preview:large">\n</head>');
      modified = true;
    }
  }

  // 4. Canonical Tag
  if (!/<link\s+rel=["']canonical["']/i.test(html)) {
    if (html.includes('</head>')) {
      html = html.replace('</head>', `    <link rel="canonical" href="${canonical}">\n</head>`);
      modified = true;
    }
  } else {
    html = html.replace(/<link\s+rel=["']canonical["']\s+href=["'](.*?)["']/i, `<link rel="canonical" href="${canonical}">`);
    modified = true;
  }

  // 5. Open Graph Meta Tags
  if (!/<meta\s+property=["']og:title["']/i.test(html)) {
    const currentTitle = (html.match(/<title[^>]*>(.*?)<\/title>/i) || [])[1] || cleanTitle;
    const ogBlock = `\n    <!-- Open Graph Social Meta -->\n` +
      `    <meta property="og:title" content="${currentTitle}">\n` +
      `    <meta property="og:description" content="${desc}">\n` +
      `    <meta property="og:type" content="article">\n` +
      `    <meta property="og:url" content="${canonical}">\n` +
      `    <meta property="og:image" content="https://sjmaths.com/assets/icons/icon-512x512.png">\n`;
    html = html.replace('</head>', `${ogBlock}</head>`);
    modified = true;
  }

  // 6. Twitter Card Meta Tags
  if (!/<meta\s+name=["']twitter:card["']/i.test(html)) {
    const currentTitle = (html.match(/<title[^>]*>(.*?)<\/title>/i) || [])[1] || cleanTitle;
    const twBlock = `\n    <!-- Twitter Card Meta -->\n` +
      `    <meta name="twitter:card" content="summary_large_image">\n` +
      `    <meta name="twitter:title" content="${currentTitle}">\n` +
      `    <meta name="twitter:description" content="${desc}">\n` +
      `    <meta name="twitter:image" content="https://sjmaths.com/assets/icons/icon-512x512.png">\n`;
    html = html.replace('</head>', `${twBlock}</head>`);
    modified = true;
  }

  // 7. JSON-LD Schema
  if (!html.includes('"BreadcrumbList"')) {
    const breadcrumbItems = [
      { "@type": "ListItem", "position": 1, "name": "Home", "item": "https://sjmaths.com/" },
      { "@type": "ListItem", "position": 2, "name": "UPSC IAS Prep", "item": "https://sjmaths.com/upsc/" },
      { "@type": "ListItem", "position": 3, "name": subjectName, "item": `https://sjmaths.com/upsc/${subjectSlug}/` },
      { "@type": "ListItem", "position": 4, "name": topicName, "item": canonical }
    ];

    const schemaGraph = [
      {
        "@type": "BreadcrumbList",
        "itemListElement": breadcrumbItems
      },
      {
        "@type": "LearningResource",
        "name": topicName,
        "description": desc,
        "learningResourceType": "Mindmap / Revision Notes",
        "educationalLevel": "UPSC Civil Services / IAS",
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

  // 8. Clean up duplicate stylesheet link tags if present
  if (html.includes('<link rel="stylesheet" href="/assets/css/mindmap.min.css?v=2055e39c">\n    <link rel="stylesheet" href="/assets/css/mindmap.min.css?v=2055e39c">')) {
    html = html.replace('<link rel="stylesheet" href="/assets/css/mindmap.min.css?v=2055e39c">\n    <link rel="stylesheet" href="/assets/css/mindmap.min.css?v=2055e39c">', '<link rel="stylesheet" href="/assets/css/mindmap.min.css?v=2055e39c">');
    modified = true;
  }

  // 9. Clean up any double closing brackets
  if (html.includes('">>')) {
    html = html.replaceAll('">>', '">');
    modified = true;
  }

  if (modified) {
    fs.writeFileSync(filePath, html, 'utf8');
    processedCount++;
  }
}

console.log(`🎉 Successfully optimized SEO, metadata, social cards, and schema across ${processedCount} UPSC pages.`);
