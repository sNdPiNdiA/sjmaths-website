// Read-only inventory. Educational payload size is not classified as waste.
const fs = require('node:fs');
const path = require('node:path');
const crypto = require('node:crypto');
const { ROOT, siteFiles } = require('./seo-html.cjs');

const files = siteFiles().filter(file => !file.startsWith('scratch/') && fs.existsSync(path.join(ROOT, file)));
const folders = {}, extensions = {}, consumers = {}, css = new Map(), js = new Map();
let totalBytes = 0, htmlBytes = 0, inlineCssBytes = 0, inlineJsBytes = 0;
function collectBlock(map, body, file) {
  const normalized = body.trim();
  if (Buffer.byteLength(normalized) < 500) return;
  const sha256 = crypto.createHash('sha256').update(normalized).digest('hex');
  if (!map.has(sha256)) map.set(sha256, { sha256, bytes: Buffer.byteLength(normalized), occurrences: 0, files: [] });
  const group = map.get(sha256);
  group.occurrences++;
  if (!group.files.includes(file)) group.files.push(file);
}
for (const file of files) {
  const absolute = path.join(ROOT, file);
  const stat = fs.statSync(absolute);
  if (!stat.isFile()) continue;
  const extension = path.extname(file) || '(none)';
  const folder = file.includes('/') ? file.split('/')[0] : '(root)';
  extensions[extension] = (extensions[extension] || 0) + 1;
  folders[folder] ||= { files: 0, bytes: 0 };
  folders[folder].files++;
  folders[folder].bytes += stat.size;
  totalBytes += stat.size;
  if (extension !== '.html') continue;
  htmlBytes += stat.size;
  const source = fs.readFileSync(absolute, 'utf8');
  for (const match of source.matchAll(/<style\b[^>]*>([\s\S]*?)<\/style>/gi)) {
    inlineCssBytes += Buffer.byteLength(match[1]);
    collectBlock(css, match[1], file);
  }
  for (const match of source.matchAll(/<script\b(?![^>]*\bsrc=)([^>]*)>([\s\S]*?)<\/script>/gi)) {
    if (/application\/(?:ld\+)?json|text\/plain/i.test(match[1])) continue;
    inlineJsBytes += Buffer.byteLength(match[2]);
    collectBlock(js, match[2], file);
  }
  for (const match of source.matchAll(/<(?:link|script)\b[^>]*(?:href|src)=["']([^"']+)["'][^>]*>/gi)) {
    const url = match[1];
    if (!/\.(css|js)(?:[?#]|$)/i.test(url) || /^(https?:|\/\/|data:)/i.test(url)) continue;
    const clean = url.split(/[?#]/)[0];
    const resolved = clean.startsWith('/') ? clean.slice(1) : path.posix.normalize(path.posix.join(path.posix.dirname(file), clean));
    consumers[resolved] ||= [];
    if (!consumers[resolved].includes(file)) consumers[resolved].push(file);
  }
}
function duplicates(map) {
  const groups = [...map.values()].filter(group => group.occurrences > 1);
  groups.sort((a, b) => (b.occurrences - 1) * b.bytes - (a.occurrences - 1) * a.bytes);
  return { extraBytes: groups.reduce((sum, group) => sum + (group.occurrences - 1) * group.bytes, 0), groups };
}
const result = {
  scope: 'tracked and non-ignored source files; excludes deployment output and scratch; duplicate blocks are candidates requiring cascade/execution inspection',
  totalBytes, htmlBytes, inlineCssBytes, inlineJsBytes, folders, extensions, consumers,
  css: duplicates(css), js: duplicates(js),
};
const output = path.join(ROOT, 'scratch/refactor/inventory.json');
fs.mkdirSync(path.dirname(output), { recursive: true });
fs.writeFileSync(output, JSON.stringify(result, null, 2) + '\n');
console.log(JSON.stringify({ htmlFiles: extensions['.html'], localSharedAssets: Object.keys(consumers).length, duplicateCssGroups: result.css.groups.length, duplicateJsGroups: result.js.groups.length, repeatedCssBytes: result.css.extraBytes, repeatedJsBytes: result.js.extraBytes, output: path.relative(ROOT, output) }, null, 2));
