const fs = require('fs');
const path = require('path');

const ROOT_DIR = process.cwd();
const EXCLUDED_DIRS = new Set(['.git', 'node_modules', 'assets']);

function walk(dir, callback) {
    fs.readdirSync(dir, { withFileTypes: true }).forEach(dirent => {
        if (EXCLUDED_DIRS.has(dirent.name)) return;
        const res = path.join(dir, dirent.name);
        if (dirent.isDirectory()) {
            walk(res, callback);
        } else if (dirent.isFile() && dirent.name.endsWith('.html')) {
            callback(res);
        }
    });
}

let fixedCount = 0;

walk(ROOT_DIR, (filePath) => {
    let content = fs.readFileSync(filePath, 'utf8');
    if (content.startsWith('?<!DOCTYPE html>')) {
        console.log(`Fixing: ${filePath}`);
        content = content.replace('?<!DOCTYPE html>', '<!DOCTYPE html>');
        fs.writeFileSync(filePath, content, 'utf8');
        fixedCount++;
    }
});

console.log(`Finished! Fixed ${fixedCount} files.`);
