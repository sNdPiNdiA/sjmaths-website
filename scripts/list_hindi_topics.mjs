import fs from 'node:fs';
import path from 'node:path';

const ROOT = process.cwd();
const HINDI_DIR = path.join(ROOT, 'up-upper-primary-teacher', 'hindi');
const HINDI_HUB = path.join(HINDI_DIR, 'index.html');

const html = fs.readFileSync(HINDI_HUB, 'utf8');

// Get all dirs
const subdirs = fs.readdirSync(HINDI_DIR, { withFileTypes: true })
  .filter(d => d.isDirectory())
  .map(d => d.name)
  .sort();

console.log(`Found ${subdirs.length} subdirectories in ${HINDI_DIR}:`);

subdirs.forEach((dirName, idx) => {
  const file = path.join(HINDI_DIR, dirName, 'index.html');
  const exists = fs.existsSync(file);
  let title = '';
  let lines = 0;
  let size = 0;
  if (exists) {
    const content = fs.readFileSync(file, 'utf8');
    lines = content.split('\n').length;
    size = content.length;
    const titleMatch = content.match(/<title>([^<]+)<\/title>/);
    title = titleMatch ? titleMatch[1] : '';
  }
  console.log(`${idx + 1}. ${dirName} | exists: ${exists} | lines: ${lines} | size: ${size} | title: ${title.slice(0, 60)}`);
});
