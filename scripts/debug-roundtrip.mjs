import fs from 'fs';
import { externalizeMusicInstrumentalAssets, hydrateMusicInstrumentalAssets } from './lib/music-instrumental-assets.mjs';

const before = fs.readFileSync('music-instrumental/avanaddh-vadya/bol-notation/kathin-layakari/index.html', 'utf8');
const after = externalizeMusicInstrumentalAssets(before);
const roundtrip = hydrateMusicInstrumentalAssets(after);

const norm = t => t.replace(/\r\n/g, '\n').replace(/\s+/g, ' ').trim();
const nb = norm(before);
const nr = norm(roundtrip);

console.log('nb len:', nb.length, 'nr len:', nr.length);
for (let i = 0; i < Math.max(nb.length, nr.length); i++) {
  if (nb[i] !== nr[i]) {
    console.log('Diff at index', i);
    console.log('nb:', JSON.stringify(nb.slice(Math.max(0, i - 20), i + 40)));
    console.log('nr:', JSON.stringify(nr.slice(Math.max(0, i - 20), i + 40)));
    break;
  }
}
