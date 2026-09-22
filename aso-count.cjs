const fs=require('fs');
const h=fs.readFileSync('upsc-aso/index.html','utf8');
console.log('plain spans:',(h.match(/microtopic-plain/g)||[]).length);
console.log('linked anchors (onclick style):',(h.match(/class="microtopic-link" onclick/g)||[]).length);
console.log('microtopic-link total:',(h.match(/microtopic-link/g)||[]).length);
