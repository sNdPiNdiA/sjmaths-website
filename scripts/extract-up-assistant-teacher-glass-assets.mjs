import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { commitBuildWrites } from './lib/build-transaction.mjs';
import {
  upAssistantTeacherGlassCss,
  upAssistantTeacherGlassStyleLink,
  externalizeUpAssistantGlassAssets,
  hydrateUpAssistantGlassAssets
} from './lib/up-assistant-teacher-glass-assets.mjs';

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

const dir = path.join(root, 'up-assistant-teacher');
const files = findHtmlFiles(dir);

const writes = new Map();
const changedPages = [];

for (const absolute of files) {
  const relative = path.relative(root, absolute).replace(/\\/g, '/');
  const before = fs.readFileSync(absolute, 'utf8');
  const after = hydrate ? hydrateUpAssistantGlassAssets(before) : externalizeUpAssistantGlassAssets(before);
  if (before === after) continue;

  if (!hydrate) {
    // Verify that the body content is 100% byte-for-byte identical
    const bodyStartBefore = before.search(/<body\b/i);
    const bodyStartAfter = after.search(/<body\b/i);
    if (before.slice(bodyStartBefore) !== after.slice(bodyStartAfter)) {
      throw new Error(`Body content altered in ${relative}`);
    }

    // Verify roundtrip
    const roundtrip = hydrateUpAssistantGlassAssets(after);
    const normBefore = before.replace(/\r\n/g, '\n').trim();
    const normRoundtrip = roundtrip.replace(/\r\n/g, '\n').trim();
    if (normBefore !== normRoundtrip) {
      throw new Error(`Roundtrip mismatch in ${relative}`);
    }
  }

  changedPages.push(relative);
  writes.set(absolute, Buffer.from(after, 'utf8'));
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
