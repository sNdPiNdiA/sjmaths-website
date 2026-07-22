const fs = require('fs');
const path = require('path');

const sscCglDir = 'c:/Users/sande/Documents/GitHub/sjmaths-website/ssc-cgl';

function getHtmlFiles(dir) {
    let results = [];
    const list = fs.readdirSync(dir);
    list.forEach(file => {
        const fullPath = path.join(dir, file);
        const stat = fs.statSync(fullPath);
        if (stat && stat.isDirectory()) {
            results = results.concat(getHtmlFiles(fullPath));
        } else if (file === 'index.html') {
            results.push(fullPath);
        }
    });
    return results;
}

const htmlFiles = getHtmlFiles(sscCglDir);
console.log('Total index.html files under ssc-cgl:', htmlFiles.length);

let reorderedCount = 0;

htmlFiles.forEach(file => {
    let content = fs.readFileSync(file, 'utf8');

    if (content.includes('tab-notes') && content.includes('tab-tricks') && content.includes('<!-- Tab 1 Panel -->')) {
        const newNavBar = `<div class="main-tabs-nav">
            <button class="tab-btn active" onclick="openTab(event, 'tab-theory')">
                <i class="fas fa-book-open"></i> 1. Concept & Theory
            </button>
            <button class="tab-btn" onclick="openTab(event, 'tab-tricks')">
                <i class="fas fa-bolt"></i> 2. Topper Tricks
            </button>
            <button class="tab-btn" onclick="openTab(event, 'tab-notes')">
                <i class="fas fa-file-alt"></i> 3. Notes & FAQs
            </button>
            <button class="tab-btn" onclick="openTab(event, 'tab-practice')">
                <i class="fas fa-tasks"></i> 4. Practice MCQs
            </button>
            <button class="tab-btn" onclick="openTab(event, 'tab-pyqs')">
                <i class="fas fa-history"></i> 5. PYQs (MCQs)
            </button>
        </div>`;

        // Swap nav bar
        content = content.replace(/<div class="(?:main-tabs-nav|tab-nav)">[\s\S]*?<\/div>/, newNavBar);

        // Perform clean extraction & reordering of panels
        const mainStart = content.indexOf('<!-- Tab 1 Panel -->');
        const mainEnd = content.indexOf('</main>');

        if (mainStart !== -1 && mainEnd !== -1 && mainEnd > mainStart) {
            const beforeMain = content.slice(0, mainStart);
            const afterMain = content.slice(mainEnd);

            const t1Block = content.slice(content.indexOf('<!-- Tab 1 Panel -->'), content.indexOf('<!-- Tab 2 Panel -->'));
            const t2Block = content.slice(content.indexOf('<!-- Tab 2 Panel -->'), content.indexOf('<!-- Tab 3 Panel -->'));
            const t3Block = content.slice(content.indexOf('<!-- Tab 3 Panel -->'), content.indexOf('<!-- Tab 4 Panel -->'));
            const t4Block = content.slice(content.indexOf('<!-- Tab 4 Panel -->'), content.indexOf('<!-- Tab 5 Panel -->'));
            const t5Block = content.slice(content.indexOf('<!-- Tab 5 Panel -->'), mainEnd);

            const reorderedPanels = `<!-- Tab 1 Panel -->\n${t1Block.slice(t1Block.indexOf('<div id="tab-theory"'))}\n\n` +
                                    `<!-- Tab 2 Panel -->\n${t2Block.slice(t2Block.indexOf('<div id="tab-tricks"'))}\n\n` +
                                    `<!-- Tab 3 Panel: Notes & FAQs -->\n${t5Block.slice(t5Block.indexOf('<div id="tab-notes"'))}\n\n` +
                                    `<!-- Tab 4 Panel: Practice MCQs -->\n${t3Block.slice(t3Block.indexOf('<div id="tab-practice"'))}\n\n` +
                                    `<!-- Tab 5 Panel: PYQs -->\n${t4Block.slice(t4Block.indexOf('<div id="tab-pyqs"'))}\n\n`;

            content = beforeMain + reorderedPanels + afterMain;
            fs.writeFileSync(file, content, 'utf8');
            reorderedCount++;
        }
    }
});

console.log('✅ Successfully reordered tabs in ' + reorderedCount + ' SSC CGL HTML files.');
