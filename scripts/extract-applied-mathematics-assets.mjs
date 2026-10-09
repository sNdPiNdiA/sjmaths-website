import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import { fileURLToPath } from 'node:url';
import { commitBuildWrites } from './lib/build-transaction.mjs';
import {
  appliedMathematicsTopicCss,
  appliedMathematicsTopicJs,
  appliedMathematicsTopicStyleLink,
  appliedMathematicsTopicScriptTag,
  externalizeAppliedMathematicsAssets,
  hydrateAppliedMathematicsAssets
} from './lib/applied-mathematics-assets.mjs';

const root = fileURLToPath(new URL('..', import.meta.url));
const apply = process.argv.includes('--apply');

function findHtmlFiles(dir) {
  let results = [];
  for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
    const full = path.join(dir, entry.name);
    if (entry.isDirectory()) results.push(...findHtmlFiles(full));
    else if (entry.name.endsWith('.html')) results.push(full);
  }
  return results;
}

const dir = path.join(root, 'class-11-applied-mathematics');
const files = findHtmlFiles(dir);

const writes = new Map();
const changedPages = [];

for (const absolute of files) {
  const relative = path.relative(root, absolute).replace(/\\/g, '/');
  const before = fs.readFileSync(absolute, 'utf8');
  const after = externalizeAppliedMathematicsAssets(before);
  if (before === after) continue;

  // Verify that the body content except for the script tag replacement did not change
  const stripScript = s => s.replace(/<script\b(?![^>]*\bsrc=)[^>]*>[\s\S]*?<\/script>/gi, '')
                            .replace(/<script\b[^>]*data-applied-maths-script="tabs"[^>]*><\/script>/gi, '')
                            .replace(/\s+/g, ' ').trim();
  const bodyBefore = stripScript(before.slice(before.search(/<body\b/i)));
  const bodyAfter = stripScript(after.slice(after.search(/<body\b/i)));

  if (bodyBefore !== bodyAfter) {
    throw new Error(`Body content altered in ${relative}`);
  }

  // Verify roundtrip
  const roundtrip = hydrateAppliedMathematicsAssets(after);
  const normalize = t => t.replace(/\r\n/g, '\n').replace(/\s+/g, ' ').trim();
  if (normalize(roundtrip) !== normalize(before)) {
    throw new Error(`Roundtrip mismatch in ${relative}`);
  }

  changedPages.push(relative);
  writes.set(absolute, Buffer.from(after, 'utf8'));
}

console.log(JSON.stringify({
  mode: apply ? 'apply' : 'dry-run',
  totalFiles: files.length,
  changedPagesCount: changedPages.length,
  savedCssBytes: changedPages.length * appliedMathematicsTopicCss.length,
  savedJsBytes: changedPages.length * appliedMathematicsTopicJs.length,
  sampleChanged: changedPages.slice(0, 3)
}, null, 2));

if (apply) {
  commitBuildWrites(writes);
  console.log(`Successfully committed updates to ${writes.size} files.`);
}
