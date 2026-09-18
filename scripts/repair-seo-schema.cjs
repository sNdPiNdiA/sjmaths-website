// Remove or normalize only broken internal URLs from JSON-LD. Visible content is untouched.
const fs = require('fs');
const path = require('path');
const { ROOT, siteFiles, parse, applyEdits, editElement } = require('./seo-html.cjs');
const { createResolver } = require('./seo-routes.cjs');

const files = siteFiles();
const resolveUrl = createResolver(files);
const internal = value => typeof value === 'string' && /^https?:\/\/(?:www\.)?sjmaths\.com\//i.test(value) && !/[{}]/.test(value);
let filesChanged = 0;
let normalizedUrls = 0;
let removedUrls = 0;
let removedNodes = 0;
const sleepBuffer = new Int32Array(new SharedArrayBuffer(4));
function writeFile(target, content) {
  for (let attempt = 0; ; attempt++) {
    try { fs.writeFileSync(target, content); return; }
    catch (error) {
      if (attempt >= 8 || !['UNKNOWN', 'EBUSY', 'EPERM'].includes(error.code)) throw error;
      Atomics.wait(sleepBuffer, 0, 0, 100 * (attempt + 1));
    }
  }
}

function normalize(value) {
  const url = new URL(value);
  url.hostname = 'sjmaths.com';
  url.pathname = url.pathname.replace(/\/{2,}/g, '/');
  return url.href;
}

function valid(value, route) {
  const result = resolveUrl(value, route);
  return Boolean(result.external || result.file);
}

function repair(node, route) {
  if (!node || typeof node !== 'object') return node;
  if (Array.isArray(node)) return node.map(value => repair(value, route)).filter(Boolean);

  // A ListItem without a resolvable destination makes a false navigation claim.
  if (node['@type'] === 'ListItem') {
    for (const key of ['item', 'url']) {
      if (!internal(node[key])) continue;
      const normalized = normalize(node[key]);
      if (valid(normalized, route)) {
        if (normalized !== node[key]) normalizedUrls++;
        node[key] = normalized;
      } else {
        removedNodes++;
        return null;
      }
    }
  }

  for (const [key, value] of Object.entries(node)) {
    if (typeof value === 'string' && internal(value)) {
      const normalized = normalize(value);
      if (valid(normalized, route)) {
        if (normalized !== value) normalizedUrls++;
        node[key] = normalized;
      } else {
        delete node[key];
        removedUrls++;
      }
    } else if (value && typeof value === 'object') {
      const repaired = repair(value, route);
      if (repaired == null || Array.isArray(repaired) && !repaired.length) delete node[key];
      else node[key] = repaired;
    }
  }
  if (Array.isArray(node.itemListElement)) {
    node.itemListElement.forEach((item, index) => { if (item && typeof item === 'object') item.position = index + 1; });
  }
  if (['ItemList', 'BreadcrumbList'].includes(node['@type']) && !node.itemListElement?.length) {
    removedNodes++;
    return null;
  }
  return node;
}

for (const file of files.filter(file => file.endsWith('.html'))) {
  const target = path.join(ROOT, file);
  if (!fs.existsSync(target)) continue;
  const source = fs.readFileSync(target, 'utf8');
  const $ = parse(source);
  const edits = [];
  $('script[type="application/ld+json"]').each((_, el) => {
    let data;
    try { data = JSON.parse($(el).text()); } catch { return; }
    const before = JSON.stringify(data);
    data = repair(data, 'https://sjmaths.com/' + file.replace(/index\.html$/, '').replace(/\.html$/, ''));
    if (data && JSON.stringify(data) !== before) {
      const loc = el.sourceCodeLocation;
      edits.push({ start: loc.startTag.endOffset, end: loc.endTag.startOffset, text: `\n${JSON.stringify(data, null, 2).replace(/</g, '\\u003c')}\n` });
    } else if (!data) edits.push(editElement(el, ''));
  });
  if (edits.length) {
    writeFile(target, applyEdits(source, edits));
    filesChanged++;
  }
}
console.log(JSON.stringify({ filesChanged, normalizedUrls, removedUrls, removedNodes }));
