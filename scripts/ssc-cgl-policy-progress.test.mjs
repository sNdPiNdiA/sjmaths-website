import assert from 'node:assert/strict';
import crypto from 'node:crypto';
import fs from 'node:fs';
import path from 'node:path';
import { createRequire } from 'node:module';
import { test } from 'node:test';
import { readGitBaseline } from './lib/git-baseline.mjs';
import { externalizeSscCglPolicyProgress, sscCglPolicyProgressRuntime } from './lib/ssc-cgl-policy-progress.mjs';
import { externalizeSscCglPolicyMiniTest, sscCglPolicyMiniTestRuntime } from './lib/ssc-cgl-policy-mini-test.mjs';

const require = createRequire(import.meta.url);
const { ROOT, siteFiles } = require('./seo-html.cjs');
const baseline = '9dd18d6c9c2c8b8bc252757a2cd10d404d3e2773';
const pages = siteFiles().filter(file => file.startsWith('ssc-cgl/general-awareness/general-policy-polity/') && file.endsWith('/index.html'));

test('SSC-CGL polity shared controllers are exact and preserve every other page byte', async () => {
  let progressReferences = 0;
  let miniTestReferences = 0;
  let progressMigrations = 0;
  let miniTestMigrations = 0;
  for await (const [file, bytes] of readGitBaseline(pages, { root: ROOT, baseline })) {
    const original = bytes.toString('utf8');
    const progressExpected = externalizeSscCglPolicyProgress(original);
    const expected = externalizeSscCglPolicyMiniTest(progressExpected);
    const current = fs.readFileSync(path.join(ROOT, file), 'utf8');
    if (progressExpected !== original) progressMigrations++;
    if (expected !== progressExpected) miniTestMigrations++;
    if (expected !== original) assert.equal(current, expected, `only the exact controller changes in ${file}`);
    else assert.equal(current, original, `unrelated polity page remains byte-identical: ${file}`);
    progressReferences += (current.match(new RegExp(sscCglPolicyProgressRuntime.attribute, 'g')) || []).length;
    miniTestReferences += (current.match(new RegExp(sscCglPolicyMiniTestRuntime.attribute, 'g')) || []).length;
  }
  assert.equal(progressMigrations, 18);
  assert.equal(miniTestMigrations, 18);
  assert.equal(progressReferences, 18);
  assert.equal(miniTestReferences, 18);
  for (const runtime of [sscCglPolicyProgressRuntime, sscCglPolicyMiniTestRuntime]) {
    const asset = fs.readFileSync(path.join(ROOT, runtime.asset.slice(1)), 'utf8').trim();
    assert.equal(Buffer.byteLength(asset), runtime.bytes);
    assert.equal(crypto.createHash('sha256').update(asset).digest('hex'), runtime.sha256);
  }
});

