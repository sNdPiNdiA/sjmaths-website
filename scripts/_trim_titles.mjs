#!/usr/bin/env node
/**
 * Trims <title> tags that exceed 120 characters.
 * Strategy: keep everything before the last pipe " | " suffix,
 * but always preserve " | UP TGT & PGT <Subject>" at the end.
 * If still too long, hard-truncate at a word boundary.
 */

import fs from 'fs';
import path from 'path';

const BASE = process.cwd();
const TARGET_DIRS = ['geography', 'english'];

function discoverPages(dirs) {
  const pages = [];
  function walk(dir) {
    if (!fs.existsSync(dir)) return;
    for (const item of fs.readdirSync(dir, { withFileTypes: true })) {
      const full = path.join(dir, item.name);
      if (item.isDirectory()) walk(full);
      else if (item.name === 'index.html') pages.push(full);
    }
  }
  for (const d of dirs) walk(d);
  return pages;
}

const pages = discoverPages(TARGET_DIRS.map(d => path.join(BASE, d)));
console.log(`\n✂️  Title Trimmer — scanning ${pages.length} pages...\n`);

const MAX = 120;
let trimmed = 0;

for (const filePath of pages) {
  let html = fs.readFileSync(filePath, 'utf8');
  const m = html.match(/<title>([^<]*)<\/title>/i);
  if (!m) continue;

  const original = m[1];
  if (original.length <= MAX) continue;

  // Strategy: split on last " | " — keep subject suffix, shorten main part
  const pipeIdx = original.lastIndexOf(' | ');
  let suffix = pipeIdx !== -1 ? original.slice(pipeIdx) : ''; // e.g. " | UP TGT & PGT Geography"
  let main   = pipeIdx !== -1 ? original.slice(0, pipeIdx) : original;

  // Available chars for main part
  const budget = MAX - suffix.length;

  if (budget < 20) {
    // suffix itself is very long — just hard truncate suffix too
    suffix = suffix.substring(0, 40);
  }

  if (main.length > budget) {
    // Trim at last space within budget
    main = main.substring(0, budget).replace(/\s+\S*$/, '').trimEnd();
    if (!main.endsWith('…')) main += '…';
  }

  const newTitle = main + suffix;

  if (newTitle !== original) {
    html = html.replace(`<title>${original}</title>`, `<title>${newTitle}</title>`);
    // Also update og:title to match
    html = html.replace(
      /<meta property="og:title" content="[^"]*"/,
      `<meta property="og:title" content="${newTitle.substring(0, 95)}"`
    );
    html = html.replace(
      /<meta name="twitter:title" content="[^"]*"/,
      `<meta name="twitter:title" content="${newTitle.substring(0, 95)}"`
    );
    fs.writeFileSync(filePath, html, 'utf8');
    trimmed++;
  }
}

console.log(`  ✅ Trimmed ${trimmed} titles to ≤ ${MAX} chars`);
console.log('\n✅ Done! Re-run node scripts/_seo_audit.mjs to verify.\n');
