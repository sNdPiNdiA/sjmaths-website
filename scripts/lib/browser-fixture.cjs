// Reusable local browser fixture routing; this is not deployed-origin proof.
const fs = require('node:fs');
const path = require('node:path');
const { createResolver } = require('../seo-routes.cjs');
const mime = { '.html': 'text/html', '.js': 'text/javascript', '.css': 'text/css', '.json': 'application/json', '.png': 'image/png', '.jpg': 'image/jpeg', '.svg': 'image/svg+xml', '.woff2': 'font/woff2', '.ico': 'image/x-icon' };

async function routeRepositoryFixtures(page, { root, files }) {
  const resolver = createResolver(files);
  const evidence = { errors: [], missing: [], externalFailures: [], exclusions: [] };
  page.on('pageerror', error => evidence.errors.push(error.message));
  page.on('console', message => { if (message.type() === 'error') evidence.errors.push(message.text()); });
  page.on('requestfailed', request => {
    const url = new URL(request.url());
    if (!['sjmaths.com', 'www.sjmaths.com'].includes(url.hostname)) evidence.externalFailures.push(`${url.hostname}${url.pathname}: ${request.failure()?.errorText}`);
  });
  await page.route('**/*', async route => {
    const url = new URL(route.request().url());
    if (/googlesyndication|google-analytics|googletagmanager|doubleclick/.test(url.hostname)) {
      evidence.exclusions.push(url.hostname);
      return route.fulfill({ status: 204, body: '' });
    }
    if (!['sjmaths.com', 'www.sjmaths.com'].includes(url.hostname)) return route.continue();
    const resolved = resolver(url.href);
    if (resolved.redirect) return route.fulfill({ status: 301, headers: { location: resolved.redirect + url.search + url.hash } });
    if (!resolved.file) { evidence.missing.push(url.pathname); return route.fulfill({ status: 404, body: 'Not found' }); }
    return route.fulfill({ contentType: mime[path.extname(resolved.file)] || 'application/octet-stream', body: fs.readFileSync(path.join(root, resolved.file)) });
  });
  return evidence;
}
module.exports = { routeRepositoryFixtures };
