const fs = require('fs');
const path = require('path');

const repoRoot = path.resolve(__dirname, '..');
const sscRoot = path.join(repoRoot, 'ssc-cgl');

console.log('Auditing SSC CGL files...');

function getAllFiles(dir, ext = '.html') {
  let results = [];
  const list = fs.readdirSync(dir);
  for (const file of list) {
    const full = path.join(dir, file);
    const stat = fs.statSync(full);
    if (stat && stat.isDirectory()) {
      results = results.concat(getAllFiles(full, ext));
    } else if (file.endsWith(ext)) {
      results.push(full);
    }
  }
  return results;
}

const htmlFiles = getAllFiles(sscRoot, '.html');
console.log(`Total HTML files in ssc-cgl: ${htmlFiles.length}`);

const brokenLinks = [];
const missingAssets = [];
const missingJson = [];
const layoutIssues = [];
const emptyBodyOrBrokenTags = [];

const subjectHubs = [
  'computer-knowledge',
  'english',
  'finance-economics',
  'general-awareness',
  'quantitative-aptitude',
  'reasoning',
  'statistics',
  'syllabus'
];

for (const filePath of htmlFiles) {
  const relPath = path.relative(repoRoot, filePath).replace(/\\/g, '/');
  const fileDir = path.dirname(filePath);
  const content = fs.readFileSync(filePath, 'utf8');

  // Check required containers
  if (!content.includes('header-container')) {
    layoutIssues.push({ file: relPath, issue: 'Missing header-container' });
  }
  if (!content.includes('footer-container')) {
    layoutIssues.push({ file: relPath, issue: 'Missing footer-container' });
  }
  if (!content.includes('id="main-content"') && !content.includes("id='main-content'")) {
    layoutIssues.push({ file: relPath, issue: 'Missing #main-content' });
  }

  // Check basic HTML tags
  if (!content.includes('<html') || !content.includes('</html>')) {
    emptyBodyOrBrokenTags.push({ file: relPath, issue: 'Missing html tags' });
  }
  if (!content.includes('<body') || !content.includes('</body>')) {
    emptyBodyOrBrokenTags.push({ file: relPath, issue: 'Missing body tags' });
  }

  // Check CSS links
  const cssMatches = content.matchAll(/<link[^>]+href=["']([^"']+\.css(\?[^"']*)?)["']/gi);
  for (const m of cssMatches) {
    const rawHref = m[1];
    if (rawHref.startsWith('http://') || rawHref.startsWith('https://') || rawHref.startsWith('//')) continue;
    const cleanHref = rawHref.split('?')[0];
    const target = cleanHref.startsWith('/')
      ? path.join(repoRoot, cleanHref.replace(/^\//, ''))
      : path.join(fileDir, cleanHref);
    if (!fs.existsSync(target)) {
      missingAssets.push({ file: relPath, asset: rawHref });
    }
  }

  // Check JS scripts
  const scriptMatches = content.matchAll(/<script[^>]+src=["']([^"']+\.js(\?[^"']*)?)["']/gi);
  for (const m of scriptMatches) {
    const rawSrc = m[1];
    if (rawSrc.startsWith('http://') || rawSrc.startsWith('https://') || rawSrc.startsWith('//')) continue;
    const cleanSrc = rawSrc.split('?')[0];
    const target = cleanSrc.startsWith('/')
      ? path.join(repoRoot, cleanSrc.replace(/^\//, ''))
      : path.join(fileDir, cleanSrc);
    if (!fs.existsSync(target)) {
      missingAssets.push({ file: relPath, asset: rawSrc });
    }
  }

  // Check fetch json
  const fetchMatches = content.matchAll(/fetch\(["']([^"']+\.json(\?[^"']*)?)["']/gi);
  for (const m of fetchMatches) {
    const rawJson = m[1];
    if (rawJson.startsWith('http://') || rawJson.startsWith('https://')) continue;
    const cleanJson = rawJson.split('?')[0];
    const target = cleanJson.startsWith('/')
      ? path.join(repoRoot, cleanJson.replace(/^\//, ''))
      : path.join(fileDir, cleanJson);
    if (!fs.existsSync(target)) {
      missingJson.push({ file: relPath, json: rawJson });
    }
  }

  // Check <a> links
  const linkMatches = content.matchAll(/<a[^>]+href=["']([^"']+)["']/gi);
  for (const m of linkMatches) {
    let href = m[1].trim();
    if (!href || href.startsWith('#') || href.startsWith('http://') || href.startsWith('https://') ||
        href.startsWith('mailto:') || href.startsWith('tel:') || href.startsWith('javascript:')) {
      continue;
    }
    const cleanHref = href.split('#')[0].split('?')[0];
    if (!cleanHref) continue;

    let target = cleanHref.startsWith('/')
      ? path.join(repoRoot, cleanHref.replace(/^\//, ''))
      : path.join(fileDir, cleanHref);

    if (fs.existsSync(target)) {
      if (fs.statSync(target).isDirectory() && !fs.existsSync(path.join(target, 'index.html'))) {
        brokenLinks.push({ file: relPath, href, error: 'Directory missing index.html' });
      }
    } else {
      if (fs.existsSync(target + '.html')) {
        // ok
      } else if (fs.existsSync(path.join(target, 'index.html'))) {
        // ok
      } else {
        brokenLinks.push({ file: relPath, href, error: 'Target file/dir does not exist' });
      }
    }
  }
}

console.log('\n--- AUDIT RESULTS ---');
console.log(`1. Broken Links: ${brokenLinks.length}`);
brokenLinks.slice(0, 30).forEach(b => console.log(`  [${b.file}] ${b.href} -> ${b.error}`));
if (brokenLinks.length > 30) console.log(`  ... and ${brokenLinks.length - 30} more`);

console.log(`\n2. Missing Assets (CSS/JS): ${missingAssets.length}`);
missingAssets.slice(0, 20).forEach(a => console.log(`  [${a.file}] ${a.asset}`));

console.log(`\n3. Missing JSON: ${missingJson.length}`);
missingJson.slice(0, 20).forEach(j => console.log(`  [${j.file}] ${j.json}`));

console.log(`\n4. Layout Issues: ${layoutIssues.length}`);
layoutIssues.forEach(l => console.log(`  [${l.file}] ${l.issue}`));

console.log(`\n5. Broken HTML/Body tags: ${emptyBodyOrBrokenTags.length}`);
emptyBodyOrBrokenTags.slice(0, 20).forEach(e => console.log(`  [${e.file}] ${e.issue}`));

// Detailed check on Main Index & Subject Hubs
console.log('\n--- CHECKING SUBJECT HUBS & TOPIC TILES ---');
const allHubs = [
  'index.html',
  ...subjectHubs.map(h => `${h}/index.html`)
];

for (const hubRel of allHubs) {
  const hubPath = path.join(sscRoot, hubRel);
  const exists = fs.existsSync(hubPath);
  console.log(`\nHub ${hubRel}: ${exists ? 'EXISTS' : 'MISSING'}`);
  if (exists) {
    const hubContent = fs.readFileSync(hubPath, 'utf8');
    const links = [...hubContent.matchAll(/<a[^>]+href=["']([^"']+)["']/gi)].map(m => m[1]);
    const broken = [];
    for (const href of links) {
      if (href.startsWith('#') || href.startsWith('http') || href.startsWith('mailto') || href.startsWith('tel') || href.startsWith('javascript')) continue;
      const clean = href.split('#')[0].split('?')[0];
      if (!clean) continue;
      const target = clean.startsWith('/')
        ? path.join(repoRoot, clean.replace(/^\//, ''))
        : path.join(path.dirname(hubPath), clean);
      if (!fs.existsSync(target) && !fs.existsSync(target + '.html') && !fs.existsSync(path.join(target, 'index.html'))) {
        broken.push(href);
      }
    }
    console.log(`  -> ${links.length} total links | Broken: ${broken.length}`);
    if (broken.length) {
      broken.forEach(b => console.log(`     BROKEN: ${b}`));
    }
  }
}
