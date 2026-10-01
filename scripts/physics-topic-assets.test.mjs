import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import crypto from 'node:crypto';
import { execFileSync } from 'node:child_process';
import { createRequire } from 'node:module';
import {
  externalizePhysicsTopicAssets,
  externalizePhysicsTopicGenerator,
  physicsTopicRuntimeTag,
  physicsTopicStyleLink,
} from './lib/physics-topic-assets.mjs';

const require = createRequire(import.meta.url);
const { ROOT } = require('./seo-html.cjs');
const baseline = '4a81ff7b7c9adce1ae0eba3f7243c9d722ad400a';
const style = fs.readFileSync(new URL('../assets/css/physics-topic.css', import.meta.url), 'utf8').trim();
const runtime = fs.readFileSync(new URL('../assets/js/physics-topic.js', import.meta.url), 'utf8').trim();
const digest = value => crypto.createHash('sha256').update(value).digest('hex');

test('Physics assets are the exact audited shared sources', () => {
  assert.equal(Buffer.byteLength(style), 3882);
  assert.equal(digest(style), 'fdf3c36424441f087480b91f456c40fb6dd73df9937ceef0f6806e758e7b54b4');
  assert.equal(Buffer.byteLength(runtime), 863);
  assert.equal(digest(runtime), '5313d99c8342d8310f6f7b1d126e28098be256e42f6e62614d0560fff3bd5544');
});

test('exact extraction preserves neighbors and leaves attributed variants untouched', () => {
  const page = `<head><style>\n${style}\n</style><style media="print">print-only</style></head><body><script>\n${runtime}\n</script><script defer>${runtime}</script><script type="application/ld+json">{"name":"Physics"}</script></body>`;
  const expected = `<head>${physicsTopicStyleLink}<style media="print">print-only</style></head><body>${physicsTopicRuntimeTag}<script defer>${runtime}</script><script type="application/ld+json">{"name":"Physics"}</script></body>`;
  const external = externalizePhysicsTopicAssets(page, style, runtime);
  assert.equal(external, expected);
  assert.equal(externalizePhysicsTopicAssets(external, style, runtime), external);
  assert.match(external, /<script defer>/);
  assert.match(external, /application\/ld\+json/);
});

test('generator changes only the exact stylesheet and parser-blocking controller', () => {
  const original = execFileSync('git', ['show', `${baseline}:scripts/generate_physics.mjs`], {
    cwd: ROOT, encoding: 'utf8', maxBuffer: 20e6,
  });
  const current = fs.readFileSync(new URL('../scripts/generate_physics.mjs', import.meta.url), 'utf8');
  assert.equal(externalizePhysicsTopicGenerator(original, style, runtime), current);
  assert.equal((current.match(/data-physics-topic-style="lesson"/g) || []).length, 1);
  assert.equal((current.match(/data-physics-topic-runtime="lesson"/g) || []).length, 1);
});
