const fs = require('fs').promises;
const path = require('path');
const glob = require('glob');

async function inlineIncludes() {
    try {
        const headerPath = path.join(__dirname, '..', 'components', 'header.html');
        const footerPath = path.join(__dirname, '..', 'components', 'footer.html');

        const headerHtml = await fs.readFile(headerPath, 'utf-8');
        const footerHtml = await fs.readFile(footerPath, 'utf-8');

        const files = glob.sync('**/*.html', {
            ignore: ['node_modules/**', 'components/**'],
            cwd: path.join(__dirname, '..')
        });

        for (const file of files) {
            const filePath = path.join(__dirname, '..', file);
            let content = await fs.readFile(filePath, 'utf-8');

            const headerPlaceholder = /<div id="header-container"[^>]*>[\s\S]*?<\/div>/;
            const footerPlaceholder = /<div id="footer-container"[^>]*>[\s\S]*?<\/div>/;
            
            // Inject Header and Footer HTML
            content = content.replace(headerPlaceholder, `<div id="header-container">${headerHtml}</div>`);
            content = content.replace(footerPlaceholder, `<div id="footer-container">${footerHtml}</div>`);
            
            // Remove the script that dynamically loads the header/footer
            const scriptToRemove = /<script type="module">[\s\S]*?initSharedHeader\(.*?\);[\s\S]*?<\/script>/;
            content = content.replace(scriptToRemove, '');

            await fs.writeFile(filePath, content, 'utf-8');
            console.log(`Inlined header and footer in: ${file}`);
        }

        console.log('HTML inlining process completed successfully.');

    } catch (error) {
        console.error('Error during HTML inlining:', error);
        process.exit(1);
    }
}

inlineIncludes();
