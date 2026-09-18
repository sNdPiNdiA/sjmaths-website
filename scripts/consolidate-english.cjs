const fs = require('fs');
const path = require('path');

const config = JSON.parse(fs.readFileSync('scripts/english_consolidation_config.json', 'utf8'));

console.log(`Starting consolidation for ${config.length} target English modules...`);

config.forEach(item => {
  const targetDir = path.resolve(item.target);
  fs.mkdirSync(targetDir, { recursive: true });

  const targetHtml = path.join(targetDir, 'index.html');
  const canonicalUrl = `https://sjmaths.com/${item.target.replace(/\\/g, '/')}/`;

  // Pick first available source template
  let templateContent = '';
  for (const src of item.sources) {
    const srcHtml = path.join(src, 'index.html');
    if (fs.existsSync(srcHtml)) {
      templateContent = fs.readFileSync(srcHtml, 'utf8');
      break;
    }
  }

  if (templateContent) {
    let updatedHtml = templateContent
      .replace(/<title>.*?<\/title>/s, `<title>${item.title} — English Study Guide | SJ Maths</title>`)
      .replace(/<link rel="canonical" href=".*?">/, `<link rel="canonical" href="${canonicalUrl}">`)
      .replace(/<h1>.*?<\/h1>/s, `<h1>${item.title}</h1>`)
      .replace(/<meta property="og:url" content=".*?">/, `<meta property="og:url" content="${canonicalUrl}">`)
      .replace(/<meta property="og:title" content=".*?">/, `<meta property="og:title" content="${item.title} — English Study Guide">`)
      .replace(/<meta name="twitter:title" content=".*?">/, `<meta name="twitter:title" content="${item.title} — English Study Guide">`);

    fs.writeFileSync(targetHtml, updatedHtml, 'utf8');
    console.log(`✓ Created consolidated page: ${item.target}/index.html`);
  } else {
    console.warn(`! No source template found for: ${item.target}`);
  }

  // Remove old source directories
  item.sources.forEach(src => {
    const srcDir = path.resolve(src);
    if (srcDir !== targetDir && fs.existsSync(srcDir)) {
      fs.rmSync(srcDir, { recursive: true, force: true });
      console.log(`  Removed old source: ${src}`);
    }
  });
});

console.log('\nConsolidation of files completed successfully.');
