const fs = require('fs');
const path = require('path');
const crypto = require('crypto');
const cheerio = require('cheerio');
const { execSync } = require('child_process');

// global fetch is available in Node 20.x, fallback to undici if needed
const fetchFn = typeof fetch !== 'undefined' ? fetch : require('undici').fetch;

const DATA_DIR = path.join(__dirname, '..', '..', 'current-affairs', 'data', 'raw');

const SITE_CONFIGS = {
  'gktoday.in': {
    title: 'h1.entry-title, h1.post-title, h1',
    content: '.entry-content, .post-content, .content',
    splitHeadings: false
  },
  'insightsonindia.com': {
    title: 'h1.entry-title, h1.post-title, h1',
    content: '.entry-content, .post-content, .pf-content',
    splitHeadings: true,
    headingSelector: 'h3, h4, h2'
  },
  'drishtiias.com': {
    title: '.page-title, h1',
    content: '.content, .post-content, .article-detail',
    splitHeadings: false,
    headingSelector: 'h3, h4, h2'
  },
  'iasbaba.com': {
    title: 'h1.entry-title, h1',
    content: '.entry-content, .post-content',
    splitHeadings: true,
    headingSelector: 'h3, h4, h2, .su-box-title'
  },
  'jagranjosh.com': {
    title: 'h1',
    content: '.story-detail, .content',
    splitHeadings: false
  }
};

const TRUSTED_DOMAINS = [
  'gktoday.in',
  'insightsonindia.com',
  'iasbaba.com',
  'drishtiias.com',
  'jagranjosh.com',
  'testbook.com',
  'oliveboard.in',
  'unacademy.com',
  'byjus.com',
  'nextias.com',
  'visionias.in'
];

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

// Helper to format date object to ISO-like IST string: YYYY-MM-DDTHH:mm:ss+05:30
function formatToIST(date) {
  const formatter = new Intl.DateTimeFormat('en-IN', {
    timeZone: 'Asia/Kolkata',
    year: 'numeric',
    month: '2-digit',
    day: '2-digit',
    hour: '2-digit',
    minute: '2-digit',
    second: '2-digit',
    hour12: false
  });
  const parts = formatter.formatToParts(date);
  const yyyy = parts.find(p => p.type === 'year').value;
  const mm = parts.find(p => p.type === 'month').value;
  const dd = parts.find(p => p.type === 'day').value;
  const hh = parts.find(p => p.type === 'hour').value;
  const min = parts.find(p => p.type === 'minute').value;
  const ss = parts.find(p => p.type === 'second').value;
  return `${yyyy}-${mm}-${dd}T${hh}:${min}:${ss}+05:30`;
}

