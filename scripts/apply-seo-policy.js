const fs = require('fs');
const path = require('path');
const {
  isManagedHtmlPath,
  isHighConfidenceIndexPath,
  hasRedirect,
  hasTitle,
  hasDescription,
  shouldSkipDir,
  normalizePath,
  toUrl,
} = require('./seo-policy');

const ROOT_DIR = path.resolve(__dirname, '..');
const DRY_RUN = process.argv.includes('--dry-run');

const ROBOTS_INDEX = 'index, follow, max-image-preview:large';
const ROBOTS_NOINDEX = 'noindex, follow';

const TAGS = {
  doctype: /<!DOCTYPE html>\s*/gi,
  htmlOpen: /<html\b[^>]*>\s*/gi,
  headOpen: /<head\b[^>]*>\s*/gi,
  title: /<title>[\s\S]*?<\/title>\s*/gi,
  charset: /<meta\s+[^>]*charset=[^>]*>\s*/gi,
  viewport: /<meta\s+[^>]*name=["']viewport["'][^>]*>\s*/gi,
  description: /<meta\s+[^>]*name=["']description["'][^>]*>\s*/gi,
  robots: /<meta\s+[^>]*name=["']robots["'][^>]*>\s*/gi,
  canonical: /<link\s+[^>]*rel=["']canonical["'][^>]*>\s*/gi,
};

function walkHtmlFiles(dirPath, files = []) {
  const dirents = fs.readdirSync(dirPath, { withFileTypes: true });

  for (const dirent of dirents) {
    const fullPath = path.join(dirPath, dirent.name);

    if (dirent.isDirectory()) {
      if (!shouldSkipDir(dirent.name)) {
        walkHtmlFiles(fullPath, files);
      }
      continue;
    }

    if (dirent.isFile() && dirent.name.endsWith('.html')) {
      files.push(fullPath);
    }
  }

  return files;
}

function escapeAttr(value) {
  return value
    .replace(/&/g, '&amp;')
    .replace(/"/g, '&quot;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;');
}

function stripAllButFirst(content, regex) {
  let seen = 0;
  return content.replace(regex, (match) => {
    seen += 1;
    return seen === 1 ? match : '';
  });
}

function keepLastTag(content, regex) {
  const matches = content.match(regex);
  if (!matches || matches.length < 2) {
    return content;
  }

  let seen = 0;
  return content.replace(regex, (match) => {
    seen += 1;
    return seen === matches.length ? match : '';
  });
}

function removeTags(content, regex) {
  return content.replace(regex, '');
}

function getAttribute(tag, attributeName) {
  const match = tag.match(new RegExp(`${attributeName}\\s*=\\s*["']([^"']*)["']`, 'i'));
  return match ? match[1].trim() : '';
}

function hasExpectedRobotsAndCanonical(head, robotsValue, canonicalUrl) {
  const robotsTags = head.match(TAGS.robots) || [];
  const canonicalTags = head.match(TAGS.canonical) || [];

  return (
    robotsTags.length === 1 &&
    canonicalTags.length === 1 &&
    getAttribute(robotsTags[0], 'content') === robotsValue &&
    getAttribute(canonicalTags[0], 'href') === canonicalUrl
  );
}

function insertIntoHead(head, snippet) {
  const anchors = [TAGS.description, TAGS.viewport, TAGS.charset, TAGS.title];
  let insertAt = 0;

  for (const regex of anchors) {
    const matches = [...head.matchAll(new RegExp(regex.source, regex.flags))];
    if (matches.length) {
      const lastMatch = matches[matches.length - 1];
      insertAt = Math.max(insertAt, lastMatch.index + lastMatch[0].length);
      break;
    }
  }

  const prefix = insertAt > 0 && !head.slice(0, insertAt).endsWith('\n') ? '\n' : '';
  const suffix = head.slice(insertAt).startsWith('\n') ? '' : '\n';
  return `${head.slice(0, insertAt)}${prefix}${snippet}${suffix}${head.slice(insertAt)}`;
}

function getHeadBounds(content) {
  const openMatch = content.match(/<head\b[^>]*>/i);
  const closeMatch = content.match(/<\/head>/i);

  if (!openMatch || !closeMatch || openMatch.index > closeMatch.index) {
    return null;
  }

  return {
    openStart: openMatch.index,
    openEnd: openMatch.index + openMatch[0].length,
    closeStart: closeMatch.index,
  };
}

function extractTitle(head) {
  const match = head.match(/<title>\s*([^<]+?)\s*<\/title>/i);
  return match ? match[1].replace(/\s+/g, ' ').trim() : '';
}

function buildFallbackDescription(relativePath, head) {
  const title = extractTitle(head).replace(/\s+\|\s*SJMaths$/i, '');
  const subject = title || relativePath.replace(/[-_/]+/g, ' ').replace(/\.html$/i, '').trim();
  return `${subject} on SJMaths with CBSE Maths notes, practice resources, and exam preparation support.`;
}

function normalizeDocumentShell(content) {
  let next = content;
  next = stripAllButFirst(next, TAGS.doctype);
  next = stripAllButFirst(next, TAGS.htmlOpen);
  next = stripAllButFirst(next, TAGS.headOpen);
  return next;
}

function normalizeHead(head, relativePath, shouldIndex) {
  let next = head;

  next = keepLastTag(next, TAGS.title);
  next = keepLastTag(next, TAGS.charset);
  next = keepLastTag(next, TAGS.viewport);
  next = keepLastTag(next, TAGS.description);

  if (shouldIndex && !hasDescription(next)) {
    const description = escapeAttr(buildFallbackDescription(relativePath, next));
    next = insertIntoHead(next, `    <meta name="description" content="${description}">`);
  }

  const robotsValue = shouldIndex ? ROBOTS_INDEX : ROBOTS_NOINDEX;
  const canonicalUrl = escapeAttr(toUrl(relativePath));

  if (!hasExpectedRobotsAndCanonical(next, robotsValue, canonicalUrl)) {
    next = removeTags(next, TAGS.robots);
    next = removeTags(next, TAGS.canonical);
    const seoTags = `    <meta name="robots" content="${robotsValue}">\n    <link rel="canonical" href="${canonicalUrl}">`;
    next = insertIntoHead(next, seoTags);
  }

  return next.replace(/\n{4,}/g, '\n\n\n');
}

function applyToFile(filePath) {
  const relativePath = normalizePath(filePath, ROOT_DIR);
  const original = fs.readFileSync(filePath, 'utf8');

  if (!isManagedHtmlPath(relativePath)) {
    return { changed: false, skipped: true, indexed: false };
  }

  let next = normalizeDocumentShell(original);
  const shouldIndex =
    isHighConfidenceIndexPath(relativePath) &&
    !hasRedirect(next) &&
    hasTitle(next);

  const bounds = getHeadBounds(next);
  if (!bounds) {
    return { changed: false, skipped: true, indexed: false, reason: 'missing-head' };
  }

  const head = next.slice(bounds.openEnd, bounds.closeStart);
  const normalizedHead = normalizeHead(head, relativePath, shouldIndex);
  next = `${next.slice(0, bounds.openEnd)}${normalizedHead}${next.slice(bounds.closeStart)}`;

  if (next === original) {
    return { changed: false, skipped: false, indexed: shouldIndex };
  }

  if (!DRY_RUN) {
    fs.writeFileSync(filePath, next, 'utf8');
  }

  return { changed: true, skipped: false, indexed: shouldIndex };
}

function main() {
  const files = walkHtmlFiles(ROOT_DIR);
  const summary = {
    scanned: 0,
    changed: 0,
    skipped: 0,
    index: 0,
    noindex: 0,
    missingHead: 0,
  };

  for (const filePath of files) {
    const result = applyToFile(filePath);
    summary.scanned += 1;

    if (result.skipped) {
      summary.skipped += 1;
      if (result.reason === 'missing-head') {
        summary.missingHead += 1;
      }
      continue;
    }

    if (result.changed) {
      summary.changed += 1;
    }

    if (result.indexed) {
      summary.index += 1;
    } else {
      summary.noindex += 1;
    }
  }

  console.log(`${DRY_RUN ? '[dry-run] ' : ''}SEO policy applied`);
  console.table(summary);
}

main();
