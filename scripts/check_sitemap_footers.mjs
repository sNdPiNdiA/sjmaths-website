import fs from 'node:fs';
import path from 'node:path';

const subSitemaps = [
  'sitemap-main.xml',
  'sitemap-class-10.xml',
  'sitemap-class-10-science.xml',
  'sitemap-class-10-social-science.xml',
  'sitemap-class-12.xml',
  'sitemap-class-9.xml',
  'sitemap-class-11.xml',
  'sitemap-class-11-applied-mathematics.xml',
  'sitemap-sat.xml',
  'sitemap-ssc-cgl.xml',
  'sitemap-upsssc-pet.xml'
];

let totalUrls = 0;
let fileFound = 0;
let fileMissing = 0;
let hasSiteFooter = 0;
let hasEmptyContainer = 0;
let hasOldFooter = 0;
let noFooter = 0;

for (const sm of subSitemaps) {
  if (!fs.existsSync(sm)) continue;
  const content = fs.readFileSync(sm, 'utf8');
  const locs = content.match(/<loc>(.*?)<\/loc>/g) || [];
  for (const l of locs) {
    totalUrls++;
    const url = l.replace(/<\/?loc>/g, '');
    let pathname = new URL(url).pathname;
    if (pathname.endsWith('/')) {
      pathname += 'index.html';
    } else if (!pathname.endsWith('.html')) {
      pathname += '.html';
    }
    const localPath = path.join(process.cwd(), pathname.replace(/^\//, '').replace(/\//g, path.sep));
    if (fs.existsSync(localPath)) {
      fileFound++;
      const html = fs.readFileSync(localPath, 'utf8');
      if (html.includes('id="site-footer"') || html.includes("id='site-footer'")) {
        hasSiteFooter++;
      } else if (/<div id=["']footer-container["']>\s*<\/div>/i.test(html)) {
        hasEmptyContainer++;
      } else if (/<footer[\s>]/i.test(html)) {
        hasOldFooter++;
      } else {
        noFooter++;
      }
    } else {
      fileMissing++;
    }
  }
}

console.log({
  totalUrls,
  fileFound,
  fileMissing,
  hasSiteFooter,
  hasEmptyContainer,
  hasOldFooter,
  noFooter
});

