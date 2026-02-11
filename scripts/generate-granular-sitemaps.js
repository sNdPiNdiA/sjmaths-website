const fs = require('fs');
const path = require('path');

const BASE_URL = 'https://www.sjmaths.com';
const ROOT_DIR = '.';

const EXCLUDE_DIRS = [
    'node_modules', '.git', 'scripts', 'assets', 'components', 'dist',
    '.firebase', '.vscode', '_legacy_site', 'questions-module'
];

const EXCLUDE_FILES = [
    '404.html', 'offline.html', 'dashboard.html', 'profile.html',
    'settings.html', 'google-site-verification.html'
];

function getAllHtmlFiles(dir) {
    let results = [];
    if (!fs.existsSync(dir)) return results;

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

function writeSitemap(filename, files) {
    const urls = files.map(file => {
        let urlPath = file.replace(/\\/g, '/');
        // Remove leading ./ if present
        if (urlPath.startsWith('./')) urlPath = urlPath.substring(2);

        // Canonical directory URLs
        if (urlPath === 'index.html') urlPath = '';
        else if (urlPath.endsWith('/index.html')) urlPath = urlPath.replace('index.html', '');

        let priority = '0.8';
        let changefreq = 'monthly';

        if (urlPath === '') { priority = '1.0'; changefreq = 'weekly'; }
        else if (urlPath.match(/^classes\/class-\d+\/$/)) { priority = '0.9'; changefreq = 'weekly'; }

        return `
  <url>
    <loc>${BASE_URL}/${urlPath}</loc>
    <lastmod>${new Date().toISOString().split('T')[0]}</lastmod>
    <changefreq>${changefreq}</changefreq>
    <priority>${priority}</priority>
  </url>`;
    });

    const content = `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
${urls.join('')}
</urlset>`;

    fs.writeFileSync(filename, content);
    console.log(`✅ Generated ${filename} with ${urls.length} URLs.`);
}

// 1. Get ALL valid HTML files in the project
const allFiles = getAllHtmlFiles(ROOT_DIR);

// 2. Separate them into buckets
const mainSitemapFiles = [];
const classSitemaps = {
    'class-9': [],
    'class-10': [],
    'class-11': [],
    'class-12': []
};

allFiles.forEach(file => {
    const relativePath = path.relative(ROOT_DIR, file).replace(/\\/g, '/');

    if (relativePath.startsWith('classes/class-9/')) {
        classSitemaps['class-9'].push(file);
    } else if (relativePath.startsWith('classes/class-10/')) {
        classSitemaps['class-10'].push(file);
    } else if (relativePath.startsWith('classes/class-11/')) {
        classSitemaps['class-11'].push(file);
    } else if (relativePath.startsWith('classes/class-12/')) {
        classSitemaps['class-12'].push(file);
    } else {
        // Core pages: root pages, classes/index.html, etc.
        mainSitemapFiles.push(file);
    }
});

// 3. Write sitemaps
writeSitemap('sitemap-main.xml', mainSitemapFiles);
for (const [cls, files] of Object.entries(classSitemaps)) {
    writeSitemap(`sitemap-${cls}.xml`, files);
}

console.log('🚀 All granular sitemaps updated successfully!');
