#!/usr/bin/env node
/**
 * SEO Audit Script — checks all generated geography (and english) pages
 * for unique, well-formed SEO signals.
 *
 * Checks per page:
 *   [1] <title> exists and is unique (≤ 120 chars)
 *   [2] <meta name="description"> exists, is unique, and is 120–300 chars
 *   [3] <link rel="canonical"> exists and matches expected URL
 *   [4] Exactly one <h1> per page
 *   [5] <h1> text matches the topic (not a placeholder)
 *   [6] <meta name="robots"> present
 *   [7] <html lang="en"> present
 *   [8] No unrendered template literals (${)
 *   [9] Page ends with </html>
 *  [10] Breadcrumb <nav> present
 *  [11] Exam badge chips present
 *  [12] Open Graph tags (og:title, og:description) — optional, flagged as warning
 */

import fs from 'fs';
import path from 'path';

// ── helpers ────────────────────────────────────────────────────────────────────

function getAttr(html, tag, attr) {
  const re = new RegExp(`<${tag}[^>]*\\s${attr}="([^"]*)"`, 'i');
  const m = html.match(re);
  return m ? m[1] : null;
}

function getTagContent(html, tag) {
  const re = new RegExp(`<${tag}[^>]*>([\\s\\S]*?)<\\/${tag}>`, 'i');
  const m = html.match(re);
  return m ? m[1].trim() : null;
}

function countTags(html, tag) {
  const re = new RegExp(`<${tag}[\\s>]`, 'gi');
  return (html.match(re) || []).length;
}

// ── page discovery ─────────────────────────────────────────────────────────────

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

const BASE = process.cwd();
const TARGET_DIRS = ['geography', 'english'];
const pages = discoverPages(TARGET_DIRS.map(d => path.join(BASE, d)));

console.log(`\n🔍 SEO Audit — scanning ${pages.length} pages in [${TARGET_DIRS.join(', ')}]...\n`);

// ── audit ─────────────────────────────────────────────────────────────────────

const titlesSeen = new Map();
const descsSeen  = new Map();

let totalIssues   = 0;
let totalWarnings = 0;
const report = [];

for (const filePath of pages) {
  const rel = path.relative(BASE, filePath).replace(/\\/g, '/');
  const urlPath = '/' + rel.replace(/index\.html$/, '');
  const html = fs.readFileSync(filePath, 'utf8');

  const errors   = [];
  const warnings = [];

  // [1] <title>
  const title = getTagContent(html, 'title');
  if (!title) {
    errors.push('Missing <title>');
  } else {
    if (title.length > 120) warnings.push(`<title> too long (${title.length} chars, max 120)`);
    if (title.includes('${')) errors.push('<title> has unrendered template literal');
    if (titlesSeen.has(title)) {
      errors.push(`Duplicate <title> (also used by ${titlesSeen.get(title)})`);
    } else {
      titlesSeen.set(title, urlPath);
    }
  }

  // [2] <meta description>
  const desc = getAttr(html, 'meta[^>]*name="description"', 'content') 
    || (() => { const m = html.match(/<meta\s+name="description"\s+content="([^"]*)"/i); return m ? m[1] : null; })();
  if (!desc) {
    errors.push('Missing <meta name="description">');
  } else {
    if (desc.length < 120) warnings.push(`Meta description too short (${desc.length} chars, min 120)`);
    if (desc.length > 320) warnings.push(`Meta description too long (${desc.length} chars, max 320)`);
    if (desc.includes('${')) errors.push('Meta description has unrendered template literal');
    if (descsSeen.has(desc)) {
      errors.push(`Duplicate meta description (also used by ${descsSeen.get(desc)})`);
    } else {
      descsSeen.set(desc, urlPath);
    }
  }

  // [3] canonical
  const canonical = (() => { const m = html.match(/<link\s+rel="canonical"\s+href="([^"]*)"/i); return m ? m[1] : null; })();
  if (!canonical) {
    errors.push('Missing <link rel="canonical">');
  } else {
    const expectedCanonical = `https://sjmaths.com${urlPath}`;
    if (canonical !== expectedCanonical) {
      errors.push(`Canonical mismatch — got "${canonical}", expected "${expectedCanonical}"`);
    }
  }

  // [4] & [5] <h1>
  const h1Count = countTags(html, 'h1');
  if (h1Count === 0) errors.push('No <h1> found');
  else if (h1Count > 1) errors.push(`Multiple <h1> tags found (${h1Count})`);
  const h1Content = getTagContent(html, 'h1');
  if (h1Content && h1Content.includes('${')) errors.push('<h1> has unrendered template literal');
  if (h1Content && h1Content.length < 5) errors.push(`<h1> seems too short: "${h1Content}"`);

  // [6] robots meta
  if (!html.includes('name="robots"')) errors.push('Missing <meta name="robots">');

  // [7] lang attribute
  if (!html.match(/<html[^>]+lang="en"/i)) errors.push('Missing lang="en" on <html>');

  // [8] unrendered template literals
  if (html.includes('${')) errors.push('Page contains unrendered ${...} template literals');

  // [9] proper html close
  if (!html.trimEnd().endsWith('</html>')) errors.push('Page does not end with </html> (possibly truncated)');

  // [10] breadcrumb
  if (!html.includes('class="breadcrumb"')) warnings.push('No breadcrumb nav found');

  // [11] exam badges
  if (!html.includes('exam-chip')) warnings.push('No exam badge chips found');

  // [12] OG tags (warning only)
  if (!html.includes('og:title')) warnings.push('Missing og:title (Open Graph)');
  if (!html.includes('og:description')) warnings.push('Missing og:description (Open Graph)');

  if (errors.length || warnings.length) {
    report.push({ urlPath, errors, warnings });
    totalIssues   += errors.length;
    totalWarnings += warnings.length;
  }
}

// ── summary ───────────────────────────────────────────────────────────────────

const CLEAN  = pages.length - report.filter(r => r.errors.length).length;
const BROKEN = report.filter(r => r.errors.length).length;
const WARN   = report.filter(r => r.warnings.length && !r.errors.length).length;

console.log('══════════════════════════════════════════════════════════════');
console.log(`  Total pages audited : ${pages.length}`);
console.log(`  ✅ Fully clean       : ${CLEAN}`);
console.log(`  ❌ Pages with errors : ${BROKEN}`);
console.log(`  ⚠️  Pages with only warnings: ${WARN}`);
console.log(`  Total errors        : ${totalIssues}`);
console.log(`  Total warnings      : ${totalWarnings}`);
console.log('══════════════════════════════════════════════════════════════\n');

if (report.length === 0) {
  console.log('🎉 All pages pass SEO audit!');
  process.exit(0);
}

// Group: errors first, then warning-only
const withErrors = report.filter(r => r.errors.length);
const warnOnly   = report.filter(r => !r.errors.length && r.warnings.length);

if (withErrors.length) {
  console.log(`❌ ERRORS (${withErrors.length} pages):\n`);
  for (const { urlPath, errors, warnings } of withErrors) {
    console.log(`  📄 ${urlPath}`);
    for (const e of errors)   console.log(`     ❌ ${e}`);
    for (const w of warnings) console.log(`     ⚠️  ${w}`);
    console.log('');
  }
}

if (warnOnly.length) {
  console.log(`\n⚠️  WARNINGS ONLY (${warnOnly.length} pages):\n`);
  for (const { urlPath, warnings } of warnOnly) {
    console.log(`  📄 ${urlPath}`);
    for (const w of warnings) console.log(`     ⚠️  ${w}`);
    console.log('');
  }
}

process.exit(BROKEN > 0 ? 1 : 0);