// Helper to clean HTML tags and entities
function cleanHtml(text) {
  if (!text) return '';
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

// Get domain from URL
function getDomain(urlStr) {
  try {
    const parsed = new URL(urlStr);
    return parsed.hostname.replace('www.', '');
  } catch (e) {
    return '';
  }
}

// URL validation helper to ensure we scrape actual daily articles, not landing pages or categories
function isValidArticleUrl(urlStr) {
  const domain = getDomain(urlStr);
  const path = urlStr.replace(/^https?:\/\/[^\/]+/, '');
  
  if (domain === 'gktoday.in') {
    return urlStr.length > 28 && 
           !path.includes('/category/') && 
           !path.includes('/quizbase/') && 
           !path.includes('/tag/') && 
           !path.includes('/feed/') && 
           !path.includes('/gk-') && 
           !path.includes('/current-affairs-monthly-') && 
           !path.includes('/contact-us/') && 
           !path.includes('/about-us/') && 
           !path.includes('/privacy-policy/') &&
           path !== '/current-affairs/';
  }
  
  if (domain === 'insightsonindia.com') {
    return urlStr.includes('/2026/') && 
           !urlStr.includes('/downloads/') && 
           !urlStr.includes('/quiz/') && 
           !urlStr.includes('/rtm/') && 
           !urlStr.includes('/secure/') && 
           !urlStr.includes('/magazine/');
  }
  
  if (domain === 'drishtiias.com') {
    return (urlStr.includes('/daily-updates/daily-news-analysis/') || urlStr.includes('/daily-updates/daily-news-editorials/')) &&
           !urlStr.includes('/downloads/') && 
           !urlStr.includes('/quiz/') &&
           urlStr.length > 50;
  }
  
  if (domain === 'iasbaba.com') {
    return (urlStr.includes('/2026/') || urlStr.includes('/latest/iasbabas-daily-current-affairs')) && 
           !urlStr.includes('/category/') && 
           !urlStr.includes('/tag/') && 
           !urlStr.includes('/feed/');
  }
  
  if (domain === 'jagranjosh.com') {
    return urlStr.includes('/current-affairs/') && 
           !urlStr.includes('/monthly-') && 
           urlStr.length > 40;
  }
  
  return true;
}

// Extract article's publication date using smart heuristics
function extractArticleDate(urlStr, htmlContent, $) {
  // 1. Try to extract from URL (e.g., /2026/06/09/ or /2026/06/09)
  const urlDateRegex = /\/(\d{4})\/(\d{2})\/(\d{2})/;
  const urlMatch = urlStr.match(urlDateRegex);
  if (urlMatch) {
    return `${urlMatch[1]}-${urlMatch[2]}-${urlMatch[3]}`;
  }

  // 2. Try to find date in time tags
  const timeTag = $('time').attr('datetime');
  if (timeTag) {
    const timeMatch = timeTag.match(/^(\d{4})-(\d{2})-(\d{2})/);
    if (timeMatch) return `${timeMatch[1]}-${timeMatch[2]}-${timeMatch[3]}`;
  }

  // 3. Try schema meta tags
  const ogPubDate = $('meta[property="article:published_time"]').attr('content') ||
                    $('meta[name="publish-date"]').attr('content') ||
                    $('meta[property="og:updated_time"]').attr('content');
  if (ogPubDate) {
    const pubMatch = ogPubDate.match(/^(\d{4})-(\d{2})-(\d{2})/);
    if (pubMatch) return `${pubMatch[1]}-${pubMatch[2]}-${pubMatch[3]}`;
  }

  // 3.5 Try finding date text in common date classes (especially for WordPress sites like GKToday)
  const dateClassSelectors = ['.post-date', '.entry-date', '.date', '.post-meta', '.meta-info', '.published'];
  for (const selector of dateClassSelectors) {
    const el = $(selector).first();
    if (el && el.length > 0) {
      const text = el.text().trim();
      const cleanText = text.replace(/\s+/g, ' ');
      const monthNames = ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december",
                          "jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"];
      const dateRegex = new RegExp(`(?:(\\d{1,2})\\s+)?(${monthNames.join('|')})\\s+(?:(\\d{1,2}),?\\s+)?(\\d{4})`, 'i');
      const match = cleanText.match(dateRegex);
      if (match) {
        const monthName = match[2].toLowerCase();
        let monthIdx = monthNames.indexOf(monthName);
        if (monthIdx >= 12) monthIdx -= 12; // handle short names
        const month = String(monthIdx + 1).padStart(2, '0');
        const day = String(match[1] || match[3] || '01').padStart(2, '0');
        const year = match[4];
        return `${year}-${month}-${day}`;
      }
    }
  }

  // 4. Try parsing from page headings or title (e.g. "9 June 2026")
  const titleText = $('title').text() + ' ' + $('h1').text();
  const monthNames = ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december",
                      "jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"];
  
  const dateRegex = new RegExp(`(?:(\\d{1,2})\\s+)?(${monthNames.join('|')})\\s+(?:(\\d{1,2}),?\\s+)?(\\d{4})`, 'i');
  const match = titleText.match(dateRegex);
  if (match) {
    const monthName = match[2].toLowerCase();
    let monthIdx = monthNames.indexOf(monthName);
    if (monthIdx >= 12) monthIdx -= 12; // handle short names
    const month = String(monthIdx + 1).padStart(2, '0');
    const day = String(match[1] || match[3] || '01').padStart(2, '0');
    const year = match[4];
    return `${year}-${month}-${day}`;
  }

  // Fallback to today
  return getTodayIST();
}

