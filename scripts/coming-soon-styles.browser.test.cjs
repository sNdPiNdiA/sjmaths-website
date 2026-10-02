const assert = require('node:assert/strict');
const fs = require('node:fs');
const http = require('node:http');
const path = require('node:path');
const { chromium } = require('playwright');

const ROOT = path.resolve(__dirname, '..');
const DIST = path.join(ROOT, '.pages-dist');
const CSS = fs.readFileSync(path.join(DIST, 'assets/css/coming-soon-page.css'), 'utf8');
const ROUTES = [
  '/art/indian-mural-painting/mural-techniques/index.html',
  '/up-pgt-biology/botany/angiosperms/development/index.html',
  '/up-pgt-civics/section-a/challenges-to-indian-political-system/casteism/index.html',
  '/up-pgt-education/achievement-tests-and-evaluation/choice-based-credit-system/index.html',
];
const VIEWPORTS = [{ width: 390, height: 844 }, { width: 1280, height: 900 }];

function contentType(file) {
  if (file.endsWith('.html')) return 'text/html; charset=utf-8';
  if (file.endsWith('.css')) return 'text/css; charset=utf-8';
  if (file.endsWith('.js')) return 'text/javascript; charset=utf-8';
  if (file.endsWith('.json')) return 'application/json; charset=utf-8';
  return 'application/octet-stream';
}

function styleSnapshot() {
  const pick = (selector, properties) => {
    const element = document.querySelector(selector);
    const style = getComputedStyle(element);
    return Object.fromEntries(properties.map(property => [property, style[property]]));
  };
  return {
    body: pick('body', ['backgroundColor', 'color', 'margin', 'fontFamily', 'lineHeight']),
    header: pick('.site-header', ['height', 'position', 'backgroundColor', 'borderBottomColor']),
    wrap: pick('.wrap', ['width', 'marginLeft', 'marginRight']),
    placeholder: pick('.coming-soon', ['paddingTop', 'paddingRight', 'paddingBottom', 'textAlign']),
    heading: pick('.coming-soon h1', ['fontSize', 'fontWeight', 'marginBottom']),
    backButton: pick('.back-btn', ['display', 'paddingTop', 'paddingRight', 'backgroundColor', 'borderRadius']),
    footer: pick('footer', ['paddingTop', 'textAlign', 'fontSize', 'borderTopColor']),
  };
}

(async () => {
  assert.ok(fs.existsSync(DIST), 'Build .pages-dist before browser verification.');
  const server = http.createServer((request, response) => {
    const pathname = decodeURIComponent(new URL(request.url, 'http://localhost').pathname);
    const file = path.resolve(DIST, `.${pathname}`);
    if (!file.startsWith(`${DIST}${path.sep}`) && file !== path.join(DIST, 'index.html')) {
      response.writeHead(403).end();
      return;
    }
    if (!fs.existsSync(file) || !fs.statSync(file).isFile()) {
      response.writeHead(404).end();
      return;
    }
    response.writeHead(200, { 'content-type': contentType(file) });
    fs.createReadStream(file).pipe(response);
  });

  await new Promise(resolve => server.listen(0, '127.0.0.1', resolve));
  const address = server.address();
  const browser = await chromium.launch({ headless: true });
  try {
    for (const route of ROUTES) {
      for (const viewport of VIEWPORTS) {
        const page = await browser.newPage({ viewport });
        const failures = [];
        page.on('pageerror', error => failures.push(error.message));
        page.on('console', message => {
          if (message.type() === 'error') failures.push(message.text());
        });
        const response = await page.goto(`http://127.0.0.1:${address.port}${route}`, { waitUntil: 'networkidle' });
        assert.equal(response.status(), 200, `${route} should load`);
        assert.equal(await page.locator('link[href*="coming-soon-page.min.css"]').count(), 1, `${route} should use shared CSS`);

        const externalStyles = await page.evaluate(styleSnapshot);
        const noOverflow = await page.evaluate(() => document.documentElement.scrollWidth <= window.innerWidth);
        assert.equal(noOverflow, true, `${route} overflows at ${viewport.width}px`);

        await page.locator('link[href*="coming-soon-page.min.css"]').evaluate(link => { link.disabled = true; });
        await page.addStyleTag({ content: CSS });
        const inlineStyles = await page.evaluate(styleSnapshot);
        assert.deepEqual(externalStyles, inlineStyles, `${route} computed styles changed at ${viewport.width}px`);
        assert.deepEqual(failures, [], `${route} browser errors at ${viewport.width}px`);
        await page.close();
      }
    }
  } finally {
    await browser.close();
    await new Promise(resolve => server.close(resolve));
  }
  console.log(`Passed ${ROUTES.length * VIEWPORTS.length} built-page visual/runtime checks.`);
})().catch(error => {
  console.error(error);
  process.exitCode = 1;
});
