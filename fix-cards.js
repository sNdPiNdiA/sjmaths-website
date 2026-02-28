const fs = require('fs');
const path = require('path');

function walk(dir) {
    let results = [];
    const list = fs.readdirSync(dir);
    list.forEach(file => {
        file = path.resolve(dir, file);
        const stat = fs.statSync(file);
        if (stat && stat.isDirectory()) {
            results = results.concat(walk(file));
        } else if (file.endsWith('index.html')) {
            results.push(file);
        }
    });
    return results;
}

const files = walk('classes');
let count = 0;

const darkModeCSS = `
        /* --- Dark Mode for Cards --- */
        body.dark-mode .chapter-card,
        body.dark-mode .class-card {
            background: rgba(31, 41, 55, 0.8);
            border-color: rgba(255, 255, 255, 0.08);
        }
        body.dark-mode .chapter-card:hover,
        body.dark-mode .class-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 15px 35px rgba(190, 147, 212, 0.15);
            border-color: rgba(190, 147, 212, 0.3);
        }
        body.dark-mode .chap-info h2,
        body.dark-mode .card-content h3 {
            color: #ecf0f1;
        }
        body.dark-mode .chap-info span,
        body.dark-mode .card-content p {
            color: #bdc3c7;
        }
        body.dark-mode .arrow-icon,
        body.dark-mode .card-action i {
            background: rgba(31, 41, 55, 0.9);
            color: #be93d4;
        }
        body.dark-mode .chapter-card:hover .arrow-icon,
        body.dark-mode .class-card:hover .card-action i {
            background: #be93d4;
            color: white;
        }
        body.dark-mode .chap-number {
            color: rgba(190, 147, 212, 0.2);
        }
        body.dark-mode .chapter-card:hover .chap-number {
            color: rgba(190, 147, 212, 0.3);
        }
    </style>`;

files.forEach(file => {
    let content = fs.readFileSync(file, 'utf8');
    if ((content.includes('.chapter-card') || content.includes('.class-card')) && !content.includes('body.dark-mode .chapter-card')) {
        content = content.replace(/<\/style>/, darkModeCSS);
        fs.writeFileSync(file, content, 'utf8');
        count++;
    }
});

// Also fix main index.html
const mainIndex = 'index.html';
if (fs.existsSync(mainIndex)) {
    let content = fs.readFileSync(mainIndex, 'utf8');
    if (content.includes('.class-card') && !content.includes('body.dark-mode .class-card')) {
        content = content.replace(/<\/style>/, darkModeCSS);
        fs.writeFileSync(mainIndex, content, 'utf8');
        count++;
    }
}

console.log('Injected dark mode CSS into ' + count + ' files.');
