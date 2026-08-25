const fs = require('fs');
const path = require('path');
const cheerio = require('cheerio');

const ROOT_DIR = __dirname.replace(/[\\/]scripts$/, '');
const APFC_DIR = path.join(ROOT_DIR, 'upsc-apfc');

function getAllHtml(dir) {
  let res = [];
  const items = fs.readdirSync(dir);
  for (const item of items) {
    const full = path.join(dir, item);
    if (fs.statSync(full).isDirectory()) {
      res = res.concat(getAllHtml(full));
    } else if (item.endsWith('.html')) {
      res.push(full);
    }
  }
  return res;
}

function toTitleCase(slug) {
  return slug
    .replace(/-/g, ' ')
    .replace(/\b\w/g, c => c.toUpperCase());
}

function main() {
  const files = getAllHtml(APFC_DIR);
  console.log('Injecting targeted meta keywords across ' + files.length + ' upsc-apfc files...');

  let updated = 0;

  files.forEach(file => {
    const content = fs.readFileSync(file, 'utf8');
    const $ = cheerio.load(content, { decodeEntities: false });
    const relPath = path.relative(ROOT_DIR, file).replace(/\\/g, '/');

    $('meta[name="keywords"]').remove();
    $('meta[name="Keywords"]').remove();

    const isHub = (relPath === 'upsc-apfc/index.html');
    const parts = relPath.replace('upsc-apfc/', '').replace('/index.html', '').split('/');
    const subjectSlug = parts[0] || '';
    const subtopicSlug = parts[1] || '';

    const subjectName = subjectSlug ? toTitleCase(subjectSlug) : 'All Subjects';
    const rawH1 = $('h1').first().text().trim();
    const topicName = rawH1 || (subtopicSlug ? toTitleCase(subtopicSlug) : 'UPSC APFC Hub');

    let keywords = [];

    if (isHub) {
      keywords = [
        'UPSC APFC',
        'UPSC APFC Syllabus',
        'UPSC APFC Study Material',
        'EPFO APFC Preparation',
        'Assistant Provident Fund Commissioner',
        'Social Security in India',
        'Labour Codes',
        'Accountancy & Auditing APFC',
        'UPSC APFC MCQs',
        'UPSC APFC PYQs',
        'SJMaths'
      ];
    } else {
      keywords = [
        topicName,
        topicName + ' UPSC APFC',
        'UPSC APFC ' + subjectName,
        topicName + ' Notes',
        topicName + ' MCQs',
        topicName + ' PYQs',
        'UPSC APFC Preparation',
        'EPFO APFC Exam',
        '2026 Rules & Central Acts',
        'SJMaths'
      ];
    }

    const kwTag = '<meta name="keywords" content="' + keywords.join(', ') + '">';

    if ($('link[rel="canonical"]').length > 0) {
      $('link[rel="canonical"]').after('\n  ' + kwTag);
    } else {
      $('head').append('\n  ' + kwTag);
    }

    fs.writeFileSync(file, $.html(), 'utf8');
    updated++;
  });

  console.log('Successfully injected meta keywords in ' + updated + ' upsc-apfc HTML files.');
}

main();
