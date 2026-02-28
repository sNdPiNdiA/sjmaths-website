const puppeteer = require('puppeteer');
const fs = require('fs');
const path = require('path');

async function captureScreenshots() {
    const browser = await puppeteer.launch();
    const page = await browser.newPage();

    // Set dark mode explicitly via localStorage
    await page.evaluateOnNewDocument(() => {
        localStorage.setItem('sjmaths-dark', 'on');
    });

    // Screenshot 1: Home Page (.class-card)
    await page.goto('http://127.0.0.1:8080/index.html', { waitUntil: 'networkidle2' });

    // Ensure dark mode is active (click toggle if needed, or by localStorage it's already there)

    await page.setViewport({ width: 1280, height: 800 });
    await page.evaluate(() => {
        document.body.classList.add('dark-mode');
        // Scroll down to cards
        window.scrollBy(0, 500);
    });
    await page.waitForTimeout(1000);
    await page.screenshot({ path: 'C:\\Users\\sande\\.gemini\\antigravity\\brain\\08443d21-f57e-45aa-85df-0cbb0b2f935f\\media_dark_home.png' });

    // Screenshot 2: Class 9 Dashboard (.feature-card)
    await page.goto('http://127.0.0.1:8080/classes/class-9/index.html', { waitUntil: 'networkidle2' });
    await page.evaluate(() => {
        document.body.classList.add('dark-mode');
        window.scrollBy(0, 200);
    });
    await page.waitForTimeout(1000);
    await page.screenshot({ path: 'C:\\Users\\sande\\.gemini\\antigravity\\brain\\08443d21-f57e-45aa-85df-0cbb0b2f935f\\media_dark_class9.png' });

    // Screenshot 3: Class 12 Chapter Notes (.chapter-card)
    await page.goto('http://127.0.0.1:8080/classes/class-12/chapter-wise-notes/index.html', { waitUntil: 'networkidle2' });
    await page.evaluate(() => {
        document.body.classList.add('dark-mode');
        window.scrollBy(0, 200);
    });
    await page.waitForTimeout(1000);
    await page.screenshot({ path: 'C:\\Users\\sande\\.gemini\\antigravity\\brain\\08443d21-f57e-45aa-85df-0cbb0b2f935f\\media_dark_chapters.png' });

    await browser.close();
    console.log("Screenshots captured");
}

captureScreenshots();
