import fs from 'node:fs';
import path from 'node:path';
import { execFileSync } from 'node:child_process';
import { fileURLToPath } from 'node:url';
import crypto from 'node:crypto';
import { ROOT, siteFiles, parse } from './seo-html.cjs';

const hash = value => crypto.createHash('sha256').update(value).digest('hex');

function nodeSourceRange(element) {
  const location = element.sourceCodeLocation;
  if (!location || !Number.isInteger(location.startOffset) || !Number.isInteger(location.endOffset)) return null;
  return { start: location.startOffset, end: location.endOffset, tag: element.tagName };
}

function includeLineWhitespace(source, range) {
  let { start, end } = range;
  const lineStart = source.lastIndexOf('\n', start - 1) + 1;
  if (/^[\t ]*$/.test(source.slice(lineStart, start))) start = lineStart;

  let lineEnd = end;
  while (source[lineEnd] === ' ' || source[lineEnd] === '\t') lineEnd++;
  if (source.startsWith('\r\n', lineEnd)) lineEnd += 2;
  else if (source[lineEnd] === '\n') lineEnd++;
  return { ...range, start, end: lineEnd };
}

function exactMarkup(element, $) {
  return $.html(element);
}

export function findExactDuplicateRanges(source) {
  const $ = parse(source);
  const candidates = [];

  function keepFirst(selector, signatureFor, label) {
    const seen = new Set();
    $(selector).each((_, element) => {
      const signature = signatureFor(element);
      if (!signature || !seen.has(signature)) {
        if (signature) seen.add(signature);
        return;
      }
      const range = nodeSourceRange(element);
      if (range) candidates.push({ ...includeLineWhitespace(source, range), label });
    });
  }

  keepFirst('main', element => `main:${hash($(element).html() || '')}`, 'identical main content');
  keepFirst(
    'body > header, body > footer, body > div#header-container, body > div#footer-container',
    element => `${element.tagName}:${hash(exactMarkup(element, $))}`,
    'identical page shell',
  );
  keepFirst(
    'script',
    element => `script:${hash(JSON.stringify(element.attribs) + '\0' + ($(element).html() || ''))}`,
    'identical script',
  );
  keepFirst('style', element => `style:${hash($(element).html() || '')}`, 'identical style');
  keepFirst(
    'link[rel="stylesheet"]',
    element => `stylesheet:${hash(JSON.stringify(element.attribs))}`,
    'identical stylesheet link',
  );

  // An outer duplicate main already includes any repeated scripts inside it.
  // Prefer removing the largest exact duplicate node, and skip overlaps.
  candidates.sort((a, b) => a.start - b.start || b.end - a.end);
  const ranges = [];
  for (const candidate of candidates) {
    if (ranges.some(range => candidate.start >= range.start && candidate.end <= range.end)) continue;
    if (ranges.some(range => candidate.start < range.end && candidate.end > range.start)) continue;
    ranges.push(candidate);
  }
  return ranges.sort((a, b) => b.start - a.start);
}

export function removeExactDuplicates(source) {
  const ranges = findExactDuplicateRanges(source);
  let result = source;
  for (const { start, end } of ranges) result = result.slice(0, start) + result.slice(end);
  return { source: result, ranges };
}

function main() {
  const apply = process.argv.includes('--apply');
  const changedOnly = process.argv.includes('--changed');
  const changedHtml = changedOnly
    ? new Set(execFileSync('git', ['diff', '--name-only', '--diff-filter=ACMRT', 'HEAD'], { cwd: ROOT, encoding: 'utf8' }).split(/\r?\n/))
    : null;
  const paths = siteFiles().filter(file => path.extname(file).toLowerCase() === '.html'
    && !file.startsWith('scratch/')
    && (!changedHtml || changedHtml.has(file)));
  const summary = { mode: apply ? 'apply' : 'dry-run', scope: changedOnly ? 'changed HTML' : 'all HTML', scannedHtml: paths.length, affectedPages: 0, removedBlocks: 0, removedBytes: 0, byType: {} };

  for (const relativePath of paths) {
    const absolutePath = path.join(ROOT, relativePath);
    if (!fs.existsSync(absolutePath)) continue;
    const before = fs.readFileSync(absolutePath, 'utf8');
    const result = removeExactDuplicates(before);
    if (!result.ranges.length) continue;

    summary.affectedPages++;
    summary.removedBlocks += result.ranges.length;
    summary.removedBytes += Buffer.byteLength(before) - Buffer.byteLength(result.source);
    for (const range of result.ranges) summary.byType[range.label] = (summary.byType[range.label] || 0) + 1;
    if (apply) fs.writeFileSync(absolutePath, result.source, 'utf8');
  }

  console.log(JSON.stringify(summary, null, 2));
}

if (process.argv[1] && path.resolve(process.argv[1]) === fileURLToPath(import.meta.url)) main();
