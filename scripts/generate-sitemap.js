// ============================================
// FILE: scripts/generate-sitemap.js
// Run with: node scripts/generate-sitemap.js
// ============================================

const fs = require('fs');
const path = require('path');

const BASE_URL = 'https://www.sjmaths.com';
const ROOT_DIR = '.';
const OUTPUT_FILE = 'sitemap.xml';

// Directories to ignore (System folders, assets, etc.)
const EXCLUDE_DIRS = [
    'node_modules', 
    '.git', 
    'scripts', 
    'assets', 
    'components', 
    'dist', 
    '.firebase',
    '.vscode',
    'questions-module' // Assuming this contains templates/assets not direct pages
];

// Files to ignore (Private pages, error pages, utility pages)
const EXCLUDE_FILES = [
    '404.html',
    'offline.html',
    'search.html',
    'dashboard.html',
    'profile.html',
    'settings.html',
    'notifications.html',
    'google-site-verification.html'
];

function getAllHtmlFiles(dir) {
    let results = [];
    const list = fs.readdirSync(dir);
    
    list.forEach(file => {
        const fullPath = path.join(dir, file);
        const stat = fs.statSync(fullPath);
        
        if (stat && stat.isDirectory()) {
            if (!EXCLUDE_DIRS.includes(file)) {
                results = results.concat(getAllHtmlFiles(fullPath));
            }
        } else {
            if (file.endsWith('.html') && !EXCLUDE_FILES.includes(file)) {
                results.push(fullPath);
            }
        }
    });
    return results;
}

function generateSitemap() {
    console.log('🔍 Scanning for public HTML files...');
    const files = getAllHtmlFiles(ROOT_DIR);
    console.log(`   Found ${files.length} pages.`);

    const urls = files.map(file => {
        // Convert file path to URL path
        let urlPath = file.replace(/\\/g, '/'); // Fix Windows slashes
        
        // Clean up relative path prefixes
        if (urlPath.startsWith('./')) urlPath = urlPath.substring(2);
        else if (urlPath.startsWith('/')) urlPath = urlPath.substring(1);

        // Handle index.html (Canonical URLs usually end in / for directories)
        if (urlPath === 'index.html') {
            urlPath = '';
        } else if (urlPath.endsWith('/index.html')) {
            urlPath = urlPath.replace('index.html', '');
        }

        // Determine Priority and Change Frequency based on content type
        let priority = '0.8';
        let changefreq = 'monthly';

        if (urlPath === '') { // Homepage
            priority = '1.0';
            changefreq = 'weekly';
        } else if (urlPath.match(/^classes\/class-\d+\/$/)) { // Class Landing Pages
            priority = '0.9';
            changefreq = 'weekly';
        } else if (urlPath.includes('login') || urlPath.includes('signup')) {
            priority = '0.5';
            changefreq = 'yearly';
        }

        return `
  <url>
    <loc>${BASE_URL}/${urlPath}</loc>
    <lastmod>${new Date().toISOString().split('T')[0]}</lastmod>
    <changefreq>${changefreq}</changefreq>
    <priority>${priority}</priority>
  </url>`;
    });

    const sitemapContent = `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
${urls.join('')}
</urlset>`;

    fs.writeFileSync(OUTPUT_FILE, sitemapContent);
    console.log(`✅ Sitemap generated at ${OUTPUT_FILE} with ${urls.length} URLs!`);
}

generateSitemap();