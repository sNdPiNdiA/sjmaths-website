const fs = require('fs');
const path = require('path');

const RAW_DIR = path.join(__dirname, '..', '..', 'current-affairs', 'data', 'raw');
const PROCESSED_DIR = path.join(__dirname, '..', '..', 'current-affairs', 'data', 'processed');

// Helper to get current date in YYYY-MM-DD IST
function getTodayIST() {
  const formatter = new Intl.DateTimeFormat('en-CA', {
    timeZone: 'Asia/Kolkata',
    year: 'numeric',
    month: '2-digit',
    day: '2-digit'
  });
  return formatter.format(new Date());
}

// Jaccard similarity of two strings based on space-separated words
function getJaccardSimilarity(str1, str2) {
  if (!str1 || !str2) return 0;
  const set1 = new Set(str1.split(' '));
  const set2 = new Set(str2.split(' '));
  if (set1.size === 0 || set2.size === 0) return 0;

  const intersection = new Set([...set1].filter(x => set2.has(x)));
  const union = new Set([...set1, ...set2]);
  return intersection.size / union.size;
}

// Get the date string for N days ago
function getDateNDaysAgo(n) {
  const pastDate = new Date(Date.now() - (n * 24 * 60 * 60 * 1000));
  const formatter = new Intl.DateTimeFormat('en-CA', {
    timeZone: 'Asia/Kolkata',
    year: 'numeric',
    month: '2-digit',
    day: '2-digit'
  });
  return formatter.format(pastDate);
}

function deduplicate() {
  const todayStr = getTodayIST();
  const todayRawPath = path.join(RAW_DIR, `${todayStr}.json`);
  const todayDedupPath = path.join(RAW_DIR, `${todayStr}-deduped.json`);

  if (!fs.existsSync(todayRawPath)) {
    console.log(`No raw items file found for today (${todayStr}). Nothing to deduplicate.`);
    if (!fs.existsSync(RAW_DIR)) {
      fs.mkdirSync(RAW_DIR, { recursive: true });
    }
    // If running in pipeline, we can just write an empty array to avoid failing subsequent scripts
    fs.writeFileSync(todayDedupPath, JSON.stringify([], null, 2), 'utf8');
    return;
  }

  let items = [];
  try {
    items = JSON.parse(fs.readFileSync(todayRawPath, 'utf8'));
  } catch (err) {
    console.error(`Error reading ${todayRawPath}:`, err.message);
    process.exit(1);
  }

  console.log(`Loaded ${items.length} raw items from today to deduplicate.`);

  // Load hashes of processed items from the last 7 days
  const pastHashes = new Set();
  console.log('Loading processed hashes from the last 7 days for cross-day deduplication...');
  
  for (let i = 1; i <= 7; i++) {
    const pastDateStr = getDateNDaysAgo(i);
    const pastProcessedPath = path.join(PROCESSED_DIR, `${pastDateStr}.json`);
    if (fs.existsSync(pastProcessedPath)) {
      try {
        const pastItems = JSON.parse(fs.readFileSync(pastProcessedPath, 'utf8'));
        pastItems.forEach(item => {
          if (item.hash) pastHashes.add(item.hash);
        });
        console.log(`Loaded processed items from ${pastDateStr} (${pastItems.length} items)`);
      } catch (err) {
        console.error(`Error reading past processed file ${pastProcessedPath}:`, err.message);
      }
    }
  }

  const dedupedItems = [];
  let dayDupCount = 0;
  let pastDupCount = 0;

  for (const item of items) {
    // 1. Check against the last 7 days' hashes (exact or high similarity)
    let isPastDuplicate = false;
    if (item.hash) {
      if (pastHashes.has(item.hash)) {
        isPastDuplicate = true;
      } else {
        // Run a fuzzy check against past hashes if Jaccard similarity is very high
        for (const pastHash of pastHashes) {
          if (getJaccardSimilarity(item.hash, pastHash) >= 0.85) {
            isPastDuplicate = true;
            break;
          }
        }
      }
    }

    if (isPastDuplicate) {
      pastDupCount++;
      continue;
    }

    // 2. Check against already added items in today's deduped list
    let isDayDuplicate = false;
    for (const addedItem of dedupedItems) {
      if (item.hash && addedItem.hash) {
        if (item.hash === addedItem.hash || getJaccardSimilarity(item.hash, addedItem.hash) >= 0.85) {
          isDayDuplicate = true;
          break;
        }
      }
    }

    if (isDayDuplicate) {
      dayDupCount++;
      continue;
    }

    dedupedItems.push(item);
  }

  fs.writeFileSync(todayDedupPath, JSON.stringify(dedupedItems, null, 2), 'utf8');
  console.log(`Deduplication complete for ${todayStr}:`);
  console.log(`  - Removed ${pastDupCount} duplicate items from past 7 days.`);
  console.log(`  - Removed ${dayDupCount} duplicate items from today's feed.`);
  console.log(`  - Kept ${dedupedItems.length} unique items.`);
  console.log(`Saved deduped items to: ${todayDedupPath}`);
}

deduplicate();
