/**
 * Performance Optimization Script for SJMaths
 * Applies Font Awesome async loading and lazy analytics to all HTML files
 * 
 * Run with: node scripts/apply-perf-fixes.js
 */

const fs = require('fs');
const path = require('path');

const ROOT_DIR = path.join(__dirname, '..');

// Stats tracking
const stats = {
    processed: 0,
    fontAwesomeFixed: 0,
    analyticsFixed: 0,
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
 * Fix render-blocking Font Awesome
 * Replaces: <link rel="stylesheet" href="...font-awesome...">
 * With: <link rel="preload" as="style" ... onload="this.onload=null;this.rel='stylesheet'">
 */
function fixFontAwesome(content) {
    // Pattern to match render-blocking Font Awesome link
    const blockingPattern = /<link\s+rel="stylesheet"\s+href="(https:\/\/cdnjs\.cloudflare\.com\/ajax\/libs\/font-awesome\/[^"]+)"[^>]*>/gi;

    // Skip if already using preload pattern
    if (content.includes('font-awesome') && content.includes('rel="preload"')) {
        return { content, fixed: false };
    }

    const match = blockingPattern.exec(content);
    if (!match) {
        return { content, fixed: false };
    }

    const fontAwesomeUrl = match[1];

    const asyncPattern = `<link rel="preload" as="style" href="${fontAwesomeUrl}"
        onload="this.onload=null;this.rel='stylesheet'" crossorigin="anonymous">
    <noscript>
        <link rel="stylesheet" href="${fontAwesomeUrl}">
    </noscript>`;

    const newContent = content.replace(match[0], asyncPattern);

    return { content: newContent, fixed: true };
}

/**
 * Fix synchronous analytics
 * Replaces synchronous firebase analytics import with lazy loading
 */
function fixAnalytics(content) {
    // Skip if already using lazy pattern
    if (content.includes('requestIdleCallback') && content.includes('firebase-config')) {
        return { content, fixed: false };
    }

    // More flexible pattern to match various analytics formats
    // Matches: import { analytics, logEvent } from "...firebase-config.js"; followed by logEvent call
    const syncAnalyticsPattern = /<script\s+type="module">\s*(?:\/\/[^\n]*\n)?\s*import\s*\{\s*analytics\s*,\s*logEvent\s*\}\s*from\s*["']([^"']+firebase-config\.js)["'];?\s*(?:\/\/[^\n]*\n)?\s*logEvent\s*\(\s*analytics\s*,\s*["']page_view["']\s*,\s*\{[^}]+\}\s*\)\s*;?\s*<\/script>/gi;

    const match = syncAnalyticsPattern.exec(content);
    if (!match) {
        return { content, fixed: false };
    }

    const configPath = match[1];

    const lazyAnalytics = `<script type="module">
        const loadAnalytics = async () => {
            try {
                const { analytics, logEvent } = await import("${configPath}");
                logEvent(analytics, "page_view", {
                    page_title: document.title,
                    page_path: window.location.pathname
                });
            } catch (e) { console.debug("Analytics deferred load"); }
        };
        if ('requestIdleCallback' in window) requestIdleCallback(loadAnalytics);
        else setTimeout(loadAnalytics, 3000);
    </script>`;

    const newContent = content.replace(match[0], lazyAnalytics);

    return { content: newContent, fixed: true };
}

/**
 * Process a single HTML file
 */
function processFile(filePath) {
    try {
        let content = fs.readFileSync(filePath, 'utf8');
        let modified = false;

        // Fix Font Awesome
        const faResult = fixFontAwesome(content);
        if (faResult.fixed) {
            content = faResult.content;
            modified = true;
            stats.fontAwesomeFixed++;
        }

        // Fix Analytics
        const analyticsResult = fixAnalytics(content);
        if (analyticsResult.fixed) {
            content = analyticsResult.content;
            modified = true;
            stats.analyticsFixed++;
        }

        if (modified) {
            fs.writeFileSync(filePath, content, 'utf8');
            console.log(`✅ Fixed: ${path.relative(ROOT_DIR, filePath)}`);
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
    console.log('🚀 SJMaths Performance Optimization Script\n');
    console.log('Scanning for HTML files...\n');

    const htmlFiles = findHtmlFiles(ROOT_DIR);
    console.log(`Found ${htmlFiles.length} HTML files\n`);

    htmlFiles.forEach(processFile);

    // Summary
    console.log('\n' + '='.repeat(50));
    console.log('📊 Summary');
    console.log('='.repeat(50));
    console.log(`Total files processed: ${stats.processed}`);
    console.log(`Font Awesome fixed:    ${stats.fontAwesomeFixed}`);
    console.log(`Analytics fixed:       ${stats.analyticsFixed}`);
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
