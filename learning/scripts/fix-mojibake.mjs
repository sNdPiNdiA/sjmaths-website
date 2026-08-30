// Definitive repair: rebuild index.html = clean HEAD + mojibake-fixed injected block.
// Uses the CORRECT windows-1252 reverse map (with holes at 0x81,0x8D,0x8F,0x90,0x9D).
// All non-ASCII written as \u escapes so this script is encoding-proof.
import { readFileSync, writeFileSync } from 'node:fs';
import { execSync } from 'node:child_process';

const repo = 'C:/Users/sande/Documents/GitHub/sjmaths-website';
const rel = 'learning/topics/class-10/mathematics/index.html';
const FILE = `${repo}/${rel}`;

// char -> original cp1252 byte (holes omitted)
const CP1252 = new Map([
  [0x20AC, 0x80], [0x201A, 0x82], [0x0192, 0x83], [0x201E, 0x84], [0x2026, 0x85],
  [0x2020, 0x86], [0x2021, 0x87], [0x02C6, 0x88], [0x2030, 0x89], [0x0160, 0x8A],
  [0x2039, 0x8B], [0x0152, 0x8C], [0x017D, 0x8E], [0x2018, 0x91], [0x2019, 0x92],
  [0x201C, 0x93], [0x201D, 0x94], [0x2022, 0x95], [0x2013, 0x96], [0x2014, 0x97],
  [0x02DC, 0x98], [0x2122, 0x99], [0x0161, 0x9A], [0x203A, 0x9B], [0x0153, 0x9C],
  [0x017E, 0x9E], [0x0178, 0x9F],
]);
function toByte(ch) {
  const c = ch.codePointAt(0);
  if (c >= 0x80 && c <= 0xff) return c;
  return CP1252.get(c) ?? null;
}
// Greedy: decode runs of misdecoded UTF-8 back to real characters
function fixMojibake(s) {
  let out = '', i = 0, fixed = 0;
  while (i < s.length) {
    const b0 = toByte(s[i]);
    if (b0 !== null && b0 >= 0xc2 && b0 <= 0xf4) {
      const bytes = [b0];
      let j = i + 1;
      const mc = b0 >= 0xf0 ? 3 : b0 >= 0xe0 ? 2 : 1;
      let ok = true;
      for (let c = 0; c < mc; c++) {
        if (j >= s.length) { ok = false; break; }
        const bc = toByte(s[j]);
        if (bc === null || bc < 0x80 || bc > 0xbf) { ok = false; break; }
        bytes.push(bc); j++;
      }
      if (ok) {
        const d = Buffer.from(bytes).toString('utf8');
        if (d && [...d].every((ch) => ch.codePointAt(0) > 0x7f)) {
          out += d; fixed++; i = j; continue;
        }
      }
    }
    out += s[i]; i++;
  }
  return { out, fixed };
}

// Verification strategy: the working tree has legit uncommitted changes, so we
// can't diff byte-exact against HEAD. Instead verify:
//   1. zero mojibake signatures remain after fixing
//   2. every HEAD line (trimmed, >20 chars) still present in the fixed file
//   3. structural sanity (one </body>, one </html>, block intact)

const cur = readFileSync(FILE).toString('utf8');
const head = execSync(`git -C "${repo}" show HEAD:${rel}`, { maxBuffer: 1 << 26 }).toString('utf8');

const SIG = /\u00E2\u20AC|\u00C3[\u0080-\u00BF\u2013\u2014\u201A\u0192\u201E\u2026\u2020\u2021\u02C6\u2030\u0160\u2039\u0152\u017D\u2018\u2019\u201C\u201D\u2022\u02DC\u2122\u0161\u203A\u0153\u017E\u0178]|\u00C2[\u00A0-\u00BF]|\u00F0\u0178|\u00CE[\u00B1\u00B2\u00B3\u00B8\u00A3\u0094\u00B7]|\u00E2\u2020|\u00E2\u2021/g;
const countSigs = (t) => (t.match(SIG) || []).length;

console.log('mojibake sigs in current file:', countSigs(cur));

const res = fixMojibake(cur.replace(/\r\n/g, '\n'));
const fixed = res.out;
console.log('sequences repaired:', res.fixed);
console.log('mojibake sigs after fix:', countSigs(fixed));

// Every HEAD line containing NON-ASCII must survive verbatim (the encoding fix's
// safety property). ASCII-only reflows are pre-existing working-tree edits and
// are out of scope for this repair.
const fixedLines = new Set(fixed.split('\n').map((l) => l.trim()));
const hasNonAscii = (l) => [...l].some((c) => c.codePointAt(0) > 0x7f);
const nonAsciiHeadLines = head.split('\n').map((l) => l.trim()).filter((l) => l.length > 20 && hasNonAscii(l));
const missing = nonAsciiHeadLines.filter((l) => !fixedLines.has(l));
console.log('non-ASCII HEAD lines:', nonAsciiHeadLines.length, '| missing after fix:', missing.length);
missing.slice(0, 10).forEach((l) => console.log('  MISSING:', JSON.stringify(l.slice(0, 100))));

// Structural checks
const checks = {
  'single </body>': (fixed.match(/<\/body>/g) || []).length === 1,
  'single </html>': (fixed.match(/<\/html>/g) || []).length === 1,
  'foundation block present': fixed.includes('FOUNDATIONS_BY_CHAPTER'),
  'em-dash restored': (fixed.match(/\u2014/g) || []).length >= 1,
  'arrow \u2192 restored': (fixed.match(/\u2192/g) || []).length >= 1,
  'arrow \u2794 restored': (fixed.match(/\u2794/g) || []).length >= 1,
  'emoji \u{1F9F1} present': fixed.includes('\u{1F9F1}'),
  'no U+FFFD': !fixed.includes('\uFFFD'),
  'title clean': !/Mathematics \u00E2/.test(fixed) && /Adaptive Smart Mastery/.test(fixed),
};
let ok = true;
for (const [k, v] of Object.entries(checks)) {
  console.log((v ? '  OK  ' : '  FAIL') + ' ' + k);
  if (!v) ok = false;
}

// Show the key repaired lines for eyeballing
const t = fixed.indexOf('<title>');
console.log('\ntitle  :', fixed.slice(t, t + 80));
const lm = fixed.indexOf('Launch Module');
console.log('launch :', fixed.slice(lm, lm + 20));
const ch = fixed.match(/const chips[\s\S]{0,220}/)?.[0];
console.log('chips  :', ch);

if (process.argv.includes('--check-only')) process.exit(ok && countSigs(fixed) === 0 && missing.length === 0 ? 0 : 1);

if (!ok || countSigs(fixed) > 0 || missing.length > 0) {
  console.log('\nNOT writing — verification failed');
  process.exit(1);
}

writeFileSync(FILE, fixed, 'utf8');
console.log('\nWROTE file — chars:', fixed.length, 'bytes:', Buffer.byteLength(fixed), '(LF line endings)');
