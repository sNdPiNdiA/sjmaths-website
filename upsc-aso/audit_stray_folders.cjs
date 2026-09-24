const fs = require('fs');
const path = require('path');

const allTopics = require('./all_544_microtopics.json');
const indexHtml = fs.readFileSync('upsc-aso/index.html', 'utf8');

// Collect all known valid URLs / relative paths in upsc-aso
const validSlugs = new Set();

allTopics.forEach(t => {
  const parts = t.href.split('/').filter(Boolean);
  if (parts.length >= 3) {
    validSlugs.add(parts[1] + '/' + parts[2]);
  }
});

// Extract all hrefs from index.html
const hrefRegex = /href="\/upsc-aso\/([^\/"]+)\/([^\/"]+)\/?"/g;
let m;
while ((m = hrefRegex.exec(indexHtml)) !== null) {
  validSlugs.add(m[1] + '/' + m[2]);
}

console.log('Total valid recognized subject/slug paths in system:', validSlugs.size);

const subjects = [
  'fluid-mechanics-machinery',
  'heat-transfer',
  'aerodynamics-performance-stability',
  'aircraft-structures-materials',
  'propulsion',
  'aircraft-systems-instrumentation-maintenance',
  'avionics-navigation-surveillance',
  'atc-aerodromes-flight-planning',
  'regulations-aviation-safety'
];

const strayFolders = [];

subjects.forEach(subj => {
  const subjPath = path.join('upsc-aso', subj);
  if (!fs.existsSync(subjPath)) return;
  const entries = fs.readdirSync(subjPath, { withFileTypes: true });
  entries.forEach(e => {
    if (e.isDirectory()) {
      const key = subj + '/' + e.name;
      if (!validSlugs.has(key)) {
        strayFolders.push({ subject: subj, folder: e.name, fullPath: path.join(subjPath, e.name) });
      }
    }
  });
});

console.log('Stray / unlisted folders found on disk:', strayFolders.length);
if (strayFolders.length > 0) {
  console.log(JSON.stringify(strayFolders, null, 2));
} else {
  console.log('Zero stray folders found! Disk is 100% clean and synchronized with syllabus.');
}
