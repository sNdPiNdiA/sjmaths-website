const fs = require('fs');

// Read the template (Prehistoric-Time-Periods) - the reference page
const templatePath = 'upsc/ancient-history/Prehistory/Prehistoric-Time-Periods/index.html';
const template = fs.readFileSync(templatePath, 'utf8');
const templateLines = template.split('\n');

// Extract everything from "<!-- Reusable renderers -->" onwards
const reusableRenderersLine = templateLines.findIndex(l => l.includes('<!-- Reusable renderers -->'));
const templateFooterSection = templateLines.slice(reusableRenderersLine).join('\n');

console.log('Template footer section found starting at line:', reusableRenderersLine);
console.log('Footer section length:', templateFooterSection.length, 'chars');

// Pages to update
const pagesToUpdate = [
    'upsc/ancient-history/Prehistory/History-of-Mesolithic-or-Middle-Stone-Age/index.html',
    'upsc/ancient-history/Prehistory/History-of-Neolithic-Age-or-New-Stone-Age/index.html',
    'upsc/ancient-history/Prehistory/History-of-Paleolithic-or-Old-Stone-Age/index.html',
    'upsc/ancient-history/Prehistory/History-of-Chalcolithic-Age/index.html',
    'upsc/ancient-history/Prehistory/History-of-Early-Iron-Age/index.html',
    'upsc/ancient-history/Prehistory/Geographical-Distribution-and-Characteristics-of-Pre-History/index.html',
    'upsc/ancient-history/Prehistory/Sources-of-Information-of-Pre-History/index.html'
];

pagesToUpdate.forEach(pagePath => {
    console.log(`\nProcessing: ${pagePath}`);

    // First, restore the original page (since previous scripts may have corrupted it)
    // We read the page.manifest.json to get the original generated content
    // Actually, we'll just overwrite everything after the upsc-page-data script element
    const pageContent = fs.readFileSync(pagePath, 'utf8');
    const pageLines = pageContent.split('\n');

    // Find the upsc-page-data closing script tag
    const pageDataEndIndex = pageLines.findIndex(l => l.includes('</script>') &&
        pageLines.indexOf(l) > pageLines.findIndex(x => x.includes('upsc-page-data')));

    if (pageDataEndIndex === -1) {
        console.log('  ✗ Could not find upsc-page-data end in', pagePath);
        return;
    }

    // Find the topic-content div closing
    const topicContentEnd = pageLines.findIndex(l => l.includes('</main>'));

    // Find the </body> tag 
    const bodyEndLine = pageLines.findIndex(l => l.includes('</body>'));

    // Build updated page: keep everything from start to the end of page data, 
    // then insert the template footer section, then close body/html
    const updatedPage = [
        ...pageLines.slice(0, pageDataEndIndex + 1),
        '',
        templateFooterSection
    ].join('\n');

    // Ensure it ends properly
    const finalPage = updatedPage.endsWith('</html>') || updatedPage.endsWith('</html>\n')
        ? updatedPage
        : updatedPage + '\n</body>\n</html>\n';

    fs.writeFileSync(pagePath, finalPage);
    console.log(`  ✓ Updated ${pagePath}`);
});

console.log('\n✓ All Prehistory pages updated with template structure!');