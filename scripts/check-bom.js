const fs = require('fs');
const path = require('path');

function checkBOM(filePath) {
    const buffer = fs.readFileSync(filePath);
    console.log(`File: ${filePath}`);
    console.log(`Hex: ${buffer.slice(0, 4).toString('hex')}`);
    console.log(`String: ${buffer.slice(0, 4).toString()}`);
}

const file = 'c:/Users/sande/Documents/GitHub/sjmaths-website/class-11-maths/chapter-wise-notes/chapter-1-sets/index.html';
checkBOM(file);
