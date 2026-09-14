const test = require('node:test');
const assert = require('node:assert/strict');
const fs = require('fs');
const path = require('path');
const policy = require('./seo-policy.cjs');
const { ROOT, siteFiles, setMetadata, parse } = require('./seo-html.cjs');
const { createResolver } = require('./seo-routes.cjs');
const { cleanUrlPath } = require('./normalize-seo-urls.cjs');
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
