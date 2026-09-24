const test = require('node:test');
const assert = require('node:assert/strict');
const fs = require('fs');
const path = require('path');
const policy = require('./seo-policy.cjs');
const { ROOT, siteFiles, setMetadata, parse } = require('./seo-html.cjs');
const { createResolver } = require('./seo-routes.cjs');
const { cleanUrlPath } = require('./normalize-seo-urls.cjs');
const { analyzeRedirects } = require('./check-cloudflare-redirects.cjs');
const { collectRuntimeJsonFiles } = require('./runtime-json-assets.cjs');
const files = siteFiles();
const resolve = createResolver(files);

test('canonical normalization preserves both query strings and fragments', () => {
  assert.equal(cleanUrlPath('../chapter/index.html?x=1#q2'), '../chapter/?x=1#q2');
  assert.equal(cleanUrlPath('exercise-1.html#q1'), 'exercise-1#q1');
  assert.equal(cleanUrlPath('/assets/file.pdf#page=2'), '/assets/file.pdf#page=2');
  assert.equal(policy.toUrl('index.html'), 'https://sjmaths.com/');
  assert.equal(policy.toUrl('pages/pricing.html'), 'https://sjmaths.com/pages/pricing');
});
test('ordinary navigation is not mistaken for an automatic redirect', () => {
  assert.equal(policy.hasRedirect('<button onclick="location.href=\'/lesson/\'">Study</button>'), false);
  assert.equal(policy.hasRedirect('<meta http-equiv="refresh" content="0;url=/">'), true);
});
test('metadata repairs are idempotent and leave learning content byte-for-byte intact', () => {
  const body = '<body><h1>Practice</h1><p>\\(x^2 + y^2 = 1\\)</p></body></html>';
  const source = '<html><head><title>Old</title><meta name="description" content="Old"><meta name="description" content="Duplicate"></head>' + body;
  const values = { title: 'Practice & Solutions', description: 'Revise the equation.', canonical: 'https://sjmaths.com/practice' };
  const once = setMetadata(source, values);
  assert.equal(setMetadata(once, values), once);
  assert.ok(once.endsWith(body));
  assert.equal(parse(once)('meta[name="description"]').length, 1);
});
test('current-affairs JSON and real topic/test routes are no longer swallowed by redirects', () => {
  for (const file of ['current-affairs/data/manifest.json', 'ssc-cgl/reasoning/analogies/index.html']) {
    const result = resolve('https://sjmaths.com/' + (file.endsWith('/index.html') ? file.slice(0, -10) : file));
    assert.equal(result.file, file);
    assert.equal(result.redirect, undefined);
  }
  const tests = files.filter(file => /^class-10-maths\/tests\/unit-wise\/.*\.html$/.test(file));
  assert.ok(tests.length);
  for (const file of tests) {
    const result = resolve(policy.toUrl(file));
    assert.equal(result.file, file, file);
    assert.equal(result.redirect, undefined, file);
  }
});
test('empty placeholder pages are excluded without excluding real new subjects', () => {
  assert.ok(policy.isPlaceholderHtml('<p>This study resource is currently being compiled and reviewed. It is temporarily offline to maintain content quality.</p>'));
  assert.equal(policy.isPlaceholderHtml('<main><a href="/topic/">Published topic</a><p>Complete study material for this topic is being prepared. Check back later.</p></main>'), false);
  const file = 'class-12-physics/index.html';
  assert.ok(policy.isSitemapEligibleHtml(file, fs.readFileSync(path.join(ROOT, file), 'utf8')));
  assert.equal(policy.isSitemapEligibleHtml('login.html', '<title>Login</title>'), false);
});

test('Cloudflare redirects stay ordered, unique, resolvable, and within platform limits', () => {
  const result = analyzeRedirects(fs.readFileSync(path.join(ROOT, '_redirects'), 'utf8'));
  assert.deepEqual(result.errors, []);
});

test('Cloudflare deployment prep preserves runtime JSON dependencies', () => {
  const runtimeJsonFiles = collectRuntimeJsonFiles({ root: ROOT });
  for (const file of [
    'class-11-maths/ncert-exemplar-practice/chapter-1-sets/exemplar-1-1.json',
    'class-10-maths/full-length-test-papers/set1/questions.json',
    'learning/topics/class-10/mathematics/chapter-1-real-numbers/fta/fta.json',
    'current-affairs/data/manifest.json',
    'current-affairs/data/weekly/2026/06/2026-06-01.json',
    'current-affairs/data/weekly/2026/07/2026-07-26.json',
    'current-affairs/data/weekly/2026/08/2026-08-30.json',
  ]) {
    assert.ok(runtimeJsonFiles.has(file), file);
  }
  assert.ok(runtimeJsonFiles.size >= 300);
});

test('Cloudflare deployment uses an isolated staged output directory', () => {
  const packageJson = JSON.parse(fs.readFileSync(path.join(ROOT, 'package.json'), 'utf8'));
  const prep = fs.readFileSync(path.join(ROOT, 'scripts/prepare-pages.cjs'), 'utf8');
  const verify = fs.readFileSync(path.join(ROOT, 'scripts/verify-pages-artifact.cjs'), 'utf8');
  const deploy = fs.readFileSync(path.join(ROOT, 'scripts/deploy-pages.cjs'), 'utf8');
  const readme = fs.readFileSync(path.join(ROOT, 'README.md'), 'utf8');

  assert.match(packageJson.scripts['pages:build'], /--output-dir \.pages-dist/);
  assert.match(packageJson.scripts['pages:build'], /verify-pages-artifact/);
  assert.match(packageJson.scripts['pages:deploy'], /deploy-pages/);
  assert.match(prep, /fs\.mkdirSync\(deploymentRoot/);
  assert.match(prep, /fs\.readdirSync\(ROOT, \{ withFileTypes: true \}\)/);
  assert.match(prep, /const productionRoot = stagedOutput \? deploymentRoot : ROOT/);
  assert.match(prep, /if \(stagedOutput\) DIRS_TO_REMOVE\.push\('scripts'\)/);
  assert.match(verify, /missingRuntimeFiles/);
  assert.match(verify, /forbiddenDirectories/);
  assert.match(deploy, /CF_PAGES_PROJECT/);
  assert.match(deploy, /wrangler/);
  assert.match(readme, /Output directory:\*\* `\.pages-dist`/);
});

test('CSS sources do not contain embedded NUL bytes', () => {
  for (const file of [
    'assets/css/class-12-notes.css',
    'assets/css/class11-notes.css',
    'assets/css/class9-notes.css',
  ]) {
    assert.equal(fs.readFileSync(path.join(ROOT, file)).includes(0), false, file);
  }
});

test('Newton page serializes MathJax after shared components load', () => {
  const page = fs.readFileSync(
    path.join(ROOT, 'class-9-advanced-science/chapter-3-newtons-laws-of-motion/index.html'),
    'utf8'
  );

  assert.match(page, /startup:\s*\{\s*typeset:\s*false\s*\}/);
  assert.match(page, /sjmaths:component-loaded/);
  assert.match(page, /queueMathJaxTypeset/);
});
