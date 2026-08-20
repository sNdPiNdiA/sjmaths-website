import fs from 'fs';
import path from 'path';

const baseDir = 'c:\\Users\\sande\\Documents\\GitHub\\sjmaths-website\\upsc';
const subjects = fs.readdirSync(baseDir).filter(f => {
  const full = path.join(baseDir, f);
  return fs.statSync(full).isDirectory() && !['assets', 'css', 'js'].includes(f);
});

let duplicatePairs = [];

for (const s of subjects) {
  const sPath = path.join(baseDir, s);
  const parents = fs.readdirSync(sPath).filter(d => fs.statSync(path.join(sPath, d)).isDirectory());
  for (const p of parents) {
    const pPath = path.join(sPath, p);
    const topics = fs.readdirSync(pPath).filter(d => fs.statSync(path.join(pPath, d)).isDirectory());

    for (let i = 0; i < topics.length; i++) {
      for (let j = i + 1; j < topics.length; j++) {
        const t1 = topics[i];
        const t2 = topics[j];
        if (t2.startsWith(t1 + '-') || t1.startsWith(t2 + '-')) {
          const shorter = t1.length <= t2.length ? t1 : t2;
          const longer = t1.length > t2.length ? t1 : t2;
          duplicatePairs.push({
            subject: s,
            parent: p,
            keep: shorter,
            remove: longer,
            keepPath: path.join(pPath, shorter),
            removePath: path.join(pPath, longer)
          });
        }
      }
    }
  }
}

console.log(`Found ${duplicatePairs.length} duplicate pairs to consolidate.`);

let removedCount = 0;
for (const pair of duplicatePairs) {
  if (fs.existsSync(pair.removePath)) {
    const removeIdx = path.join(pair.removePath, 'index.html');
    const keepIdx = path.join(pair.keepPath, 'index.html');

    if (fs.existsSync(removeIdx)) {
      const removeHtml = fs.readFileSync(removeIdx, 'utf8');
      const isRemoveGood = removeHtml.includes('upsc-renderer.min.js');
      const isKeepGood = fs.existsSync(keepIdx) && fs.readFileSync(keepIdx, 'utf8').includes('upsc-renderer.min.js');

      if (isRemoveGood && !isKeepGood) {
        fs.cpSync(pair.removePath, pair.keepPath, { recursive: true });
        console.log(`Copied modern content from ${pair.remove} -> ${pair.keep}`);
      }
    }

    fs.rmSync(pair.removePath, { recursive: true, force: true });
    removedCount++;
    console.log(`🗑️ Removed duplicate: [${pair.subject}] ${pair.parent} -> ${pair.remove}`);
  }
}

console.log(`\n🎉 Successfully consolidated and removed ${removedCount} duplicate folders.`);
