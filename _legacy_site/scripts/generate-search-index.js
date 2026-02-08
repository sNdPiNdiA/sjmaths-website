// ============================================
// FILE: scripts/generate-search-index.js
// Run with: node scripts/generate-search-index.js
// ============================================

const fs = require('fs');
const path = require('path');

const ROOT_DIR = '.';
const OUTPUT_FILE = 'assets/js/search-index.json';

// Directories to ignore
const EXCLUDE_DIRS = ['node_modules', '.git', 'scripts', 'assets', 'components', 'dist', '.firebase'];

// Specific files to ignore (utility pages, auth pages, etc.)
const EXCLUDE_FILES = [
    '404.html', 
    'login.html', 
    'signup.html', 
    'offline.html', 
    'notifications.html', 
    'profile.html', 
    'settings.html', 
    'dashboard.html',
    'search.html'
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

function extractMetadata(filePath) {
    const content = fs.readFileSync(filePath, 'utf8');
    
    // Extract Title
    const titleMatch = content.match(/<title>(.*?)<\/title>/i);
    let title = titleMatch ? titleMatch[1].replace(' - SJMaths', '').trim() : '';
    
    // Extract Description
    const descMatch = content.match(/<meta\s+name=["']description["']\s+content=["'](.*?)["']/i);
    const description = descMatch ? descMatch[1].trim() : '';
    
    // Extract Keywords (optional, split by comma)
    const keywordsMatch = content.match(/<meta\s+name=["']keywords["']\s+content=["'](.*?)["']/i);
    // We store keywords as a single string for easier searching, or you can split them
    const keywords = keywordsMatch ? keywordsMatch[1] : '';

    // Determine Category based on path
    let category = 'General';
    const normalizedPath = filePath.replace(/\\/g, '/');
    
    if (normalizedPath.includes('chapter-wise-notes')) category = 'Chapter Notes';
    else if (normalizedPath.includes('ncert-exercise-practice')) category = 'NCERT Solutions';
    else if (normalizedPath.includes('ncert-exemplar-practice')) category = 'NCERT Exemplar';
    else if (normalizedPath.includes('previous-year-questions') || normalizedPath.includes('pyq')) category = 'Previous Year Questions';
    else if (normalizedPath.includes('sample-papers')) category = 'Sample Papers';
    else if (normalizedPath.includes('live-class')) category = 'Live Classes';
    else if (normalizedPath.includes('classes/class-')) {
        const classMatch = normalizedPath.match(/class-(\d+)/);
        if (classMatch) category = `Class ${classMatch[1]}`;
    }

    // Generate URL (relative to root, ensure forward slashes)
    let url = '/' + normalizedPath;
    // Clean up path if it starts with ./
    if (url.startsWith('/./') || url.startsWith('/.\\')) url = url.substring(2);
    if (url.startsWith('./')) url = url.substring(1);

    return { title, description, keywords, category, url };
}

console.log('🔍 Scanning for HTML files...');
const files = getAllHtmlFiles(ROOT_DIR);
console.log(`   Found ${files.length} files.`);

console.log('📝 Extracting metadata...');
const searchIndex = files.map(file => extractMetadata(file)).filter(item => item.title);

fs.writeFileSync(OUTPUT_FILE, JSON.stringify(searchIndex, null, 4));
console.log(`✅ Search index generated at ${OUTPUT_FILE} with ${searchIndex.length} items!`);