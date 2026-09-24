const fs = require('fs');

async function checkCardsAccurately() {
  const gen = await import('./generate_gemini_study_page.mjs');
  const days = gen.parseAllDays();
  const htmlIndex = fs.readFileSync('upsc-aso/index.html', 'utf8');

  // Parse microtopics count per day from index.html
  const microCountByDay = {};
  const dayRegex = /Day\s+(\d+)\s+•\s+STUDY[\s\S]*?<ul class="syllabus-list"[^>]*>([\s\S]*?)<\/ul>/gi;
  let match;
  while ((match = dayRegex.exec(htmlIndex)) !== null) {
    const d = parseInt(match[1], 10);
    const listHtml = match[2];
    const linkMatches = listHtml.match(/class="microtopic-link"[^>]*>([^<]+)<\/a>/gi) || [];
    microCountByDay[d] = linkMatches.length;
  }

  const results = [];

  days.forEach(d => {
    if (!fs.existsSync(d.outputPath)) return;
    const html = fs.readFileSync(d.outputPath, 'utf8');

    // Count how many "1. Formal Technical Definition" or "Concept X" or "Subtopic X" or "Card X" exist in Tab 1
    // Tab 1 is roughly from switchTab(1) / tab-1 to tab-2 / switchTab(2)
    const tab1Start = html.search(/id=["']?(?:tab-1|tabContent1|tab-study)["']?/i);
    const tab2Start = html.search(/id=["']?(?:tab-2|tabContent2|tab-quiz)["']?/i);

    let tab1Html = '';
    if (tab1Start !== -1 && tab2Start !== -1 && tab2Start > tab1Start) {
      tab1Html = html.substring(tab1Start, tab2Start);
    } else {
      tab1Html = html;
    }

    const defCount = (tab1Html.match(/Formal Technical Definition/gi) || []).length;
    const cardCount = (tab1Html.match(/class=["'][^"']*(?:concept-card|step-card)[^"']*/gi) || []).length;
    const count = Math.max(defCount, cardCount);
    const expected = microCountByDay[d.day] || 0;

    results.push({ day: d.day, count, expected, topic: d.topic });
  });

  const complete = results.filter(r => r.count >= 4);
  const sparse = results.filter(r => r.count < 4);

  console.log(`Total Days: ${results.length}`);
  console.log(`Days with 4+ Full Subtopic Cards: ${complete.length}`);
  console.log(`Days with <4 Subtopic Cards: ${sparse.length}`);

  console.log('\nSparse Days (<4 cards):');
  sparse.forEach(s => console.log(`Day ${s.day} (${s.count}/${s.expected} cards): ${s.topic}`));
}

checkCardsAccurately();
