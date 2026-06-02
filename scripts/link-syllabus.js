const fs = require('fs');
const path = require('path');
const cheerio = require('cheerio');

const ROOT_DIR = path.resolve(__dirname, '..');
const SYLLABUS_PATH = path.join(ROOT_DIR, 'ssc-cgl', 'syllabus', 'index.html');

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
    console.error('Syllabus index.html not found!');
    return;
  }

  let html = fs.readFileSync(SYLLABUS_PATH, 'utf8');
  const $ = cheerio.load(html);

  // Link syllabus items
  $('.subject-card').each((_, card) => {
    const titleLink = $(card).find('.subject-title a').first();
    const href = titleLink.attr('href') || '';
    
    // Extract subject slug
    const match = href.match(/\/ssc-cgl\/([^/]+)\//);
    if (!match) return;
    const subjectSlug = match[1];

    $(card).find('.syllabus-item').each((_, item) => {
      const textSpan = $(item).find('.syllabus-text');
      if (textSpan.find('a').length > 0) return; // already linked

      const topicText = textSpan.text().trim();
      if (!topicText) return;

      const slug = generateSlug(topicText);
      const targetUrl = `../${subjectSlug}/${slug}/`;

      textSpan.html(`<a href="${targetUrl}" class="syllabus-link" style="color: inherit; text-decoration: none; border-bottom: 1px dashed rgba(142, 68, 173, 0.3); transition: all 0.2s;">${topicText}</a>`);
    });
  });

  // Let's add hover style for the links in the `<style>` block if not present
  const styleTag = $('style').first();
  if (styleTag.length > 0) {
    let css = styleTag.html();
    if (!css.includes('.syllabus-link:hover')) {
      css += `
        .syllabus-link:hover {
            color: var(--primary) !important;
            border-bottom-color: var(--primary) !important;
        }
      `;
      styleTag.html(css);
    }
  }

  let updatedHtml = $.html();

  // Patch the event listener in script to prevent checkbox toggle when clicking anchor links
  updatedHtml = updatedHtml.replace(
    `if (e.target !== checkbox) {`,
    `if (e.target !== checkbox && e.target.tagName !== 'A') {`
  );

  fs.writeFileSync(SYLLABUS_PATH, updatedHtml, 'utf8');
  console.log('Successfully made syllabus topics clickable!');
}

processSyllabus();
