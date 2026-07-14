const fs = require('fs');
const path = require('path');

const srcJainism = path.join('upsc', 'ancient-history', 'Jainism');
const srcBuddhism = path.join('upsc', 'ancient-history', 'Buddhism');
const destDir = path.join('upsc', 'ancient-history', 'Jainism-and-Buddhism');

// 1. Move contents of Jainism to Jainism-and-Buddhism
if (fs.existsSync(srcJainism)) {
    const files = fs.readdirSync(srcJainism);
    files.forEach(file => {
        fs.renameSync(path.join(srcJainism, file), path.join(destDir, file));
    });
    fs.rmdirSync(srcJainism);
    console.log('Moved Jainism contents to Jainism-and-Buddhism and removed Jainism folder.');
}

// 2. Move contents of Buddhism to Jainism-and-Buddhism
if (fs.existsSync(srcBuddhism)) {
    const files = fs.readdirSync(srcBuddhism);
    files.forEach(file => {
        fs.renameSync(path.join(srcBuddhism, file), path.join(destDir, file));
    });
    fs.rmdirSync(srcBuddhism);
    console.log('Moved Buddhism contents to Jainism-and-Buddhism and removed Buddhism folder.');
}

// 3. Update upsc/index.html
const indexFile = path.join('upsc', 'index.html');
if (fs.existsSync(indexFile)) {
    let content = fs.readFileSync(indexFile, 'utf8');
    content = content.replace(/href="\.\/ancient-history\/Jainism\//g, 'href="./ancient-history/Jainism-and-Buddhism/');
    content = content.replace(/href="\.\/ancient-history\/Buddhism\//g, 'href="./ancient-history/Jainism-and-Buddhism/');
    fs.writeFileSync(indexFile, content, 'utf8');
    console.log('Updated upsc/index.html links.');
}

console.log('Consolidation complete!');
