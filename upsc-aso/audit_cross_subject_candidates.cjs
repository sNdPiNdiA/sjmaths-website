const fs = require('fs');

const allTopics = require('./all_544_microtopics.json');
const issues = [];

function getPhase(day) {
  if (day <= 20) return { num: 1, name: 'Phase 1: Fluids & Heat', dirs: ['fluid-mechanics-machinery', 'heat-transfer'] };
  if (day <= 40) return { num: 2, name: 'Phase 2: Aerodynamics & Flight Performance', dirs: ['aerodynamics-performance-stability'] };
  if (day <= 55) return { num: 3, name: 'Phase 3: Structures & Materials', dirs: ['aircraft-structures-materials'] };
  if (day <= 65) return { num: 4, name: 'Phase 4: Propulsion', dirs: ['propulsion'] };
  if (day <= 80) return { num: 5, name: 'Phase 5: Systems & Maintenance', dirs: ['aircraft-systems-instrumentation-maintenance'] };
  if (day <= 88) return { num: 6, name: 'Phase 6: Avionics & Surveillance', dirs: ['avionics-navigation-surveillance'] };
  if (day <= 94) return { num: 7, name: 'Phase 7: ATC & Flight Planning', dirs: ['atc-aerodromes-flight-planning'] };
  if (day <= 97) return { num: 8, name: 'Phase 8: Rules & Safety', dirs: ['regulations-aviation-safety'] };
  return { num: 9, name: 'Phase 9: Mocks', dirs: [] };
}

// Get all existing directories per subject
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

const subjectDirs = {};
subjects.forEach(s => {
  const p = 'upsc-aso/' + s;
  if (fs.existsSync(p)) {
    subjectDirs[s] = fs.readdirSync(p, { withFileTypes: true })
      .filter(d => d.isDirectory())
      .map(d => d.name);
  } else {
    subjectDirs[s] = [];
  }
});

// Let's audit all 544 topics
const crossSubjectList = [];

allTopics.forEach(t => {
  const phase = getPhase(t.day);
  const parts = t.href.split('/').filter(Boolean);
  const currentSubj = parts[1];
  const currentSlug = parts[2];

  if (phase.dirs.length > 0 && !phase.dirs.includes(currentSubj)) {
    // Look for matching folders in the correct subject dirs
    const candidateFolders = [];
    phase.dirs.forEach(d => {
      const dirs = subjectDirs[d] || [];
      const titleWords = t.title.toLowerCase().replace(/[^a-z0-9]/g, ' ').split(/\s+/).filter(w => w.length > 3);
      dirs.forEach(f => {
        const fWords = f.toLowerCase().split('-');
        const matches = titleWords.filter(tw => fWords.some(fw => fw.includes(tw) || tw.includes(fw)));
        if (matches.length > 0) {
          candidateFolders.push({ subject: d, folder: f, score: matches.length });
        }
      });
    });

    candidateFolders.sort((a, b) => b.score - a.score);

    crossSubjectList.push({
      id: t.id,
      day: t.day,
      phase: phase.name,
      title: t.title,
      currentHref: t.href,
      currentSubject: currentSubj,
      bestMatchInCorrectSubject: candidateFolders[0] || null
    });
  }
});

console.log('Cross Subject Items Count:', crossSubjectList.length);
crossSubjectList.forEach((item, idx) => {
  console.log(`\n#${idx + 1}: [ID ${item.id}] Day ${item.day} - "${item.title}"`);
  console.log(`   Current: /${item.currentSubject}/... (${item.currentHref})`);
  if (item.bestMatchInCorrectSubject) {
    console.log(`   Found in Correct Subject: /${item.bestMatchInCorrectSubject.subject}/${item.bestMatchInCorrectSubject.folder}/`);
  } else {
    console.log(`   No direct folder match found in correct subject.`);
  }
});
