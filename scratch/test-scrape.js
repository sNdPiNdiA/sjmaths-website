const cheerio = require('cheerio');
const { fetch } = require('undici');

async function test() {
  const url = 'https://pib.gov.in/PressReleaseIframePage.aspx?PRID=2267611';
  console.log('Fetching', url);
  try {
    const response = await fetch(url, {
      headers: {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) SJMathsCurrentAffairs/1.0'
      }
    });
    console.log('Status:', response.status);
    const htmlText = await response.text();
    const $ = cheerio.load(htmlText);
    
    // Grab first 3 significant paragraphs
    const paragraphs = [];
    $('p').each((i, el) => {
      const text = $(el).text().trim().replace(/\s+/g, ' ');
      console.log(`P ${i}:`, text.substring(0, 100));
      if (text.length > 60 && !text.includes('function(') && !text.includes('var ') && !text.includes('jQuery')) {
        paragraphs.push(text);
      }
    });
    
    console.log('Total paragraph matches:', paragraphs.length);
    console.log('Scraped result:', paragraphs.slice(0, 3).join(' '));
  } catch (err) {
    console.error('Error:', err);
  }
}

test();
