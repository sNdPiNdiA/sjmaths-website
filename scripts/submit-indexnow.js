const fs = require('fs');
const path = require('path');
const https = require('https');

const ROOT_DIR = path.resolve(__dirname, '..');
const SITEMAP_FILES = ['sitemap-main.xml', 'sitemap-ncert.xml', 'sitemap-ssc.xml', 'sitemap-upsc.xml'];
const KEY = '9ba46f5de0e34c1bba48b1bf762e8790';

// 1. Gather all URLs from sitemaps
let urls = [];
for (const file of SITEMAP_FILES) {
  const filePath = path.join(ROOT_DIR, file);
  if (fs.existsSync(filePath)) {
    const xml = fs.readFileSync(filePath, 'utf8');
    const matches = xml.match(/<loc>(https:\/\/sjmaths\.com\/.*?)<\/loc>/g);
    if (matches) {
      matches.forEach(m => {
        const url = m.replace('<loc>', '').replace('</loc>', '');
        urls.push(url);
      });
    }
  }
}

console.log(`Found ${urls.length} URLs to submit to IndexNow.`);

if (urls.length === 0) {
  console.error("Error: No URLs found in sitemaps.");
  process.exit(1);
}

// 2. Prepare payload
const payload = JSON.stringify({
  host: 'sjmaths.com',
  key: KEY,
  keyLocation: `https://sjmaths.com/${KEY}.txt`,
  urlList: urls
});

// 3. Send POST request to IndexNow
const options = {
  hostname: 'api.indexnow.org',
  path: '/indexnow',
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
    'Content-Length': Buffer.byteLength(payload)
  }
};

console.log("Sending POST request to api.indexnow.org...");

const req = https.request(options, (res) => {
  console.log(`IndexNow Server Response Status Code: ${res.statusCode}`);
  let responseData = '';
  res.on('data', (chunk) => {
    responseData += chunk;
  });
  res.on('end', () => {
    if (res.statusCode === 200) {
      console.log("✅ Success! URLs submitted successfully to IndexNow.");
    } else {
      console.error(`❌ Request failed. Response: ${responseData}`);
    }
  });
});

req.on('error', (e) => {
  console.error(`❌ HTTP request error: ${e.message}`);
});

req.write(payload);
req.end();
