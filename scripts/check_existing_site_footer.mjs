import fs from 'node:fs';
import path from 'node:path';

let siteFooterCount = 0;
let siteFooterWithPrivacy = 0;
let siteFooterWithoutPrivacy = 0;

function scan(dir) {
  for (const item of fs.readdirSync(dir, { withFileTypes: true })) {
    if (['node_modules', '.git', '.pages-dist'].includes(item.name)) continue;
    const p = path.join(dir, item.name);
    if (item.isDirectory()) scan(p);
    else if (item.name.endsWith('.html')) {
      const c = fs.readFileSync(p, 'utf8');
      if (c.includes('id="site-footer"') || c.includes("id='site-footer'")) {
        siteFooterCount++;
        if (c.includes('privacy-policy.html') || c.includes('/privacy-policy/')) {
          siteFooterWithPrivacy++;
        } else {
          siteFooterWithoutPrivacy++;
        }
      }
    }
  }
}

scan('.');
console.log({ siteFooterCount, siteFooterWithPrivacy, siteFooterWithoutPrivacy });