// Search DuckDuckGo HTML (free, no API keys required)
async function searchWeb(query) {
  console.log(`Searching DuckDuckGo for: "${query}"`);
  const url = `https://html.duckduckgo.com/html/?q=${encodeURIComponent(query)}`;
  try {
    const response = await fetchFn(url, {
      headers: {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
      }
    });
    if (!response.ok) {
      throw new Error(`HTTP status ${response.status}`);
    }
    const html = await response.text();
    const $ = cheerio.load(html);
    const results = [];

    $('.result').each((i, el) => {
      const title = $(el).find('.result__a').text().trim();
      const href = $(el).find('.result__a').attr('href');
      const snippet = $(el).find('.result__snippet').text().trim();

      if (title && href) {
        let finalUrl = href;
        if (href.includes('uddg=')) {
          const match = href.match(/uddg=([^&]+)/);
          if (match) {
            finalUrl = decodeURIComponent(match[1]);
          }
        }
        results.push({ title, url: finalUrl, snippet });
      }
    });
    return results;
  } catch (err) {
    console.error(`Search failed for "${query}":`, err.message);
    return [];
  }
}

// Scrape article and optionally split into sub-topics if it's a compilation post
async function scrapeAndParseArticle(urlStr, searchSnippet = '') {
  const domain = getDomain(urlStr);
  console.log(`Scraping article: ${urlStr} (${domain})`);
  
  try {
    const response = await fetchFn(urlStr, {
      headers: {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
      }
    });
    if (!response.ok) {
      throw new Error(`HTTP status ${response.status}`);
    }
    const html = await response.text();
    const $ = cheerio.load(html);

    const config = SITE_CONFIGS[domain] || {
      title: 'h1',
      content: 'article, .content, .entry-content, main, body',
      splitHeadings: false
    };

    const mainTitle = $(config.title).first().text().trim() || cleanHtml($('title').text());
    const contentContainer = $(config.content).first();

    const dateStr = extractArticleDate(urlStr, html, $);
    console.log(`  -> Extracted publication date: ${dateStr}`);

    if (!contentContainer || contentContainer.length === 0) {
      // Fallback: use snippet if we can't find content
      return [{
        title: mainTitle,
        description: cleanHtml(searchSnippet),
        url: urlStr,
        date: dateStr
      }];
    }

    const fetchedItems = [];

    if (config.splitHeadings && config.headingSelector) {
      // Split compilation page into sub-topics by headings
      let currentSubTitle = '';
      let currentParagraphs = [];

      contentContainer.find('*').each((i, el) => {
        const $el = $(el);
        if ($el.is(config.headingSelector)) {
          // Save previous section if it has content
          if (currentSubTitle && currentParagraphs.length > 0) {
            const desc = currentParagraphs.join(' ').replace(/\s+/g, ' ').trim();
            if (desc.length > 100) {
              fetchedItems.push({
                title: currentSubTitle,
                description: desc,
                url: urlStr,
                date: dateStr
              });
            }
          }
          currentSubTitle = cleanHtml($el.text().replace(/^\d+\.\s+/, '')); // strip numbering like "1. "
          currentParagraphs = [];
        } else if ($el.is('p')) {
          const text = $el.text().trim();
          if (text.length > 40 && !text.includes('function(') && !text.includes('cookie')) {
            currentParagraphs.push(text);
          }
        }
      });

      // Save last section
      if (currentSubTitle && currentParagraphs.length > 0) {
        const desc = currentParagraphs.join(' ').replace(/\s+/g, ' ').trim();
        if (desc.length > 100) {
          fetchedItems.push({
            title: currentSubTitle,
            description: desc,
            url: urlStr,
            date: dateStr
          });
        }
      }
    }

    // If no sub-topics were extracted or splitHeadings is false, treat the whole page as a single item
    if (fetchedItems.length === 0) {
      const paragraphs = [];
      contentContainer.find('p').each((i, el) => {
        const text = $(el).text().trim();
        if (text.length > 50 && !text.includes('function(') && !text.includes('cookie')) {
          paragraphs.push(text);
        }
      });

      let desc = paragraphs.slice(0, 4).join(' ');
      if (desc.length < 100) {
        desc = searchSnippet || desc;
      }

      fetchedItems.push({
        title: mainTitle,
        description: cleanHtml(desc),
        url: urlStr,
        date: dateStr
      });
    }

    return fetchedItems;
  } catch (err) {
    console.error(`Failed to scrape ${urlStr}:`, err.message);
    // Return fallback using snippet
    return [{
      title: cleanHtml(searchSnippet) || 'Current Affairs Update',
      description: cleanHtml(searchSnippet),
      url: urlStr,
      date: getTodayIST()
    }];
  }
}

