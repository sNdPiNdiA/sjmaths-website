const fs = require('fs');
const path = require('path');

const chapters = [
  'chapter-1-chemical-reactions-and-equations',
  'chapter-2-acids-bases-and-salts',
  'chapter-3-metals-and-non-metals',
  'chapter-4-carbon-and-its-compounds',
  'chapter-5-life-processes',
  'chapter-6-control-and-coordination',
  'chapter-7-how-do-organisms-reproduce',
  'chapter-8-heredity',
  'chapter-9-light-reflection-and-refraction',
  'chapter-10-human-eye-and-the-colourful-world',
  'chapter-11-electricity',
  'chapter-12-magnetic-effects-of-electric-current',
  'chapter-13-our-environment'
];

const base = 'c:/Users/sande/Documents/GitHub/sjmaths-website/class-10-science';

// AI-style phrases to detect
const aiPhrases = [
  /\bembark on\b/i,
  /\bdelve into\b/i,
  /\bunlock\b.*\bpotential\b/i,
  /\bcomprehensive\s+(guide|overview|resource|study|journey|notes)\b/i,
  /\bmaster(?:ing)?\s+(?:this|the|your|concepts|skills)\b/i,
  /\bseamless(?:ly)?\b/i,
  /\btransform(?:ative|ation)?\b/i,
  /\bleverage\b/i,
  /\brobust\b/i,
  /\bcutting[- ]edge\b/i,
  /\bstate[- ]of[- ]the[- ]art\b/i,
  /\bin\s+today['']?s\s+(world|era|age)\b/i,
  /\b(?:carefully|meticulously|thoroughly)\s+(?:crafted|designed|curated|selected)\b/i,
  /\bstudents?\s+will\s+(?:be able to|learn|explore|discover|gain)\b/i,
  /\bthis\s+(?:chapter|unit|page|guide|resource)\s+(?:covers|explores|explains|provides|offers|equips)\b/i,
  /\bempowers?\s+(?:you|students?|learners?)\b/i,
  /\bjourney\s+through\b/i,
  /\bdive\s+(?:deep|into)\b/i,
  /\bget\s+ready\s+to\b/i,
  /\bstep[- ]by[- ]step\s+(?:guide|approach|breakdown)\b/i,
  /\btake\s+your\s+(?:preparation|learning|studies|understanding)\s+to\s+the\s+next\s+level\b/i,
  /\bboost\s+your\s+(?:score|performance|learning|confidence)\b/i,
  /\byour\s+ultimate\s+(?:guide|resource|companion)\b/i,
  /designed\s+to\s+help\s+(?:you|students?)\b/i,
  /\bwhether\s+you\s+are\b/i,
  /\bwhat\s+(?:you\'ll|you\s+will)\s+(?:learn|find|explore|get)\b/i,
  /\bwhy\s+this\s+(?:chapter|unit|page|topic)\s+matters?\b/i,
];

for (const ch of chapters) {
  const fpath = path.join(base, ch, 'index.html');
  if (!fs.existsSync(fpath)) {
    console.log(`MISSING: ${ch}`);
    continue;
  }
  const content = fs.readFileSync(fpath, 'utf8');
  const lines = content.split('\n');
  
  let found = [];
  for (let i = 0; i < lines.length; i++) {
    const line = lines[i];
    for (const pat of aiPhrases) {
      if (pat.test(line)) {
        found.push({ line: i+1, text: line.trim().substring(0, 120), pat: pat.toString() });
        break;
      }
    }
  }
  
  if (found.length > 0) {
    console.log(`\n=== ${ch} (${found.length} hits) ===`);
    for (const f of found) {
      console.log(`  L${f.line}: ${f.text}`);
    }
  } else {
    console.log(`OK: ${ch}`);
  }
}
