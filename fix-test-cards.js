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
        /* --- Dark Mode Overrides for Test Cards --- */
        body.dark-mode .test-card {
            background: #1e1e1e;
            border-color: #333;
        }
        body.dark-mode .test-card:hover {
            border-color: var(--primary);
            box-shadow: 0 15px 30px rgba(142, 68, 173, 0.2);
        }
        body.dark-mode .test-card h3 {
            color: #ecf0f1;
        }
        body.dark-mode .test-card p {
            color: #bdc3c7;
        }
        body.dark-mode .icon-box {
            background: #252525;
            color: var(--primary-light);
        }
        body.dark-mode summary {
            background: #2c2c2c;
            color: #e0e0e0;
        }
        body.dark-mode summary:hover {
            background: #333;
        }
        body.dark-mode details[open] summary {
            background: var(--primary-dark);
            color: white;
        }
        body.dark-mode .dropdown-content {
            background: #1e1e1e;
            border-color: #333;
        }
        body.dark-mode .dropdown-content a {
            color: #bdc3c7;
            border-bottom-color: #2c2c2c;
        }
        body.dark-mode .dropdown-content a:hover {
            background: #252525;
            color: var(--primary-light);
        }
        body.dark-mode .tag {
            background: #333;
            color: #aaa;
        }
    </style>`;

files.forEach(file => {
    let content = fs.readFileSync(file, 'utf8');
    if (content.includes('.test-card') && !content.includes('Dark Mode Overrides for Test Cards')) {
        content = content.replace(/<\/style>/, darkModeCSS);
        fs.writeFileSync(file, content, 'utf8');
        count++;
        console.log("Updated: " + file);
    }
});

console.log('Injected dark mode CSS into ' + count + ' test index files.');
