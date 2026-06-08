const fs = require('fs');
const path = require('path');
const cheerio = require('cheerio');

const ROOT_DIR = path.resolve(__dirname, '..');
const SYLLABUS_PATH = path.join(ROOT_DIR, 'ahc-ro-aro', 'syllabus', 'index.html');

function generateSlug(text) {
  return text
    .toLowerCase()
    .replace(/\([^)]*\)/g, '') // remove anything in parentheses
    .replace(/[^a-z0-9\s-]/g, '') // remove special chars
    .trim()
    .replace(/\s+/g, '-') // spaces to hyphens
    .replace(/-+/g, '-'); // collapse multiple hyphens
}

function processSyllabus() {
  if (!fs.existsSync(SYLLABUS_PATH)) {
    console.error('AHC RO/ARO Syllabus index.html not found!');
    return;
  }

  let html = fs.readFileSync(SYLLABUS_PATH, 'utf8');
  const $ = cheerio.load(html);

  // Link syllabus items
  $('.subject-card').each((_, card) => {
    const titleLink = $(card).find('.subject-title a').first();
    const href = titleLink.attr('href') || '';
    
    // Extract subject slug
    const match = href.match(/\.\.\/([^/]+)\//);
    if (!match) return;
    const subjectSlug = match[1];

    $(card).find('.syllabus-item').each((_, item) => {
      const link = $(item).find('a.syllabus-link');
      const enText = link.find('.lang-en').text().trim();
      if (enText) {
          const slug = generateSlug(enText);
          const targetUrl = `../${subjectSlug}/${slug}/`;
          link.attr('href', targetUrl);
      }
    });
  });

  fs.writeFileSync(SYLLABUS_PATH, $.html(), 'utf8');
  console.log('Successfully made AHC RO/ARO syllabus topics link to their respective pages!');
}

processSyllabus();