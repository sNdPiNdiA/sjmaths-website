const fs = require('fs');
const path = require('path');
const crypto = require('crypto');
const { XMLParser } = require('fast-xml-parser');
const cheerio = require('cheerio');

// Import undici fetch if needed, but in Node 20 global fetch is available.
// Fallback to undici if global fetch is not defined.
const fetchFn = typeof fetch !== 'undefined' ? fetch : require('undici').fetch;

const CONFIG_PATH = path.join(__dirname, 'config', 'rss-sources.json');
const DATA_DIR = path.join(__dirname, '..', '..', 'current-affairs', 'data', 'raw');

// Helper to get current date in YYYY-MM-DD IST
function getTodayIST() {
  const date = new Date();
  const tzOffset = 5.5 * 60 * 60 * 1000; // IST is UTC+5.5
  const istTime = date.getTime() + date.getTimezoneOffset() * 60000 + tzOffset;
  const istDate = new Date(istTime);
  const yyyy = istDate.getFullYear();
  const mm = String(istDate.getMonth() + 1).padStart(2, '0');
  const dd = String(istDate.getDate()).padStart(2, '0');
  return `${yyyy}-${mm}-${dd}`;
}

// Helper to format date object to ISO-like IST string: YYYY-MM-DDTHH:mm:ss+05:30
function formatToIST(date) {
  const tzOffset = 5.5 * 60 * 60 * 1000;
  const istTime = date.getTime() + date.getTimezoneOffset() * 60000 + tzOffset;
  const istDate = new Date(istTime);
  const yyyy = istDate.getFullYear();
  const mm = String(istDate.getMonth() + 1).padStart(2, '0');
  const dd = String(istDate.getDate()).padStart(2, '0');
  const hh = String(istDate.getHours()).padStart(2, '0');
  const min = String(istDate.getMinutes()).padStart(2, '0');
  const ss = String(istDate.getSeconds()).padStart(2, '0');
  return `${yyyy}-${mm}-${dd}T${hh}:${min}:${ss}+05:30`;
}

// Helper to clean HTML tags and entities
function cleanHtml(text) {
  if (!text) return '';
  // If it's an object (e.g. parsed from XML with attributes), serialize or extract text
  if (typeof text === 'object') {
    text = text['#text'] || JSON.stringify(text);
  }
  return text
    .replace(/<[^>]*>/g, '')
    .replace(/&nbsp;/g, ' ')
    .replace(/&amp;/g, '&')
    .replace(/&lt;/g, '<')
    .replace(/&gt;/g, '>')
    .replace(/&quot;/g, '"')
    .replace(/&#39;/g, "'")
    .replace(/&apos;/g, "'")
    .replace(/\s+/g, ' ')
    .trim();
}

// Helper to generate a unique deterministic ID
function generateId(sourceId, title, link) {
  const uniqueString = `${sourceId}_${title}_${link || ''}`;
  const hash = crypto.createHash('sha256').update(uniqueString).digest('hex');
  return `${sourceId}-${hash.substring(0, 16)}`;
}

// Helper to extract image URL from item
function extractImage(item) {
  // Check enclosure
  if (item.enclosure && item.enclosure['@_url']) {
    return item.enclosure['@_url'];
  }
  if (item.enclosure && item.enclosure['@_type'] && item.enclosure['@_type'].startsWith('image/')) {
    return item.enclosure['@_url'];
  }
  // Check media:content or media:thumbnail
  const mediaContent = item['media:content'] || item['media:thumbnail'];
  if (mediaContent) {
    if (Array.isArray(mediaContent) && mediaContent.length > 0) {
      return mediaContent[0]['@_url'] || mediaContent[0].url;
    }
    return mediaContent['@_url'] || mediaContent.url || mediaContent['@_href'] || mediaContent.href;
  }
  // Scrape image from description if it contains an <img> tag
  if (item.description && typeof item.description === 'string') {
    const imgRegex = /<img[^>]+src=["']([^"']+)["']/i;
    const match = item.description.match(imgRegex);
    if (match && match[1]) {
      return match[1];
    }
  }
  return null;
}

// Helper to scrape a brief description from the source URL if it's empty in RSS
async function scrapeDescription(url) {
  try {
    const response = await fetchFn(url, {
      headers: {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) SJMathsCurrentAffairs/1.0'
      }
    });
    if (!response.ok) return '';
    const htmlText = await response.text();
    const $ = cheerio.load(htmlText);
    
    // Grab first 3 significant paragraphs
    const paragraphs = [];
    $('p').each((i, el) => {
      const text = $(el).text().trim().replace(/\s+/g, ' ');
      // Filter out short links/headers, function calls, style blocks
      if (text.length > 60 && !text.includes('function(') && !text.includes('var ') && !text.includes('jQuery')) {
        paragraphs.push(text);
      }
    });
    
    if (paragraphs.length === 0) {
      const bodyText = $('body').text().trim().replace(/\s+/g, ' ');
      return bodyText.substring(0, 300) + '...';
    }
    
    return paragraphs.slice(0, 3).join(' ');
  } catch (err) {
    console.error(`Failed to scrape description for ${url}:`, err.message);
    return '';
  }
}

