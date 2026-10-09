import fs from 'fs';

const files = [
  'sanskrit/laukika-sahitya/gadya/nalachampu/prathama-ucchvasa/index.html',
  'logic/deductive-arguments/categorical-syllogism/fallacies/index.html',
  'civics/district-administration/district-magistrate/index.html',
  'commerce/business-organization/forms-of-business-organization/sole-proprietorship/index.html'
];

for (const f of files) {
  if (fs.existsSync(f)) {
    const content = fs.readFileSync(f, 'utf8');
    const style = content.match(/<style\b[^>]*>([\s\S]*?)<\/style>/i)?.[1] || '';
    const rootLine = style.split('\n').find(l => l.includes(':root'));
    console.log(`\nFile: ${f}`);
    console.log(`Root line: ${rootLine}`);
    console.log(`Style length: ${style.length}`);
  }
}
