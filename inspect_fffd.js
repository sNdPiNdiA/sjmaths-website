const fs = require('fs');

const file = 'c:/Users/sande/Documents/GitHub/sjmaths-website/ssc-cgl/quantitative-aptitude/right-prism-right-circular-cone-right-circular-cylinder/3d-figures-volume-csa-tsa/index.html';
const content = fs.readFileSync(file, 'utf8');

const lines = content.split('\n');
lines.forEach((line, index) => {
    if (line.includes('\uFFFD')) {
        console.log(`Line ${index + 1}: ${line.trim()}`);
    }
});
