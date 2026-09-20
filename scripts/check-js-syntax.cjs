const fs = require('fs');
const path = require('path');
const { spawnSync } = require('child_process');

const ROOT = path.resolve(__dirname, '..');
const SEARCH_ROOTS = ['assets/js', 'utils', 'scripts'];
const EXTENSIONS = new Set(['.js', '.mjs', '.cjs']);
const files = [];

function collect(directory) {
  for (const entry of fs.readdirSync(path.join(ROOT, directory), { withFileTypes: true })) {
    const relative = path.posix.join(directory.replaceAll(path.sep, '/'), entry.name);
    if (entry.isDirectory()) {
      collect(relative);
      continue;
    }
    if (EXTENSIONS.has(path.extname(entry.name)) && !entry.name.endsWith('.min.js')) {
      files.push(relative);
    }
  }
}

for (const directory of SEARCH_ROOTS) collect(directory);
files.sort();

const failures = [];
for (const file of files) {
  const result = spawnSync(process.execPath, ['--check', path.join(ROOT, file)], {
    cwd: ROOT,
    encoding: 'utf8'
  });
  if (result.status !== 0) failures.push({ file, error: (result.stderr || result.stdout).trim() });
}

console.log(`Checked ${files.length} non-minified JavaScript files.`);
if (failures.length) {
  for (const failure of failures) console.error(`\n${failure.file}\n${failure.error}`);
  process.exitCode = 1;
} else {
  console.log('All JavaScript files passed syntax checks.');
}
