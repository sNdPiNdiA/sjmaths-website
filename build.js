const fs = require('fs');
const path = require('path');
const esbuild = require('esbuild');

const ROOT_DIR = __dirname;
const ASSETS_DIR = path.join(ROOT_DIR, 'assets');
const UTILS_DIR = path.join(ROOT_DIR, 'utils');

// Helper to find all JS/CSS files recursively
function getTargetFiles(dir, extensions) {
    let results = [];
    if (!fs.existsSync(dir)) return results;
    const list = fs.readdirSync(dir);
    list.forEach(file => {
        const fullPath = path.join(dir, file);
        const stat = fs.statSync(fullPath);
        if (stat && stat.isDirectory()) {
            results = results.concat(getTargetFiles(fullPath, extensions));
        } else {
            const ext = path.extname(file);
            if (extensions.includes(ext) && !file.includes('.min.')) {
                results.push(path.relative(ROOT_DIR, fullPath).replace(/\\/g, '/'));
            }
        }
    });
    return results;
}

const JS_FILES = getTargetFiles(ASSETS_DIR, ['.js']).concat(getTargetFiles(UTILS_DIR, ['.js']));
const CSS_FILES = getTargetFiles(ASSETS_DIR, ['.css']);

// Filter out minified files from source list and ensure relative paths are clean
const ALL_FILES = [...JS_FILES, ...CSS_FILES].filter(f => !f.includes('.min.'));

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
            // Skip vendor directories (pre-minified third-party assets)
            if (file === 'vendor') {
                console.log(`⏩ Skipping vendor directory: ${path.relative(ROOT_DIR, fullPath)}`);
                return;
            }
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

// 1.5. Manually add FontAwesome to mapping for cache busting
// This ensures that references to vendor files also get versioned
const faPath = 'assets/vendor/fontawesome/css/all.min.css';
if (fs.existsSync(path.join(ROOT_DIR, faPath))) {
    mapping['./' + faPath] = './' + faPath; // Match SW format
    mapping[faPath] = faPath;               // Match HTML format
}
const faBase = 'assets/vendor/fontawesome/css/fontawesome.min.css';
if (fs.existsSync(path.join(ROOT_DIR, faBase))) {
    mapping['./' + faBase] = './' + faBase;
    mapping[faBase] = faBase;
}

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

                const ext = path.extname(original);
                const baseName = original.slice(0, -ext.length);
                const escapedBase = baseName.replace(/\./g, '\\.');
                const escapedExt = ext.replace(/\./g, '\\.');

                // Matches original, /original, ./original, ../original
                // with optional .min and optional ?v=...
                const regex = new RegExp('(\\/?|\\.\\/|\\.\\.\\/)' + escapedBase + '(\\.min)?' + escapedExt + '(\\?v=[a-zA-Z0-9\\.]*)?', 'g');

                if (regex.test(content)) {
                    content = content.replace(regex, (match, p1) => {
                        return `${p1}${minified}?v=${NEW_VERSION}`;
                    });
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