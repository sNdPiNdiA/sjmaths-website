const fs = require('fs');
const f = 'upsc-aso/index.html';
let h = fs.readFileSync(f, 'utf8');
// Map by keyword in summary text -> pillar slug
const MAP = [
  [/Aerodynamic/i, 'aerodynamics-performance-stability'],
  [/Structur|Material/i, 'aircraft-structures-materials'],
  [/Systems|Instrument/i, 'aircraft-systems-instrumentation-maintenance'],
  [/ATC|Aerodrom/i, 'atc-aerodromes-flight-planning'],
  [/Avionic|Navigation|Surveill/i, 'avionics-navigation-surveillance'],
  [/Fluid/i, 'fluid-mechanics-machinery'],
  [/Heat/i, 'heat-transfer'],
  [/Propuls/i, 'propulsion'],
  [/Regulation|Safety|Human/i, 'regulations-aviation-safety'],
];
let count = 0;
h = h.replace(/<summary>((?!<a )[^<]{3,80}?) <span class="topic-count">/g, (m, label) => {
  for (const [re, slug] of MAP) {
    if (re.test(label)) {
      count++;
      return `<summary><a href="/upsc-aso/${slug}/">${label}</a> <span class="topic-count">`;
    }
  }
  console.log('NO MATCH:', label);
  return m;
});
fs.writeFileSync(f, h);
console.log('summaries linked this pass:', count);
