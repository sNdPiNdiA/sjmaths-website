const fs = require('fs');
const path = require('path');

const ROOT_DIR = path.join(__dirname, '..');
const CLASS10_DIR = path.join(ROOT_DIR, 'class-10-maths');

function getHtmlFiles(dir, fileList = []) {
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

const allHtmlFiles = getHtmlFiles(CLASS10_DIR);

let totalFixed = 0;

for (const filePath of allHtmlFiles) {
  let html = fs.readFileSync(filePath, 'utf8');
  let modified = false;

  const relPath = path.relative(ROOT_DIR, filePath).replace(/\\/g, '/');

  // Skip redirect files
  if (/<meta\s+name=["']robots["']\s+content=["'][^"']*noindex/i.test(html) || /http-equiv=["']refresh["']/i.test(html)) {
    continue;
  }

  // Extract canonical
  const canonicalM = html.match(/<link\s+rel=["']canonical["']\s+href=["'](.*?)["']/i);
  let canonical = canonicalM ? canonicalM[1].trim() : `https://sjmaths.com/${relPath}`;

  // Extract Title
  let titleM = html.match(/<title[^>]*>(.*?)<\/title>/i);
  let title = titleM ? titleM[1].trim() : '';

  if (title.length < 25) {
    if (title.includes('Ogive PYQs')) {
      const newTitle = 'Class 10 Statistics Ogive Curve PYQs & Solutions | SJMaths';
      html = html.replace(/<title[^>]*>(.*?)<\/title>/i, `<title>${newTitle}</title>`);
      title = newTitle;
      modified = true;
    }
  }

  // Extract Description
  let descM = html.match(/<meta\s+name=["']description["']\s+content=["'](.*?)["']/i);
  let desc = descM ? descM[1].trim() : `Study ${title.replace(/\s*\|\s*SJMaths/i, '')} for Class 10 CBSE Maths on SJMaths.`;

  // Fix JSON-LD Schema
  const jsonLdMatch = html.match(/<script\s+type=["']application\/ld\+json["']>([\s\S]*?)<\/script>/gi);

  let needsSchemaUpdate = false;
  if (!jsonLdMatch) {
    needsSchemaUpdate = true;
  } else {
    // Check if BreadcrumbList or LearningResource is missing in existing JSON-LD
    let hasBreadcrumb = false;
    let hasEdu = false;
    for (const block of jsonLdMatch) {
      if (block.includes('BreadcrumbList')) hasBreadcrumb = true;
      if (['Course', 'LearningResource', 'FAQPage', 'Article', 'EducationalOccupationalCredential'].some(t => block.includes(t))) {
        hasEdu = true;
      }
    }
    if (!hasBreadcrumb || !hasEdu) {
      needsSchemaUpdate = true;
    }
  }

  if (needsSchemaUpdate) {
    const breadcrumbItems = [
      { "@type": "ListItem", "position": 1, "name": "Home", "item": "https://sjmaths.com/" },
      { "@type": "ListItem", "position": 2, "name": "Class 10 Maths", "item": "https://sjmaths.com/class-10-maths/" },
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
        "learningResourceType": "Practice Problem / Study Material",
        "educationalLevel": "Class 10 CBSE",
        "url": canonical
      }
    ];

    const fullSchema = {
      "@context": "https://schema.org",
      "@graph": schemaGraph
    };

    const scriptBlock = `\n    <!-- Comprehensive Structured Data (JSON-LD) -->\n    <script type="application/ld+json">\n${JSON.stringify(fullSchema, null, 2)}\n    </script>\n`;

    if (html.includes('</head>')) {
      html = html.replace('</head>', `${scriptBlock}</head>`);
      modified = true;
    }
  }

  if (modified) {
    fs.writeFileSync(filePath, html, 'utf8');
    totalFixed++;
  }
}

console.log(`🎉 Final Class 10 SEO Polish complete. Updated ${totalFixed} files.`);
