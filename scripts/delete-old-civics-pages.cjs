const fs = require('fs');
const path = require('path');

const ROOT = path.resolve(__dirname, '..');

// List of older fragmented sub-directories to delete
const oldDirsToDelete = [
  // 1. foundations/civics
  'civics/foundations/civics/definition',
  'civics/foundations/civics/nature',
  'civics/foundations/civics/subject-matter',
  'civics/foundations/civics/scope',

  // 2. foundations/state
  'civics/foundations/state/definition',
  'civics/foundations/state/elements',
  'civics/foundations/state/theories-of-origin',

  // 3. political-concepts
  'civics/political-concepts/rights',
  'civics/political-concepts/citizenship',

  // 4. government/forms
  'civics/government/forms/parliamentary',
  'civics/government/forms/presidential',
  'civics/government/forms/unitary',
  'civics/government/forms/federal',

  // 5. government/organs
  'civics/government/organs/legislature',
  'civics/government/organs/executive',
  'civics/government/organs/judiciary',

  // 6. elections
  'civics/elections/electoral-reforms',
  'civics/elections/voting-behaviour',

  // 7. union-government/executive
  'civics/union-government/executive/prime-minister',
  'civics/union-government/executive/council-of-ministers',

  // 8. union-government/parliament
  'civics/union-government/parliament/lok-sabha',
  'civics/union-government/parliament/rajya-sabha',

  // 9. judiciary
  'civics/judiciary/supreme-court',
  'civics/judiciary/high-court',

  // 10. state-government
  'civics/state-government/governor',
  'civics/state-government/chief-minister',

  // 11. democracy-and-decentralization
  'civics/democracy-and-decentralization/democratic-decentralization',
  'civics/democracy-and-decentralization/panchayati-raj',

  // 12. challenges-of-indian-democracy
  'civics/challenges-of-indian-democracy/casteism',
  'civics/challenges-of-indian-democracy/regionalism',
  'civics/challenges-of-indian-democracy/communalism',

  // 13. political-organization
  'civics/political-organization/political-party',
  'civics/political-organization/pressure-group',

  // 14. indian-administration
  'civics/indian-administration/ombudsman',
  'civics/indian-administration/lokpal',
  'civics/indian-administration/lokayukta'
];

let deletedCount = 0;
for (const relDir of oldDirsToDelete) {
  const fullPath = path.join(ROOT, relDir);
  if (fs.existsSync(fullPath)) {
    fs.rmSync(fullPath, { recursive: true, force: true });
    console.log(`Deleted: ${relDir}`);
    deletedCount++;
  } else {
    console.log(`Not found (already deleted): ${relDir}`);
  }
}

console.log(`Total directories deleted: ${deletedCount}`);
