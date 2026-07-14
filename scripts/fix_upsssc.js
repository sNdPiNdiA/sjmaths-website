const fs = require('fs');

let content = fs.readFileSync('upsssc-lower-mains/index.html', 'utf8');

// The file currently has:
// <link rel="stylesheet" href="/assets/css/main.min.css?v=4ba21ce7">`n    <link rel="stylesheet" href="/assets/css/layout.min.css?v=e4922b08">

// Fix it to have properly separated lines, and include component.min.css too
content = content.replace(
    /<link rel="stylesheet" href="\/assets\/css\/main\.min\.css\?v=4ba21ce7">`n    <link rel="stylesheet" href="\/assets\/css\/layout\.min\.css\?v=e4922b08">/g,
    `<link rel="stylesheet" href="/assets/css/main.min.css?v=4ba21ce7">\n    <link rel="stylesheet" href="/assets/css/layout.min.css?v=e4922b08">\n    <link rel="stylesheet" href="/assets/css/component.min.css?v=8c99f11f">`
);

fs.writeFileSync('upsssc-lower-mains/index.html', content, 'utf8');
console.log('Fixed upsssc-lower-mains/index.html');
