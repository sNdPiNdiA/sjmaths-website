const fs = require('fs');
const path = require('path');

const ROOT = path.resolve(__dirname, '..');
const SKIP = new Set(['.git', '.firebase', '.vscode', 'assets', 'node_modules', 'scratch']);
const DOMAIN_URL = /https:\/\/sjmaths\.com\/[^"'<>\s)]+/g;
const HREF_REGEX = /href=(["'])([^"'\s]+)\1/gi;

function cleanUrlPath(targetUrl) {
  // Skip external, anchors, mailto, tel, assets
  if (targetUrl.startsWith('http://') || targetUrl.startsWith('https://') || targetUrl.startsWith('//') ||
      targetUrl.startsWith('#') || targetUrl.startsWith('mailto:') || targetUrl.startsWith('tel:') ||
      targetUrl.startsWith('javascript:')) {
    return targetUrl;
  }

  // Skip static asset extensions
  if (/\.(css|js|png|jpg|jpeg|svg|gif|webp|ico|json|xml|pdf|txt)(\?|#|$)/i.test(targetUrl)) {
    return targetUrl;
  }

  let [mainPath, queryHash] = targetUrl.split(/(?=[?#])/);
  queryHash = queryHash || '';

  // index.html -> /
  if (mainPath === 'index.html' || mainPath === './index.html') {
    return `./${queryHash}`;
  }
  if (mainPath.endsWith('/index.html')) {
    return `${mainPath.slice(0, -10)}/${queryHash}`;
  }

  // .html -> clean extensionless
  if (mainPath.endsWith('.html')) {
    return `${mainPath.slice(0, -5)}${queryHash}`;
  }

  return targetUrl;
}

let modifiedCount = 0;

function walk(dir) {
  for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
    if (entry.isDirectory()) {
      if (!SKIP.has(entry.name)) walk(path.join(dir, entry.name));
      continue;
    }
    if (!entry.isFile() || !entry.name.endsWith('.html')) continue;

    const file = path.join(dir, entry.name);
    const original = fs.readFileSync(file, 'utf8');

    // 1. Clean absolute domain URLs
    let updated = original.replace(DOMAIN_URL, (url) => {
      const match = url.match(/^(.*?)(\/index\.html|\.html)([?#].*)?$/);
      if (!match) return url;
      const [, base, suffix, tail = ''] = match;
      return `${base}${suffix === '/index.html' ? '/' : ''}${tail}`;
    });

    // 2. Clean href attributes
    updated = updated.replace(HREF_REGEX, (fullMatch, quote, targetUrl) => {
      const cleaned = cleanUrlPath(targetUrl);
      return `href=${quote}${cleaned}${quote}`;
    });

    if (updated !== original) {
      fs.writeFileSync(file, updated, 'utf8');
      modifiedCount++;
    }
  }
}

walk(ROOT);
console.log(`Normalized internal URLs in ${modifiedCount} HTML files.`);
