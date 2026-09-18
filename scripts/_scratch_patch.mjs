import fs from 'fs';
const patches = [
  ['geography/human-geography/approaches/neo-determinism/index.html', 'Neo Determinism (Human Geography Perspective) | UP TGT & PGT Geography'],
  ['geography/human-geography/approaches/possibilism/index.html', 'Possibilism (Human Geography Perspective) | UP TGT & PGT Geography'],
  ['geography/india/agriculture/major-crops/rice/index.html', 'Rice Cultivation in India: Geographic Analysis | UP TGT & PGT Geography'],
  ['geography/india/agriculture/major-crops/sugarcane/index.html', 'Sugarcane Cultivation in India: Geographic Analysis | UP TGT & PGT Geography'],
  ['geography/india/agriculture/major-crops/tea/index.html', 'Tea Cultivation in India: Geographic Analysis | UP TGT & PGT Geography'],
  ['geography/india/agriculture/major-crops/wheat/index.html', 'Wheat Cultivation in India: Geographic Analysis | UP TGT & PGT Geography'],
  ['geography/india/resources/energy-resources/index.html', 'Energy Resources of India: Geographic Analysis | UP TGT & PGT Geography'],
  ['geography/india/agriculture/major-crops/index.html', 'Major Crops of India: Geographic & Agricultural Analysis | UP TGT & PGT Geography'],
  ['geography/physical-geography/atmosphere/structure/index.html', 'Structure of Atmosphere (Physical Geography) | UP TGT & PGT Geography'],
];
for (const [f, newTitle] of patches) {
  if (!fs.existsSync(f)) { console.log('MISSING:', f); continue; }
  let h = fs.readFileSync(f, 'utf8');
  h = h.replace(/<title>[^<]*<\/title>/, `<title>${newTitle}</title>`);
  const ogShort = newTitle.substring(0, 95);
  h = h.replace(/(<meta property="og:title" content=")[^"]*(")/,  `$1${ogShort}$2`);
  h = h.replace(/(<meta name="twitter:title" content=")[^"]*(")/,`$1${ogShort}$2`);
  fs.writeFileSync(f, h, 'utf8');
  console.log('Patched:', f);
}
console.log('Done');
