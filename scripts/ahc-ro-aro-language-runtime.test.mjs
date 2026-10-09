import assert from 'node:assert/strict';
import crypto from 'node:crypto';
import fs from 'node:fs';
import path from 'node:path';
import { execFileSync } from 'node:child_process';
import { createRequire } from 'node:module';
import { test } from 'node:test';
import { externalizeAhcRoAroLanguageRuntime, deduplicateAhcRoAroLanguageReferences, ahcRoAroLanguageRuntime } from './lib/ahc-ro-aro-language-runtime.mjs';

const require = createRequire(import.meta.url);
const { ROOT, siteFiles } = require('./seo-html.cjs');
const pages = siteFiles().filter(file => file.startsWith('ahc-ro-aro/') && file.endsWith('/index.html'));
const expectedPages = [
  'ahc-ro-aro/index.html',
  'ahc-ro-aro/agriculture-commerce-trade/allied-revolutions/index.html',
  'ahc-ro-aro/agriculture-commerce-trade/major-crops/index.html',
  'ahc-ro-aro/agriculture-commerce-trade/types-of-farming/index.html',
  'ahc-ro-aro/computer-knowledge/cpu-architecture-registers/index.html',
  'ahc-ro-aro/computer-knowledge/inputoutput-devices/index.html',
  'ahc-ro-aro/computer-knowledge/memory-types/index.html',
  'ahc-ro-aro/general-science/acids-bases-salts/index.html',
  'ahc-ro-aro/general-science/atomic-structure/index.html',
  'ahc-ro-aro/general-science/carbon-its-compounds/index.html',
  'ahc-ro-aro/general-science/cell-biology/index.html',
  'ahc-ro-aro/general-science/electricity-magnetism/index.html',
  'ahc-ro-aro/general-science/matter-its-states/index.html',
  'ahc-ro-aro/general-science/metals-non-metals/index.html',
  'ahc-ro-aro/general-science/motion-forces/index.html',
  'ahc-ro-aro/general-science/sound-light/index.html',
  'ahc-ro-aro/general-science/units-measurements/index.html',
  'ahc-ro-aro/general-science/work-energy-power/index.html',
  'ahc-ro-aro/geography/continents-major-oceans/index.html',
  'ahc-ro-aro/geography/mountains-plateaus-plains/index.html',
  'ahc-ro-aro/history-of-india/buddhism/index.html',
  'ahc-ro-aro/history-of-india/indus-valley-civilization/index.html',
  'ahc-ro-aro/history-of-india/jainism/index.html',
  'ahc-ro-aro/history-of-india/pre-historic-period/index.html',
  'ahc-ro-aro/history-of-india/vedic-period/index.html',
  'ahc-ro-aro/indian-national-movement/formation-of-inc/index.html',
  'ahc-ro-aro/indian-national-movement/moderate-extremist-phases/index.html',
  'ahc-ro-aro/indian-national-movement/swadeshi-movement/index.html',
  'ahc-ro-aro/polity-economy-culture/constituent-assembly/index.html',
  'ahc-ro-aro/polity-economy-culture/preamble/index.html',
  'ahc-ro-aro/population-ecology-urbanisation/census-2011-highlights/index.html',
  'ahc-ro-aro/up-special-knowledge/major-universities-institutes/index.html',
  'ahc-ro-aro/up-special-knowledge/primary-secondary-schemes/index.html',
].sort();

test('AHC reference deduplication retains all CPU lesson bytes except two identical script-tag lines', () => {
  const file = 'ahc-ro-aro/computer-knowledge/cpu-architecture-registers/index.html';
  const original = execFileSync('git', ['show', `5d341a929ac7484c0c9c6e84486dab4e33a95995:${file}`], { cwd: ROOT, encoding: 'utf8', maxBuffer: 5e6 });
  const current = fs.readFileSync(path.join(ROOT, file), 'utf8').replace(/\r\n/g, '\n');
  assert.equal((original.match(/data-ahc-ro-aro-language="shared"/g) || []).length, 3);
  const normalizeAssetVersions = html => html.replace(/([?&]v=)[^"'&#\s]+/g, '$1<CACHE_VERSION>');
  assert.equal(normalizeAssetVersions(current), normalizeAssetVersions(deduplicateAhcRoAroLanguageReferences(original).replace(/\r\n/g, '\n')));
  assert.equal((current.match(/data-ahc-ro-aro-language="shared"/g) || []).length, 1);
  assert.equal(deduplicateAhcRoAroLanguageReferences(current), current);
  assert.throws(() => deduplicateAhcRoAroLanguageReferences('<script data-ahc-ro-aro-language="shared" src="other.js"></script>'), /cannot deduplicate/);
});

test('AHC RO/ARO language controller extraction has exact coverage and stays idempotent', () => {
  const migratedPages = [];
  for (const file of pages) {
    const current = fs.readFileSync(path.join(ROOT, file), 'utf8');
    if (current.includes(ahcRoAroLanguageRuntime.attribute)) migratedPages.push(file);
    assert.equal(externalizeAhcRoAroLanguageRuntime(current), current, `no residual inline or duplicate runtime in ${file}`);
  }
  assert.equal(pages.length, 249);
  assert.deepEqual(migratedPages.sort(), expectedPages, 'only the 32 intended language-variant pages use the shared runtime');
  const source = fs.readFileSync(path.join(ROOT, ahcRoAroLanguageRuntime.asset.slice(1)), 'utf8').trim();
  assert.equal(Buffer.byteLength(source), ahcRoAroLanguageRuntime.bytes);
  assert.equal(crypto.createHash('sha256').update(source).digest('hex'), ahcRoAroLanguageRuntime.sha256);
});

