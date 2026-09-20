const assert = require('assert/strict');
const fs = require('fs');
const path = require('path');
const test = require('node:test');

const ROOT = path.resolve(__dirname, '..');
const read = relative => fs.readFileSync(path.join(ROOT, relative), 'utf8');

test('search rendering keeps user input escaped and URLs same-origin', () => {
  const source = read('assets/js/search.js');
  assert.match(source, /function escapeHtml\(/);
  assert.match(source, /function escapeRegExp\(/);
  assert.match(source, /function getSafeSearchUrl\(/);
  assert.match(source, /window\.openSearch = openSearch/);
  assert.doesNotMatch(source, /new RegExp\(`\(\$\{term\}\)`/);
});

test('notifications and toasts do not inject external content as HTML', () => {
  const notifications = read('notifications.html');
  const main = read('assets/js/main.js');
  const utils = read('assets/js/utils.js');

  assert.doesNotMatch(notifications, /card\.innerHTML/);
  assert.match(notifications, /title\.textContent/);
  assert.match(notifications, /markRead\.addEventListener\('click'/);
  assert.match(main, /toast\.textContent = String\(message/);
  assert.match(utils, /toast\.textContent = String\(message/);
  assert.doesNotMatch(main, /Save push notification to Firestore/);
});

test('Firestore rules do not allow anonymous public writes', () => {
  const rules = read('firestore.rules');

  assert.doesNotMatch(rules, /allow create: if true/);
  assert.doesNotMatch(rules, /source == ['"]fcm['"]/);
  assert.match(rules, /match \/notifications\/\{notifId\}/);
  assert.match(rules, /allow write: if isAdmin\(\) \|\| isOwner\(\);/);
  assert.match(rules, /allow create: if isSignedIn\(\) && request\.resource\.data\.userId == request\.auth\.uid/);
});

test('question loader preserves prerendered lessons when a JSON refresh is unavailable', () => {
  const loader = read('assets/js/questions-loader.js');

  assert.match(loader, /const prerenderedQuestions = document\.querySelector\('#question-container \.question-card'\)/);
  assert.match(loader, /Question data refresh unavailable; keeping prerendered questions/);
  assert.match(loader, /if \(prerenderedQuestions\) \{[\s\S]*?return;/);
});

test('Concept Mastery sanitizes authored HTML at the render boundary', () => {
  const app = read('learning/ui/concept-mastery/app.js');

  assert.match(app, /sanitizeRenderedHtml\(html\)/);
  assert.match(app, /dangerousElements = new Set\(\['base', 'embed', 'iframe', 'link', 'meta', 'object', 'script', 'style'\]\)/);
  assert.match(app, /name\.startsWith\('on'\)/);
  assert.match(app, /btn-reload-topic/);
});

test('auth overlay is excluded from MathJax traversal while it is mounted', () => {
  const auth = read('assets/js/require-auth.js');

  assert.match(auth, /overlay\.className = ['"]mathjax_ignore['"]/);
  assert.match(auth, /overlay\.style\.display = 'none'/);
  assert.match(auth, /window\.MathJax\?\.startup\?\.promise/);
});
