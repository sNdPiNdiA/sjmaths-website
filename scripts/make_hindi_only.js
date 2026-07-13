const fs = require('fs');
const path = require('path');
const cheerio = require('cheerio');

const targetDir = 'C:\\\\Users\\\\sande\\\\Documents\\\\GitHub\\\\sjmaths-website\\\\upsssc-lower-mains\\\\hindi';

function processFiles(dir) {
    const files = fs.readdirSync(dir);
    for (const file of files) {
        const fullPath = path.join(dir, file);
        const stat = fs.statSync(fullPath);
        if (stat.isDirectory()) {
            processFiles(fullPath);
        } else if (file === 'index.html') {
            let html = fs.readFileSync(fullPath, 'utf8');
            let originalHtml = html;

            // Configure cheerio to be as non-destructive as possible
            const $ = cheerio.load(html, { decodeEntities: false });

            let modified = false;

            // Target practice/PYQ questions and test questions
            $('.practice-question-card, .test-qblock').each((i, el) => {
                // Delete all .lang-en elements inside these blocks
                const langEnElems = $(el).find('.lang-en');
                if (langEnElems.length > 0) {
                    langEnElems.remove();
                    modified = true;
                }
                
                // Remove the .lang-hi class from all elements inside these blocks
                const langHiElems = $(el).find('.lang-hi');
                if (langHiElems.length > 0) {
                    langHiElems.removeClass('lang-hi');
                    modified = true;
                }
            });
            
            if (modified) {
                // Save the file
                fs.writeFileSync(fullPath, $.html());
                console.log(`Updated ${fullPath}`);
            }
        }
    }
}

processFiles(targetDir);
console.log("Done.");
