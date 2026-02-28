const puppeteer = require('puppeteer');

async function captureTestCards() {
    const browser = await puppeteer.launch();
    const page = await browser.newPage();

    // Set dark mode explicitly via localStorage
    await page.evaluateOnNewDocument(() => {
        localStorage.setItem('sjmaths-dark', 'on');
    });

    // Screenshot 1: Class 11 Test Index (.test-card)
    await page.goto('http://127.0.0.1:8080/classes/class-11/tests/index.html', { waitUntil: 'networkidle2' });

    await page.setViewport({ width: 1280, height: 800 });
    await page.evaluate(() => {
        document.body.classList.add('dark-mode');
        // Scroll down to cards
        window.scrollBy(0, 300);
        // Expand the dropdown
        const details = document.querySelector('details');
        if (details) details.open = true;
    });
    await page.waitForTimeout(1000);
    await page.screenshot({ path: 'C:\\Users\\sande\\.gemini\\antigravity\\brain\\08443d21-f57e-45aa-85df-0cbb0b2f935f\\media_dark_test_cards.png' });

    await browser.close();
    console.log("Screenshots captured");
}

captureTestCards();
