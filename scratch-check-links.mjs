import { chromium } from 'playwright';
import fs from 'fs';
import path from 'path';

(async () => {
    const browser = await chromium.launch({ headless: true });
    const page = await browser.newPage({ viewport: { width: 1366, height: 768 } });

    console.log('Navigating to homepage http://localhost:8082/...');
    await page.goto('http://localhost:8082/', { waitUntil: 'networkidle', timeout: 15000 });

    // Wait for dynamic header/footer loaders if any
    await page.waitForTimeout(1000);

    // Extract all links
    const links = await page.evaluate(() => {
        const anchors = Array.from(document.querySelectorAll('a[href]'));
        return anchors.map(a => {
            return {
                text: (a.innerText || a.getAttribute('aria-label') || a.title || '').trim().replace(/\s+/g, ' '),
                href: a.getAttribute('href'),
                resolvedHref: a.href,
                tag: a.outerHTML.substring(0, 150)
            };
        });
    });

    console.log(`Found ${links.length} links on homepage.`);

    const results = [];
    const checkedUrls = new Map();

    for (const item of links) {
        const { text, href, resolvedHref, tag } = item;

        // Ignore javascript:, mailto:, tel:, #anchors without path
        if (!href || href.startsWith('javascript:') || href.startsWith('mailto:') || href.startsWith('tel:') || href === '#') {
            continue;
        }

        if (checkedUrls.has(resolvedHref)) {
            results.push({
                text,
                href,
                ...checkedUrls.get(resolvedHref)
            });
            continue;
        }

        let status = null;
        let ok = false;
        let error = null;

        if (resolvedHref.startsWith('http://localhost:8082/')) {
            // Internal URL - check via fetch on local server
            try {
                const resp = await page.request.get(resolvedHref);
                status = resp.status();
                ok = resp.ok();
            } catch (err) {
                error = err.message;
            }

            // Also check filesystem mapping
            let relativePath = resolvedHref.replace('http://localhost:8082/', '');
            if (relativePath.includes('#')) relativePath = relativePath.split('#')[0];
            if (relativePath.includes('?')) relativePath = relativePath.split('?')[0];

            let filePath = path.resolve(relativePath);
            let fileExists = false;
            if (fs.existsSync(filePath)) {
                if (fs.statSync(filePath).isDirectory()) {
                    fileExists = fs.existsSync(path.join(filePath, 'index.html'));
                } else {
                    fileExists = true;
                }
            } else if (fs.existsSync(filePath + '.html')) {
                fileExists = true;
            }

            const checkResult = {
                status,
                ok: ok || fileExists,
                fileExists,
                error
            };
            checkedUrls.set(resolvedHref, checkResult);
            results.push({ text, href, resolvedHref, ...checkResult });
        } else {
            // External URL
            try {
                const resp = await page.request.head(resolvedHref, { timeout: 8000 });
                status = resp.status();
                ok = resp.ok() || status === 403 || status === 405 || status === 301 || status === 302; 
                // some sites block automated HEAD with 403/405
            } catch (err) {
                // Try GET if HEAD failed
                try {
                    const resp = await page.request.get(resolvedHref, { timeout: 8000 });
                    status = resp.status();
                    ok = resp.ok() || status === 403 || status === 301 || status === 302;
                } catch (getErr) {
                    error = getErr.message;
                }
            }

            const checkResult = {
                status,
                ok,
                error,
                isExternal: true
            };
            checkedUrls.set(resolvedHref, checkResult);
            results.push({ text, href, resolvedHref, ...checkResult });
        }
    }

    const deadLinks = results.filter(r => !r.ok || r.status === 404);
    console.log(`\n=== AUDIT FINISHED ===`);
    console.log(`Total unique links tested: ${checkedUrls.size}`);
    console.log(`Total dead / broken links: ${deadLinks.length}`);

    if (deadLinks.length > 0) {
        console.log('\n--- DEAD LINKS FOUND ---');
        console.log(JSON.stringify(deadLinks, null, 2));
    } else {
        console.log('No dead links found!');
    }

    // Save full report
    fs.writeFileSync('scratch-link-report.json', JSON.stringify({ total: links.length, unique: checkedUrls.size, dead: deadLinks, all: results }, null, 2));

    await browser.close();
})();
