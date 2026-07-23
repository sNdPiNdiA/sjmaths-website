const fs = require('fs');
const path = require('path');

const baseDirs = [
    'c:/Users/sande/Documents/GitHub/sjmaths-website/ssc-cgl/quantitative-aptitude',
    'c:/Users/sande/Documents/GitHub/sjmaths-website/ssc-cgl/statistics'
];

// Define tab list sequence
const tabSequence = [
    { id: 'tab-theory', nextId: 'tab-tricks', en: 'Next: Topper Tricks', hi: 'आगे: टॉपर ट्रिक्स' },
    { id: 'tab-tricks', nextId: 'tab-notes', en: 'Next: Notes & FAQs', hi: 'आगे: नोट्स और अक्सर पूछे जाने वाले प्रश्न' },
    { id: 'tab-notes', nextId: 'tab-practice', en: 'Next: Practice MCQs', hi: 'आगे: अभ्यास प्रश्न (MCQs)' },
    { id: 'tab-practice', nextId: 'tab-pyqs', en: 'Next: PYQs (MCQs)', hi: 'आगे: पिछले वर्षों के प्रश्न (PYQs)' }
];

function processHtmlFile(filePath) {
    let content = fs.readFileSync(filePath, 'utf8');
    let original = content;

    // We can do standard string replacements.
    // Each tab panel has structure: <div id="tab-..." class="tab-panel..."> ... </div>
    // Let's insert the next button inside the panel just before the closing </div> of that tab-panel.
    
    // We will find the closing </div> of the tab-panels. Since tab panels are nested, it's safer to target the opening of the next panel
    // or locate the end of the panel content block.
    // Specifically, for our generated files:
    // Tab 1 ends right before: <!-- Tab 2 Panel --> or <div id="tab-tricks"
    // Tab 2 ends right before: <!-- Tab 3 Panel --> or <div id="tab-notes"
    // Tab 3 (notes) ends right before: <!-- Tab 4 Panel --> or <div id="tab-practice"
    // Tab 4 (practice) ends right before: <!-- Tab 5 Panel --> or <div id="tab-pyqs"

    // Let's create helper replacements.
    
    // 1. Tab 1: Concept & Theory -> next tab-tricks
    const buttonHtml1 = `\n<div class="next-tab-btn-container">\n  <button type="button" class="next-tab-btn" onclick="const btn = document.querySelector('.main-tabs-nav button[onclick*=\\'tab-tricks\\']') || document.querySelector('.main-tabs-nav button[data-tab=\\'tab-tricks\\']'); if (btn) { btn.click(); } else { const event = { currentTarget: this }; openTab(event, 'tab-tricks'); } window.scrollTo({top: 0, behavior: 'smooth'});">\n    <span class="lang-en">Next: Topper Tricks</span>\n    <span class="lang-hi">आगे: टॉपर ट्रिक्स</span>\n    <i class="fas fa-arrow-right"></i>\n  </button>\n</div>\n`;

    // 2. Tab 2: Topper Tricks -> next tab-notes
    const buttonHtml2 = `\n<div class="next-tab-btn-container">\n  <button type="button" class="next-tab-btn" onclick="const btn = document.querySelector('.main-tabs-nav button[onclick*=\\'tab-notes\\']') || document.querySelector('.main-tabs-nav button[data-tab=\\'tab-notes\\']'); if (btn) { btn.click(); } else { const event = { currentTarget: this }; openTab(event, 'tab-notes'); } window.scrollTo({top: 0, behavior: 'smooth'});">\n    <span class="lang-en">Next: Notes & FAQs</span>\n    <span class="lang-hi">आगे: नोट्स और अक्सर पूछे जाने वाले प्रश्न</span>\n    <i class="fas fa-arrow-right"></i>\n  </button>\n</div>\n`;

    // 3. Tab 3: Notes & FAQs -> next tab-practice
    const buttonHtml3 = `\n<div class="next-tab-btn-container">\n  <button type="button" class="next-tab-btn" onclick="const btn = document.querySelector('.main-tabs-nav button[onclick*=\\'tab-practice\\']') || document.querySelector('.main-tabs-nav button[data-tab=\\'tab-practice\\']'); if (btn) { btn.click(); } else { const event = { currentTarget: this }; openTab(event, 'tab-practice'); } window.scrollTo({top: 0, behavior: 'smooth'});">\n    <span class="lang-en">Next: Practice MCQs</span>\n    <span class="lang-hi">आगे: अभ्यास प्रश्न (MCQs)</span>\n    <i class="fas fa-arrow-right"></i>\n  </button>\n</div>\n`;

    // 4. Tab 4: Practice MCQs -> next tab-pyqs
    const buttonHtml4 = `\n<div class="next-tab-btn-container">\n  <button type="button" class="next-tab-btn" onclick="const btn = document.querySelector('.main-tabs-nav button[onclick*=\\'tab-pyqs\\']') || document.querySelector('.main-tabs-nav button[data-tab=\\'tab-pyqs\\']'); if (btn) { btn.click(); } else { const event = { currentTarget: this }; openTab(event, 'tab-pyqs'); } window.scrollTo({top: 0, behavior: 'smooth'});">\n    <span class="lang-en">Next: PYQs (MCQs)</span>\n    <span class="lang-hi">आगे: पिछले वर्षों के प्रश्न (PYQs)</span>\n    <i class="fas fa-arrow-right"></i>\n  </button>\n</div>\n`;

    // Ensure we clean up any pre-existing containers to prevent stacking on re-runs
    content = content.replace(/<div class="next-tab-btn-container">[\s\S]*?<\/div>\s*(?=\s*(?:<\/div>\s*<!--|\s*<\/div>\s*<div id="tab-|\s*<\/div>\s*<\/main>))/g, '');

    // Let's insert the buttons precisely before the closing div of each tab-panel.
    // We can match:
    // 1. The transition from tab-theory to tab-tricks:
    // ... </div> \s* <!-- Tab 2 Panel -->
    // We can replace the closing `</div>` of tab-theory with buttonHtml1 + `</div>`
    content = content.replace(/(id="tab-theory"[\s\S]*?)(\s*<\/div>\s*(?:<!--\s*Tab\s*2\s*Panel\s*-->|<div\s*id="tab-tricks"))/i, (m, p1, p2) => {
        return p1 + buttonHtml1 + p2;
    });

    // 2. The transition from tab-tricks to tab-notes:
    content = content.replace(/(id="tab-tricks"[\s\S]*?)(\s*<\/div>\s*(?:<!--\s*Tab\s*3\s*Panel\s*-->|<!--\s*Tab\s*3\s*Panel:\s*Notes\s*-->|<div\s*id="tab-notes"))/i, (m, p1, p2) => {
        return p1 + buttonHtml2 + p2;
    });

    // 3. The transition from tab-notes to tab-practice:
    content = content.replace(/(id="tab-notes"[\s\S]*?)(\s*<\/div>\s*(?:<!--\s*Tab\s*4\s*Panel\s*-->|<div\s*id="tab-practice"))/i, (m, p1, p2) => {
        return p1 + buttonHtml3 + p2;
    });

    // 4. The transition from tab-practice to tab-pyqs:
    content = content.replace(/(id="tab-practice"[\s\S]*?)(\s*<\/div>\s*(?:<!--\s*Tab\s*5\s*Panel\s*-->|<div\s*id="tab-pyqs"))/i, (m, p1, p2) => {
        return p1 + buttonHtml4 + p2;
    });

    if (content !== original) {
        fs.writeFileSync(filePath, content, 'utf8');
        console.log(`Injected next tab buttons in: ${filePath}`);
    }
}

function walk(dir) {
    const files = fs.readdirSync(dir);
    for (const file of files) {
        const fullPath = path.join(dir, file);
        const stat = fs.statSync(fullPath);
        if (stat.isDirectory()) {
            walk(fullPath);
        } else if (file === 'index.html') {
            processHtmlFile(fullPath);
        }
    }
}

baseDirs.forEach(dir => {
    if (fs.existsSync(dir)) {
        walk(dir);
    }
});

console.log('Regex-based Next Tab buttons injection completed successfully.');
