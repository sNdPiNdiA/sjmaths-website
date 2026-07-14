const fs = require('fs');

let html = fs.readFileSync('upsc/index.html', 'utf8');

const regex = /href="\.\/science_and_tech\//g;
let fixes = (html.match(regex) || []).length;
html = html.replace(regex, 'href="./science-and-tech/');

fs.writeFileSync('upsc/index.html', html);
console.log(`Fixed ${fixes} science_and_tech links`);
