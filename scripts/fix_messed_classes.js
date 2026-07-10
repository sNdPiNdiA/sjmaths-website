const fs = require('fs');
const path = 'upsssc-lower-mains/history/social-aspects/index.html';
let content = fs.readFileSync(path, 'utf8');

let lines = content.split('\n');
let modified = false;

for (let i = 0; i < lines.length; i++) {
    let l = lines[i];
    if (l.includes('class=" "')) {
        modified = true;
        
        // details tags in PYQ section
        if (l.includes('<details class=" ">')) {
            lines[i] = l.replace('<details class=" ">', '<details class="solution-details">');
        }
        // h4 theory headings
        else if (l.includes('<h4 class=" ">')) {
            if (l.match(/[\u0900-\u097F]/)) { // contains Hindi characters
                lines[i] = l.replace('<h4 class=" ">', '<h4 class="lang-hi theory-heading">');
            } else {
                lines[i] = l.replace('<h4 class=" ">', '<h4 class="lang-en theory-heading">');
            }
        }
        // p tags (questions in practice/PYQs)
        else if (l.includes('<p class=" ">')) {
            if (l.match(/[\u0900-\u097F]/)) {
                lines[i] = l.replace('<p class=" ">', '<p class="lang-hi q-text">');
            } else {
                lines[i] = l.replace('<p class=" ">', '<p class="lang-en q-text">');
            }
        }
        // div class=" " (around line 761) -> might have been sub-nav or tabs?
        // Let's check context. Usually <div class="lang-en ...">
        else if (l.includes('<div class=" ">')) {
            if (l.match(/[\u0900-\u097F]/)) {
                lines[i] = l.replace('<div class=" ">', '<div class="lang-hi info-box">'); // guessing info-box
            } else if (l.match(/[a-zA-Z]/)) {
                lines[i] = l.replace('<div class=" ">', '<div class="lang-en info-box">');
            } else {
                lines[i] = l.replace('<div class=" ">', '<div>');
            }
        }
        // button class=" " (line 5812) -> test tab button
        else if (l.includes('class=" "') && l.includes('<button') || l.includes('onclick')) {
            lines[i] = l.replace('class=" "', 'class="tact-btn"');
        }
        else {
            // generic fallback
            lines[i] = l.replace('class=" "', '');
        }
    }
}

if (modified) {
    fs.writeFileSync(path, lines.join('\n'), 'utf8');
    console.log('Fixed classes');
} else {
    console.log('No modifications needed');
}
