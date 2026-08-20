import fs from 'fs';
import path from 'path';

const baseDir = 'c:\\Users\\sande\\Documents\\GitHub\\sjmaths-website\\upsc';
const subjects = fs.readdirSync(baseDir).filter(f => {
  const full = path.join(baseDir, f);
  return fs.statSync(full).isDirectory() && !['assets', 'css', 'js'].includes(f);
});

let stats = {
  total: 0,
  modernComplete: 0,
  stubsRemaining: 0,
  bySubject: {}
};

for (const s of subjects) {
  stats.bySubject[s] = { total: 0, completed: 0, remaining: 0 };
  const sPath = path.join(baseDir, s);
  const parents = fs.readdirSync(sPath).filter(d => fs.statSync(path.join(sPath, d)).isDirectory());

  for (const p of parents) {
    const pPath = path.join(sPath, p);
    const topics = fs.readdirSync(pPath).filter(d => fs.statSync(path.join(pPath, d)).isDirectory());

    for (const t of topics) {
      const idxPath = path.join(pPath, t, 'index.html');
      stats.total++;
      stats.bySubject[s].total++;

      if (fs.existsSync(idxPath)) {
        const html = fs.readFileSync(idxPath, 'utf8');
        const isModern = html.includes('upsc-renderer.min.js');
        const isLegacyStub = html.includes('competitive-exam-guide.min.js') && !html.includes('id="embedded-study-guide-data"');

        if (isModern && !isLegacyStub) {
          stats.modernComplete++;
          stats.bySubject[s].completed++;
        } else {
          stats.stubsRemaining++;
          stats.bySubject[s].remaining++;
        }
      } else {
        stats.stubsRemaining++;
        stats.bySubject[s].remaining++;
      }
    }
  }
}

console.log('=== UPSC SYLLABUS AUDIT STATUS ===');
console.log(`Total Unique Topics: ${stats.total}`);
console.log(`Completed (Modern & Populated): ${stats.modernComplete} (${Math.round(stats.modernComplete/stats.total*100)}%)`);
console.log(`Remaining Stubs to Generate: ${stats.stubsRemaining} (${Math.round(stats.stubsRemaining/stats.total*100)}%)\n`);

console.log('--- Breakdown by Subject ---');
for (const [subj, data] of Object.entries(stats.bySubject)) {
  console.log(`${subj.padEnd(22)}: Completed ${String(data.completed).padStart(4)} / ${String(data.total).padStart(4)} | Remaining: ${String(data.remaining).padStart(4)}`);
}
