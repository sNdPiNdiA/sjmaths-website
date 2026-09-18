const fs = require('fs');
const tgt = fs.readFileSync('up-tgt-commerce/index.html', 'utf8');
const pgt = fs.readFileSync('up-pgt-commerce/index.html', 'utf8');

const tgtMatches = [...tgt.matchAll(/href="\/commerce\/([^"]+)\/"/g)].map(x => x[1]);
const pgtMatches = [...pgt.matchAll(/href="\/commerce\/([^"]+)\/"/g)].map(x => x[1]);

console.log('Unique commerce links in TGT:', new Set(tgtMatches).size);
console.log('Unique commerce links in PGT:', new Set(pgtMatches).size);
const combined = new Set([...tgtMatches, ...pgtMatches]);
console.log('Total unique commerce links tracked across both:', combined.size);
