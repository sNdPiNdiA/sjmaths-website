const fs = require('fs');
const path = require('path');

const ROOT = path.resolve(__dirname, '..');

// Map of old long path -> clean short SEO path
const renames = [
  {
    oldPath: 'civics/democracy-and-decentralization/panchayati-raj-and-local-governance',
    newPath: 'civics/panchayati-raj',
    title: 'Democratic Decentralization and Panchayati Raj',
    sectionName: 'Democracy and Decentralization'
  },
  {
    oldPath: 'civics/union-government/executive/prime-minister-and-council-of-ministers',
    newPath: 'civics/union-government/prime-minister-and-cabinet',
    title: 'Prime Minister and Union Council of Ministers',
    sectionName: 'Union Government'
  },
  {
    oldPath: 'civics/government/forms/parliamentary-and-presidential',
    newPath: 'civics/forms-of-government/parliamentary-vs-presidential',
    title: 'Parliamentary and Presidential Government',
    sectionName: 'Government and Its Organs'
  },
  {
    oldPath: 'civics/government/forms/unitary-and-federal',
    newPath: 'civics/forms-of-government/unitary-vs-federal',
    title: 'Unitary and Federal Government',
    sectionName: 'Government and Its Organs'
  },
  {
    oldPath: 'civics/government/organs',
    newPath: 'civics/organs-of-government',
    title: 'Organs of Government: Legislature, Executive and Judiciary',
    sectionName: 'Government and Its Organs'
  },
  {
    oldPath: 'civics/indian-administration/lokpal-and-lokayukta',
    newPath: 'civics/lokpal-and-lokayukta',
    title: 'Ombudsman, Lokpal and Lokayukta',
    sectionName: 'Political Organization and Indian Administration'
  },
  {
    oldPath: 'civics/elections/reforms-and-voting-behaviour',
    newPath: 'civics/elections/electoral-reforms',
    title: 'Electoral Reforms and Voting Behaviour',
    sectionName: 'Elections and Political Behaviour'
  }
];

// 1. Move and rewrite HTML for each renamed folder
for (const r of renames) {
  const oldDir = path.join(ROOT, r.oldPath);
  const newDir = path.join(ROOT, r.newPath);
  const oldHtmlFile = path.join(oldDir, 'index.html');
  const newHtmlFile = path.join(newDir, 'index.html');

  if (!fs.existsSync(oldHtmlFile)) {
    console.warn(`Old file not found: ${oldHtmlFile}`);
    continue;
  }

  let html = fs.readFileSync(oldHtmlFile, 'utf8');

  // Replace canonical and og:url / json-ld URLs with new URL
  const oldUrl = `https://sjmaths.com/${r.oldPath}/`;
  const newUrl = `https://sjmaths.com/${r.newPath}/`;

  html = html.split(oldUrl).join(newUrl);

  // Ensure new directory exists
  if (!fs.existsSync(newDir)) {
    fs.mkdirSync(newDir, { recursive: true });
  }

  // Write new HTML
  fs.writeFileSync(newHtmlFile, html, 'utf8');
  console.log(`Created: ${r.newPath}/index.html`);

  // Remove old folder
  fs.rmSync(oldDir, { recursive: true, force: true });
  console.log(`Deleted old: ${r.oldPath}`);

  // Clean up any empty parent directory left behind (e.g. civics/government/forms)
  let parent = path.dirname(oldDir);
  while (parent !== path.join(ROOT, 'civics') && fs.existsSync(parent) && fs.readdirSync(parent).length === 0) {
    fs.rmdirSync(parent);
    console.log(`Removed empty parent folder: ${path.relative(ROOT, parent)}`);
    parent = path.dirname(parent);
  }
}

// 2. Update up-tgt-social-science/index.html
const trackerPath = path.join(ROOT, 'up-tgt-social-science/index.html');
let trackerHtml = fs.readFileSync(trackerPath, 'utf8');

for (const r of renames) {
  const oldKey = r.oldPath;
  const newKey = r.newPath;
  const oldHref = `/${r.oldPath}/`;
  const newHref = `/${r.newPath}/`;

  trackerHtml = trackerHtml.split(`data-key="${oldKey}"`).join(`data-key="${newKey}"`);
  trackerHtml = trackerHtml.split(oldHref).join(newHref);
}

fs.writeFileSync(trackerPath, trackerHtml, 'utf8');
console.log('Updated up-tgt-social-science/index.html with new URLs.');

// 3. Update sitemap-main.xml
const sitemapPath = path.join(ROOT, 'sitemap-main.xml');
let sitemapXml = fs.readFileSync(sitemapPath, 'utf8');

for (const r of renames) {
  const oldUrl = `https://sjmaths.com/${r.oldPath}/`;
  const newUrl = `https://sjmaths.com/${r.newPath}/`;
  sitemapXml = sitemapXml.split(oldUrl).join(newUrl);
}

fs.writeFileSync(sitemapPath, sitemapXml, 'utf8');
console.log('Updated sitemap-main.xml with new URLs.');
