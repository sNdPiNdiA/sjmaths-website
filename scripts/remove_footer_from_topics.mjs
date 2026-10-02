import fs from 'node:fs';
import path from 'node:path';

const ROOT = process.cwd();
const targetDirs = [
  path.join(ROOT, 'up-upper-primary-teacher', 'social-studies'),
  path.join(ROOT, 'up-upper-primary-teacher', 'general-knowledge')
];

let totalModified = 0;

for (const dir of targetDirs) {
  if (!fs.existsSync(dir)) continue;
  const subs = fs.readdirSync(dir).filter(f => fs.statSync(path.join(dir, f)).isDirectory());

  for (const s of subs) {
    const file = path.join(dir, s, 'index.html');
    if (!fs.existsSync(file)) continue;

    let content = fs.readFileSync(file, 'utf8');
    let changed = false;

    // Remove footer container
    if (content.includes('id="footer-container"')) {
      content = content.replace(/\s*<div id="footer-container"><\/div>\s*/g, '\n\n');
      changed = true;
    }

    // Remove global footer script
    if (content.includes('global-footer')) {
      content = content.replace(/\s*<script[^>]*src="[^"]*global-footer[^"]*"[^>]*><\/script>\s*/g, '\n');
      changed = true;
    }

    if (changed) {
      fs.writeFileSync(file, content, 'utf8');
      totalModified++;
    }
  }
}

console.log(`Successfully removed footer from ${totalModified} topic pages.`);
