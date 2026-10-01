// Read-only proof of source moves, not an API generation run.
import fs from 'node:fs';
import { fileURLToPath } from 'node:url';
import { readGitBaseline } from './lib/git-baseline.mjs';
import { agricultureGeneratedRuntime } from './lib/agriculture-runtime.mjs';
const baseline = process.argv.find(arg => arg.startsWith('--baseline='))?.slice(11) || '41b8e41e51';
const originals = new Map();
for await (const [file, bytes] of readGitBaseline(['scripts/generate_agriculture.mjs', 'scripts/redesign_all_agriculture.mjs'], { root: fileURLToPath(new URL('../', import.meta.url)), baseline })) originals.set(file, bytes.toString('utf8').replace(/\r\n/g, '\n'));
const read = name => fs.readFileSync(new URL(name, import.meta.url), 'utf8').replace(/\r\n/g, '\n');
const generator = originals.get('scripts/generate_agriculture.mjs');
const redesign = originals.get('scripts/redesign_all_agriculture.mjs');
const renderer = generator.slice(generator.indexOf('function renderTopicHtml('), generator.indexOf('/**\n * Process single topic')).trim();
const section = redesign.slice(redesign.indexOf('const customCss ='), redesign.indexOf('let successCount =')).trimEnd();
const css = section.slice(0, section.indexOf('const upgradedScript =')).trimEnd();
const transform = section.slice(section.indexOf('function transformHtml('));
if (!renderer.startsWith('function ') || !transform.startsWith('function ')) throw new Error('Use a pre-extraction source baseline.');
const expectedGenerator = generator.replace(renderer + '\n', '')
  .replace("import { jsonrepair } from 'jsonrepair';", "import { jsonrepair } from 'jsonrepair';\nimport { renderTopicHtml } from './lib/agriculture-renderer.mjs';")
  .replace('/**\n * Convert structured data into static, accessible English HTML\n */\n\n', '');
const expectedRedesign = redesign.replace(section + '\n', '')
  .replace("import path from 'path';", "import path from 'path';\nimport { transformHtml } from './lib/agriculture-redesign.mjs';");
const expectedRenderer = renderer.replace(/^function renderTopicHtml/, 'export function renderTopicHtml')
  .replace('<script>\n' + agricultureGeneratedRuntime + '\n</script>', '${agricultureGeneratedScript}');
const expectedTransform = css + '\n\n' + transform.replace(/^function transformHtml/, 'export function transformHtml').replace('let updated = html;', 'let updated = hydrateAgricultureRuntime(html);');
const currentRenderer = read('./lib/agriculture-renderer.mjs');
const currentTransform = read('./lib/agriculture-redesign.mjs');
const checks = {
  generatorPromptsAndOrchestration: expectedGenerator.trim() === read('./generate_agriculture.mjs').trim(),
  redesignInventoryAndWriteLoop: expectedRedesign.trim() === read('./redesign_all_agriculture.mjs').trim(),
  completeRendererBody: expectedRenderer.trim() === currentRenderer.slice(currentRenderer.indexOf('export function renderTopicHtml')).trim(),
  completeRedesignBody: expectedTransform.trim() === currentTransform.slice(currentTransform.indexOf('const customCss =')).trim(),
};
console.log(JSON.stringify({ baseline, checks }, null, 2));
if (!Object.values(checks).every(Boolean)) process.exitCode = 1;
