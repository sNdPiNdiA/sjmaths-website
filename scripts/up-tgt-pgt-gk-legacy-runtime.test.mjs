import test from 'node:test';
import assert from 'node:assert/strict';
import crypto from 'node:crypto';
import { execFileSync } from 'node:child_process';
import { ROOT } from './seo-html.cjs';
import {
  externalizeUpTgtPgtGkTopicRuntime,
  legacyEnglishOnlyUpTgtPgtGkRuntimeHash,
  upTgtPgtGkRuntimeTag,
} from './lib/up-tgt-pgt-gk-runtime.mjs';

const sample = 'up-tgt-pgt-gk/indian-history/vijayanagara/index.html';
const baseline = execFileSync('git', ['show', `afb5a3473445d7609eb3004b999c66b9d0215c70:${sample}`], { cwd: ROOT, encoding: 'utf8', maxBuffer: 20e6 });

test('legacy English-only GK runtime fingerprint and shared replacement are exact', () => {
  const originalScript = [...baseline.matchAll(/<script\b([^>]*)>([\s\S]*?)<\/script>/gi)]
    .map(match => match[2])
    .find(source => requireHash(source) === legacyEnglishOnlyUpTgtPgtGkRuntimeHash);
  assert.ok(originalScript);
  assert.equal(Buffer.byteLength(originalScript.trim()), 5069);
  for (const name of ['markQuiz', 'submitTest', 'startTimer']) assert.ok(originalScript.includes(`function ${name}(`));
  const after = externalizeUpTgtPgtGkTopicRuntime(baseline, legacyEnglishOnlyUpTgtPgtGkRuntimeHash);
  assert.equal((after.match(/data-up-tgt-pgt-gk-runtime="topic"/g) || []).length, 1);
  assert.ok(after.includes(upTgtPgtGkRuntimeTag));
  assert.equal(externalizeUpTgtPgtGkTopicRuntime(after, legacyEnglishOnlyUpTgtPgtGkRuntimeHash), after);
});

function requireHash(source) {
  return crypto.createHash('sha256').update(source).digest('hex');
}
