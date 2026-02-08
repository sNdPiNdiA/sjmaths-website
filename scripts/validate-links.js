const fs = require('fs');
const path = require('path');
const { promisify } = require('util');

const readdir = promisify(fs.readdir);
const readFile = promisify(fs.readFile);
const stat = promisify(fs.stat);

const ROOT_DIR = path.resolve(__dirname, '../');
const CLASSES_DIR = path.join(ROOT_DIR, 'classes');

async function getDirectories(source) {
    const dirents = await readdir(source, { withFileTypes: true });
    return dirents.filter(dirent => dirent.isDirectory()).map(dirent => dirent.name);
}

async function validateLinks() {
    console.log('Starting Link Validation for Class Cards...');
    const classDirs = await getDirectories(CLASSES_DIR);

    let totalLinks = 0;
    let brokenLinks = 0;

    for (const classDir of classDirs) {
        if (!classDir.startsWith('class-')) continue;

        const indexFile = path.join(CLASSES_DIR, classDir, 'index.html');
        if (!fs.existsSync(indexFile)) {
            console.warn(`WARNING: No index.html found for ${classDir}`);
            continue;
        }

        console.log(`\nChecking ${classDir}...`);
        const content = await readFile(indexFile, 'utf8');

        // Regex to find cards with hrefs
        // <a href="..." class="feature-card"> or similar
        const linkRegex = /<a[^>]+href=["'](.*?)["'][^>]*class=["'][^"']*feature-card[^"']*["'][^>]*>/gi;

        let match;
        while ((match = linkRegex.exec(content)) !== null) {
            const href = match[1];
            // Resolve path
            // href might be relative "chapter-wise-notes/index.html" or absolute "/classes/..."

            let targetPath;
            if (href.startsWith('/')) {
                // Absolute from root
                targetPath = path.join(ROOT_DIR, href);
            } else if (href.startsWith('http')) {
                // External - skip or checked via fetch (skipping for now)
                continue;
            } else {
                // Relative
                targetPath = path.join(path.dirname(indexFile), href);
            }

            // Remove anchors #
            targetPath = targetPath.split('#')[0];
            // Remove query params ?
            targetPath = targetPath.split('?')[0];

            totalLinks++;
            if (fs.existsSync(targetPath)) {
                // console.log(`  [OK] ${href}`);
            } else {
                console.error(`  [BROKEN] ${href}`);
                console.error(`       -> Resolved: ${targetPath}`);
                brokenLinks++;
            }
        }
    }

    console.log('\n------------------------------------------------');
    console.log(`Validation Complete.`);
    console.log(`Total Card Links Checked: ${totalLinks}`);
    console.log(`Broken Links: ${brokenLinks}`);

    if (brokenLinks === 0) {
        console.log('SUCCESS: All card paths are valid.');
    } else {
        console.error('FAILURE: Some card paths are broken. See details above.');
    }
}

validateLinks().catch(console.error);
