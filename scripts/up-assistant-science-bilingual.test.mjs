import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const SCIENCE = path.join(ROOT, 'up-assistant-teacher', 'science');
const STRUCTURAL_KEYS = new Set(['type', 'id', 'slug', 'url', 'href', 'src', 'icon']);

function assertBilingual(value, topic, key = '') {
  if (Array.isArray(value)) {
    for (const item of value) assertBilingual(item, topic, key);
    return;
  }
  if (value && typeof value === 'object') {
    if (typeof value.en === 'string' && typeof value.hi === 'string') {
      assert(value.en.trim(), `${topic}: empty English value at ${key}`);
      assert(value.hi.trim(), `${topic}: empty Hindi value at ${key}`);
      const formulas = text => [...text.matchAll(/\$[^$]*\$/g)].map(match => match[0]);
      assert.deepEqual(formulas(value.en), formulas(value.hi), `${topic}: formula mismatch at ${key}`);
      return;
    }
    for (const [childKey, child] of Object.entries(value)) assertBilingual(child, topic, childKey);
    return;
  }
  if (typeof value === 'string' && value.trim() && !STRUCTURAL_KEYS.has(key)) {
    assert.fail(`${topic}: untranslated string at ${key}: ${value.slice(0, 80)}`);
  }
}

const topics = fs.readdirSync(SCIENCE, { withFileTypes: true }).filter(entry => entry.isDirectory()).map(entry => entry.name).sort();

test('every Assistant Teacher Science topic keeps complete bilingual source data and matching crawlable data', () => {
  assert.equal(topics.length, 12);
  for (const topic of topics) {
    const directory = path.join(SCIENCE, topic);
    const data = JSON.parse(fs.readFileSync(path.join(directory, 'data.json'), 'utf8'));
    const html = fs.readFileSync(path.join(directory, 'index.html'), 'utf8');
    const match = html.match(/<script id="upsc-page-data" type="application\/json">([\s\S]*?)<\/script>/);
    assert(match, `${topic}: embedded page data is missing`);
    const pageData = JSON.parse(match[1]);
    assertBilingual(data.concepts, topic);
    assert.deepEqual(pageData.concepts, data.concepts, `${topic}: inline concepts differ from data.json`);
    assert.equal((html.match(/id="upsc-page-data"/g) || []).length, 1, `${topic}: duplicate page data block`);
    assert.equal((html.match(/<\/html>/g) || []).length, 1, `${topic}: invalid closing HTML structure`);
    assert.match(html, /upsc-renderer\.e208a1f3d3da\.min\.js\?v=e208a1f3d3da-bilingual-v4/, `${topic}: shared renderer asset is stale`);
  }
});

test('shared renderer typesets formulas added by tab changes and revises from existing takeaways', () => {
  const renderer = fs.readFileSync(path.join(ROOT, 'assets', 'js', 'upsc-renderer.js'), 'utf8');
  assert.match(renderer, /window\.renderMathInElement\(topicContent/);
  assert.match(renderer, /const revisionTakeaways = pageData\.concepts\?\.keyTakeaways \|\| \[\]/);
  assert.match(renderer, /!hasStructuredRevision && revisionTakeaways\.length/);
});
