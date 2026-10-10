const fs = require('fs');
const path = require('path');
const sscRoot = path.join(process.cwd(), 'ssc-cgl');

function walk(dir) {
  let files = [];
  for (const item of fs.readdirSync(dir)) {
    const full = path.join(dir, item);
    if (fs.statSync(full).isDirectory()) files = files.concat(walk(full));
    else if (item.endsWith('.html')) files.push(full);
  }
  return files;
}

const all = walk(sscRoot);
let noHeaderContainer = [];
let noGlobalHeader = [];
let noFooterContainer = [];
let noGlobalFooter = [];
let noMainContent = [];

for (const f of all) {
  const c = fs.readFileSync(f, 'utf8');
  const rel = path.relative(process.cwd(), f).replace(/\\/g, '/');
  if (!c.includes('header-container')) noHeaderContainer.push(rel);
  if (!c.includes('global-header')) noGlobalHeader.push(rel);
  if (!c.includes('footer-container')) noFooterContainer.push(rel);
  if (!c.includes('global-footer')) noGlobalFooter.push(rel);
  if (!c.includes('id="main-content"') && !c.includes("id='main-content'")) noMainContent.push(rel);
}

console.log('Total files:', all.length);
console.log('Missing header-container:', noHeaderContainer.length);
console.log('Missing global-header script:', noGlobalHeader.length);
console.log('Missing footer-container:', noFooterContainer.length);
console.log('Missing global-footer script:', noGlobalFooter.length);
console.log('Missing id=main-content:', noMainContent.length);

if (noFooterContainer.length) {
  console.log(`\nAll ${noFooterContainer.length} files missing footer-container:`);
  noFooterContainer.forEach(f => console.log('  ', f));
}

if (noGlobalFooter.length) {
  console.log(`\nAll ${noGlobalFooter.length} files missing global-footer:`);
  noGlobalFooter.forEach(f => console.log('  ', f));
}

if (noMainContent.length) {
  console.log(`\nAll ${noMainContent.length} files missing id=main-content:`);
  noMainContent.forEach(f => console.log('  ', f));
}
