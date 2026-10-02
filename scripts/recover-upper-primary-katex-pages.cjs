const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');
const { ROOT, siteFiles } = require('./seo-html.cjs');
const { recoverRepeatedBodyPage } = require('./lib/recover-katex-expanded-pages.cjs');
const { inspectInlineScripts } = require('./lib/inline-script-integrity.cjs');
async function main() {
const apply = process.argv.includes('--apply');
const repairSource = fs.readFileSync(path.join(ROOT, 'scripts/fix_maths_rendering_all_files.mjs'), 'utf8');
const blockMatch = repairSource.match(/const KATEX_HEAD_BLOCK = (`[\s\S]*?`);/);
if (!blockMatch) throw new Error('Cannot find the literal maintained KaTeX head template.');
const katexBlock = vm.runInNewContext(blockMatch[1]);
const files = siteFiles().filter(file => file.startsWith('up-upper-primary-teacher/') && file.endsWith('.html'));
const changes = new Map(), refused = [];
for (const file of files) {
  const absolute = path.join(ROOT, file), before = fs.readFileSync(absolute, 'utf8');
  if (!before.includes('document.addEventListener("DOMContentLoaded", function () {\n        if (typeof renderMathInElement')) continue;
  if ((before.match(/<body\b/gi) || []).length === 1 && (before.match(/<html\b/gi) || []).length === 1 && !inspectInlineScripts(before).some(script => script.syntaxError)) continue;
  const after = recoverRepeatedBodyPage(before, katexBlock);
  if (!after || inspectInlineScripts(after).some(script => script.syntaxError) || (after.match(/<html\b/gi) || []).length !== 1 || (after.match(/<body\b/gi) || []).length !== 1) { refused.push(file); continue; }
  changes.set(absolute, Buffer.from(after, 'utf8'));
}
if (apply && refused.length) throw new Error(`Refusing partial recovery; ${refused.length} pages did not match the strict recovery shape.`);
if (apply) {
  const { commitBuildWrites } = await import('./lib/build-transaction.mjs');
  commitBuildWrites(changes);
}
console.log(JSON.stringify({ mode: apply ? 'apply' : 'dry-run', candidates: changes.size, refused, files: [...changes.keys()].map(file => path.relative(ROOT, file)) }, null, 2));
}
main().catch(error => { console.error(error); process.exitCode = 1; });
