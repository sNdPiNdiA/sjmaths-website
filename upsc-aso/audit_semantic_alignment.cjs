const fs = require('fs');
const allTopics = require('./all_544_microtopics.json');

// Check topics where the day of the topic does NOT match the day of the page it links to
const dayToPageMap = {}; // find which day each page belongs to
allTopics.forEach(t => {
  // Let's see if the page is also used on the same day
});

// Let's check how many microtopics link to a page whose primary topic or day is completely different
const semanticMismatches = [];

allTopics.forEach(t => {
  const parts = t.href.split('/').filter(Boolean);
  const slug = parts[2] || '';
  const titleClean = t.title.toLowerCase().replace(/[^a-z0-9]/g, ' ');
  const slugClean = slug.replace(/[^a-z0-9]/g, ' ');
  
  // check words in title that appear in slug
  const titleWords = titleClean.split(/\s+/).filter(w => w.length > 3 && !['with', 'from', 'into', 'over', 'under', 'days', 'test', 'concept', 'concepts', 'basics', 'intro'].includes(w));
  const slugWords = slugClean.split(/\s+/).filter(w => w.length > 3);
  
  const hasWordMatch = titleWords.some(tw => slugWords.some(sw => sw.includes(tw) || tw.includes(sw)));
  
  if (!hasWordMatch) {
    semanticMismatches.push({
      id: t.id,
      day: t.day,
      title: t.title,
      href: t.href,
      slug
    });
  }
});

console.log(`Found ${semanticMismatches.length} potential semantic mismatches where title words don't match slug words:`);
console.log(JSON.stringify(semanticMismatches.slice(0, 50), null, 2));
