import fs from 'node:fs';
import path from 'node:path';

const patterns = {
  hasSiteFooter: 0,
  hasEmptyContainer: 0,
  hasFooterTag: 0,
  noFooterAtAll: 0
};

const sampleFooterTags = [];
const sampleNoFooter = [];

function scan(dir) {
  for (const item of fs.readdirSync(dir, { withFileTypes: true })) {
    if (['node_modules', '.git', '.pages-dist'].includes(item.name)) continue;
    const p = path.join(dir, item.name);
    if (item.isDirectory()) scan(p);
    else if (item.name.endsWith('.html')) {
      const c = fs.readFileSync(p, 'utf8');
      if (c.includes('site-footer')) {
        patterns.hasSiteFooter++;
      } else if (/<div id=["']footer-container["']>\s*<\/div>/i.test(c)) {
        patterns.hasEmptyContainer++;
      } else if (/<footer[\s>]/i.test(c)) {
        patterns.hasFooterTag++;
        if (sampleFooterTags.length < 15) {
          const m = c.match(/<footer[\s\S]*?<\/footer>/i);
          sampleFooterTags.push({ path: p, footerSnippet: m ? m[0].slice(0, 150) : '' });
        }
      } else {
        patterns.noFooterAtAll++;
        if (sampleNoFooter.length < 15) {
          sampleNoFooter.push(p);
        }
      }
    }
  }
}

scan('.');
console.log('Breakdown:', patterns);
console.log('\nSample with <footer ...> but not site-footer:');
sampleFooterTags.forEach(s => console.log(s.path, '-->', JSON.stringify(s.footerSnippet)));
console.log('\nSample with NO footer tag at all:');
sampleNoFooter.forEach(s => console.log(s));

