import fs from 'fs';

const html = fs.readFileSync('up-upper-primary-teacher/sanskrit/index.html', 'utf8');

// Find all topic links and cards
// In up-upper-primary-teacher hub pages, topics are defined in cards with links, checkbox ids, titles, etc.
const linkRegex = /href="\/up-upper-primary-teacher\/sanskrit\/([^"\/]+)\/?"/g;
let m;
const links = [];
while ((m = linkRegex.exec(html)) !== null) {
  if (!links.includes(m[1])) {
    links.push(m[1]);
  }
}

console.log('Unique topic slugs from links (' + links.length + '):');
console.log(links);

// Check files currently in up-upper-primary-teacher/sanskrit/
const diskDirs = fs.readdirSync('up-upper-primary-teacher/sanskrit', { withFileTypes: true })
  .filter(d => d.isDirectory())
  .map(d => d.name);

console.log('\nDisk subdirectories (' + diskDirs.length + '):');
console.log(diskDirs);

// Check which directories have an index.html and what's inside
const status = [];
for (const d of diskDirs) {
  const p = `up-upper-primary-teacher/sanskrit/${d}/index.html`;
  const exists = fs.existsSync(p);
  const size = exists ? fs.statSync(p).size : 0;
  status.push({ slug: d, exists, size });
}
console.log('\nSubdirectory status:');
console.table(status);
