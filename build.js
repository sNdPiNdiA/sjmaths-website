import fs from 'fs';
import path from 'path';
import esbuild from 'esbuild';
import crypto from 'crypto';
import { fileURLToPath } from 'url';
import { commitBuildWrites } from './scripts/lib/build-transaction.mjs';
import { createReferenceUpdater } from './scripts/lib/build-references.mjs';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const rootArgument = process.argv.find(argument => argument.startsWith('--root='));
const ROOT_DIR = rootArgument ? path.resolve(rootArgument.slice(7)) : __dirname;
const DRY_RUN = process.argv.includes('--dry-run');
const ASSETS_DIR = path.join(ROOT_DIR, 'assets');
const UTILS_DIR = path.join(ROOT_DIR, 'utils');

// Helper to calculate file hash
function getFileHash(filePath) {
    const resolvedPath = path.resolve(ROOT_DIR, filePath);
    if (!fs.existsSync(resolvedPath)) {
        return 'no-file';
    }
    const content = fs.readFileSync(resolvedPath);
    return crypto.createHash('md5').update(content).digest('hex').substring(0, 8);
}

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

console.log('Preparing assets before changing served files.');
// Keep existing outputs until all replacement assets and references are ready.
const plannedWrites = new Map();
const compileFailures = [];

// 1. Minify Files
let mapping = {}; // maps 'assets/js/main.js' -> 'assets/js/main.min.js'

ALL_FILES.forEach(file => {
    const ext = path.extname(file);
    const minFile = file.replace(ext, `.min${ext}`);
    const inFile = path.join(ROOT_DIR, file);
    const outFile = path.join(ROOT_DIR, minFile);

    try {
        if (fs.existsSync(inFile)) {
            const result = esbuild.buildSync({
                entryPoints: [inFile],
                outfile: outFile,
                minify: true,
                sourcemap: false,
                write: false,
            });
            for (const output of result.outputFiles) plannedWrites.set(output.path, Buffer.from(output.contents));
            console.log(`✅ Minified: ${file} -> ${minFile}`);
            mapping[file] = minFile;
        }
    } catch (e) {
        compileFailures.push(file);
        console.error(`❌ Failed to minify ${file}:`, e.message);
    }
});

if (compileFailures.length) {
    throw new Error(`Build aborted without writing files: ${compileFailures.length} asset(s) failed to compile.`);
}

// 1.5. Manually add FontAwesome to mapping for cache busting
const faPath = 'assets/vendor/fontawesome/css/all.min.css';
if (fs.existsSync(path.join(ROOT_DIR, faPath))) {
    mapping['./' + faPath] = './' + faPath; 
    mapping[faPath] = faPath;               
}
const faBase = 'assets/vendor/fontawesome/css/fontawesome.min.css';
if (fs.existsSync(path.join(ROOT_DIR, faBase))) {
    mapping['./' + faBase] = './' + faBase;
    mapping[faBase] = faBase;
}

// Compute stable hashes for all mapped minified/vendor files
const fileHashes = {};
const uniqueMinFiles = new Set();
Object.values(mapping).forEach(minFile => {
    uniqueMinFiles.add(minFile);
});

uniqueMinFiles.forEach(minFile => {
    const prepared = plannedWrites.get(path.resolve(ROOT_DIR, minFile));
    fileHashes[minFile] = prepared
        ? crypto.createHash('md5').update(prepared).digest('hex').substring(0, 8)
        : getFileHash(minFile);
});

// Combined global assets hash for service worker
const sortedUniqueFiles = Array.from(uniqueMinFiles).sort();
const combinedHashes = sortedUniqueFiles.map(f => fileHashes[f]).join('-');
const GLOBAL_ASSETS_HASH = crypto.createHash('md5').update(combinedHashes).digest('hex').substring(0, 8);

console.log(`📦 Global Assets Hash: ${GLOBAL_ASSETS_HASH}`);

const updateAssetReferences = createReferenceUpdater(mapping, fileHashes);

// 2. Update References in HTML and Service Worker
function updateReferences(dir) {
    const files = fs.readdirSync(dir);
    files.forEach(file => {
        const filePath = path.join(dir, file);
        const stat = fs.statSync(filePath);

        if (stat.isDirectory()) {
            // Exclude heavy data directories and internal folders
            const ignoreDirs = ['node_modules', '.git', '.firebase', 'gs-question-bank', 'assets', 'utils', 'scripts', '.github', '.venv', 'scratch', '.pages-dist'];
            if (!ignoreDirs.includes(file)) updateReferences(filePath);
        } else if (file.endsWith('.html') || file === 'service-worker.js') {
            let content = fs.readFileSync(filePath, 'utf8');
            let updated = false;

            const newContent = updateAssetReferences(content);
            if (newContent !== content) {
                content = newContent;
                updated = true;
            }

            // Update Service Worker Cache Name
            if (file === 'service-worker.js') {
                const cacheRegex = /(const CACHE_NAME = ['"])([^'"]+)(['"])/;
                if (cacheRegex.test(content)) {
                    const newCacheContent = content.replace(cacheRegex, `$1sjmaths-v${GLOBAL_ASSETS_HASH}$3`);
                    if (newCacheContent !== content) {
                        content = newCacheContent;
                        updated = true;
                    }
                }
            }

            if (updated) {
                plannedWrites.set(filePath, Buffer.from(content, 'utf8'));
            }
        }
    });
}

updateReferences(ROOT_DIR);
const changedWrites = new Map([...plannedWrites].filter(([file, contents]) =>
    !fs.existsSync(file) || !fs.readFileSync(file).equals(contents)));
if (DRY_RUN) {
    console.log(`Build dry run complete: ${changedWrites.size} files would change; no files written.`);
} else {
    commitBuildWrites(changedWrites);
    console.log(`Build complete: ${changedWrites.size} files updated.`);
}
