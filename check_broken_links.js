const fs = require('fs');
const path = require('path');

const syllabusPath = 'ssc-cgl/syllabus/index.html';
const baseDir = 'ssc-cgl';

// Read the syllabus HTML
const html = fs.readFileSync(syllabusPath, 'utf8');

// Extract all href values
const hrefRegex = /\bhref\s*=\s*["']([^"']+)["']/g;
const linkedPaths = new Set();
let match;

while ((match = hrefRegex.exec(html)) !== null) {
    const href = match[1];

    // Resolve the path relative to ssc-cgl/syllabus/
    let resolvedPath;
    if (href.startsWith('/ssc-cgl/')) {
        resolvedPath = href.replace(/^\/ssc-cgl\//, '');
    } else if (href.startsWith('../')) {
        resolvedPath = href.replace(/^\.\.\//, '');
    } else if (href.startsWith('./')) {
        resolvedPath = href.replace(/^\.\//, '');
    } else {
        // Skip external or other links
        continue;
    }

    // Normalize path
    resolvedPath = resolvedPath.replace(/\\/g, '/').replace(/\/+/g, '/').replace(/\/+$/, '');

    if (resolvedPath) {
        linkedPaths.add(resolvedPath);
    }
}

console.log(`Checking ${linkedPaths.size} unique linked paths for broken links...\n`);

const brokenLinks = [];

for (const linkedPath of linkedPaths) {
    // Check if the linked path exists as a directory with index.html
    const indexPath = path.join(baseDir, linkedPath, 'index.html');
    const directPath = path.join(baseDir, linkedPath);

    // Try directory with index.html first
    if (fs.existsSync(indexPath)) {
        continue; // Link is valid
    }

    // Try as direct file path
    if (fs.existsSync(directPath)) {
        const stat = fs.statSync(directPath);
        if (stat.isFile()) {
            continue; // Link is valid
        }
    }

    // Link is broken
    brokenLinks.push({
        linkedPath: linkedPath,
        expectedIndex: indexPath,
        expectedDirect: directPath
    });
}

if (brokenLinks.length > 0) {
    console.log(`Found ${brokenLinks.length} broken links (would result in 404 errors):\n`);
    for (const link of brokenLinks) {
        console.log(`  /ssc-cgl/${link.linkedPath}/`);
        console.log(`    Expected: ${link.expectedIndex}`);
        console.log(`    Or: ${link.expectedDirect}\n`);
    }
} else {
    console.log('All links are valid - no 404 errors found.');
}