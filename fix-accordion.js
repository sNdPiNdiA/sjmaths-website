const fs = require('fs');
const path = require('path');

function walk(dir) {
    let results = [];
    const list = fs.readdirSync(dir);
    list.forEach(file => {
        const fullPath = path.resolve(dir, file);
        const stat = fs.statSync(fullPath);
        if (stat && stat.isDirectory() && !fullPath.includes('node_modules')) {
            results = results.concat(walk(fullPath));
        } else if (fullPath.endsWith('.html')) {
            results.push(fullPath);
        }
    });
    return results;
}

const files = walk('classes');
let count = 0;

const darkModeCSS = `
        /* --- Dark Mode Overrides for Accordion --- */
        body.dark-mode .chapter-item {
            background: #1e1e1e;
            border-color: #333;
        }
        body.dark-mode .chapter-header {
            background: #1e1e1e;
        }
        body.dark-mode .chapter-header:hover {
            background: #252525;
        }
        body.dark-mode .chap-title {
            color: #ecf0f1;
        }
        body.dark-mode .chap-meta {
            color: #94a3b8;
        }
        body.dark-mode .chap-badge {
            background: #2c2c2c;
            color: var(--primary-light);
            box-shadow: inset 0 0 0 1px rgba(255, 255, 255, 0.1);
        }
        body.dark-mode .chapter-item.active .chap-badge {
            background: var(--primary);
            color: white;
        }
        body.dark-mode .toggle-icon {
            background: #333;
            color: #ccc;
        }
        body.dark-mode .chapter-item.active .toggle-icon {
            background: var(--primary-light);
            color: white;
        }
        body.dark-mode .exercise-panel {
            background: #121212;
            border-top-color: #333;
        }
        body.dark-mode .ex-btn {
            background: #252525;
            border-color: #444;
            color: #e0e0e0;
        }
        body.dark-mode .ex-btn:hover {
            background: var(--primary);
            border-color: var(--primary);
            color: white;
        }
        body.dark-mode .btn-misc {
            background: rgba(243, 156, 18, 0.1);
            border-color: var(--accent);
            color: var(--accent);
        }
        body.dark-mode .btn-misc:hover {
            background: var(--accent);
            color: white;
        }
    </style>`;

files.forEach(file => {
    let content = fs.readFileSync(file, 'utf8');
    if (content.includes('.chapter-item') && !content.includes('Dark Mode Overrides for Accordion')) {
        content = content.replace(/<\/style>/, darkModeCSS);
        fs.writeFileSync(file, content, 'utf8');
        count++;
        console.log("Updated: " + file);
    }
});

console.log('Injected dark mode CSS into ' + count + ' accordion files.');
