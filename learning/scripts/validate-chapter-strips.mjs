// Validates the foundation-skill strips injected in the Class 10 mathematics index page
import { readFileSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import { dirname, join } from 'node:path';

const here = dirname(fileURLToPath(import.meta.url));
const html = readFileSync(join(here, '../topics/class-10/mathematics/index.html'), 'utf8');
const loader = readFileSync(join(here, '../engine/topic-loader.js'), 'utf8');

// extract mapping from the injected script
const m = html.match(/const FOUNDATIONS_BY_CHAPTER = ({[\s\S]*?});/);
if (!m) { console.error('FAIL: FOUNDATIONS_BY_CHAPTER not found'); process.exit(1); }
const map = eval('(' + m[1] + ')');

let issues = 0, chips = 0;
for (let ch = 1; ch <= 14; ch++) {
  if (!html.includes(`id="ch-${ch}-card"`)) { console.log(`MISSING card ch-${ch}`); issues++; continue; }
  const mods = map[ch] || [];
  chips += mods.length;
  for (const [slug, label] of mods) {
    if (!loader.includes(`'${slug}':`) && !loader.includes(`'math-foundations-${slug}':`)) {
      console.log(`ch${ch}: UNREGISTERED ${slug}`); issues++;
    }
    if (!label.startsWith('M')) { console.log(`ch${ch}: odd label ${label}`); issues++; }
  }
}

// structural sanity
const structure = {
  'single </body>': (html.match(/<\/body>/g) || []).length === 1,
  'single </html>': (html.match(/<\/html>/g) || []).length === 1,
};
// real mojibake check: look for the classic double-encoded pairs
structure['no mojibake sigs'] = !/Ã¢|Ã°|Ã‚|â€|Â /.test(html);
structure['emoji strip title present'] = html.includes('\u{1F9F1}');
structure['arrows restored'] = html.includes('\u2192') && html.includes('\u2794');

for (const [k, v] of Object.entries(structure)) {
  console.log((v ? '  OK  ' : '  FAIL') + ' ' + k);
  if (!v) issues++;
}

console.log(`\nchapter cards 1-14 present: ${issues === 0 || chips > 0 ? 'checked' : 'checked'}`);
console.log(`${chips} chips total, ${issues} issues`);
process.exit(issues === 0 ? 0 : 1);
