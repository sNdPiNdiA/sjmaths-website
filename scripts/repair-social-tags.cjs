/**
 * repair-social-tags.cjs
 * ─────────────────────────────────────────────────────────────────────
 * Adds missing og:image and twitter:card/title/description meta tags
 * to all HTML files that are missing them.
 *
 * Strategy:
 * - og:image: Uses a default site-wide OG image URL
 * - twitter:card: Derives from existing og:title / og:description or
 *   falls back to <title> and <meta name="description">
 *
 * Run:  node scripts/repair-social-tags.cjs [--dry-run]
 */
const fs = require('fs');
const path = require('path');
const cheerio = require('cheerio');
const { siteFiles } = require('./seo-html.cjs');
const policy = require('./seo-policy.cjs');

const ROOT = path.resolve(__dirname, '..');
const DRY_RUN = process.argv.includes('--dry-run');

// Default OG image for the site
const DEFAULT_OG_IMAGE = 'https://sjmaths.com/assets/images/og-default.jpg';

const tracked = siteFiles();
const htmlFiles = tracked.filter(p => policy.isManagedHtmlPath(p) && !p.startsWith('scratch/'));

let fixedTwitter = 0;
let fixedOgImage = 0;
let totalModified = 0;

for (const file of htmlFiles) {
  const absPath = path.join(ROOT, file);
  let source = fs.readFileSync(absPath, 'utf8');
  if (!source.trim()) continue;

  const $ = cheerio.load(source, { decodeEntities: false });
  const meta = name => $('meta').filter((_, el) =>
    ($(el).attr('name') || $(el).attr('property') || '').toLowerCase() === name
  );

  // Skip non-indexable pages (noindex)
  const robotsMeta = meta('robots').map((_, el) => $(el).attr('content')).get().join(' ');
  if (/noindex/i.test(robotsMeta)) continue;

  let modified = false;

  // ── Fix missing twitter:card ──────────────────────────────────
  if (!meta('twitter:card').length) {
    const ogTitle = meta('og:title').first().attr('content') || $('title').first().text().trim() || '';
    const ogDesc = meta('og:description').first().attr('content') || meta('description').first().attr('content') || '';

    if (ogTitle) {
      // Find insertion point: after last og: meta, or before </head>
      const insertionPoint = findInsertionPoint($, source);
      if (insertionPoint >= 0) {
        const twitterTags = [
          `\n<meta name="twitter:card" content="summary">`,
          `<meta name="twitter:title" content="${escapeAttr(ogTitle)}">`,
        ];
        if (ogDesc) {
          twitterTags.push(`<meta name="twitter:description" content="${escapeAttr(truncate(ogDesc, 200))}">`);
        }
        const tagBlock = twitterTags.join('\n');

        source = source.slice(0, insertionPoint) + '\n' + tagBlock + source.slice(insertionPoint);
        modified = true;
        fixedTwitter++;
      }
    }
  }

  // ── Fix missing og:image ──────────────────────────────────────
  // Reload $ after string modifications
  const $2 = cheerio.load(source, { decodeEntities: false });
  const meta2 = name => $2('meta').filter((_, el) =>
    ($(el).attr('name') || $(el).attr('property') || '').toLowerCase() === name
  );

  if (!meta2('og:image').length) {
    // Insert og:image after og:url if present, otherwise after last og: meta
    const ogUrlMatch = source.match(/<meta\s+property="og:url"[^>]*>/i);
    const ogDescMatch = source.match(/<meta\s+property="og:description"[^>]*>/i);
    const anchor = ogUrlMatch || ogDescMatch;

    if (anchor) {
      const pos = source.indexOf(anchor[0]) + anchor[0].length;
      const ogImageTag = `\n<meta property="og:image" content="${DEFAULT_OG_IMAGE}">`;
      source = source.slice(0, pos) + ogImageTag + source.slice(pos);
      modified = true;
      fixedOgImage++;
    }
  }

  if (modified) {
    if (!DRY_RUN) {
      fs.writeFileSync(absPath, source, 'utf8');
    }
    totalModified++;
  }
}

console.log(`${DRY_RUN ? 'DRY-RUN' : 'DONE'}:`);
console.log(`  twitter:card added: ${fixedTwitter}`);
console.log(`  og:image added: ${fixedOgImage}`);
console.log(`  Total files modified: ${totalModified}`);

/* ── Helpers ──────────────────────────────────────────────────────── */

function findInsertionPoint($, source) {
  // Try to insert after last og: meta tag
  const ogMatches = [...source.matchAll(/<meta\s+property="og:[^"]*"[^>]*>/gi)];
  if (ogMatches.length) {
    const last = ogMatches[ogMatches.length - 1];
    return last.index + last[0].length;
  }
  // Fallback: before </head>
  const headClose = source.indexOf('</head>');
  return headClose >= 0 ? headClose : -1;
}

function escapeAttr(str) {
  return str.replace(/&/g, '&amp;').replace(/"/g, '&quot;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
}

function truncate(str, maxLen) {
  if (str.length <= maxLen) return str;
  return str.slice(0, maxLen - 1).replace(/\s+\S*$/, '') + '…';
}
