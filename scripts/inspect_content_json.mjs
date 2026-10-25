import fs from 'fs';

// Check competitive-exam-guide content.json
const c1 = 'upsc/ancient-history/Age-of-Mahajanapadas/Administrative-Setup/content.json';
if (fs.existsSync(c1)) {
  const d1 = JSON.parse(fs.readFileSync(c1, 'utf8'));
  console.log('Competitive content.json keys:', Object.keys(d1));
}

// Check upsc-renderer tabs/concepts.json
const c2 = 'upsc/art-and-culture/Miscellaneous/Places-of-Cultural-Interest/tabs/concepts.json';
if (fs.existsSync(c2)) {
  const d2 = JSON.parse(fs.readFileSync(c2, 'utf8'));
  console.log('upsc-renderer concepts.json keys:', Object.keys(d2));
}

// Check upsc-renderer tabs/overview.json
const c3 = 'upsc/art-and-culture/Miscellaneous/Places-of-Cultural-Interest/tabs/overview.json';
if (fs.existsSync(c3)) {
  const d3 = JSON.parse(fs.readFileSync(c3, 'utf8'));
  console.log('upsc-renderer overview.json keys:', Object.keys(d3));
}

