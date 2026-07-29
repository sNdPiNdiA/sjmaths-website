const fs = require('fs');

// Read the template file
const templatePath = 'upsc/ancient-history/Prehistory/Prehistoric-Time-Periods/index.html';
const template = fs.readFileSync(templatePath, 'utf8');
const templateLines = template.split('\n');

// Find key sections in template
const premiumStyleStart = templateLines.findIndex(l => l.includes('<!-- Premium Page Styles -->'));
const premiumStyleEnd = templateLines.findIndex(l => l.includes('</style>')) + 1;
const langToggleStart = templateLines.findIndex(l => l.includes('// Language toggle:'));
const langToggleEnd = templateLines.findIndex(l => l.includes('</script>')) + 1;

// Extract sections to copy
const premiumStyles = templateLines.slice(premiumStyleStart, premiumStyleEnd).join('\n');
const langToggleScript = templateLines.slice(langToggleStart, langToggleEnd).join('\n');

console.log('Template sections extracted:', {
    premiumStyles: premiumStyleStart + '-' + premiumStyleEnd,
    langToggle: langToggleStart + '-' + langToggleEnd
});

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

    const pageContent = fs.readFileSync(pagePath, 'utf8');
    const pageLines = pageContent.split('\n');

    // Find insertion points
    const faqSchemaEnd = pageLines.findIndex(l => l.includes('</script>') && l.includes('FAQPage'));
    const reusableRenderersLine = pageLines.findIndex(l => l.includes('<!-- Reusable renderers -->'));
    const globalFooterLine = pageLines.findIndex(l => l.includes('global-footer.min.js'));

    // Build updated page
    const updatedPage = [
        ...pageLines.slice(0, faqSchemaEnd + 1),
        '',
        premiumStyles,
        '',
        ...pageLines.slice(faqSchemaEnd + 1, reusableRenderersLine),
        '',
        langToggleScript,
        '',
        ...pageLines.slice(reusableRenderersLine, globalFooterLine),
        '',
        ...pageLines.slice(globalFooterLine)
    ].join('\n');

    fs.writeFileSync(pagePath, updatedPage);
    console.log(`  ✓ Updated ${pagePath}`);
});

console.log('\n✓ All Prehistory pages updated with template structure!');
console.log('Added: Premium styles, language toggle, failsafe overlay, debug helpers');