// Fallback direct scraping of GKToday Index page
async function directScrapeGKToday() {
  console.log('Direct GKToday Index Scraping...');
  try {
    const response = await fetchFn('https://www.gktoday.in/current-affairs/', {
      headers: {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
      }
    });
    if (!response.ok) return [];
    const html = await response.text();
    const $ = cheerio.load(html);
    const links = [];

    $('a').each((i, el) => {
      const title = $(el).text().trim();
      let href = $(el).attr('href');
      if (!href) return;
      if (href.startsWith('/')) {
        href = 'https://www.gktoday.in' + href;
      }
      const domain = getDomain(href);
      if (domain !== 'gktoday.in') return;

      if (isValidArticleUrl(href) && !links.some(l => l.url === href)) {
        links.push({ title, url: href, snippet: '' });
      }
    });
    return links;
  } catch (e) {
    console.error('GKToday direct scrape failed:', e.message);
    return [];
  }
}

// Fallback direct scraping of InsightsIAS Daily Current Affairs listing
async function directScrapeInsights() {
  console.log('Direct InsightsIAS Listing Scraping...');
  try {
    const response = await fetchFn('https://www.insightsonindia.com/insights-ias-upsc-current-affairs/', {
      headers: {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
      }
    });
    if (!response.ok) return [];
    const html = await response.text();
    const $ = cheerio.load(html);
    const links = [];

    $('a').each((i, el) => {
      const title = $(el).text().trim();
      let href = $(el).attr('href');
      if (!href) return;
      if (href.startsWith('/')) {
        href = 'https://www.insightsonindia.com' + href;
      }
      const domain = getDomain(href);
      if (domain !== 'insightsonindia.com') return;

      if (isValidArticleUrl(href) && !links.some(l => l.url === href)) {
        links.push({ title, url: href, snippet: '' });
      }
    });
    return links;
  } catch (e) {
    console.error('InsightsIAS direct scrape failed:', e.message);
    return [];
  }
}

