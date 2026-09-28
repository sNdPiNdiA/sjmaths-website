// Mechanical migration: replace only an exact stylesheet, never serialize HTML.
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import { fileURLToPath } from 'node:url';
import { externalizeHistoryStyles } from './lib/history-styles.mjs';

const root = fileURLToPath(new URL('..', import.meta.url));
const apply = process.argv.includes('--apply');
const target = process.argv.find(arg => arg.startsWith('--file='))?.slice(7);
const files = [];
function collect(directory) {
  for (const entry of fs.readdirSync(directory, { withFileTypes: true })) {
    const absolute = path.join(directory, entry.name);
    if (entry.isDirectory()) collect(absolute);
    else if (entry.name.endsWith('.html')) files.push(absolute);
  }
}
if (target) {
  const absolute = path.resolve(root, target);
  const relative = path.relative(path.join(root, 'history'), absolute);
  if (relative.startsWith('..') || path.isAbsolute(relative) || !absolute.endsWith('.html')) throw new Error('Choose a History HTML file.');
  files.push(absolute);
} else collect(path.join(root, 'history'));
const hash = text => crypto.createHash('sha256').update(text).digest('hex');
const changes = [];
for (const file of files) {
  const before = fs.readFileSync(file, 'utf8');
  const after = externalizeHistoryStyles(before);
  if (before === after) continue;
  const body = html => html.slice(html.indexOf('<body'));
  if (body(before) !== body(after)) throw new Error(`Body changed: ${file}`);
  changes.push({ file: path.relative(root, file), before: hash(before), after: hash(after), bodyUnchanged: true });
  if (apply) fs.writeFileSync(file, after);
}
console.log(JSON.stringify({ mode: apply ? 'apply' : 'dry-run', changed: changes.length, changes }, null, 2));
