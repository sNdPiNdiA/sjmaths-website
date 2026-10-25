import fs from 'fs';

const samples = [
  'upsc/ancient-history/Age-of-Mahajanapadas/Administrative-Setup/tabs/revision.json',
  'upsc/art-and-culture/Miscellaneous/Places-of-Cultural-Interest/tabs/revision.json',
  'upsc/ancient-history/Age-of-Mahajanapadas/Administrative-Setup/tabs/mains.json',
  'upsc/art-and-culture/Miscellaneous/Places-of-Cultural-Interest/tabs/mains.json',
  'upsc/ancient-history/Age-of-Mahajanapadas/Administrative-Setup/tabs/test.json',
  'upsc/art-and-culture/Miscellaneous/Places-of-Cultural-Interest/tabs/test.json'
];

for (const s of samples) {
  if (fs.existsSync(s)) {
    console.log(`Found sample: ${s}`);
    const d = JSON.parse(fs.readFileSync(s, 'utf8'));
    console.log('Keys:', Object.keys(d));
  } else {
    console.log(`Not found: ${s}`);
  }
}

