import assert from 'node:assert/strict';
import crypto from 'node:crypto';
import fs from 'node:fs';
import path from 'node:path';
import { createRequire } from 'node:module';
import { test } from 'node:test';
import { readGitBaseline } from './lib/git-baseline.mjs';
import { externalizeSscCglPolicyTabs, sscCglPolicyTabsRuntime } from './lib/ssc-cgl-policy-tabs.mjs';

const require = createRequire(import.meta.url);
const { ROOT, siteFiles } = require('./seo-html.cjs');
const baseline = 'aec62244f2281ab9fa115837f315ffd91e3faa6c';
const pages = siteFiles().filter(file => file.startsWith('ssc-cgl/general-awareness/general-policy-polity/') && file.endsWith('/index.html'));
const baselineSamples = [
  'ssc-cgl/general-awareness/general-policy-polity/citizenship-articles-5-11-and-caa/index.html',
  'ssc-cgl/general-awareness/general-policy-polity/parliament-lok-sabha-rajya-sabha-and-officers/index.html',
];

test('SSC-CGL policy tab runtime extraction is exact, scoped and idempotent', async () => {
  let sharedPages = 0;
  let targetedPages = 0;
  for (const file of pages) {
    const current = fs.readFileSync(path.join(ROOT, file), 'utf8');
    const shared = current.includes(sscCglPolicyTabsRuntime.attribute);
    const hasInline = [...current.matchAll(/<script\b([^>]*)>([\s\S]*?)<\/script>/gi)]
      .some(match => !/\bsrc\s*=/i.test(match[1]) && crypto.createHash('sha256').update(match[2].trim()).digest('hex') === sscCglPolicyTabsRuntime.sha256);
    if (shared || hasInline) targetedPages++;
    if (shared) sharedPages++;
    if (!shared && !hasInline) continue;
    assert.equal(externalizeSscCglPolicyTabs(current), current, `no residual inline or duplicate tab controller in ${file}`);
    assert.equal((current.match(/data-ssc-cgl-policy-progress="shared"/g) || []).length, 1, `${file} retains progress runtime`);
    assert.equal((current.match(/data-ssc-cgl-policy-mini-test="shared"/g) || []).length, 1, `${file} retains mini-test runtime`);
  }
  assert.equal(targetedPages, 18);
  assert.equal(sharedPages, 18);

  for await (const [file, bytes] of readGitBaseline(baselineSamples, { root: ROOT, baseline })) {
    const expected = externalizeSscCglPolicyTabs(bytes.toString('utf8'));
    const current = fs.readFileSync(path.join(ROOT, file), 'utf8');
    assert.equal(current.replace(/\r\n/g, '\n'), expected.replace(/\r\n/g, '\n'), `only the exact controller changes in ${file}`);
  }

  const source = fs.readFileSync(path.join(ROOT, sscCglPolicyTabsRuntime.asset.slice(1)), 'utf8').trim();
  assert.equal(Buffer.byteLength(source), sscCglPolicyTabsRuntime.bytes);
  assert.equal(crypto.createHash('sha256').update(source).digest('hex'), sscCglPolicyTabsRuntime.sha256);
});
