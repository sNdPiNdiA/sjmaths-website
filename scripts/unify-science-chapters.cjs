const fs = require('fs');
const path = require('path');

const scienceDir = path.join(__dirname, '..', 'class-9-advanced-science');

function cleanAndUnifyAll() {
    const entries = fs.readdirSync(scienceDir, { withFileTypes: true });
    const chapters = entries
        .filter(entry => entry.isDirectory() && entry.name.startsWith('chapter-'))
        .map(entry => entry.name);

    chapters.forEach(chapter => {
        const filePath = path.join(scienceDir, chapter, 'index.html');
        if (!fs.existsSync(filePath)) return;

        let content = fs.readFileSync(filePath, 'utf8');

        // 1. Remove all inline <style>...</style> blocks
        content = content.replace(/<style>[\s\S]*?<\/style>/g, '');

        // 2. Remove the inline tab script block safely
        const inlineScriptRegex = /<script>(?![\s\S]*?<script>)[\s\S]*?const tabs = document\.querySelectorAll\((['"])\.science-tab\1\);[\s\S]*?<\/script>/g;
        content = content.replace(inlineScriptRegex, '');

        // 3. Clean up any leftover duplicate links, broken tags, or old asset references
        content = content.replace(/<link rel="stylesheet" href="science-chapter\.css">/g, '');
        content = content.replace(/<link rel="stylesheet" href="\.\.\/\.\.\/\.\.\/assets\/css\/science-chapter\.css">/g, '');
        content = content.replace(/<link rel="stylesheet" href="\.\.\/\.\.\/assets\/css\/science-chapter\.css">/g, '');
        content = content.replace(/<link rel="stylesheet" href="\.\.\/science-chapter\.css">/g, '');
        content = content.replace(/<script src="\.\.\/\.\.\/\.\.\/assets\/js\/science-chapter\.js" defer><\/script>/g, '');
        content = content.replace(/<script src="\.\.\/\.\.\/assets\/js\/science-chapter\.js" defer><\/script>/g, '');
        content = content.replace(/<script src="\.\.\/science-chapter\.js" defer><\/script>/g, '');
        content = content.replace(/<script src="\.\.\/\.\.\/\.\.\/assets\/js\/main\.min\.js" defer><\/script>/g, '');
        content = content.replace(/<script src="\.\.\/\.\.\/assets\/js\/main\.min\.js" defer><\/script>/g, '');
        content = content.replace(/<script>\s*src="\.\.\/\.\.\/\.\.\/assets\/js\/science-chapter\.js"\s*defer\s*><\/script>/g, '');
        content = content.replace(/<script>\s*<\/script>/g, '');

        // 4. Ensure the new common CSS link (../science-chapter.css) is present before </head>
        if (!content.includes('../science-chapter.css')) {
            content = content.replace('</head>', '    <link rel="stylesheet" href="../science-chapter.css">\n</head>');
        }

        // 5. Ensure global site layout CSS files are present in all chapters (using correct relative path: ../../)
        const globalCSS = [
            '../../assets/css/main.min.css',
            '../../assets/css/layout.min.css',
            '../../assets/css/component.min.css',
            '../../assets/css/improved-ui.min.css'
        ];

        // First clean up any incorrect ../../../ references
        content = content.replace(/\.\.\/\.\.\/\.\.\/assets\/css\//g, '../../assets/css/');

        globalCSS.forEach(cssPath => {
            if (!content.includes(cssPath)) {
                content = content.replace(
                    '    <link rel="stylesheet" href="../science-chapter.css">',
                    `    <link rel="stylesheet" href="${cssPath}">\n    <link rel="stylesheet" href="../science-chapter.css">`
                );
            }
        });

        // 6. First clean up incorrect main.min.js path if exists
        content = content.replace(/\.\.\/\.\.\/\.\.\/assets\/js\/main\.min\.js/g, '../../assets/js/main.min.js');

        // Ensure the site-wide main.min.js is loaded for global header, footer, PWA & Dark Mode toggle
        if (!content.includes('assets/js/main.min.js') && !content.includes('assets/js/main.js')) {
            content = content.replace('</body>', '    <script src="../../assets/js/main.min.js" defer></script>\n</body>');
        }

        // 7. Ensure the new common JS link (../science-chapter.js) is present before </body>
        if (!content.includes('../science-chapter.js')) {
            content = content.replace('</body>', '    <script src="../science-chapter.js" defer></script>\n</body>');
        }

        // 7b. Ensure the premium authentication gate script is present before </body>
        if (!content.includes('require-auth.min.js')) {
            content = content.replace('</body>', '    <script type="module" src="/assets/js/require-auth.min.js?v=2c63810b"></script>\n</body>');
        }

        // 8. Swap CDN Three.js link for local copy (using correct relative path: ../../)
        content = content.replace(
            /https:\/\/cdnjs\.cloudflare\.com\/ajax\/libs\/three\.js\/r128\/three\.min\.js/g,
            '../../assets/js/three.min.js'
        );
        content = content.replace(/\.\.\/\.\.\/\.\.\/assets\/js\/three\.min\.js/g, '../../assets/js/three.min.js');

        fs.writeFileSync(filePath, content, 'utf8');
        console.log(`Cleaned and successfully unified ${chapter}/index.html with correct relative paths`);
    });
}

cleanAndUnifyAll();
