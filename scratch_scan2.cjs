const fs = require('fs');
const path = require('path');
const chapters = [
  'chapter-3-metals-and-non-metals',
  'chapter-4-carbon-and-its-compounds',
  'chapter-5-life-processes',
  'chapter-10-human-eye-and-the-colourful-world',
  'chapter-11-electricity',
  'chapter-12-magnetic-effects-of-electric-current'
];
const base = 'c:/Users/sande/Documents/GitHub/sjmaths-website/class-10-science';

const patterns = [
  /comprehensive/i, /seamless/i, /empower/i, /unlock.*potential/i,
  /journey through/i, /dive into/i, /leverage/i, /state-of-the-art/i,
  /cutting.edge/i, /students will learn/i, /delve/i, /embark/i,
  /this chapter (?:covers|provides|offers|explores)/i,
  /master(?:ing)? (?:the|this|concepts|skills)/i
];

const cssSkip = ['transform=', 'text-transform', 'transition:', 'translateY', 'translateX', 'rotate('];

for (const ch of chapters) {
  const fpath = path.join(base, ch, 'index.html');
  const content = fs.readFileSync(fpath, 'utf8');
  const lines = content.split('\n');
  
  let found = [];
  for (let i = 0; i < lines.length; i++) {
    const line = lines[i];
    const skip = cssSkip.some(s => line.includes(s));
    if (skip) continue;
    
    for (const p of patterns) {
      if (p.test(line)) {
        found.push({ line: i+1, text: line.trim().substring(0, 130) });
        break;
      }
    }
  }
  if (found.length) {
    console.log('\n=== ' + ch + ' ===');
    found.forEach(function(f) { console.log('  L' + f.line + ': ' + f.text); });
  } else {
    console.log('OK: ' + ch);
  }
}
