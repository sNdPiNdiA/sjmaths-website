const fs=require('fs');
const { asoFile } = require('./paths.cjs');
const h=fs.readFileSync(asoFile('index.html'),'utf8');
console.log('plain spans:',(h.match(/microtopic-plain/g)||[]).length);
console.log('linked anchors (onclick style):',(h.match(/class="microtopic-link" onclick/g)||[]).length);
console.log('microtopic-link total:',(h.match(/microtopic-link/g)||[]).length);
