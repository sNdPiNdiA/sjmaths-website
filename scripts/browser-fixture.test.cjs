const test = require('node:test');
const assert = require('node:assert/strict');
const { ROOT } = require('./seo-html.cjs');
const { routeRepositoryFixtures } = require('./lib/browser-fixture.cjs');

test('browser fixtures acknowledge guest analytics writes locally and leave other Firestore requests untouched', async () => {
  let handler;
  const page = { on() {}, async route(pattern, callback) { handler = callback; } };
  const evidence = await routeRepositoryFixtures(page, { root: ROOT, files: ['index.html'] });
  const root = 'https://firestore.googleapis.com/v1/projects/sjmaths-web/databases/(default)/documents/users/';
  for (const [resource, method, expected] of [
    ['user_abc123_1790951725355?currentDocument.exists=false', 'PATCH', 'fixture'],
    ['user_abc123_1790951725355/user_actions', 'POST', 'fixture'],
    ['user_abc123_1790951725355/page_views', 'POST', 'fixture'],
    ['signedInFirebaseUid', 'PATCH', 'continue'],
    ['user_abc123_1790951725355', 'GET', 'continue'],
    ['user_abc123_1790951725355/learning-progress', 'POST', 'continue'],
  ]) {
    let outcome;
    await handler({
      request() { return { url: () => root + resource, method: () => method }; },
      async fulfill(response) { assert.equal(response.status, 200); assert.deepEqual(JSON.parse(response.body), {}); outcome = 'fixture'; },
      async continue() { outcome = 'continue'; },
    });
    assert.equal(outcome, expected, `${method} ${resource}`);
  }
  assert.equal(evidence.exclusions.filter(value => value === 'firestore-guest-analytics').length, 3);
});
