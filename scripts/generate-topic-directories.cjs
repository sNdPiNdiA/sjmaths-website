// Build missing navigation hubs from existing published topics; never invent lessons.
const fs = require('fs');
const path = require('path');
const policy = require('./seo-policy.cjs');
const { ROOT, siteFiles, escapeHtml: esc, compact, parse } = require('./seo-html.cjs');
const { createResolver } = require('./seo-routes.cjs');
const roots = {
  upsc: 'UPSC',
  'upsc-apfc': 'UPSC APFC',
  'upsc-aso': 'UPSC ASO',
  'ssc-cgl': 'SSC CGL',
  'upsssc-pet': 'UPSSSC PET',
  'upsssc-lower-mains': 'UPSSSC Lower Mains',
  'class-9-advanced-maths': 'Class 9 Advanced Maths',
};
const marker = '<!-- SJMaths generated topic directory -->';
const label = value => roots[value] || value.replace(/-/g, ' ').replace(/\b[a-z]/g, c => c.toUpperCase());
const pages = new Map();
const dirs = new Set();
const files = siteFiles();
const resolveUrl = createResolver(files);
for (const file of files) {
  if (!file.endsWith('.html') || !roots[file.split('/')[0]] || /\/hi\//.test(file)) continue;
  const source = fs.readFileSync(path.join(ROOT, file), 'utf8');
  if (policy.hasNoindex(source) || policy.hasRedirect(source) || policy.isPlaceholderHtml(source) || resolveUrl(policy.toUrl(file)).redirect) continue;
  const $ = parse(source.slice(0, source.indexOf('</head>') + 7));
  pages.set(file, { title: compact($('title').first().text()).replace(/\s*(?:\||-)\s*(?:SJMaths|UPSC Prep|SSC CGL Prep).*$/i, ''), generated: source.includes(marker) });
  let dir = path.posix.dirname(file);
  while (dir !== '.') { dirs.add(dir); dir = path.posix.dirname(dir); }
}
let changed = 0;
for (const dir of [...dirs].sort((a, b) => b.length - a.length)) {
  const file = `${dir}/index.html`;
  if (fs.existsSync(path.join(ROOT, file)) && !pages.get(file)?.generated) continue;
  const course = roots[dir.split('/')[0]];
  const name = label(path.posix.basename(dir));
  const title = `${name === course ? course : name + ' — ' + course} Topics | SJMaths`;
  const url = policy.toUrl(file);
  const items = [];
  for (const child of [...dirs].filter(d => path.posix.dirname(d) === dir).sort()) {
    const childFile = child + '/index.html';
    if (fs.existsSync(path.join(ROOT, childFile)) && !resolveUrl(policy.toUrl(childFile)).redirect) items.push({ url: policy.toUrl(childFile), name: label(path.posix.basename(child)) });
  }
  for (const [child, data] of pages) {
    if (path.posix.dirname(child) === dir && path.posix.basename(child) !== 'index.html') items.push({ url: policy.toUrl(child), name: data.title });
  }
  if (!items.length) continue;
  const description = `Browse ${name === course ? course : name + ' for ' + course}: ${items.length} topic links to SJMaths study notes and revision resources.`;
  const ancestors = [{ name: 'Home', url: policy.DOMAIN + '/' }];
  const parts = dir.split('/');
  for (let i = 1; i <= parts.length; i++) ancestors.push({ name: label(parts[i - 1]), url: policy.DOMAIN + '/' + parts.slice(0, i).join('/') + '/' });
  const schema = { '@context': 'https://schema.org', '@graph': [
    { '@type': 'CollectionPage', name: title, description, url },
    { '@type': 'BreadcrumbList', itemListElement: ancestors.map((a, i) => ({ '@type': 'ListItem', position: i + 1, name: a.name, item: a.url })) },
    { '@type': 'ItemList', itemListElement: items.map((a, i) => ({ '@type': 'ListItem', position: i + 1, name: a.name, url: a.url })) },
  ] };
  const html = `<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>${esc(title)}</title>
  <meta name="description" content="${esc(description)}">
  <meta name="robots" content="index, follow, max-image-preview:large">
  <link rel="canonical" href="${url}">
  <meta property="og:type" content="website">
  <meta property="og:title" content="${esc(title)}">
  <meta property="og:description" content="${esc(description)}">
  <meta property="og:url" content="${url}">
  <meta property="og:image" content="https://sjmaths.com/assets/icons/icon-512x512.png">
  <meta name="twitter:card" content="summary">
  <meta name="twitter:title" content="${esc(title)}">
  <meta name="twitter:description" content="${esc(description)}">
  <meta name="twitter:image" content="https://sjmaths.com/assets/icons/icon-512x512.png">
  <link rel="icon" href="/favicon.png">
  <link rel="stylesheet" href="/assets/vendor/fontawesome/css/all.min.css">
  <link rel="stylesheet" href="/assets/css/main.min.css">
  <link rel="stylesheet" href="/assets/css/layout.min.css">
  <link rel="stylesheet" href="/assets/css/component.min.css">
  <link rel="stylesheet" href="/assets/css/pages.min.css">
  <link rel="stylesheet" href="/assets/css/topic-directory.css">
  <script type="application/ld+json">${JSON.stringify(schema).replace(/</g, '\\u003c')}</script>
</head>
<body>
  ${marker}
  <a class="directory-skip" href="#main-content">Skip to topics</a>
  <div id="header-container"></div>
  <main class="topic-directory" id="main-content">
    <nav class="breadcrumbs" aria-label="Breadcrumb">${ancestors.map((a, i) => i === ancestors.length - 1 ? `<span aria-current="page">${esc(a.name)}</span>` : `<a href="${a.url}">${esc(a.name)}</a>`).join(' <span aria-hidden="true">›</span> ')}</nav>
    <div class="page-hero"><h1>${esc(name)}${name === course ? '' : ' — ' + esc(course)}</h1><p>${esc(description)}</p></div>
    <h2>Study topics</h2>
    <ul class="directory-topics">${items.map(a => `\n      <li><a href="${a.url}">${esc(a.name)}</a></li>`).join('')}
    </ul>
  </main>
  <div id="footer-container"></div>
  <script src="/assets/js/global-header.min.js" defer></script>
  <script src="/assets/js/global-footer.min.js" defer></script>
</body>
</html>
`;
  const target = path.join(ROOT, file);
  fs.mkdirSync(path.dirname(target), { recursive: true });
  if (!fs.existsSync(target) || fs.readFileSync(target, 'utf8') !== html) { fs.writeFileSync(target, html); changed++; }
  pages.set(file, { title, generated: true });
}
console.log(`Updated ${changed} topic directories from existing content.`);
