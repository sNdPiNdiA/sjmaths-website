import fs from 'fs';
import path from 'path';
import https from 'https';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const ROOT_DIR = path.resolve(__dirname, '..');
const KEY = 'c4b18f8e02d849bfa4876b5d9284210e';
const HOST = 'sjmaths.com';
const BATCH_SIZE = 250;

const isDryRun = process.argv.includes('--dry-run');

// 1. Gather all URLs from sitemap files in the root directory
function getSitemapFiles() {
  return fs.readdirSync(ROOT_DIR).filter(file => file.startsWith('sitemap') && file.endsWith('.xml') && file !== 'sitemap.xml');
}

function gatherUrls() {
  const files = getSitemapFiles();
  const urlSet = new Set();

  for (const file of files) {
    const filePath = path.join(ROOT_DIR, file);
    if (fs.existsSync(filePath)) {
      const xml = fs.readFileSync(filePath, 'utf8');
      const matches = xml.match(/<loc>(https:\/\/sjmaths\.com\/.*?)<\/loc>/g);
      if (matches) {
        for (const m of matches) {
          const url = m.replace('<loc>', '').replace('</loc>', '').trim();
          urlSet.add(url);
        }
      }
    }
  }
  return Array.from(urlSet);
}

function sendBatch(batchUrls) {
  return new Promise((resolve, reject) => {
    const payload = JSON.stringify({
      host: HOST,
      key: KEY,
      keyLocation: `https://${HOST}/${KEY}.txt`,
      urlList: batchUrls
    });

    const options = {
      hostname: 'api.indexnow.org',
      path: '/indexnow',
      method: 'POST',
      headers: {
        'Content-Type': 'application/json; charset=utf-8',
        'Content-Length': Buffer.byteLength(payload)
      }
    };

    const req = https.request(options, (res) => {
      let data = '';
      res.on('data', chunk => { data += chunk; });
      res.on('end', () => {
        if (res.statusCode === 200 || res.statusCode === 202) {
          resolve({ status: res.statusCode, data });
        } else {
          resolve({ status: res.statusCode, error: data });
        }
      });
    });

    req.on('error', err => reject(err));
    req.write(payload);
    req.end();
  });
}

async function main() {
  console.log('Gathering sitemap URLs for IndexNow...');
  const allUrls = gatherUrls();
  console.log(`Found ${allUrls.length} total URLs.`);

  if (allUrls.length === 0) {
    console.warn('No URLs found to submit.');
    return;
  }

  if (isDryRun) {
    console.log(`[DRY RUN] Would submit ${allUrls.length} URLs in batches of ${BATCH_SIZE} using key ${KEY}.`);
    console.log(`Sample URLs (first 5):\n${allUrls.slice(0, 5).join('\n')}`);
    return;
  }

  // Submit in chunks of 250
  for (let i = 0; i < allUrls.length; i += BATCH_SIZE) {
    const batch = allUrls.slice(i, i + BATCH_SIZE);
    console.log(`Submitting batch ${Math.floor(i / BATCH_SIZE) + 1}/${Math.ceil(allUrls.length / BATCH_SIZE)} (${batch.length} URLs)...`);
    try {
      const res = await sendBatch(batch);
      console.log(`Batch response status: ${res.status}`);
      if (res.error) {
        console.error(`Response details: ${res.error}`);
      }
    } catch (err) {
      console.error(`Failed to submit batch: ${err.message}`);
    }
  }

  console.log('IndexNow submission completed.');
}

main().catch(err => {
  console.error('IndexNow submission error:', err);
  process.exit(1);
});

