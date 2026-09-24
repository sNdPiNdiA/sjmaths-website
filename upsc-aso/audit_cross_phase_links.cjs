const fs = require('fs');

const allTopics = require('./all_544_microtopics.json');

function getPhase(day) {
  if (day <= 20) return { num: 1, name: 'Phase 1: Fluids & Heat', dir: ['fluid-mechanics-machinery', 'heat-transfer'] };
  if (day <= 40) return { num: 2, name: 'Phase 2: Aerodynamics & Flight Performance', dir: ['aerodynamics-performance-stability'] };
  if (day <= 55) return { num: 3, name: 'Phase 3: Structures & Materials', dir: ['aircraft-structures-materials'] };
  if (day <= 65) return { num: 4, name: 'Phase 4: Propulsion', dir: ['propulsion'] };
  if (day <= 80) return { num: 5, name: 'Phase 5: Systems & Maintenance', dir: ['aircraft-systems-instrumentation-maintenance'] };
  if (day <= 88) return { num: 6, name: 'Phase 6: Avionics & Surveillance', dir: ['avionics-navigation-surveillance'] };
  if (day <= 94) return { num: 7, name: 'Phase 7: ATC & Flight Planning', dir: ['atc-aerodromes-flight-planning'] };
  if (day <= 97) return { num: 8, name: 'Phase 8: Rules & Safety', dir: ['regulations-aviation-safety'] };
  return { num: 9, name: 'Phase 9: Mocks', dir: [] };
}

const issues = [];

allTopics.forEach(t => {
  const phase = getPhase(t.day);
  const parts = t.href.split('/').filter(Boolean);
  const folderSubject = parts[1];
  const slug = parts[2];

  if (phase.dir.length > 0 && !phase.dir.includes(folderSubject)) {
    issues.push({
      id: t.id,
      day: t.day,
      phase: phase.num,
      phaseName: phase.name,
      title: t.title,
      href: t.href,
      folderSubject,
      slug
    });
  }
});

console.log(`TOTAL CROSS-PHASE MISMATCHES: ${issues.length}\n`);
issues.forEach((item, idx) => {
  console.log(`${idx + 1}. [ID ${item.id}] Day ${item.day} (${item.phaseName})`);
  console.log(`   Topic: "${item.title}"`);
  console.log(`   Current Target: ${item.folderSubject}/${item.slug}`);
  console.log('----------------------------------------------------');
});
