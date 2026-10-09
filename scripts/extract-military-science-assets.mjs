import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { commitBuildWrites } from './lib/build-transaction.mjs';
import {
  militaryScienceTopicCss,
  militaryScienceTopicStyleLink,
  externalizeMilitaryScienceAssets,
  hydrateMilitaryScienceAssets
} from './lib/military-science-assets.mjs';

const root = fileURLToPath(new URL('..', import.meta.url));
const apply = process.argv.includes('--apply');
const hydrate = process.argv.includes('--hydrate');

function findHtmlFiles(dir) {
  let results = [];
  try {
    for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
      const full = path.join(dir, entry.name);
      if (entry.isDirectory()) results.push(...findHtmlFiles(full));
      else if (entry.name.endsWith('.html')) results.push(full);
    }
  } catch (e) {}
  return results;
}

const dir = path.join(root, 'military-science');
const files = findHtmlFiles(dir);

const writes = new Map();
const changedPages = [];

for (const absolute of files) {
  const relative = path.relative(root, absolute).replace(/\\/g, '/');
  const before = fs.readFileSync(absolute, 'utf8');
  const after = hydrate ? hydrateMilitaryScienceAssets(before) : externalizeMilitaryScienceAssets(before);
  if (before === after) continue;

  if (!hydrate) {
    // Verify that the body content is 100% byte-for-byte identical
    const bodyStartBefore = before.search(/<body\b/i);
    const bodyStartAfter = after.search(/<body\b/i);
    if (before.slice(bodyStartBefore) !== after.slice(bodyStartAfter)) {
      throw new Error(`Body content altered in ${relative}`);
    }

    // Verify roundtrip
    const roundtrip = hydrateMilitaryScienceAssets(after);
    // Normalize newlines for strict roundtrip check
    const normBefore = before.replace(/\r\n/g, '\n').trim();
    const normRoundtrip = roundtrip.replace(/\r\n/g, '\n').trim();
    if (normBefore !== normRoundtrip) {
      // Check if diff is only style whitespace
      const stripBefore = normBefore.replace(/<style\b[^>]*>[\s\S]*?<\/style>/i, '<style></style>');
      const stripRoundtrip = normRoundtrip.replace(/<style\b[^>]*>[\s\S]*?<\/style>/i, '<style></style>');
      if (stripBefore !== stripRoundtrip) {
        throw new Error(`Roundtrip structure mismatch in ${relative}`);
      }
    }
  }

  changedPages.push(relative);
  writes.set(absolute, Buffer.from(after, 'utf8'));
}

// Also check generator scripts/generate_military_science.mjs
const generatorFile = path.join(root, 'scripts/generate_military_science.mjs');
if (fs.existsSync(generatorFile)) {
  const genBefore = fs.readFileSync(generatorFile, 'utf8');
  const genAfter = hydrate
    ? genBefore.replace(militaryScienceTopicStyleLink, `<style>\n${militaryScienceTopicCss}\n</style>`)
    : externalizeMilitaryScienceAssets(genBefore);

  if (genBefore !== genAfter) {
    writes.set(generatorFile, Buffer.from(genAfter, 'utf8'));
  }
}

const summary = {
  mode: apply ? 'applied' : 'dry-run',
  operation: hydrate ? 'hydrate' : 'externalize',
  totalFilesScanned: files.length,
  changedPagesCount: changedPages.length,
  sampleChanged: changedPages.slice(0, 5)
};

if (apply && writes.size > 0) {
  commitBuildWrites(writes);
}

console.log(JSON.stringify(summary, null, 2));
