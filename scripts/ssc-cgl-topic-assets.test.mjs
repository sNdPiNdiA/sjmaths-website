import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import crypto from 'node:crypto';
import {
  externalizeSscCglTopicAssets,
  hydrateSscCglTopicAssets,
  sscCglTopicRuntimeTag,
  sscCglTopicStyleLink,
} from './lib/ssc-cgl-topic-assets.mjs';

const style = fs.readFileSync(new URL('../assets/css/ssc-cgl-topic.css', import.meta.url), 'utf8').trim();
const runtime = fs.readFileSync(new URL('../assets/js/ssc-cgl-topic.js', import.meta.url), 'utf8').trim();
const digest = value => crypto.createHash('sha256').update(value).digest('hex');

test('SSC-CGL assets equal the audited 152-page sources', () => {
  assert.equal(Buffer.byteLength(style), 6082);
  assert.equal(digest(style), 'd39350137fcac64dc47c7464d4d16c99a53c92844b702cec96e211bc75e95fc2');
  assert.equal(Buffer.byteLength(runtime), 1784);
  assert.equal(digest(runtime), '17dbf59ea9a0a18e4c4f49f87c1d30bb71bb1cdc6f41368d9b7bbe27c6814360');
});

test('exact extraction preserves order and leaves attributed or edited variants inline', () => {
  const html = `<head><style>\n${style}\n</style><style media="print">.print{display:block}</style></head><body><script>\n${runtime}\n</script><script defer>${runtime}</script><script>${runtime}\nwindow.localVariant=true;</script><footer>Topic footer</footer></body>`;
  const expected = `<head>${sscCglTopicStyleLink}<style media="print">.print{display:block}</style></head><body>${sscCglTopicRuntimeTag}<script defer>${runtime}</script><script>${runtime}\nwindow.localVariant=true;</script><footer>Topic footer</footer></body>`;
  const external = externalizeSscCglTopicAssets(html, style, runtime);
  assert.equal(external, expected);
  assert.equal(externalizeSscCglTopicAssets(external, style, runtime), external);
});

test('hydration recognizes staged minified, cache-busted references by ownership marker', () => {
  const html = `${sscCglTopicStyleLink.replace('ssc-cgl-topic.css', 'ssc-cgl-topic.min.css?v=abc')}<script src="/assets/js/ssc-cgl-topic.min.js?v=abc" data-ssc-cgl-topic-runtime="shared"></script>`;
  assert.equal(hydrateSscCglTopicAssets(html), `<style>${style}</style><script>${runtime}</script>`);
});
