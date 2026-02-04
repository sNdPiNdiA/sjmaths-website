const fs = require('fs');
const path = require('path');

const ROOT_DIR = '.';
const EXCLUDE_DIRS = ['node_modules', '.git', '.firebase', 'components', 'assets'];

function findHtmlFiles(dir, files = []) {
    const items = fs.readdirSync(dir);
    for (const item of items) {
        const fullPath = path.join(dir, item);
        const stat = fs.statSync(fullPath);
        if (stat.isDirectory()) {
            if (!EXCLUDE_DIRS.includes(item)) {
                findHtmlFiles(fullPath, files);
            }
        } else if (item.endsWith('.html')) {
            files.push(fullPath);
        }
    }
    return files;
}

function processFiles() {
    const files = findHtmlFiles(ROOT_DIR);
    console.log(`🔍 Found ${files.length} HTML files.`);

    let modifiedCount = 0;

    files.forEach(file => {
        let content = fs.readFileSync(file, 'utf8');
        let modified = false;

        // 1. Calculate relative path to main.min.js
        const depth = file.split(path.sep).filter(Boolean).length - 1;
        const prefix = '../'.repeat(depth) || './';
        const mainScriptPath = `${prefix}assets/js/main.min.js`;

        // 2. Remove old scripts (navigation.js, shared-header.js, search.js)
        // We remove them if they are explicitly included as scripts, 
        // since main.js now handles nav and dynamic header/search.
        const scriptsToRemove = [
            / <script src=".*navigation(\.min)?\.js.*"><\/script>/gi,
            /<script src=".*shared-header\.js.*"><\/script>/gi,
            /<script type="module" src=".*shared-header\.js.*"><\/script>/gi,
            /<script type="module">[\s\S]*?initSharedHeader\(.*?\);[\s\S]*?<\/script>/gi
        ];

        scriptsToRemove.forEach(regex => {
            if (regex.test(content)) {
                content = content.replace(regex, '');
                modified = true;
            }
        });

        // 3. Inject main.min.js if not present
        if (!content.includes('main.min.js') && !content.includes('main.js')) {
            const scriptTag = `\n    <script src="${mainScriptPath}" defer></script>\n`;
            content = content.replace('</body>', `${scriptTag}</body>`);
            modified = true;
        } else if (content.includes('main.min.js')) {
            // Update path if necessary
            const regex = /<script src=".*assets\/js\/main\.min\.js.*"><\/script>/gi;
            const correctTag = `<script src="${mainScriptPath}" defer></script>`;
            if (!content.includes(correctTag)) {
                // Simplified check: just ensuring some version of the correct path is there is hard with regex matching versions
                // But build.js will handle versioning, we just ensure the path is correct-ish
            }
        }

        if (modified) {
            fs.writeFileSync(file, content, 'utf8');
            modifiedCount++;
        }
    });

    console.log(`\n✨ Propagation complete! Modified ${modifiedCount} files.`);
}

processFiles();
