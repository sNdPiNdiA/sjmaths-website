const fs = require('fs');
const path = require('path');

const unifiedCSS = `
    <!-- Stylesheets -->
    <link rel="stylesheet" href="/assets/css/main.min.css?v=4ba21ce7">
    <link rel="stylesheet" href="/assets/css/layout.min.css?v=e4922b08">
    <link rel="stylesheet" href="/assets/css/component.min.css?v=8c99f11f">
    <link rel="stylesheet" href="/assets/css/improved-ui.min.css?v=574ed909">
    <link rel="stylesheet" href="/assets/css/topic-details.min.css?v=052ea02c">
    <link rel="stylesheet" href="/assets/css/upsssc-lower.min.css?v=94ee8a40">
</head>`;

const unifiedJS = `
    <!-- JavaScript Script References -->
    <script src="/assets/js/search.min.js?v=68a0a505" defer data-cfasync="false"></script>
    <script src="/assets/js/main.min.js?v=10f0770d" defer data-cfasync="false"></script>
    <script src="/assets/js/global-header.min.js?v=4d1d595g" defer data-cfasync="false"></script>
    <script src="/assets/js/global-footer.min.js?v=c641c625" defer data-cfasync="false"></script>
    <script src="/assets/js/upsssc-lower.min.js?v=04b168f8" defer data-cfasync="false"></script>
</body>`;

function processDirectory(dir) {
    const files = fs.readdirSync(dir);
    for (const file of files) {
        const fullPath = path.join(dir, file);
        if (fs.statSync(fullPath).isDirectory()) {
            processDirectory(fullPath);
        } else if (fullPath.endsWith('.html')) {
            processFile(fullPath);
        }
    }
}

function processFile(filePath) {
    let content = fs.readFileSync(filePath, 'utf8');

    // Remove ALL existing css links except fontawesome
    content = content.replace(/<link rel="stylesheet" href="\/assets\/css\/main\.min\.css[^>]*>\s*/g, '');
    content = content.replace(/<link rel="stylesheet" href="\/assets\/css\/layout\.min\.css[^>]*>\s*/g, '');
    content = content.replace(/<link rel="stylesheet" href="\/assets\/css\/component\.min\.css[^>]*>\s*/g, '');
    content = content.replace(/<link rel="stylesheet" href="\/assets\/css\/improved-ui\.min\.css[^>]*>\s*/g, '');
    content = content.replace(/<link rel="stylesheet" href="\/assets\/css\/topic-details\.min\.css[^>]*>\s*/g, '');
    content = content.replace(/<link rel="stylesheet" href="\/assets\/css\/upsssc-lower\.min\.css[^>]*>\s*/g, '');
    content = content.replace(/<!-- \?o\. Shared UPSSSC Lower styles -->\s*/g, '');
    content = content.replace(/<!-- Stylesheets -->\s*/g, '');

    // Inject unifiedCSS right before </head>
    content = content.replace(/<\/head>/, unifiedCSS.trim());

    // Remove ALL existing js links at the bottom
    content = content.replace(/<script src="\/assets\/js\/upsssc-lower\.min\.js[^>]*><\/script>\s*/g, '');
    content = content.replace(/<script src="\/assets\/js\/main\.min\.js[^>]*><\/script>\s*/g, '');
    content = content.replace(/<script src="\/assets\/js\/search\.min\.js[^>]*><\/script>\s*/g, '');
    content = content.replace(/<script src="\/assets\/js\/global-header\.min\.js[^>]*><\/script>\s*/g, '');
    content = content.replace(/<script src="\/assets\/js\/global-footer\.min\.js[^>]*><\/script>\s*/g, '');
    content = content.replace(/<!-- \?o\. Shared UPSSSC Lower JS .*?-->\s*/g, '');
    content = content.replace(/<!-- \?o\. Global site JS -->\s*/g, '');
    content = content.replace(/<!-- JavaScript Script References -->\s*/g, '');

    // Inject unifiedJS right before </body>
    content = content.replace(/<\/body>/, unifiedJS.trim());

    // Remove the old global header comment if it exists
    content = content.replace(/<!-- GLOBAL HEADER \/ NAVBAR would go here via include or copy from other pages -->\s*/, '');

    // Add header container right after <body> if it doesn't exist
    if (!content.includes('id="header-container"')) {
        content = content.replace(/<body>/, '<body>\n  <!-- Dynamic Header Container -->\n      <div id="header-container"></div>');
    }

    fs.writeFileSync(filePath, content, 'utf8');
}

processDirectory('upsssc-lower-mains');
console.log('Done unifying upsssc-lower-mains CSS and JS!');
