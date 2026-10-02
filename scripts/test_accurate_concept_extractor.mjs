import fs from 'node:fs';

const origHtml = fs.readFileSync('up-upper-primary-teacher/social-studies/indus-valley-civilisation/index.html', 'utf8');

function extractConceptsAccurate(html) {
  const concepts = [];
  const startMarker = '<div class="topic-content-body">';
  const cardStartRegex = /<div class="prep-card">\s*<h2>\s*<i class="fas fa-bookmark"[^>]*><\/i>\s*<span>([^<]+)<\/span>\s*<\/h2>/g;

  let match;
  const matches = [];
  while ((match = cardStartRegex.exec(html)) !== null) {
    matches.push({
      heading: match[1].trim(),
      startIdx: match.index + match[0].length
    });
  }

  for (let i = 0; i < matches.length; i++) {
    const current = matches[i];
    // Find '<div class="topic-content-body">' after current.startIdx
    const bodyStart = html.indexOf(startMarker, current.startIdx);
    if (bodyStart === -1) continue;
    const contentStart = bodyStart + startMarker.length;

    // The concept card ends at the next prep-card or comparative table card
    let contentEnd;
    if (i < matches.length - 1) {
      // Look backwards from next match.index for </div>\s*</div>
      const nextCardStart = matches[i + 1].startIdx;
      const sub = html.slice(contentStart, matches[i + 1].startIdx - 100);
      // We can also find the last </div> before the next card
      const idxNextCard = html.lastIndexOf('<div class="prep-card">', matches[i + 1].startIdx);
      contentEnd = idxNextCard !== -1 ? idxNextCard : contentStart;
    } else {
      // Last concept card, ends before comparative table or next section
      const idxTable = html.indexOf('<i class="fas fa-table-columns"', contentStart);
      if (idxTable !== -1) {
        contentEnd = html.lastIndexOf('<div class="prep-card">', idxTable);
      } else {
        contentEnd = html.indexOf('</div>\n    </div>\n\n    <!-- ===', contentStart);
      }
    }

    let rawBody = html.slice(contentStart, contentEnd).trim();
    // rawBody ends with two closing </div> tags corresponding to topic-content-body and prep-card
    rawBody = rawBody.replace(/<\/div>\s*<\/div>\s*$/, '').trim();

    concepts.push({
      heading: current.heading,
      html_content: rawBody
    });
  }

  return concepts;
}

const concepts = extractConceptsAccurate(origHtml);
console.log('Found concepts:', concepts.length);
concepts.forEach((c, idx) => {
  console.log(`Concept ${idx + 1}: ${c.heading}`);
  console.log(`  Length: ${c.html_content.length} chars`);
  console.log(`  Contains point-grid: ${c.html_content.includes('point-grid')}`);
  console.log(`  Contains tip-box: ${c.html_content.includes('tip-box')}`);
  console.log(`  Contains mnemonic: ${c.html_content.includes('mnemonic-inline-box')}`);
  console.log(`  Ends with: ${c.html_content.slice(-40)}`);
});
