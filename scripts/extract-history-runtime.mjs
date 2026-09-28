// Only the exact shared runtime is replaced. All other bytes stay untouched.
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import { fileURLToPath } from 'node:url';
import { externalizeHistoryRuntime } from './lib/history-runtime.mjs';

const root = fileURLToPath(new URL('..', import.meta.url));
const apply = process.argv.includes('--apply');
const changes = [];
const hash = text => crypto.createHash('sha256').update(text).digest('hex');
function migrate(directory) {
  for (const entry of fs.readdirSync(directory, { withFileTypes: true })) {
    const file = path.join(directory, entry.name);
    if (entry.isDirectory()) { migrate(file); continue; }
    if (!entry.name.endsWith('.html')) continue;
    const before = fs.readFileSync(file, 'utf8');
    const after = externalizeHistoryRuntime(before);
    if (before === after) continue;
    const omitRuntime = html => html.replace(/<script id="history-runtime"(?: src="\/assets\/js\/history-topic\.js")?>[\s\S]*?<\/script>/g, '');
    if (omitRuntime(before) !== omitRuntime(after)) throw new Error(`Content changed: ${file}`);
    changes.push({ file: path.relative(root, file), before: hash(before), after: hash(after), otherBytesUnchanged: true });
    if (apply) fs.writeFileSync(file, after);
  }
}
migrate(path.join(root, 'history'));
console.log(JSON.stringify({ mode: apply ? 'apply' : 'dry-run', changed: changes.length, changes }, null, 2));
