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

const COMMON_STOP_WORDS = new Set([
  'the', 'and', 'for', 'with', 'from', 'this', 'that', 'are', 'was', 'were', 'is', 'in', 'on', 'at', 'by', 'of', 'a', 'an', 'to', 'it', 'its', 'as', 'or', 'be', 'has', 'have', 'more', 'new', 'latest'
]);

function normalizeText(text) {
  if (!text) return '';
  return text.toString().toLowerCase()
    .replace(/<[^>]*>/g, ' ')
    .replace(/[^a-z0-9\u0900-\u097F\s]/g, ' ')
    .replace(/\s+/g, ' ')
    .trim();
}

function getTokenSet(text) {
  return new Set(normalizeText(text)
    .split(' ')
    .filter(word => word && !COMMON_STOP_WORDS.has(word)));
}

function getJaccardSimilarity(str1, str2) {
  const set1 = getTokenSet(str1);
  const set2 = getTokenSet(str2);
  if (set1.size === 0 || set2.size === 0) return 0;

  const intersection = new Set([...set1].filter(x => set2.has(x)));
  const union = new Set([...set1, ...set2]);
  return intersection.size / union.size;
}

function normalizeUrl(url) {
  if (!url) return '';
  try {
    const parsed = new URL(url);
    const pathname = parsed.pathname.replace(/\/+$|\?.*$/g, '').toLowerCase();
    return `${parsed.hostname}${pathname}`.replace(/\/+$|\?.*$/g, '');
  } catch {
    return url.toLowerCase().replace(/[^a-z0-9\u0900-\u097F\/\._-]/g, ' ').replace(/\s+/g, ' ').trim();
  }
}

function areTitlesDuplicate(title1, title2) {
  if (!title1 || !title2) return false;
  const norm1 = normalizeText(title1);
  const norm2 = normalizeText(title2);
  if (norm1 === norm2) return true;
  return getJaccardSimilarity(norm1, norm2) >= 0.9;
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
  const todayStr = process.argv[2] || getTodayIST();
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
  const pastNormalizedTitles = new Set();
  for (let i = 1; i <= 7; i++) {
    const pastDateStr = getDateNDaysAgo(i);
    const pastProcessedPath = path.join(PROCESSED_DIR, `${pastDateStr}.json`);
    if (fs.existsSync(pastProcessedPath)) {
      try {
        const pastItems = JSON.parse(fs.readFileSync(pastProcessedPath, 'utf8'));
        pastItems.forEach(item => {
          if (item.hash) pastHashes.add(item.hash);
          if (item.title) pastNormalizedTitles.add(normalizeText(item.title));
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

  function computeItemScore(item) {
    const descriptionScore = (item.description || '').length;
    const imageScore = item.imageUrl ? 50 : 0;
    const priorityScore = item.priority != null ? (10 - item.priority) * 10 : 0;
    return descriptionScore + imageScore + priorityScore;
  }

  for (const item of items) {
    const normalizedTitle = normalizeText(item.title || '');
    const normalizedUrl = normalizeUrl(item.sourceUrl || '');
    item._normalizedTitle = normalizedTitle;
    item._normalizedUrl = normalizedUrl;

    // 1. Check against the last 7 days' hashes and normalized titles
    let isPastDuplicate = false;
    if (item.hash && pastHashes.has(item.hash)) {
      isPastDuplicate = true;
    }

    if (!isPastDuplicate && item.title) {
      const normalizedCurrentTitle = normalizeText(item.title);
      for (const pastTitle of pastNormalizedTitles) {
        if (normalizedCurrentTitle === pastTitle || getJaccardSimilarity(normalizedCurrentTitle, pastTitle) >= 0.9) {
          isPastDuplicate = true;
          break;
        }
      }
    }

    if (isPastDuplicate) {
      pastDupCount++;
      continue;
    }

    let duplicateMatch = null;
    for (const addedItem of dedupedItems) {
      const sameUrl = item._normalizedUrl && addedItem._normalizedUrl && item._normalizedUrl === addedItem._normalizedUrl;
      const sameTitle = item._normalizedTitle && addedItem._normalizedTitle && areTitlesDuplicate(item._normalizedTitle, addedItem._normalizedTitle);
      const fuzzyTitleMatch = item.hash && addedItem.hash && getJaccardSimilarity(item.hash, addedItem.hash) >= 0.85;

      if (sameTitle || fuzzyTitleMatch) {
        duplicateMatch = addedItem;
        break;
      }
    }

    if (duplicateMatch) {
      dayDupCount++;
      const existingScore = computeItemScore(duplicateMatch);
      const incomingScore = computeItemScore(item);
      if (incomingScore > existingScore) {
        const index = dedupedItems.indexOf(duplicateMatch);
        if (index >= 0) {
          dedupedItems[index] = item;
        }
      }
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
