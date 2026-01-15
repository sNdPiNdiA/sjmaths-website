const fs = require('fs');
const path = require('path');

// Configuration
const BASE_URL = 'https://www.sjmaths.com';
const EXCLUDE_DIRS = ['node_modules', '.git', 'components', 'utils', 'assets', 'scripts', 'questions-module'];
const EXCLUDE_FILES = ['404.html', 'google*.html'];

function getHtmlFiles(dir, fileList = []) {
    if (!fs.existsSync(dir)) return fileList;
    
    const files = fs.readdirSync(dir);
    
    files.forEach(file => {
        const filePath = path.join(dir, file);
        const stat = fs.statSync(filePath);
        
        if (stat.isDirectory()) {
            if (!EXCLUDE_DIRS.includes(file)) {
                getHtmlFiles(filePath, fileList);
            }
        } else {
            if (file.endsWith('.html') && !EXCLUDE_FILES.includes(file)) {
                fileList.push(filePath);
            }
        }
    });
    
    return fileList;
}

console.log('🔍 Scanning for HTML files...');
const files = getHtmlFiles('.');

const sitemapContent = `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
${files.map(file => {
    // Convert file path to URL path
    let relativePath = path.relative('.', file).replace(/\\/g, '/');
    let urlPath = relativePath === 'index.html' ? '' : relativePath;
    
    // Remove index.html from end of paths for cleaner URLs
    urlPath = urlPath.replace(/\/index\.html$/, '/');
    
    return `  <url>
    <loc>${BASE_URL}/${urlPath}</loc>
    <changefreq>weekly</changefreq>
    <priority>${urlPath === '' ? '1.0' : '0.8'}</priority>
  </url>`;
}).join('\n')}
</urlset>`;

fs.writeFileSync('sitemap.xml', sitemapContent);
console.log(`✅ Generated sitemap.xml with ${files.length} URLs`);