const fs = require('fs');
const path = require('path');

// Template file path
const templatePath = 'upsc/ancient-history/Prehistory/Prehistoric-Time-Periods/index.html';
const template = fs.readFileSync(templatePath, 'utf8');

// Extract the common structural parts from template
const templateLines = template.split('\n');

// Find key line numbers in template
const headEndLine = templateLines.findIndex(l => l.includes('</head>'));
const bodyStartLine = templateLines.findIndex(l => l.includes('<body>'));
const mainStartLine = templateLines.findIndex(l => l.includes('<main class="topic-container"'));
const mainEndLine = templateLines.findIndex(l => l.includes('</main>'));
const scriptStartLine = templateLines.findIndex(l => l.includes('<!-- Page data as JSON -->'));
const footerStartLine = templateLines.findIndex(l => l.includes('<!-- Reusable renderers -->'));

console.log('Template structure lines:', {
    headEnd: headEndLine,
    bodyStart: bodyStartLine,
    mainStart: mainStartLine,
    mainEnd: mainEndLine,
    scriptStart: scriptStartLine,
    footerStart: footerStartLine
});

// Pages to update (excluding template)
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

    // Find key sections in current page
    const pageHeadEnd = pageLines.findIndex(l => l.includes('</head>'));
    const pageBodyStart = pageLines.findIndex(l => l.includes('<body>'));
    const pageMainStart = pageLines.findIndex(l => l.includes('<main class="topic-container"'));
    const pageMainEnd = pageLines.findIndex(l => l.includes('</main>'));
    const pageScriptStart = pageLines.findIndex(l => l.includes('<!-- Page data as JSON -->'));
    const pageFooterStart = pageLines.findIndex(l => l.includes('<!-- Reusable renderers -->'));

    console.log('  Current page structure:', {
        headEnd: pageHeadEnd,
        bodyStart: pageBodyStart,
        mainStart: pageMainStart,
        mainEnd: pageMainEnd,
        scriptStart: pageScriptStart,
        footerStart: pageFooterStart
    });

    // Extract page-specific content
    const pageHead = pageLines.slice(0, pageHeadEnd + 1).join('\n');
    const pageMain = pageLines.slice(pageMainStart, pageMainEnd + 1).join('\n');
    const pageScripts = pageLines.slice(pageScriptStart).join('\n');

    // Extract template structural parts
    const templateHeadEnd = templateLines.slice(0, headEndLine + 1).join('\n');
    const templateBodyStart = templateLines.slice(bodyStartLine, bodyStartLine + 10).join('\n');
    const templateMainStart = templateLines.slice(mainStartLine, mainStartLine + 5).join('\n');
    const templateMainEnd = templateLines.slice(mainEndLine - 5, mainEndLine + 1).join('\n');
    const templateFooter = templateLines.slice(footerStartLine).join('\n');

    // Build new page structure
    const newPage = [
        ...pageLines.slice(0, pageHeadEnd), // Keep original head up to </head>
        '', // Empty line
        ...templateLines.slice(headEndLine + 1, bodyStartLine), // Add body tag and header-container
        ...pageLines.slice(pageMainStart, pageMainEnd), // Keep original main content
        '', // Empty line
        ...templateLines.slice(mainEndLine + 1, scriptStartLine), // Add page data script tag
        ...pageLines.slice(pageScriptStart, pageLines.length - 1), // Keep original scripts
        '', // Empty line
        ...templateLines.slice(templateLines.length - 2) // Closing tags
    ].join('\n');

    // Write updated page
    fs.writeFileSync(pagePath, newPage);
    console.log(`  ✓ Updated ${pagePath}`);
});

console.log('\n✓ All Prehistory pages have been updated with template structure');