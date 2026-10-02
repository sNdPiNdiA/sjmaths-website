const fs = require('node:fs');
const path = require('node:path');
const { ROOT, siteFiles } = require('./seo-html.cjs');
const { inspectInlineScripts } = require('./lib/inline-script-integrity.cjs');
const scanRoot = path.resolve(ROOT, process.argv.find(arg => arg.startsWith('--root='))?.slice(7) || '.');
const relativeRoot = path.relative(ROOT, scanRoot);
if (relativeRoot.startsWith('..') || path.isAbsolute(relativeRoot)) throw new Error('Audit root must stay inside the repository.');
const files = siteFiles().filter(file => file.startsWith('up-upper-primary-teacher/') && file.endsWith('.html'));
const findings = [];
for (const file of files) {
  const scripts = inspectInlineScripts(fs.readFileSync(path.join(scanRoot, file), 'utf8'));
  const problems = scripts.filter(script => script.syntaxError || script.duplicateOf !== null);
  if (problems.length) findings.push({ file, classicInlineScripts: scripts.length, problems });
}
const report = { scope: 'Classic inline syntax and exact within-page repetition; not runtime or educational-content validation', root: path.relative(ROOT, scanRoot) || '.', scannedPages: files.length, affectedPages: findings.length, syntaxFailures: findings.reduce((n, page) => n + page.problems.filter(script => script.syntaxError).length, 0), duplicateScripts: findings.reduce((n, page) => n + page.problems.filter(script => script.duplicateOf !== null).length, 0), findings };
const output = path.join(ROOT, `scratch/refactor/upper-primary-script-integrity-${report.root === '.' ? 'source' : 'staged'}.json`);
fs.mkdirSync(path.dirname(output), { recursive: true });
fs.writeFileSync(output, JSON.stringify(report, null, 2) + '\n');
console.log(JSON.stringify({ ...report, findings: undefined, output }, null, 2));
if (report.syntaxFailures) process.exitCode = 1;