// Fetch a single feed with timeout
async function fetchFeed(source, timeoutMs = 10000) {
  const controller = new AbortController();
  const timeoutId = setTimeout(() => controller.abort(), timeoutMs);

  try {
    console.log(`Fetching feed: ${source.name} (${source.url})`);
    const response = await fetchFn(source.url, {
      signal: controller.signal,
      headers: {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) SJMathsCurrentAffairs/1.0'
      }
    });

    clearTimeout(timeoutId);

    if (!response.ok) {
      throw new Error(`HTTP status ${response.status}`);
    }

    const xmlText = await response.text();
    return xmlText;
  } catch (err) {
    clearTimeout(timeoutId);
    console.error(`Failed to fetch ${source.name}:`, err.message);
    return null;
  }
}

// Parse feed XML to raw items
function parseFeed(xmlText, source) {
  if (!xmlText) return [];

  const parser = new XMLParser({
    ignoreAttributes: false,
    attributeNamePrefix: '@_',
    parseAttributeValue: false
  });

  try {
    const jsonObj = parser.parse(xmlText);
    let rawItems = [];

    // Detect RSS 2.0 or Atom
    if (jsonObj.rss && jsonObj.rss.channel) {
      const channel = jsonObj.rss.channel;
      let items = channel.item || [];
      if (!Array.isArray(items)) {
        items = [items];
      }
      rawItems = items;
    } else if (jsonObj.feed) {
      // Atom feed
      let entries = jsonObj.feed.entry || [];
      if (!Array.isArray(entries)) {
        entries = [entries];
      }
      // Map Atom fields to RSS-like fields for normalization
      rawItems = entries.map(entry => {
        let link = '';
        if (entry.link) {
          if (Array.isArray(entry.link)) {
            const alternate = entry.link.find(l => l['@_rel'] === 'alternate');
            link = alternate ? alternate['@_href'] : entry.link[0]['@_href'];
          } else {
            link = entry.link['@_href'] || entry.link;
          }
        }
        return {
          title: entry.title,
          link: link,
          pubDate: entry.published || entry.updated,
          description: entry.summary || entry.content,
          enclosure: entry.enclosure || null
        };
      });
    }

    const fetchTime = formatToIST(new Date());

    return rawItems.map((item, index) => {
      const title = cleanHtml(item.title);
      const link = item.link || '';
      const description = cleanHtml(item.description);
      const id = generateId(source.id, title, link);
      const pubDateParsed = item.pubDate ? new Date(item.pubDate) : new Date();
      const pubDate = formatToIST(isNaN(pubDateParsed.getTime()) ? new Date() : pubDateParsed);
      const imageUrl = extractImage(item);

      // Create a simplified hash for title deduplication: lowercase alphanumeric and Devanagari, stripped of common small words
      const cleanedTitle = title.toLowerCase()
        .replace(/[^a-z0-9\u0900-\u097F\s]/g, '')
        .split(/\s+/)
        .filter(word => word.length > 2 && !['the', 'and', 'for', 'with', 'from', 'this', 'that'].includes(word))
        .join(' ');

      return {
        id,
        title,
        source: source.name,
        sourceId: source.id,
        sourceUrl: link,
        pubDate,
        fetchDate: fetchTime,
        description,
        imageUrl,
        hash: cleanedTitle,
        priority: source.priority
      };
    });
  } catch (err) {
    console.error(`Error parsing XML for ${source.name}:`, err.message);
    return [];
  }
}

