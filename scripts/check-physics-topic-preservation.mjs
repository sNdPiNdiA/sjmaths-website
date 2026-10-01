import fs from 'node:fs';
import path from 'node:path';
import { createRequire } from 'node:module';
import { readGitBaseline } from './lib/git-baseline.mjs';
import { externalizePhysicsTopicAssets, externalizePhysicsTopicGenerator } from './lib/physics-topic-assets.mjs';

const require = createRequire(import.meta.url);
const { ROOT, siteFiles } = require('./seo-html.cjs');
const baseline = process.argv.find(value => value.startsWith('--baseline='))?.slice('--baseline='.length)
  || '4a81ff7b7c9adce1ae0eba3f7243c9d722ad400a';
const pages = siteFiles().filter(file => file.startsWith('physics/') && file.endsWith('/index.html'));
if (pages.length !== 325) throw new Error(`Expected 325 Physics topic pages; found ${pages.length}.`);
const generator = 'scripts/generate_physics.mjs';
let migrated = 0;
let checkedGenerator = false;

for await (const [file, bytes] of readGitBaseline([...pages, generator], { root: ROOT, baseline })) {
  const original = bytes.toString('utf8');
  const expected = file === generator
    ? externalizePhysicsTopicGenerator(original)
    : externalizePhysicsTopicAssets(original);
  const current = fs.readFileSync(path.join(ROOT, file), 'utf8');
  if (current !== expected) throw new Error(`Unexpected markup or generator change: ${file}`);
  if (file === generator) checkedGenerator = true;
  else if (current !== original) migrated++;
}

if (migrated !== pages.length || !checkedGenerator) {
  throw new Error(`Expected ${pages.length} exact page substitutions and one generator check; got ${migrated} pages.`);
}
console.log(JSON.stringify({ baseline, pages: pages.length, exactSubstitutions: migrated, generator: 'only the shared stylesheet and runtime references differ' }, null, 2));
