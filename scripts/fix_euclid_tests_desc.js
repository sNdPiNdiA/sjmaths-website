const fs = require('fs');
const path = require('path');

const ROOT_DIR = path.join(__dirname, '..');

const hPath = path.join(ROOT_DIR, 'class-9-maths', 'tests', 'chapter-wise', 'chapter-5-introduction-to-euclids-geometry', 'hard.html');
const sPath = path.join(ROOT_DIR, 'class-9-maths', 'tests', 'chapter-wise', 'chapter-5-introduction-to-euclids-geometry', 'standard.html');
const bPath = path.join(ROOT_DIR, 'class-9-maths', 'tests', 'chapter-wise', 'chapter-5-introduction-to-euclids-geometry', 'basic.html');

let bContent = fs.readFileSync(bPath, 'utf8');
bContent = bContent.replace(/<meta\s+name=["']description["'][\s\S]*?>/i, '<meta name="description" content="Practice Class 9 Euclid’s Geometry Basic Level Online Practice Test with step-by-step solutions and scoring on SJMaths.">');
fs.writeFileSync(bPath, bContent, 'utf8');

let hContent = fs.readFileSync(hPath, 'utf8');
hContent = hContent.replace(/<meta\s+name=["']description["'][\s\S]*?>/i, '<meta name="description" content="Practice Class 9 Euclid’s Geometry Hard Level Online Practice Test with advanced postulates and proofs on SJMaths.">');
fs.writeFileSync(hPath, hContent, 'utf8');

let sContent = fs.readFileSync(sPath, 'utf8');
sContent = sContent.replace(/<meta\s+name=["']description["'][\s\S]*?>/i, '<meta name="description" content="Practice Class 9 Euclid’s Geometry Standard Level Online Practice Test with key axioms and revision notes on SJMaths.">');
fs.writeFileSync(sPath, sContent, 'utf8');

console.log('🎉 Fixed Euclid test descriptions to be 100% unique.');
