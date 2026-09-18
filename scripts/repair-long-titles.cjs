/**
 * repair-long-titles.cjs
 * ─────────────────────────────────────────────────────────────────────
 * Shortens titles that exceed 120 characters. Strategy:
 *   1. Remove trailing "| SJ Maths" or "| Subject | SJ Maths" suffixes
 *   2. Remove filler phrases like "Study Notes, MCQs, Revision & Topic Test"
 *   3. If still too long, truncate intelligently at word boundary
 *   4. Always preserve the core topic name
 *
 * Run:  node scripts/repair-long-titles.cjs [--dry-run]
 */
const fs = require('fs');
const path = require('path');
const cheerio = require('cheerio');
const { siteFiles } = require('./seo-html.cjs');
const policy = require('./seo-policy.cjs');

const ROOT = path.resolve(__dirname, '..');
const DRY_RUN = process.argv.includes('--dry-run');
const MAX_TITLE = 110; // Target: comfortably under 120

const tracked = siteFiles();
const htmlFiles = tracked.filter(p => policy.isManagedHtmlPath(p) && !p.startsWith('scratch/'));

let fixed = 0;
let skipped = 0;

for (const file of htmlFiles) {
  const absPath = path.join(ROOT, file);
  let source = fs.readFileSync(absPath, 'utf8');
  if (!source.trim()) continue;

  const $ = cheerio.load(source, { decodeEntities: false });
  const titleEl = $('title').first();
  const origTitle = titleEl.text().trim();

  if (!origTitle || origTitle.length <= 120) continue;

  let newTitle = origTitle;

  // Step 1: Remove trailing subject suffixes like "| Agriculture | SJ Maths"
  newTitle = newTitle.replace(/\s*\|\s*(?:Agriculture|Art|Home Science|Chemistry)\s*\|\s*SJ Maths\s*$/i, ' | SJ Maths');

  // Step 2: Remove filler phrases
  const fillerPatterns = [
    /:\s*Study Notes,\s*MCQs,\s*Revision\s*&\s*Topic Test/gi,
    /:\s*Study Notes,\s*MCQs?\s*(?:&|and)\s*Revision/gi,
    /:\s*Detailed Notes,\s*MCQs?\s*(?:&|and)\s*Revision/gi,
    /:\s*Study Notes\s*(?:&|and)\s*(?:MCQs?|Revision|Practice)/gi,
    /\s*[-–—]\s*Study Notes\s*(?:&|,)\s*MCQs?/gi,
    /\s*[-–—]\s*Notes,?\s*(?:MCQs?|Questions|Practice)/gi,
    /\s*\|\s*Study Material\s*/gi,
  ];

  for (const pattern of fillerPatterns) {
    newTitle = newTitle.replace(pattern, '');
  }

  // Step 3: Remove redundant "in X and Y" phrases if they make it long
  if (newTitle.length > MAX_TITLE) {
    newTitle = newTitle.replace(/\s+in\s+[^|]+(?=\s*\|)/i, '');
  }

  // Step 4: Ensure | SJ Maths suffix
  if (!newTitle.includes('SJ Maths')) {
    newTitle = newTitle.trimEnd() + ' | SJ Maths';
  }

  // Step 5: If still too long, truncate at word boundary before | SJ Maths
  if (newTitle.length > MAX_TITLE) {
    const suffix = ' | SJ Maths';
    const maxCore = MAX_TITLE - suffix.length;
    let core = newTitle.replace(/\s*\|\s*SJ Maths\s*$/, '');
    if (core.length > maxCore) {
      core = core.slice(0, maxCore).replace(/\s+\S*$/, '').replace(/[,\s]+$/, '');
    }
    newTitle = core + suffix;
  }

  // Clean up any double spaces or leading/trailing issues
  newTitle = newTitle.replace(/\s{2,}/g, ' ').trim();

  if (newTitle === origTitle) {
    skipped++;
    continue;
  }

  // Replace in the source HTML
  // Find the <title>...</title> tag and replace its content
  const titleMatch = source.match(/<title[^>]*>([\s\S]*?)<\/title>/i);
  if (titleMatch) {
    const newTitleTag = `<title>${newTitle}</title>`;
    source = source.replace(titleMatch[0], newTitleTag);

    // Also update og:title if it matches the old title
    const ogTitleRegex = new RegExp(`(<meta\\s+property="og:title"\\s+content=")${escapeRegex(origTitle)}(")`,'i');
    if (ogTitleRegex.test(source)) {
      source = source.replace(ogTitleRegex, `$1${escapeHtml(newTitle)}$2`);
    }

    if (DRY_RUN) {
      if (fixed < 10) console.log(`${origTitle.length} → ${newTitle.length}: ${newTitle}`);
    } else {
      fs.writeFileSync(absPath, source, 'utf8');
    }
    fixed++;
  }
}

console.log(`\n${DRY_RUN ? 'DRY-RUN' : 'DONE'}: ${fixed} titles shortened, ${skipped} unchanged`);

function escapeRegex(str) {
  return str.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
}
function escapeHtml(str) {
  return str.replace(/&/g, '&amp;').replace(/"/g, '&quot;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
}
