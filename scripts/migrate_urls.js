const fs = require('fs');
const path = require('path');

console.log("Starting URL Migration...");

const SKIPPED_DIRS = new Set([
  '.git', '.firebase', '.vscode', 'assets', 'components', 'dataconnect',
  'digital-evaluation', 'node_modules', 'questions-module', 'scripts',
  'src', 'utils', 'scratch', 'venv', '.venv', 'gs-question-bank'
]);

function walk(dir, allHtmlFiles = [], nodesToRename = []) {
    const list = fs.readdirSync(dir);
    
    list.forEach(function(file) {
        if (SKIPPED_DIRS.has(file)) return;
        const filePath = path.join(dir, file);
        const stat = fs.lstatSync(filePath);
        if (stat.isSymbolicLink()) return;
        
        if (file.includes('_')) {
            nodesToRename.push({ path: filePath, isDir: stat.isDirectory() });
        }
        
        if (stat.isDirectory()) {
            walk(filePath, allHtmlFiles, nodesToRename);
        } else if (file.endsWith('.html')) {
            allHtmlFiles.push(filePath);
        }
    });
    
    return { allHtmlFiles, nodesToRename };
}

console.log("Scanning directory tree...");
const { allHtmlFiles, nodesToRename } = walk('.');

let filesToRename = nodesToRename.filter(n => !n.isDir);
let dirsToRename = nodesToRename.filter(n => n.isDir);

console.log(`Found ${filesToRename.length} files and ${dirsToRename.length} directories to rename.`);

// 1. Rename files first
filesToRename.forEach(node => {
    const dir = path.dirname(node.path);
    const oldBase = path.basename(node.path);
    const newBase = oldBase.replace(/_/g, '-');
    const newPath = path.join(dir, newBase);
    fs.renameSync(node.path, newPath);
});
console.log(`Renamed ${filesToRename.length} files.`);

// 2. Rename directories (deepest first)
dirsToRename.sort((a, b) => b.path.split(path.sep).length - a.path.split(path.sep).length);
dirsToRename.forEach(node => {
    const dir = path.dirname(node.path);
    const oldBase = path.basename(node.path);
    const newBase = oldBase.replace(/_/g, '-');
    const newPath = path.join(dir, newBase);
    fs.renameSync(node.path, newPath);
});
console.log(`Renamed ${dirsToRename.length} directories.`);

// 3. Fix internal links in ALL HTML files
console.log(`Scanning for HTML files to update internal links... (Total: ${allHtmlFiles.length})`);

let linkFixCount = 0;
let processedCount = 0;

allHtmlFiles.forEach(f => {
    processedCount++;
    if (processedCount % 1000 === 0) console.log(`Processed ${processedCount} HTML files...`);
    
    // Some paths might have changed if their parent directories had underscores!
    // But we already renamed them! So the physical path 'f' might no longer exist!
    // Let's compute the new path.
    const fSplit = f.split(path.sep);
    const newFSplit = fSplit.map(part => part.replace(/_/g, '-'));
    const actualPath = newFSplit.join(path.sep);

    if (!fs.existsSync(actualPath)) {
        return; // File might have been renamed and we missed mapping it? No, replacing all _ with - handles it.
    }

    let c = fs.readFileSync(actualPath, 'utf8');
    let changed = false;

    const urlRegex = /(href|src|content)=["'](\/[^"']+|https:\/\/sjmaths\.com\/[^"']+)["']/gi;
    
    c = c.replace(urlRegex, (match, attr, url) => {
        if (url.includes('_')) {
            const newUrl = url.replace(/_/g, '-');
            changed = true;
            return `${attr}="${newUrl}"`;
        }
        return match;
    });

    if (changed) {
        fs.writeFileSync(actualPath, c, 'utf8');
        linkFixCount++;
    }
});

console.log(`Fixed internal links in ${linkFixCount} HTML files.`);

// 4. Update firebase.json
console.log("Updating firebase.json redirects...");
const firebasePath = 'firebase.json';
const firebaseData = JSON.parse(fs.readFileSync(firebasePath, 'utf8'));

if (!firebaseData.hosting.redirects) {
    firebaseData.hosting.redirects = [];
}

const rootRenames = dirsToRename.filter(n => !path.dirname(n.path).includes('_'));

rootRenames.forEach(n => {
    const oldUrlPath = n.path.replace(/\\/g, '/');
    const newUrlPath = oldUrlPath.replace(/_/g, '-');

    firebaseData.hosting.redirects.push({
        "regex": `^/${oldUrlPath}/(.*)$`,
        "destination": `/${newUrlPath}/:1`,
        "type": 301
    });
    
    firebaseData.hosting.redirects.push({
        "source": `/${oldUrlPath}/`,
        "destination": `/${newUrlPath}/`,
        "type": 301
    });
});

fs.writeFileSync(firebasePath, JSON.stringify(firebaseData, null, 2));
console.log(`Added ${rootRenames.length * 2} redirects to firebase.json.`);

// 5. Update seo-policy.js
const seoPolicyPath = 'scripts/seo-policy.js';
let seoPolicy = fs.readFileSync(seoPolicyPath, 'utf8');
if (seoPolicy.includes('_')) {
    seoPolicy = seoPolicy.replace(/['"]([^'"]*_[^'"]*)['"]/g, (match, p1) => {
        return `"${p1.replace(/_/g, '-')}"`;
    });
    fs.writeFileSync(seoPolicyPath, seoPolicy, 'utf8');
    console.log('Updated seo-policy.js to use hyphens.');
}

console.log('Migration Complete!');
