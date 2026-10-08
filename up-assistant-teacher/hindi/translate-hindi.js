import { spawnSync } from 'node:child_process';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const scriptDir = path.dirname(fileURLToPath(import.meta.url));
const translator = path.resolve(scriptDir, '../../scripts/translate-up-assistant-content.cjs');
const args = process.argv.slice(2);
const topic = args.find(arg => !arg.startsWith('--'));
const options = args.filter(arg => arg.startsWith('--'));
if (topic && !options.some(arg => arg.startsWith('--topic='))) options.push(`--topic=${topic}`);

const result = spawnSync(process.execPath, [translator, '--subject=hindi', ...options], {
  cwd: path.resolve(scriptDir, '../..'),
  stdio: 'inherit',
});
if (result.error) throw result.error;
process.exitCode = result.status ?? 1;
