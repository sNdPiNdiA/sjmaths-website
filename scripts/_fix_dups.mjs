#!/usr/bin/env node
/**
 * Force-patch specific pages that still have duplicate titles after trimming.
 * We embed the unique URL path into the title directly.
 */

import fs from 'fs';
import path from 'path';

const BASE = process.cwd();

// Pairs of [filePath, uniqueSuffix to embed before last pipe]
const TARGETS = [
  // Geography: human-geography duplicates
  { url: '/geography/human-geography/approaches/neo-determinism/', section: 'Human Geography' },
  { url: '/geography/human-geography/approaches/possibilism/', section: 'Human Geography' },
  // India duplicates
  { url: '/geography/india/agriculture/major-crops/rice/', section: 'India' },
  { url: '/geography/india/agriculture/major-crops/sugarcane/', section: 'India' },
  { url: '/geography/india/agriculture/major-crops/tea/', section: 'India' },
  { url: '/geography/india/agriculture/major-crops/wheat/', section: 'India' },
  { url: '/geography/india/atmosphere/structure/', section: 'India' },
  { url: '/geography/india/agriculture/major-crops/', section: 'India Agriculture' },
  { url: '/geography/india/resources/energy-resources/', section: 'India Resources' },
];

let fixed = 0;

for (const { url, section } of TARGETS) {
  const filePath = path.join(BASE, url.replace(/^\//, ''), 'index.html');
  if (!fs.existsSync(filePath)) {
    console.log(`  ⚠️  Not found: ${filePath}`);
    continue;
  }

  let html = fs.readFileSync(filePath, 'utf8');
  const m = html.match(/<title>([^<]*)<\/title>/i);
  if (!m) continue;

  const original = m[1];
  const pipeIdx  = original.lastIndexOf(' | ');
  let main   = pipeIdx !== -1 ? original.slice(0, pipeIdx) : original;
  let suffix = pipeIdx !== -1 ? original.slice(pipeIdx) : '';

  // Strip trailing ellipsis then inject section
  main = main.replace(/…$/, '').trim();
  const newTitle = `${main} (${section})${suffix}`.substring(0, 120);

  html = html.replace(
    `<title>${original}</title>`,
    `<title>${newTitle}</title>`
  );
  // Update OG title too
  html = html.replace(
    /<meta property="og:title" content="[^"]*"/,
    `<meta property="og:title" content="${newTitle.substring(0, 95)}"`
  );
  html = html.replace(
    /<meta name="twitter:title" content="[^"]*"/,
    `<meta name="twitter:title" content="${newTitle.substring(0, 95)}"`
  );

  fs.writeFileSync(filePath, html, 'utf8');
  console.log(`  ✅ Patched: ${url}`);
  console.log(`     "${newTitle}"`);
  fixed++;
}

console.log(`\n✅ Fixed ${fixed} pages.\n`);
