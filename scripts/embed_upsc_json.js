/**
 * Embed content.json data into UPSC index.html files
 * This allows the competitive-exam-guide.js to render content without 404 errors
 */

const fs = require('fs');
const path = require('path');

const upscDirs = [
    'upsc/current-affairs',
    'upsc/ethics',
    'upsc/general-studies',
    'upsc/international-relations',
    'upsc/optional',
    'upsc/social-issues'
];

upscDirs.forEach(dir => {
    const jsonPath = path.join(dir, 'content.json');
    const htmlPath = path.join(dir, 'index.html');

    if (!fs.existsSync(jsonPath) || !fs.existsSync(htmlPath)) {
        console.log(`Skipping ${dir} - missing content.json or index.html`);
        return;
    }

    const jsonContent = fs.readFileSync(jsonPath, 'utf8');
    const htmlContent = fs.readFileSync(htmlPath, 'utf8');

    // Create the embedded script tag
    const embeddedScript = `<script type="application/json" id="embedded-study-guide-data">\n${jsonContent}\n</script>`;

    // Find the competitive-exam-guide script tag
    const pattern = 'competitive-exam-guide.min.js';
    const scriptIndex = htmlContent.indexOf(pattern);

    if (scriptIndex !== -1) {
        // Find the start of the script tag
        const tagStart = htmlContent.lastIndexOf('<script', scriptIndex);
        // Find the end of the script tag
        const tagEnd = htmlContent.indexOf('>', scriptIndex) + 1;
        const fullScriptTag = htmlContent.substring(tagStart, tagEnd);

        // Insert the embedded data before the script tag
        const updatedHtml = htmlContent.substring(0, tagStart) +
            embeddedScript + '\n' +
            htmlContent.substring(tagStart);

        fs.writeFileSync(htmlPath, updatedHtml, 'utf8');
        console.log(`✓ Embedded JSON in ${dir}/index.html`);
    } else {
        console.log(`⚠ Could not find competitive-exam-guide script in ${dir}/index.html`);
    }
});

console.log('\nDone! All UPSC pages now have embedded JSON data.');