// Direct scraping of Drishti IAS Daily Updates sub-listings
async function directScrapeDrishti() {
  console.log('Direct DrishtiIAS Listing Scraping...');
  const urls = [
    'https://www.drishtiias.com/daily-updates/daily-news-analysis',
    'https://www.drishtiias.com/daily-updates/daily-news-editorials'
  ];
  const links = [];
  
  for (const url of urls) {
    try {
      const response = await fetchFn(url, {
        headers: {
          'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
      });
      if (!response.ok) continue;
      const html = await response.text();
      const $ = cheerio.load(html);

      $('a').each((i, el) => {
        const title = $(el).text().trim();
        let href = $(el).attr('href');
        if (!href) return;
        if (href.startsWith('/')) {
          href = 'https://www.drishtiias.com' + href;
        }
        const domain = getDomain(href);
        if (domain !== 'drishtiias.com') return;

        if (isValidArticleUrl(href) && !links.some(l => l.url === href)) {
          links.push({ title, url: href, snippet: '' });
        }
      });
    } catch (e) {
      console.error(`DrishtiIAS direct scrape failed for ${url}:`, e.message);
    }
  }
  return links;
}

// Fallback direct scraping of IASbaba Listing page and latest analysis redirect
async function directScrapeIASbaba() {
  console.log('Direct IASbaba Listing Scraping...');
  const urls = [
    'https://iasbaba.com/latest/iasbabas-daily-current-affairs', // latest daily analysis redirect link
    'https://iasbaba.com/category/daily-current-affairs/'
  ];
  const links = [];
  
  // Pre-populate the latest analysis redirect since it resolves directly to the daily article
  links.push({ title: 'Latest IASbaba Daily Current Affairs', url: 'https://iasbaba.com/latest/iasbabas-daily-current-affairs', snippet: '' });

  for (const url of urls) {
    if (url.includes('/latest/')) continue;

    try {
      const response = await fetchFn(url, {
        headers: {
          'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
      });
      if (!response.ok) continue;
      const html = await response.text();
      const $ = cheerio.load(html);

      $('a').each((i, el) => {
        const title = $(el).text().trim();
        let href = $(el).attr('href');
        if (!href) return;
        if (href.startsWith('/')) {
          href = 'https://iasbaba.com' + href;
        }
        const domain = getDomain(href);
        if (domain !== 'iasbaba.com') return;

        if (isValidArticleUrl(href) && !links.some(l => l.url === href)) {
          links.push({ title, url: href, snippet: '' });
        }
      });
    } catch (e) {
      console.error('IASbaba direct scrape failed:', e.message);
    }
  }
  return links;
}

// Direct scraping of Jagran Josh main current affairs listing
async function directScrapeJagranJosh() {
  console.log('Direct Jagran Josh Listing Scraping...');
  try {
    const response = await fetchFn('https://www.jagranjosh.com/current-affairs', {
      headers: {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
      }
    });
    if (!response.ok) return [];
    const html = await response.text();
    const $ = cheerio.load(html);
    const links = [];

    $('a').each((i, el) => {
      const title = $(el).text().trim();
      let href = $(el).attr('href');
      if (!href) return;
      if (href.startsWith('/')) {
        href = 'https://www.jagranjosh.com' + href;
      }
      const domain = getDomain(href);
      if (domain !== 'jagranjosh.com') return;

      if (isValidArticleUrl(href) && !links.some(l => l.url === href)) {
        links.push({ title, url: href, snippet: '' });
      }
    });
    return links;
  } catch (e) {
    console.error('Jagran Josh direct scrape failed:', e.message);
    return [];
  }
}

// Helper to verify if a date string is within the last 4 days (expanded for reliability)
function isRecentDate(dateStr) {
  try {
    const today = new Date(getTodayIST());
    const articleDate = new Date(dateStr);
    const diffTime = Math.abs(today - articleDate);
    const diffDays = Math.ceil(diffTime / (1000 * 60 * 60 * 24));
    return diffDays <= 4;
  } catch (e) {
    return true; // if error, default to processing it
  }
}

async function main() {
  console.log(`Starting Current Affairs Web Search & Portal Scraping Pipeline...`);

  // Build target queries (broader for DuckDuckGo)
  const queries = [
    `site:gktoday.in "current affairs"`,
    `site:insightsonindia.com "upsc current affairs"`,
    `site:drishtiias.com "daily updates"`,
    `"daily current affairs" "SSC CGL" 2026`,
    `"current affairs" "UPSC" 2026`
  ];

  let searchResults = [];

  for (const query of queries) {
    const results = await searchWeb(query);
    searchResults.push(...results);
    // Be polite to search engines
    await new Promise(r => setTimeout(r, 1000));
  }

  // Also include direct listing scrapes as reliable primaries
  const gkLinks = await directScrapeGKToday();
  const insightsLinks = await directScrapeInsights();
  const drishtiLinks = await directScrapeDrishti();
  const iasbabaLinks = await directScrapeIASbaba();
  const jagranLinks = await directScrapeJagranJosh();

  searchResults.push(...gkLinks, ...insightsLinks, ...drishtiLinks, ...iasbabaLinks, ...jagranLinks);

  // De-duplicate links by URL and filter by article URL validation rules
  const uniqueLinksMap = new Map();
  searchResults.forEach(res => {
    if (res.url && isValidArticleUrl(res.url)) {
      uniqueLinksMap.set(res.url, res);
    }
  });

  const linksToScrape = Array.from(uniqueLinksMap.values()).filter(res => {
    const domain = getDomain(res.url);
    return TRUSTED_DOMAINS.includes(domain);
  });

  console.log(`Total unique trusted links to inspect: ${linksToScrape.length}`);

  const fetchTime = formatToIST(new Date());
  
  // We will group fetched items by their publication date (e.g. YYYY-MM-DD)
  const itemsByDate = {};

  // Scrape and parse each link
  for (const link of linksToScrape) {
    const parsedArticles = await scrapeAndParseArticle(link.url, link.snippet);
    const domain = getDomain(link.url);
    const sourceName = domain.split('.')[0].toUpperCase();

    parsedArticles.forEach(article => {
      if (!article.title || !article.description || article.description.length < 80) return;
      if (!isRecentDate(article.date)) {
        console.log(`Skipping older article: "${article.title}" from date ${article.date}`);
        return;
      }

      const id = generateId(sourceName.toLowerCase(), article.title, article.url);
      const cleanedTitle = cleanHtml(article.title);
      const cleanedDesc = cleanHtml(article.description);
      
      const normalizedTitle = cleanedTitle.toLowerCase()
        .replace(/[^a-z0-9\u0900-\u097F\s]/g, '')
        .split(/\s+/)
        .filter(word => word.length > 2 && !['the', 'and', 'for', 'with', 'from', 'this', 'that'].includes(word))
        .join(' ');

      const itemDate = article.date; // e.g. "2026-06-09"
      
      if (!itemsByDate[itemDate]) {
        itemsByDate[itemDate] = [];
      }

      itemsByDate[itemDate].push({
        id,
        title: cleanedTitle,
        source: sourceName,
        sourceId: sourceName.toLowerCase(),
        sourceUrl: article.url,
        pubDate: `${itemDate}T12:00:00+05:30`, // Construct IST pubDate for the actual article date
        fetchDate: fetchTime,
        description: cleanedDesc,
        imageUrl: null,
        hash: normalizedTitle,
        priority: 2
      });
    });

    // delay between fetches
    await new Promise(r => setTimeout(r, 500));
  }

  // Save the fetched items into the raw JSON file for their respective date
  const processedDates = Object.keys(itemsByDate);
  console.log(`Writing raw current affairs files for ${processedDates.length} distinct dates: ${processedDates.join(', ')}`);

  if (processedDates.length === 0) {
    console.error('❌ Failed to fetch any current affairs. Exiting pipeline.');
    process.exit(1);
  }

  // Create data directory if it doesn't exist
  if (!fs.existsSync(DATA_DIR)) {
    fs.mkdirSync(DATA_DIR, { recursive: true });
  }

  for (const dateStr of processedDates) {
    const outPath = path.join(DATA_DIR, `${dateStr}.json`);
    const fetchedItems = itemsByDate[dateStr];

    // Merge with existing items if file already exists
    let existingItems = [];
    if (fs.existsSync(outPath)) {
      try {
        existingItems = JSON.parse(fs.readFileSync(outPath, 'utf8'));
      } catch (err) {
        console.error(`Error reading existing file ${outPath}:`, err.message);
      }
    }

    const itemMap = new Map();
    existingItems.forEach(item => itemMap.set(item.id, item));
    fetchedItems.forEach(item => {
      if (!itemMap.has(item.id)) {
        itemMap.set(item.id, item);
      }
    });

    const finalItems = Array.from(itemMap.values());
    finalItems.sort((a, b) => new Date(b.pubDate) - new Date(a.pubDate));

    fs.writeFileSync(outPath, JSON.stringify(finalItems, null, 2), 'utf8');
    console.log(`✅ Wrote ${finalItems.length} items to ${outPath}`);

    // Automatically trigger deduplication, categorization, tagging, and MCQ generation for this specific date
    console.log(`🚀 Triggering processing scripts for date: ${dateStr}`);
    try {
      execSync(`node scripts/current-affairs/deduplicate.js ${dateStr}`, { stdio: 'inherit' });
      execSync(`node scripts/current-affairs/categorize.js ${dateStr}`, { stdio: 'inherit' });
      execSync(`node scripts/current-affairs/exam-tag.js ${dateStr}`, { stdio: 'inherit' });
      execSync(`node scripts/current-affairs/generate-mcqs.js ${dateStr}`, { stdio: 'inherit' });
      console.log(`✅ Processing scripts successfully completed for date: ${dateStr}`);
    } catch (err) {
      console.error(`❌ Failed to run processing scripts for date ${dateStr}:`, err.message);
    }
  }

  console.log('✅ Web Search Fetch Pipeline execution completed successfully!');
}

main().catch(err => {
  console.error('Fatal Web Search Pipeline Error:', err);
  process.exit(1);
});
