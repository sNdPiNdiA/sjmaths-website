/**
 * Utility to check for broken links on the current page.
 * Usage: 
 * 1. Include this script in your HTML: <script src="/utils/checkBrokenLinks.js"></script>
 * 2. Open Console (F12) and run: checkBrokenLinks()
 */

async function checkBrokenLinks() {
    const links = document.querySelectorAll('a[href]');
    console.log(`%cFound ${links.length} links. Starting check...`, 'font-weight: bold; color: #8e44ad;');

    let brokenCount = 0;
    let checkedCount = 0;

    for (const link of links) {
        const url = link.href;

        // Skip non-http links (anchors, mailto, tel, javascript)
        if (!url.startsWith('http')) {
            continue;
        }

        try {
            // Use HEAD request first for efficiency
            let response = await fetch(url, { method: 'HEAD', mode: 'cors' });

            // If HEAD fails (e.g., 405 Method Not Allowed), retry with GET
            if (!response.ok && response.status === 405) {
                response = await fetch(url, { method: 'GET', mode: 'cors' });
            }

            if (!response.ok) {
                console.error(`❌ Broken Link [${response.status}]: ${url}`, link);
                brokenCount++;
            }
        } catch (error) {
            // Network errors or CORS issues (common with external links)
            console.warn(`⚠️ Network/CORS Error: ${url}`, error.message);
        }

        checkedCount++;
    }

    console.log(`%cCheck complete. Verified ${checkedCount} links.`, 'font-weight: bold;');
    if (brokenCount === 0) {
        console.log('%c✅ No broken links found!', 'color: green; font-weight: bold; font-size: 1.2em;');
    } else {
        console.log(`%c❌ Found ${brokenCount} broken links.`, 'color: red; font-weight: bold; font-size: 1.2em;');
    }
}