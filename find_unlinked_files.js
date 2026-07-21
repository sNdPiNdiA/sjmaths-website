const fs = require('fs');
const path = require('path');

const syllabusPath = 'ssc-cgl/syllabus/index.html';
const baseDir = 'ssc-cgl';

// Read the syllabus HTML
const html = fs.readFileSync(syllabusPath, 'utf8');

// Extract all href values - match href="..." or href='...'
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
        // Keep other paths as-is if they don't start with known prefixes
        continue;
    }

    // Normalize path - remove trailing slashes
    resolvedPath = resolvedPath.replace(/\\/g, '/').replace(/\/+/g, '/').replace(/\/+$/, '');

    if (resolvedPath) {
        linkedPaths.add(resolvedPath);
    }
}

console.log(`Found ${linkedPaths.size} unique linked paths inside ssc-cgl/`);

// Get all actual files in ssc-cgl
function getAllFiles(dir, base = '') {
    let results = [];
    const items = fs.readdirSync(dir);

    for (const item of items) {
        const fullPath = path.join(dir, item);
        const relativePath = path.join(base, item).replace(/\\/g, '/');

        if (fs.statSync(fullPath).isDirectory()) {
            results.push({ path: relativePath, isDir: true });
            results = results.concat(getAllFiles(fullPath, relativePath));
        } else {
            results.push({ path: relativePath, isDir: false });
        }
    }

    return results;
}

const allFiles = getAllFiles(baseDir);

// Find unlinked files (not dirs)
// A file is considered linked if:
// 1. Its path (without index.html) is in linkedPaths, OR
// 2. The linkedPaths contains a prefix of the file's directory path
const unlinked = allFiles.filter(item => {
    if (item.isDir) return false;

    // Never delete the syllabus index.html
    if (item.path === 'syllabus/index.html') {
        return false;
    }

    // Remove /index.html from the end if present
    const withoutIndexHtml = item.path.replace(/\/index\.html$/, '');

    // Check if the path (without index.html) is directly in linkedPaths
    if (linkedPaths.has(withoutIndexHtml)) {
        return false;
    }

    // Check if any linked path is a parent directory of this file
    for (const linkedPath of linkedPaths) {
        if (withoutIndexHtml.startsWith(linkedPath + '/')) {
            return false;
        }
    }

    return true;
});

console.log(`\nTotal files in ssc-cgl: ${allFiles.filter(i => !i.isDir).length}`);
console.log(`Unlinked files: ${unlinked.length}`);

if (unlinked.length > 0) {
    console.log('\nDeleting unlinked files...');
    for (const item of unlinked) {
        const fullPath = path.join(baseDir, item.path);
        fs.unlinkSync(fullPath);
        console.log('Deleted: ' + item.path);
    }
    console.log(`\nSuccessfully deleted ${unlinked.length} files.`);
} else {
    console.log('No unlinked files found.');
}