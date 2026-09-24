const fs = require('fs');

async function inspectSample() {
  const genModule = await import('./generate_gemini_study_page.mjs');
  const allDays = genModule.parseAllDays();
  
  for (const dayNum of [3, 5, 10, 35, 81, 95]) {
    const d = allDays.find(x => x.day === dayNum);
    if (!d || !fs.existsSync(d.outputPath)) continue;
    const html = fs.readFileSync(d.outputPath, 'utf8');
    
    console.log(`\n=== DAY ${dayNum}: ${d.topic} ===`);
    // Find where Tab 2 is
    const tab2Index = html.indexOf('tab-content-2') !== -1 ? html.indexOf('tab-content-2') : html.indexOf('tab-quiz');
    if (tab2Index !== -1) {
      console.log('Tab 2 excerpt:');
      console.log(html.slice(tab2Index, tab2Index + 600));
    } else {
      console.log('Tab 2 container not found with standard IDs');
    }

    // Look for quiz scripts at bottom
    const scriptIndex = html.lastIndexOf('<script>');
    if (scriptIndex !== -1) {
      console.log('Script excerpt:');
      console.log(html.slice(scriptIndex, scriptIndex + 800));
    }
  }
}

inspectSample().catch(console.error);