async function main() {
  if (!fs.existsSync(CONFIG_PATH)) {
    console.error('Config file not found at:', CONFIG_PATH);
    process.exit(1);
  }

  const { sources } = JSON.parse(fs.readFileSync(CONFIG_PATH, 'utf8'));
  const enabledSources = sources.filter(s => s.enabled);

  console.log(`Starting fetch for ${enabledSources.length} sources...`);
  
  let allFetchedItems = [];

  for (const source of enabledSources) {
    const xml = await fetchFeed(source);
    if (xml) {
      const items = parseFeed(xml, source);
      console.log(`Successfully parsed ${items.length} items from ${source.name}`);
      allFetchedItems.push(...items);
    }
  }

  if (allFetchedItems.length === 0) {
    console.log('No items fetched today. Exiting.');
    return;
  }

  // Create data directory if it doesn't exist
  if (!fs.existsSync(DATA_DIR)) {
    fs.mkdirSync(DATA_DIR, { recursive: true });
  }

  const todayStr = getTodayIST();
  const outPath = path.join(DATA_DIR, `${todayStr}.json`);

  // Load existing raw items if file exists (to merge and avoid overwriting)
  let existingItems = [];
  if (fs.existsSync(outPath)) {
    try {
      existingItems = JSON.parse(fs.readFileSync(outPath, 'utf8'));
      console.log(`Loaded ${existingItems.length} existing items from today's raw file.`);
    } catch (err) {
      console.error(`Error reading existing file ${outPath}, overwriting.`, err.message);
    }
  }

  // Merge items based on ID
  const itemMap = new Map();
  existingItems.forEach(item => itemMap.set(item.id, item));
  
  // Find new items that don't exist in raw file or have empty/short descriptions
  const newItems = allFetchedItems.filter(item => {
    const existing = itemMap.get(item.id);
    if (!existing) return true;
    // If existing item has a useless/short description, we want to re-scrape it
    const isUseless = !existing.description || existing.description.length < 120 || existing.description.toLowerCase() === existing.title.toLowerCase();
    return isUseless;
  });
  
  console.log(`Scraping descriptions for ${newItems.length} items with empty or short descriptions...`);
  for (const item of newItems) {
    const isUseless = !item.description || item.description.length < 120 || item.description.toLowerCase() === item.title.toLowerCase();
    if (isUseless && item.sourceUrl) {
      console.log(`Scraping description for: "${item.title}"`);
      const desc = await scrapeDescription(item.sourceUrl);
      if (desc && desc.length > item.title.length) {
        item.description = desc;
      }
      // Add a small delay to avoid hitting the server too fast
      await new Promise(resolve => setTimeout(resolve, 200));
    }
  }

  // Merge the new items to map
  allFetchedItems.forEach(item => itemMap.set(item.id, item));
  const mergedItems = Array.from(itemMap.values());

  // Sort items by priority (ascending, so 1 is high) then pubDate (descending)
  mergedItems.sort((a, b) => {
    if (a.priority !== b.priority) {
      return a.priority - b.priority;
    }
    return new Date(b.pubDate) - new Date(a.pubDate);
  });

  fs.writeFileSync(outPath, JSON.stringify(mergedItems, null, 2), 'utf8');
  console.log(`Successfully wrote ${mergedItems.length} raw items to ${outPath}`);
}

main().catch(err => {
  console.error('Fatal pipeline error:', err);
  process.exit(1);
});
