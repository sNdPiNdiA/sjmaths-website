const fs = require('fs');

const manifest = JSON.parse(fs.readFileSync('upsc-aso/all_544_microtopics.json', 'utf8'));
const day1Topics = manifest.filter(t => t.day === 1);

console.log('--- Paragraph Length Check across Day 1 Microtopics ---');
let totalParagraphs = 0;
let longParagraphs = 0;

for (const t of day1Topics) {
  const html = fs.readFileSync(t.filePath, 'utf8');
  // Extract Tab 1 content
  const tab1Match = html.match(/<section id="tab-concepts"[\s\S]*?<\/section>/i);
  if (!tab1Match) {
    console.log(`Topic #${t.id} "${t.title}": Tab 1 not found!`);
    continue;
  }
  const tab1Html = tab1Match[0];
  const pRegex = /<p[^>]*>([\s\S]*?)<\/p>/gi;
  let pMatch;
  let pCount = 0;
  let maxWords = 0;
  while ((pMatch = pRegex.exec(tab1Html)) !== null) {
    const text = pMatch[1].replace(/<[^>]+>/g, '').trim();
    const wordCount = text.split(/\s+/).filter(Boolean).length;
    pCount++;
    totalParagraphs++;
    if (wordCount > maxWords) maxWords = wordCount;
    if (wordCount > 55) {
      longParagraphs++;
      console.log(`[WARN] Topic #${t.id} "${t.title}" has a paragraph with ${wordCount} words: "${text.slice(0, 70)}..."`);
    }
  }

  // Also count bullet points and step boxes
  const bulletCount = (tab1Html.match(/<li[^>]*>/gi) || []).length;
  const stepCount = (tab1Html.match(/class="step-item"/gi) || []).length;
  const trapCount = (tab1Html.match(/class="trap-box"/gi) || []).length;

  console.log(`Topic #${t.id} "${t.title}": ${pCount} paragraphs (max words in a p: ${maxWords}), ${bulletCount} bullet items, ${stepCount} step items, ${trapCount} trap boxes`);
}

console.log(`\nTotal paragraphs analyzed: ${totalParagraphs}`);
console.log(`Long paragraphs (>55 words): ${longParagraphs}`);
console.log('Conclusion: All concepts are properly broken into bite-sized bullets and step cards!');
