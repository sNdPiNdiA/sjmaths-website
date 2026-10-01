import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import { createRequire } from 'node:module';
import { commitBuildWrites } from './lib/build-transaction.mjs';
import { externalizePhysicsTopicAssets, externalizePhysicsTopicGenerator } from './lib/physics-topic-assets.mjs';

const require = createRequire(import.meta.url);
const { ROOT, siteFiles } = require('./seo-html.cjs');
const apply = process.argv.includes('--apply');
const sample = 'physics/electricity-and-magnetism/alternating-current/ac-bridges/index.html';
const expected = {
  style: { bytes: 3882, sha256: 'fdf3c36424441f087480b91f456c40fb6dd73df9937ceef0f6806e758e7b54b4' },
  runtime: { bytes: 863, sha256: '5313d99c8342d8310f6f7b1d126e28098be256e42f6e62614d0560fff3bd5544' },
};
const hash = value => crypto.createHash('sha256').update(value).digest('hex');
const sampleHtml = fs.readFileSync(path.join(ROOT, sample), 'utf8');
const styleMatch = sampleHtml.match(/<style>([\s\S]*?)<\/style>/i);
const scriptMatches = [...sampleHtml.matchAll(/<script>([\s\S]*?)<\/script>/gi)];
const runtimeMatch = scriptMatches.find(match => match[1].includes("document.querySelectorAll('.tab')"));
const styleAsset = path.join(ROOT, 'assets/css/physics-topic.css');
const runtimeAsset = path.join(ROOT, 'assets/js/physics-topic.js');
const style = (styleMatch?.[1] ?? (fs.existsSync(styleAsset) ? fs.readFileSync(styleAsset, 'utf8') : '')).trim();
const runtime = (runtimeMatch?.[1] ?? (fs.existsSync(runtimeAsset) ? fs.readFileSync(runtimeAsset, 'utf8') : '')).trim();
if (!style || !runtime) throw new Error('Canonical Physics page/assets are missing the exact style or interaction runtime.');
for (const [name, source] of [['style', style], ['runtime', runtime]]) {
  const fingerprint = { bytes: Buffer.byteLength(source), sha256: hash(source) };
  if (fingerprint.bytes !== expected[name].bytes || fingerprint.sha256 !== expected[name].sha256) {
    throw new Error(`Unexpected Physics ${name} source: ${JSON.stringify(fingerprint)}`);
  }
}

const pages = siteFiles().filter(file => file.startsWith('physics/') && file.endsWith('/index.html'));
if (pages.length !== 325) throw new Error(`Expected 325 Physics topic pages; found ${pages.length}.`);
const writes = new Map();
const changedPages = [];
for (const file of pages) {
  const absolute = path.join(ROOT, file);
  const before = fs.readFileSync(absolute, 'utf8');
  const after = externalizePhysicsTopicAssets(before, style, runtime);
  const inlineStyles = [...before.matchAll(/<style>([\s\S]*?)<\/style>/gi)].filter(match => match[1].trim() === style).length;
  const inlineRuntimes = [...before.matchAll(/<script>([\s\S]*?)<\/script>/gi)].filter(match => match[1].trim() === runtime).length;
  const existingStyleRefs = (before.match(/data-physics-topic-style="lesson"/g) || []).length;
  const existingRuntimeRefs = (before.match(/data-physics-topic-runtime="lesson"/g) || []).length;
  if (inlineStyles + existingStyleRefs !== 1 || inlineRuntimes + existingRuntimeRefs !== 1) {
    throw new Error(`Unexpected style/runtime combination in ${file}.`);
  }
  const styleRefs = (after.match(/data-physics-topic-style="lesson"/g) || []).length;
  const runtimeRefs = (after.match(/data-physics-topic-runtime="lesson"/g) || []).length;
  if (styleRefs !== 1 || runtimeRefs !== 1) throw new Error(`Expected one shared style and runtime reference in ${file}.`);
  if (before !== after) {
    changedPages.push(file);
    writes.set(absolute, Buffer.from(after, 'utf8'));
  }
}
if (![0, 325].includes(changedPages.length)) throw new Error(`Expected 0 or 325 exact page replacements; found ${changedPages.length}.`);

const generatorPath = path.join(ROOT, 'scripts/generate_physics.mjs');
const generatorBefore = fs.readFileSync(generatorPath, 'utf8');
const generatorAfter = externalizePhysicsTopicGenerator(generatorBefore, style, runtime);
if ((generatorAfter.match(/data-physics-topic-style="lesson"/g) || []).length !== 1
  || (generatorAfter.match(/data-physics-topic-runtime="lesson"/g) || []).length !== 1) {
  throw new Error('Expected exactly one owned style and runtime reference in the Physics generator.');
}
if (generatorBefore !== generatorAfter) writes.set(generatorPath, Buffer.from(generatorAfter, 'utf8'));

for (const [relative, content] of [
  ['assets/css/physics-topic.css', `${style}\n`],
  ['assets/js/physics-topic.js', `${runtime}\n`],
]) {
  const absolute = path.join(ROOT, relative);
  if (fs.existsSync(absolute)) {
    if (fs.readFileSync(absolute, 'utf8').trim() !== content.trim()) throw new Error(`Existing asset differs: ${relative}`);
  } else writes.set(absolute, Buffer.from(content, 'utf8'));
}

if (apply) commitBuildWrites(writes);
console.log(JSON.stringify({ mode: apply ? 'apply' : 'dry-run', pages: pages.length, changedPages: changedPages.length, generatorChanged: generatorBefore !== generatorAfter, extractedAssets: ['assets/css/physics-topic.css', 'assets/js/physics-topic.js'], writes: writes.size }, null, 2));
