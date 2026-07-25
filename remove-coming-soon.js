/**
 * Remove "Coming Soon" sections from SSC CGL pages
 * Removes placeholder tab panels and their CSS
 */

const fs = require('fs');
const path = require('path');

const SSC_CGL_DIR = path.join(__dirname, 'ssc-cgl');

function removeComingSoonFromFile(filePath) {
    let content = fs.readFileSync(filePath, 'utf8');
    let modified = false;

    // Check if file has coming-soon sections
    if (!content.includes('coming-soon-box') && !content.includes('Coming Soon')) {
        return false;
    }

    // Remove CSS for .coming-soon-box and related styles
    const cssPatterns = [
        /\.coming-soon-box\s*\{[^}]+\}[^}]*}/g,
        /\.coming-soon-box\s+i\s*\{[^}]+\}/g,
        /\.coming-soon-box\s+h3\s*\{[^}]+\}/g,
        /\.coming-soon-box\s+p\s*\{[^}]+\}/g,
        /body\.dark-mode\s+\.coming-soon-box\s*\{[^}]+\}/g,
        /body\.dark-mode\s+\.coming-soon-box\s+h3\s*\{[^}]+\}/g,
        /body\.dark-mode\s+\.coming-soon-box\s+p\s*\{[^}]+\}/g,
        /\/\* Coming Soon \*\//g,
        /\.coming-soon\s+i\s*\{[^}]+\}/g,
    ];

    cssPatterns.forEach(pattern => {
        const matches = content.match(pattern);
        if (matches) {
            matches.forEach(match => {
                content = content.replace(match, '');
                modified = true;
            });
        }
    });

    // Remove HTML for coming-soon tab panels
    const htmlPatterns = [
        /<div\s+id="tab-practice"\s+class="tab-panel">\s*<div\s+class="coming-soon-box[^>]*>[\s\S]*?<\/div>\s*<\/div>/g,
        /<div\s+id="tab-pyqs"\s+class="tab-panel">\s*<div\s+class="coming-soon-box[^>]*>[\s\S]*?<\/div>\s*<\/div>/g,
        /<div\s+id="tab-mini-test"\s+class="tab-panel">\s*<div\s+class="coming-soon-box[^>]*>[\s\S]*?<\/div>\s*<\/div>/g,
    ];

    htmlPatterns.forEach(pattern => {
        const matches = content.match(pattern);
        if (matches) {
            matches.forEach(match => {
                content = content.replace(match, '');
                modified = true;
            });
        }
    });

    // Remove "Coming Soon" text anywhere else
    content = content.replace(/Coming Soon/g, '');
    content = content.replace(/— Coming Soon/g, '');
    content = content.replace(/ Coming Soon/g, '');

    if (modified) {
        fs.writeFileSync(filePath, content, 'utf8');
        return true;
    }

    return false;
}

function processDirectory(dir) {
    const files = fs.readdirSync(dir);
    let modifiedCount = 0;

    files.forEach(file => {
        const filePath = path.join(dir, file);
        const stat = fs.statSync(filePath);

        if (stat.isDirectory()) {
            modifiedCount += processDirectory(filePath);
        } else if (file.endsWith('.html')) {
            if (removeComingSoonFromFile(filePath)) {
                modifiedCount++;
                console.log(`  ✅ Updated: ${path.relative(SSC_CGL_DIR, filePath)}`);
            }
        }
    });

    return modifiedCount;
}

console.log('🔍 Scanning for "Coming Soon" sections...\n');
const totalModified = processDirectory(SSC_CGL_DIR);
console.log(`\n✨ Complete! Modified ${totalModified} files.`);