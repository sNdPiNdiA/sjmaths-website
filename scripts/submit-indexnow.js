import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const ROOT_DIR = path.resolve(__dirname, '..');

const HOST = 'sjmaths.com';
const KEY = 'c4b18f8e02d849bfa4876b5d9284210e';
const KEY_LOCATION = `https://${HOST}/${KEY}.txt`;

// Read sitemaps to get main URLs
function getUrlsFromSitemaps() {
  const sitemapFiles = fs.readdirSync(ROOT_DIR).filter(f => f.startsWith('sitemap') && f.endsWith('.xml'));
  const urls = [];

  for (const file of sitemapFiles) {
    const content = fs.readFileSync(path.join(ROOT_DIR, file), 'utf8');
    const matches = content.match(/<loc>(https:\/\/sjmaths\.com\/[^<]+)<\/loc>/g);
    if (matches) {
      matches.forEach(m => {
        const u = m.replace(/<\/?loc>/g, '').trim();
        if (!urls.includes(u)) urls.push(u);
      });
    }
  }
  return urls;
}

async function submitIndexNow() {
  const urlList = getUrlsFromSitemaps();
  console.log(`Found ${urlList.length} unique URLs across sitemaps.`);

  // Submit in batches of 10,000 as per IndexNow API spec
  const batchSize = 10000;
  for (let i = 0; i < urlList.length; i += batchSize) {
    const batch = urlList.slice(i, i + batchSize);
    const payload = {
      host: HOST,
      key: KEY,
      keyLocation: KEY_LOCATION,
      urlList: batch
    };

    try {
      const response = await fetch('https://api.indexnow.org/indexnow', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json; charset=utf-8' },
        body: JSON.stringify(payload)
      });
      console.log(`IndexNow Submission Batch ${i / batchSize + 1}: Status ${response.status} ${response.statusText}`);
    } catch (err) {
      console.error('IndexNow Submission error:', err.message);
    }
  }
}

submitIndexNow();
