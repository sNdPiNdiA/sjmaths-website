#!/usr/bin/env node
/**
 * SEO Patcher — fixes two classes of issues found by _seo_audit.mjs:
 *
 *  [1] Duplicate <title> / <meta description> — makes them unique by
 *      appending the full URL path slug to both.
 *
 *  [2] Missing Open Graph tags — injects og:title, og:description,
 *      og:url, og:type, og:site_name after <meta name="robots"> on
 *      every page that lacks them.
 *
 * Run: node scripts/_seo_patch.mjs
 * Safe to re-run (idempotent — skips pages already patched).
 */

import fs from 'fs';
import path from 'path';

// ── page discovery ─────────────────────────────────────────────────────────────
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
console.log(`\n🔧 SEO Patcher — processing ${pages.length} pages...\n`);

// ── helpers ────────────────────────────────────────────────────────────────────

function getTitle(html) {
  const m = html.match(/<title>([^<]*)<\/title>/i);
  return m ? m[1] : null;
}

function getDesc(html) {
  const m = html.match(/<meta\s+name="description"\s+content="([^"]*)"/i);
  return m ? m[1] : null;
}

function slugToTitle(slug) {
  return slug.split('-').map(w => w.charAt(0).toUpperCase() + w.slice(1)).join(' ');
}

// ── Pass 1: collect all titles & descriptions ──────────────────────────────────

const titleMap  = new Map(); // title → first filePath seen
const descMap   = new Map();

for (const filePath of pages) {
  const html  = fs.readFileSync(filePath, 'utf8');
  const title = getTitle(html);
  const desc  = getDesc(html);

  if (title && !titleMap.has(title)) titleMap.set(title, filePath);
  if (desc  && !descMap.has(desc))   descMap.set(desc, filePath);
}

// ── Pass 2: patch each page ────────────────────────────────────────────────────

let patchedTitle = 0;
let patchedOG    = 0;
let skipped      = 0;

for (const filePath of pages) {
  let html = fs.readFileSync(filePath, 'utf8');
  let changed = false;

  const rel     = path.relative(BASE, filePath).replace(/\\/g, '/');
  const urlPath = '/' + rel.replace(/index\.html$/, '');
  const parts   = urlPath.split('/').filter(Boolean);
  const slug    = parts[parts.length - 1];
  const section = parts.length >= 2 ? slugToTitle(parts[parts.length - 2]) : '';
  // e.g. "Geographical Thought — Neo Determinism"
  const contextSuffix = section ? ` (${section})` : '';

  // ── [1] Fix duplicate titles ────────────────────────────────────────────────
  const origTitle = getTitle(html);
  if (origTitle) {
    const firstOwner = titleMap.get(origTitle);
    if (firstOwner && firstOwner !== filePath) {
      // This page is a duplicate. Make title unique.
      const newTitle = origTitle.replace(/ \| /, `${contextSuffix} | `);
      html = html.replace(
        `<title>${origTitle}</title>`,
        `<title>${newTitle}</title>`
      );
      changed = true;
      patchedTitle++;
    }
  }

  // ── [1b] Fix duplicate meta descriptions ────────────────────────────────────
  const origDesc = getDesc(html);
  if (origDesc) {
    const firstOwner = descMap.get(origDesc);
    if (firstOwner && firstOwner !== filePath) {
      // Append context suffix to disambiguate
      const newDesc = origDesc.trimEnd().replace(/\.$/, '') + ` Focus: ${slugToTitle(slug)} under ${section || 'Geography'}.`;
      html = html.replace(
        `<meta name="description" content="${origDesc}"`,
        `<meta name="description" content="${newDesc.substring(0, 320)}"`
      );
      changed = true;
    }
  }

  // ── [2] Inject Open Graph tags if missing ───────────────────────────────────
  if (!html.includes('og:title')) {
    const currentTitle = getTitle(html) || origTitle || '';
    const currentDesc  = getDesc(html)  || origDesc  || '';
    const canonicalUrl = `https://sjmaths.com${urlPath}`;

    const ogTags = `
<!-- Open Graph -->
<meta property="og:type" content="article">
<meta property="og:site_name" content="SJ Maths">
<meta property="og:url" content="${canonicalUrl}">
<meta property="og:title" content="${currentTitle.substring(0, 95)}">
<meta property="og:description" content="${currentDesc.substring(0, 200)}">
<!-- Twitter Card -->
<meta name="twitter:card" content="summary">
<meta name="twitter:title" content="${currentTitle.substring(0, 95)}">
<meta name="twitter:description" content="${currentDesc.substring(0, 200)}">`;

    // Insert after <meta name="robots"> line
    html = html.replace(
      /(<meta name="robots"[^>]*>)/i,
      `$1\n${ogTags}`
    );
    changed = true;
    patchedOG++;
  }

  if (changed) {
    fs.writeFileSync(filePath, html, 'utf8');
  } else {
    skipped++;
  }
}

console.log('══════════════════════════════════════════════════════════════');
console.log(`  Pages patched for duplicate titles : ${patchedTitle}`);
console.log(`  Pages patched with OG tags         : ${patchedOG}`);
console.log(`  Pages already clean (skipped)      : ${skipped}`);
console.log('══════════════════════════════════════════════════════════════');
console.log('\n✅ Done! Re-run node scripts/_seo_audit.mjs to verify.\n');
