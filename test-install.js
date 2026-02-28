const puppeteer = require('puppeteer');

async function testInstallButton() {
    console.log("Starting Chrome...");
    const browser = await puppeteer.launch({
        headless: false,
        args: ['--disable-web-security']
    });
    const page = await browser.newPage();

    // Setup a listener for the beforeinstallprompt event inside the page context
    await page.evaluateOnNewDocument(() => {
        window.installPromptFired = false;
        window.addEventListener('beforeinstallprompt', (e) => {
            window.installPromptFired = true;
            console.log("beforeinstallprompt fired!");
        });
    });

    console.log("Navigating to local server...");
    await page.goto('http://127.0.0.1:8080/index.html', { waitUntil: 'networkidle0' });

    console.log("Waiting to see if Install Button appears...");
    try {
        // Trigger generic custom event to force the button to show up for testing
        await page.evaluate(() => {
            const event = new Event('beforeinstallprompt');
            // Mock the prompt and userChoice
            event.prompt = function () { console.log("Prompt called"); };
            event.userChoice = Promise.resolve({ outcome: 'accepted' });
            window.dispatchEvent(event);
        });

        await page.waitForSelector('#installAppBtn', { visible: true, timeout: 5000 });
        console.log("Install button is visible.");

        console.log("Clicking the Install button...");
        await page.click('#installAppBtn');

        await page.waitForTimeout(2000); // give it time to process

        // Check if button is now hidden (expected behavior after 'accepted' outcome)
        const isHidden = await page.evaluate(() => {
            const btn = document.getElementById('installAppBtn');
            return btn ? btn.style.display === 'none' : true;
        });

        if (isHidden) {
            console.log("SUCCESS: Button handled click and hid itself as expected.");
        } else {
            console.error("FAILURE: Button is still visible after clicking.");
        }

    } catch (e) {
        console.error("Error during test:", e);
    }

    await browser.close();
    console.log("Test finished.");
}

testInstallButton();
