const fs = require('fs');
const html = fs.readFileSync('up-tgt-social-science/index.html', 'utf8');

const secRegex = /<article class="section-card" id="(civics-\d+-[^"]+)" data-subject="D"[\s\S]*?<\/article>/g;
let m;
while ((m = secRegex.exec(html)) !== null) {
  const secContent = m[0];
  const secId = m[1];
  const titleMatch = secContent.match(/<span class="section-title">([^<]+)<\/span>/);
  const topics = [...secContent.matchAll(/data-key="([^"]+)"/g)].map(x => x[1]);
  console.log(`${secId} (${titleMatch ? titleMatch[1] : ''}): ${topics.length} topics`);
  topics.forEach(t => console.log(`   - ${t}`));
}
