import assert from 'node:assert/strict';
import crypto from 'node:crypto';
import fs from 'node:fs';
import path from 'node:path';
import { createRequire } from 'node:module';
import { test } from 'node:test';
import { readGitBaseline } from './lib/git-baseline.mjs';
import { externalizeAhcRoAroLanguageRuntime, ahcRoAroLanguageRuntime } from './lib/ahc-ro-aro-language-runtime.mjs';

const require = createRequire(import.meta.url);
const { ROOT, siteFiles } = require('./seo-html.cjs');
const baseline = '9dd18d6c9c2c8b8bc252757a2cd10d404d3e2773';
const pages = siteFiles().filter(file => file.startsWith('ahc-ro-aro/') && file.endsWith('/index.html'));

test('AHC RO/ARO language controller extraction preserves exact pages and untouched variants', async () => {
  let migrated = 0, references = 0;
  for await (const [file, bytes] of readGitBaseline(pages, { root: ROOT, baseline })) {
    const original = bytes.toString('utf8');
    const expected = externalizeAhcRoAroLanguageRuntime(original);
    const current = fs.readFileSync(path.join(ROOT, file), 'utf8');
    if (expected !== original) migrated++;
    assert.equal(current, expected, `only the exact controller changes in ${file}`);
    references += (current.match(new RegExp(ahcRoAroLanguageRuntime.attribute, 'g')) || []).length;
  }
  assert.equal(migrated, 32);
  assert.equal(references, 32);
  const source = fs.readFileSync(path.join(ROOT, ahcRoAroLanguageRuntime.asset.slice(1)), 'utf8').trim();
  assert.equal(Buffer.byteLength(source), ahcRoAroLanguageRuntime.bytes);
  assert.equal(crypto.createHash('sha256').update(source).digest('hex'), ahcRoAroLanguageRuntime.sha256);
});

