// Remove indentation from blank lines in changed text files without touching content.
const fs = require('fs');
const path = require('path');
const { execFileSync } = require('child_process');
const { ROOT } = require('./seo-html.cjs');

const extensions = /\.(?:html?|css|js|cjs|json|xml|txt)$/i;
const changed = execFileSync('git', ['diff', '--name-only', '-z'], { cwd: ROOT, encoding: 'utf8', maxBuffer: 20e6 }).split('\0').filter(Boolean);
const untracked = execFileSync('git', ['ls-files', '--others', '--exclude-standard', '-z'], { cwd: ROOT, encoding: 'utf8', maxBuffer: 20e6 }).split('\0').filter(Boolean);
let filesChanged = 0;
let blankLinesCleaned = 0;
for (const file of [...new Set([...changed, ...untracked])].filter(file => extensions.test(file))) {
  const target = path.join(ROOT, file);
  const source = fs.readFileSync(target, 'utf8');
  let count = 0;
  const next = source.replace(/^[ \t]+(?=\r?$)/gm, () => { count++; return ''; });
  if (next !== source) {
    fs.writeFileSync(target, next);
    filesChanged++;
    blankLinesCleaned += count;
  }
}
console.log(JSON.stringify({ filesChanged, blankLinesCleaned }));
