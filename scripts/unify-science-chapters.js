const fs = require('fs');
const path = require('path');

const scienceDir = path.join(__dirname, '..', 'class-9-advanced-science');

function unifyFiles() {
    const chapters = fs.readdirSync(scienceDir).filter(name => {
        return fs.statSync(path.join(scienceDir, name)).isDirectory() && name.startsWith('chapter-');
    });

    chapters.forEach(chapter => {
        const filePath = path.join(scienceDir, chapter, 'index.html');
        if (!fs.existsSync(filePath)) return;

        let content = fs.readFileSync(filePath, 'utf8');

        // 1. Replace the first <style>...</style> block in <head>
        content = content.replace(/<style>[\s\S]*?<\/style>/, '<link rel="stylesheet" href="../../../assets/css/science-chapter.css">');

        // 2. Identify and replace the tab script block
        if (chapter === 'chapter-10-engineering-life-miracles-in-biotechnology') {
            // Standardize Chapter 10 classes in HTML
            content = content.replace(/class="tabs"/g, 'class="science-tabs"');
            content = content.replace(/class="tab([^s]|$)/g, 'class="science-tab$1');
            content = content.replace(/class="pane/g, 'class="tab-pane');

            // Remove tab-related JS logic but keep Three.js animations
            content = content.replace(
                /const tabs = document\.querySelectorAll\('\.tab'\), panes = document\.querySelectorAll\('\.pane'\);[\s\S]*?window\.toggleSolution = function[\s\S]*?{ const box = btn\.nextElementSibling; const open = box\.classList\.toggle\('open'\); btn\.textContent = open \? 'Hide Solution' : 'Show Solution' };/,
                ''
            );

            // Inject science-chapter.js reference before the animation script block
            content = content.replace(
                '<script>',
                '<script src="../../../assets/js/science-chapter.js" defer></script>\n    <script>'
            );
        } else {
            // For Chapters 1-9: Replace the main IIFE script block with science-chapter.js reference
            content = content.replace(
                /<script>[\s\S]*?const tabs = document\.querySelectorAll\("\.science-tab"\);[\s\S]*?<\/script>/,
                '<script src="../../../assets/js/science-chapter.js" defer></script>'
            );
        }

        fs.writeFileSync(filePath, content, 'utf8');
        console.log(`Successfully unified ${chapter}/index.html`);
    });
}

unifyFiles();
