const fs = require('fs');
const path = require('path');
const cheerio = require('cheerio');

const walkDir = (dir, callback) => {
    fs.readdirSync(dir).forEach(f => {
        let dirPath = path.join(dir, f);
        let isDirectory = fs.statSync(dirPath).isDirectory();
        isDirectory ? walkDir(dirPath, callback) : callback(path.join(dir, f));
    });
};

const upscDir = path.join(__dirname, '../upsc');
let mergeCount = 0;

function processDirectory(dir) {
    const enHtmlPath = path.join(dir, 'index.html');
    const hiHtmlPath = path.join(dir, 'hi', 'index.html');
    
    if (fs.existsSync(enHtmlPath) && fs.existsSync(hiHtmlPath)) {
        
        let enHtml = fs.readFileSync(enHtmlPath, 'utf8');
        let hiHtml = fs.readFileSync(hiHtmlPath, 'utf8');
        
        const $en = cheerio.load(enHtml, { decodeEntities: false });
        const $hi = cheerio.load(hiHtml, { decodeEntities: false });
        
        const enNotesPanel = $en('#notes-panel');
        if (!enNotesPanel.length) return; 
        
        const enInner = enNotesPanel.html();
        enNotesPanel.empty();
        enNotesPanel.append(`\n<div class="lang-en">\n${enInner}\n</div>\n`);
        
        const hiNotesPanel = $hi('#notes-panel');
        let hiInner = hiNotesPanel.html() || '';
        
        // Fix duplicate IDs
        hiInner = hiInner.replace(/id="prehistory-mindmap-container"/g, 'id="prehistory-mindmap-container-hi"');
        hiInner = hiInner.replace(/id="mindmap-card"/g, 'id="mindmap-card-hi"');
        
        enNotesPanel.append(`\n<div class="lang-hi" style="display:none;">\n${hiInner}\n</div>\n`);
        
        // Find mindmap script in Hindi and append it
        const hiScripts = $hi('script').filter((i, el) => {
            const scriptContent = $hi(el).html() || '';
            return scriptContent.includes('renderMindmap');
        });
        
        if (hiScripts.length > 0) {
            hiScripts.each((i, el) => {
                let scriptContent = $hi(el).html();
                scriptContent = scriptContent.replace(/undefined,\s*'hi'/g, "'prehistory-mindmap-container-hi', 'hi'");
                $en('body').append(`\n<script>\n${scriptContent}\n</script>\n`);
            });
        }
        
        // Find embedded study guide JSON in Hindi
        const hiJsonScript = $hi('script#embedded-study-guide-data');
        if (hiJsonScript.length > 0) {
            let jsonContent = hiJsonScript.html();
            $en('body').append(`\n<script type="application/json" id="embedded-study-guide-data-hi">\n${jsonContent}\n</script>\n`);
        }
        
        // Remove mobile lang toggle link (handled by JS now)
        $en('a.mobile-lang-toggle').remove();
        
        fs.writeFileSync(enHtmlPath, $en.html());
        fs.rmSync(path.join(dir, 'hi'), { recursive: true, force: true });
        
        mergeCount++;
        if (mergeCount % 100 === 0) {
            console.log(`Merged ${mergeCount} files...`);
        }
    }
}

const directories = new Set();
walkDir(upscDir, (filePath) => {
    directories.add(path.dirname(filePath));
});

console.log(`Found ${directories.size} directories to scan.`);
directories.forEach(processDirectory);
console.log(`Successfully merged ${mergeCount} content files.`);
