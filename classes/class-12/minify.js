const fs = require('fs');
const path = require('path');

// Simple minifier script for CSS and JS
// Usage: node scripts/minify.js

const dirsToScan = ['assets/css', 'assets/js'];

function minifyCSS(content) {
    return content
        .replace(/\/\*[\s\S]*?\*\//g, '') // Remove comments
        .replace(/\s+/g, ' ') // Collapse whitespace
        .replace(/\s*([\{\}\:\;\,])\s*/g, '$1') // Remove space around delimiters
        .replace(/\;}/g, '}') // Remove trailing semicolon
        .trim();
}

function minifyJS(content) {
    // Basic JS minification (safe subset)
    // Note: For production, use a tool like Terser
    return content
        .replace(/\/\*[\s\S]*?\*\//g, '') // Remove block comments
        .replace(/\/\/.*/g, '') // Remove line comments
        .replace(/^\s+|\s+$/gm, '') // Trim lines
        .replace(/\n/g, ' ') // Remove newlines
        .replace(/\s+/g, ' ') // Collapse whitespace
        .replace(/\s*([\{\}\(\)\[\]\=\,\:\;\?])\s*/g, '$1') // Remove space around delimiters
        .replace(/\s+\=\>\s+/g, '=>') // Fix arrow functions
        .trim();
}

function processDirectory(dir) {
    if (!fs.existsSync(dir)) return;

    const files = fs.readdirSync(dir);
    
    files.forEach(file => {
        const fullPath = path.join(dir, file);
        const ext = path.extname(file);
        const baseName = path.basename(file, ext);
        
        if (file.endsWith('.min.css') || file.endsWith('.min.js')) return;

        if (ext === '.css') {
            const content = fs.readFileSync(fullPath, 'utf8');
            const minified = minifyCSS(content);
            const outPath = path.join(dir, `${baseName}.min.css`);
            fs.writeFileSync(outPath, minified);
            console.log(`Minified: ${file} -> ${baseName}.min.css`);
        } else if (ext === '.js') {
            const content = fs.readFileSync(fullPath, 'utf8');
            const minified = minifyJS(content);
            const outPath = path.join(dir, `${baseName}.min.js`);
            fs.writeFileSync(outPath, minified);
            console.log(`Minified: ${file} -> ${baseName}.min.js`);
        }
    });
}

console.log('Starting minification...');
dirsToScan.forEach(dir => processDirectory(path.join(__dirname, '..', dir)));
console.log('Done.');