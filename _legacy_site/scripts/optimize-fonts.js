/**
 * Font Async Loading Script for SJMaths
 * Converts Google Fonts from render-blocking to non-blocking across all pages
 * 
 * Run with: node scripts/optimize-fonts.js
 */

const fs = require('fs');
const path = require('path');

const ROOT_DIR = path.join(__dirname, '..');

// Stats tracking
const stats = {
    processed: 0,
    poppinsFixed: 0,
    interFixed: 0,
    skipped: 0,
    errors: []
};

/**
 * Find all HTML files recursively
 */
function findHtmlFiles(dir, exclude = ['node_modules', '.git', '.firebase']) {
    let files = [];

    if (!fs.existsSync(dir)) return files;

    const items = fs.readdirSync(dir);

    items.forEach(item => {
        const fullPath = path.join(dir, item);

        if (exclude.some(ex => fullPath.includes(ex))) return;

        const stat = fs.statSync(fullPath);

        if (stat.isDirectory()) {
            files = files.concat(findHtmlFiles(fullPath, exclude));
        } else if (item.endsWith('.html')) {
            files.push(fullPath);
        }
    });

    return files;
}

/**
 * Convert render-blocking font links to async preload pattern
 */
function optimizeFonts(content) {
    let modified = false;

    // Skip if already using preload pattern for fonts.googleapis
    if (content.includes('rel="preload"') && content.includes('fonts.googleapis.com') && content.includes('onload=')) {
        return { content, modified: false };
    }

    // Pattern: render-blocking Poppins
    const poppinsPattern = /<link\s+href="(https:\/\/fonts\.googleapis\.com\/css2\?family=Poppins:[^"]+)"\s+rel="stylesheet"\s*>/gi;

    let poppinsMatch = poppinsPattern.exec(content);
    if (poppinsMatch) {
        const poppinsUrl = poppinsMatch[1];
        const asyncPoppins = `<link rel="preload" as="style" href="${poppinsUrl}"
        onload="this.onload=null;this.rel='stylesheet'">
    <noscript><link href="${poppinsUrl}" rel="stylesheet"></noscript>`;

        content = content.replace(poppinsMatch[0], asyncPoppins);
        modified = true;
        stats.poppinsFixed++;
    }

    // Pattern: render-blocking Inter
    const interPattern = /<link\s+href="(https:\/\/fonts\.googleapis\.com\/css2\?family=Inter:[^"]+)"\s+rel="stylesheet"\s*>/gi;

    let interMatch = interPattern.exec(content);
    if (interMatch) {
        const interUrl = interMatch[1];
        const asyncInter = `<link rel="preload" as="style" href="${interUrl}"
        onload="this.onload=null;this.rel='stylesheet'">
    <noscript><link href="${interUrl}" rel="stylesheet"></noscript>`;

        content = content.replace(interMatch[0], asyncInter);
        modified = true;
        stats.interFixed++;
    }

    return { content, modified };
}

/**
 * Process a single HTML file
 */
function processFile(filePath) {
    try {
        let content = fs.readFileSync(filePath, 'utf8');

        const result = optimizeFonts(content);

        if (result.modified) {
            fs.writeFileSync(filePath, result.content, 'utf8');
            console.log(`✅ Optimized: ${path.relative(ROOT_DIR, filePath)}`);
        } else {
            stats.skipped++;
        }

        stats.processed++;

    } catch (error) {
        stats.errors.push({ file: filePath, error: error.message });
        console.error(`❌ Error: ${path.relative(ROOT_DIR, filePath)} - ${error.message}`);
    }
}

/**
 * Main execution
 */
function main() {
    console.log('🚀 SJMaths Font Async Loading Script\n');
    console.log('Scanning for HTML files...\n');

    const htmlFiles = findHtmlFiles(ROOT_DIR);
    console.log(`Found ${htmlFiles.length} HTML files\n`);

    htmlFiles.forEach(processFile);

    // Summary
    console.log('\n' + '='.repeat(50));
    console.log('📊 Summary');
    console.log('='.repeat(50));
    console.log(`Total files processed: ${stats.processed}`);
    console.log(`Poppins made async:    ${stats.poppinsFixed}`);
    console.log(`Inter made async:      ${stats.interFixed}`);
    console.log(`Already optimized:     ${stats.skipped}`);

    if (stats.errors.length > 0) {
        console.log(`\n❌ Errors: ${stats.errors.length}`);
        stats.errors.forEach(({ file, error }) => {
            console.log(`   - ${path.relative(ROOT_DIR, file)}: ${error}`);
        });
    }

    console.log('\n✨ Done!');
}

main();
