// Prove the move did not alter prompts, API/status orchestration or educational
// renderer/compiler code. Only imports, exports and runtime adapters may differ.
import fs from 'node:fs';
import { createRequire } from 'node:module';
import { readGitBaseline } from './lib/git-baseline.mjs';
import { legacyChemistryEnglish } from './lib/chemistry-runtime.mjs';
const require = createRequire(import.meta.url);
const { ROOT } = require('./seo-html.cjs');
const baseline = process.argv.find(arg => arg.startsWith('--baseline='))?.slice(11) || '41b8e41e51';
const originals = new Map();
for await (const [file, bytes] of readGitBaseline(['scripts/generate_chemistry.mjs', 'scripts/translate_chemistry_hindi.mjs'], { root: ROOT, baseline })) originals.set(file, bytes.toString('utf8').replace(/\r\n/g, '\n'));
const read = file => fs.readFileSync(new URL(`../${file}`, import.meta.url), 'utf8').replace(/\r\n/g, '\n');
const generator = originals.get('scripts/generate_chemistry.mjs');
const translator = originals.get('scripts/translate_chemistry_hindi.mjs');
const renderer = generator.slice(generator.indexOf('function renderTopicHtml('), generator.indexOf('\nasync function processTopic('));
const math = translator.slice(translator.indexOf('function cleanMathHtml('), translator.indexOf('// Extract comprehensive content'));
const compiler = translator.slice(translator.indexOf('function replaceBalancedContainer('), translator.indexOf('// Process a Single Topic Directory'));
if (![renderer, math, compiler].every(value => value.startsWith('function '))) throw new Error('Use a pre-extraction authoring baseline.');
const expectedGenerator = generator.replace(renderer, '').replace("import { jsonrepair } from 'jsonrepair';", "import { jsonrepair } from 'jsonrepair';\nimport { renderTopicHtml } from './lib/chemistry-renderer.mjs';").replace('/**\n * Render Complete Topic HTML with 5 Tabs\n */\n', '');
const expectedTranslator = translator.replace(math, '').replace(compiler, '')
  .replace("import { jsonrepair } from 'jsonrepair';", "import { jsonrepair } from 'jsonrepair';\nimport { cleanMathHtml, buildCompleteBilingualHtml } from './lib/chemistry-bilingual.mjs';")
  .replace("const letters = ['A', 'B', 'C', 'D'];\n", '')
  .replace('// Clean math HTML helper: standardizes LaTeX tokens into clean semantic HTML\n', '')
  .replace('// Safe replacement of a nested div container by counting open/close depth\n', '');
const expectedRenderer = renderer.replace('<script>\n' + legacyChemistryEnglish + '\n</script>', '${chemistryEnglishScript}').replace(/^function renderTopicHtml/, 'export function renderTopicHtml').trim();
const currentRenderer = read('scripts/lib/chemistry-renderer.mjs').slice(read('scripts/lib/chemistry-renderer.mjs').indexOf('export function renderTopicHtml')).trim();
const expectedCompiler = (math.replace(/^function cleanMathHtml/, 'export function cleanMathHtml') + compiler)
  .replace('function buildCompleteBilingualHtml(', 'export function buildCompleteBilingualHtml(')
  .replace('  let html = originalHtml;', '  let html = hydrateChemistryRuntime(originalHtml);')
  .replace(/  return html;\n}\s*$/, '  return externalizeChemistryRuntime(html);\n}\n').trim();
const currentCompiler = read('scripts/lib/chemistry-bilingual.mjs').slice(read('scripts/lib/chemistry-bilingual.mjs').indexOf('export function cleanMathHtml')).trim();
const checks = {
  generatorOrchestrationAndPrompts: expectedGenerator === read('scripts/generate_chemistry.mjs'),
  translatorOrchestrationAndPrompts: expectedTranslator === read('scripts/translate_chemistry_hindi.mjs'),
  completeRendererBody: expectedRenderer === currentRenderer,
  completeCompilerAndMathBodies: expectedCompiler === currentCompiler,
};
console.log(JSON.stringify({ baseline, checks }, null, 2));
if (!checks.generatorOrchestrationAndPrompts) {
  const actual = read('scripts/generate_chemistry.mjs');
  let offset = 0;
  while (offset < Math.min(actual.length, expectedGenerator.length) && actual[offset] === expectedGenerator[offset]) offset++;
  console.log(JSON.stringify({ firstDifference: offset, expected: expectedGenerator.slice(Math.max(0, offset - 40), offset + 80), actual: actual.slice(Math.max(0, offset - 40), offset + 80) }));
}
if (Object.values(checks).some(value => !value)) process.exitCode = 1;
