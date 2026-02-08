const fs = require('fs');
const path = require('path');
const esbuild = require('esbuild');

const ROOT_DIR = __dirname;
const ASSETS_DIR = path.join(ROOT_DIR, 'assets');

// Configuration: Files to Minify
// We explicitly list JS files to avoid breaking ES modules (like firebase-config.js) that are imported by filename
const JS_FILES = [
    'assets/js/main.js',
    'assets/js/search.js',
    'assets/js/recent-viewed.js'
];

// Helper to find all CSS files recursively
function getAllCssFiles(dir) {
    let results = [];
    if (!fs.existsSync(dir)) return results;
    const list = fs.readdirSync(dir);
    list.forEach(file => {
        const fullPath = path.join(dir, file);
        const stat = fs.statSync(fullPath);
        if (stat && stat.isDirectory()) {
            results = results.concat(getAllCssFiles(fullPath));
        } else if (file.endsWith('.css') && !file.endsWith('.min.css')) {
            results.push(path.relative(ROOT_DIR, fullPath).replace(/\\/g, '/'));
        }
    });
    return results;
}

const CSS_FILES = getAllCssFiles(path.join(ASSETS_DIR, 'css'));
const ALL_FILES = [...JS_FILES, ...CSS_FILES];

// Version for Cache Busting
const NEW_VERSION = Math.floor(Date.now() / 1000);

console.log(`🚀 Starting Build & Minification (v${NEW_VERSION})...`);

// 0. Clean Old Minified Files
function cleanMinifiedFiles(dir) {
    if (!fs.existsSync(dir)) return;
    const files = fs.readdirSync(dir);
    files.forEach(file => {
        const fullPath = path.join(dir, file);
        const stat = fs.statSync(fullPath);
        if (stat.isDirectory()) {
            cleanMinifiedFiles(fullPath);
        } else if (file.endsWith('.min.js') || file.endsWith('.min.css')) {
            try {
                fs.unlinkSync(fullPath);
                console.log(`🗑️  Deleted: ${path.relative(ROOT_DIR, fullPath)}`);
            } catch (e) {
                console.error(`❌ Failed to delete ${file}:`, e.message);
            }
        }
    });
}

console.log('🧹 Cleaning old minified files...');
cleanMinifiedFiles(ASSETS_DIR);

// 1. Minify Files
let mapping = {}; // maps 'assets/js/main.js' -> 'assets/js/main.min.js'

ALL_FILES.forEach(file => {
    const ext = path.extname(file);
    const minFile = file.replace(ext, `.min${ext}`);
    const inFile = path.join(ROOT_DIR, file);
    const outFile = path.join(ROOT_DIR, minFile);

    try {
        if (fs.existsSync(inFile)) {
            esbuild.buildSync({
                entryPoints: [inFile],
                outfile: outFile,
                minify: true,
                sourcemap: false,
            });
            console.log(`✅ Minified: ${file} -> ${minFile}`);
            mapping[file] = minFile;
        }
    } catch (e) {
        console.error(`❌ Failed to minify ${file}:`, e.message);
    }
});

// 2. Update References in HTML and Service Worker
function updateReferences(dir) {
    const files = fs.readdirSync(dir);
    files.forEach(file => {
        const filePath = path.join(dir, file);
        const stat = fs.statSync(filePath);

        if (stat.isDirectory()) {
            if (file !== 'node_modules' && file !== '.git' && file !== '.firebase') updateReferences(filePath);
        } else if (file.endsWith('.html') || file === 'service-worker.js') {
            let content = fs.readFileSync(filePath, 'utf8');
            let updated = false;

            // Replace references (e.g., main.css -> main.min.css)
            Object.keys(mapping).forEach(original => {
                const minified = mapping[original];
                // Regex to match filename, ensuring we don't double-min or match partials incorrectly
                // Matches: "assets/js/main.js" or 'assets/js/main.js'
                const regex = new RegExp(original.replace(/\./g, '\\.') + '(\\?v=[a-zA-Z0-9\\.]*)?', 'g');

                if (regex.test(content)) {
                    content = content.replace(regex, `${minified}?v=${NEW_VERSION}`);
                    updated = true;
                }
            });

            // Update Service Worker Cache Name
            if (file === 'service-worker.js') {
                const cacheRegex = /(const CACHE_NAME = ['"])([^'"]+)(['"])/;
                if (cacheRegex.test(content)) {
                    content = content.replace(cacheRegex, `$1sjmaths-v${NEW_VERSION}$3`);
                    updated = true;
                }
            }

            if (updated) {
                fs.writeFileSync(filePath, content, 'utf8');
                console.log(`📝 Updated references in: ${path.relative(ROOT_DIR, filePath)}`);
            }
        }
    });
}

updateReferences(ROOT_DIR);
console.log('✨ Build Complete!');