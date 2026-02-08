// ============================================
// FILE: scripts/inject-canonical.js
// Run with: node scripts/inject-canonical.js
// ============================================

const fs = require('fs');
const path = require('path');

// Configuration
const DOMAIN = 'https://www.sjmaths.com';
const EXCLUDE_DIRS = ['node_modules', '.git', 'components', 'assets', 'scripts', 'dist'];

function getHtmlFiles(dir) {
    let results = [];
    const list = fs.readdirSync(dir);
    
    list.forEach(file => {
        const fullPath = path.join(dir, file);
        const stat = fs.statSync(fullPath);
        
        if (stat && stat.isDirectory()) {
            if (!EXCLUDE_DIRS.includes(file)) {
                results = results.concat(getHtmlFiles(fullPath));
            }
        } else {
            if (file.endsWith('.html')) {
                results.push(fullPath);
            }
        }
    });
    return results;
}

function generateCanonicalUrl(filePath) {
    // Normalize path separators for Windows
    let relativePath = filePath.replace(/\\/g, '/');
    
    // Remove leading ./ if present
    if (relativePath.startsWith('./')) relativePath = relativePath.substring(2);
    
    // Handle root index.html
    if (relativePath === 'index.html') {
        return `${DOMAIN}/`;
    }
    
    // Handle directory indexes (e.g., classes/class-9/index.html -> classes/class-9/)
    if (relativePath.endsWith('/index.html')) {
        return `${DOMAIN}/${relativePath.replace('index.html', '')}`;
    }

    // Handle standard pages
    return `${DOMAIN}/${relativePath}`;
}

function injectCanonical(filePath) {
    let content = fs.readFileSync(filePath, 'utf8');
    
    // Skip if already present
    if (content.includes('<link rel="canonical"')) {
        console.log(`⚠️  Skipping ${filePath}: Canonical tag already exists.`);
        return;
    }

    const url = generateCanonicalUrl(filePath);
    const tag = `<link rel="canonical" href="${url}">`;

    // Injection logic: Try to place after <title>, otherwise before </head>
    let modified = false;
    
    if (content.includes('</title>')) {
        content = content.replace('</title>', `</title>\n    ${tag}`);
        modified = true;
    } else if (content.includes('</head>')) {
        content = content.replace('</head>', `    ${tag}\n</head>`);
        modified = true;
    }

    if (modified) {
        fs.writeFileSync(filePath, content, 'utf8');
        console.log(`✅ Injected: ${url} into ${filePath}`);
    } else {
        console.log(`❌ Failed to inject into ${filePath}: No <title> or <head> tag found.`);
    }
}

console.log('🚀 Starting Canonical Tag Injection...');
const files = getHtmlFiles('.');
files.forEach(injectCanonical);
console.log('✨ Injection Complete!');