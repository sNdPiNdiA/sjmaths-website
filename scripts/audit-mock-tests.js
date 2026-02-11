const fs = require('fs');
const path = require('path');

const baseDir = 'c:\\Users\\sande\\Documents\\GitHub\\sjmaths-website\\classes\\class-9\\tests\\full-length-tests';
const rootDir = 'c:\\Users\\sande\\Documents\\GitHub\\sjmaths-website';

const files = fs.readdirSync(baseDir);

files.forEach(file => {
    const filePath = path.join(baseDir, file);
    if (file.endsWith('.json')) {
        try {
            const content = fs.readFileSync(filePath, 'utf8');
            JSON.parse(content);
            console.log(`[OK] JSON: ${file}`);
        } catch (e) {
            console.log(`[ERROR] JSON Syntax: ${file} - ${e.message}`);
        }
    } else if (file.endsWith('.html')) {
        const content = fs.readFileSync(filePath, 'utf8');

        // Check CSS path
        const cssMatch = content.match(/href="([^"]*test-interface[^"]*)"/);
        if (cssMatch) {
            const relPath = cssMatch[1];
            const absPath = path.resolve(baseDir, relPath);
            if (fs.existsSync(absPath)) {
                console.log(`[OK] HTML CSS: ${file}`);
            } else {
                console.log(`[ERROR] HTML CSS Path: ${file} -> ${relPath} (Resolved: ${absPath})`);
            }
        } else {
            console.log(`[WARNING] HTML CSS Not Found: ${file}`);
        }

        // Check JS path
        const jsMatch = content.match(/src="([^"]*test-engine[^"]*)"/);
        if (jsMatch) {
            const relPath = jsMatch[1];
            const absPath = path.resolve(baseDir, relPath);
            if (fs.existsSync(absPath)) {
                console.log(`[OK] HTML JS: ${file}`);
            } else {
                console.log(`[ERROR] HTML JS Path: ${file} -> ${relPath} (Resolved: ${absPath})`);
            }
        } else {
            console.log(`[WARNING] HTML JS Not Found: ${file}`);
        }
    }
});
