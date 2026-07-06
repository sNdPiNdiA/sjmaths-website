const fs = require('fs');
const path = require('path');

const ROOT_DIR = 'C:\\Users\\sande\\Documents\\GitHub\\sjmaths-website';

const targets = [
  'upsc/ancient_history/Buddhism/3-Jewels-Buddhism/hi/index.html',
  'upsc/ancient_history/Buddhism/3-Jewels-Buddhism/index.html',
  'upsc/ancient_history/Buddhism/3-Pittakas/hi/index.html',
  'upsc/ancient_history/Buddhism/3-Pittakas/index.html',
  'upsc/ancient_history/Buddhism/4-Noble-Truths-Buddhism/hi/index.html',
  'upsc/ancient_history/Buddhism/4-Noble-Truths-Buddhism/index.html',
  'upsc/ancient_history/Buddhism/5-Principles-Buddhism/hi/index.html',
  'upsc/ancient_history/Buddhism/5-Principles-Buddhism/index.html',
  'upsc/ancient_history/Buddhism/8-fold-Path-Buddhism/hi/index.html',
  'upsc/ancient_history/Buddhism/8-fold-Path-Buddhism/index.html',
  'upsc/ancient_history/Buddhism/Birth-and-Life-of-Buddha/hi/index.html',
  'upsc/ancient_history/Buddhism/Birth-and-Life-of-Buddha/index.html',
  'upsc/ancient_history/Buddhism/Causes-for-the-Decline-Buddhism/hi/index.html',
  'upsc/ancient_history/Buddhism/Causes-for-the-Decline-Buddhism/index.html',
  'upsc/ancient_history/Buddhism/Literary-Sources-of-Buddhism/hi/index.html',
  'upsc/ancient_history/Buddhism/Literary-Sources-of-Buddhism/index.html',
  'upsc/ancient_history/Buddhism/Teachings-of-Buddha/hi/index.html',
  'upsc/ancient_history/Buddhism/Teachings-of-Buddha/index.html',
  'upsc/current_affairs/index.html',
  'upsc/ethics/index.html',
  'upsc/general_studies/index.html',
  'upsc/international_relations/index.html',
  'upsc/modern_history/Arrival-of-Europeans-in-India/Portuguese-De-Almeida/questions_data/hi/index.html',
  'upsc/modern_history/Arrival-of-Europeans-in-India/Portuguese-De-Almeida/questions_data/index.html',
  'upsc/modern_history/Arrival-of-Europeans-in-India/Portuguese-Pedro-Alvarez-Cabral/questions_data/hi/index.html',
  'upsc/modern_history/Arrival-of-Europeans-in-India/Portuguese-Pedro-Alvarez-Cabral/questions_data/index.html',
  'upsc/modern_history/Arrival-of-Europeans-in-India/Portuguese-Vasco-Da-Gama/questions_data/hi/index.html',
  'upsc/modern_history/Arrival-of-Europeans-in-India/Portuguese-Vasco-Da-Gama/index.html',
  'upsc/modern_history/Arrival-of-Europeans-in-India/Portuguese-Vasco-Da-Gama/questions_data/index.html',
  'upsc/modern_history/Arrival-of-Europeans-in-India/Responsible-Factors-for-Arrival-of-Europeans/questions_data/hi/index.html',
  'upsc/modern_history/Arrival-of-Europeans-in-India/Responsible-Factors-for-Arrival-of-Europeans/questions_data/index.html',
  'upsc/modern_history/Arrival-of-Europeans-in-India/The-Portuguese-in-India/questions_data/hi/index.html',
  'upsc/modern_history/Arrival-of-Europeans-in-India/The-Portuguese-in-India/questions_data/index.html',
  'upsc/optional/index.html',
  'upsc/social_issues/index.html'
];

let fixed = 0;

for (const relPath of targets) {
  const filePath = path.join(ROOT_DIR, relPath);
  if (!fs.existsSync(filePath)) continue;

  let html = fs.readFileSync(filePath, 'utf8');

  // Determine language, subject category, and clean title
  const isHindi = relPath.includes('/hi/');
  const dirParts = relPath.split('/');
  const subjectSlug = dirParts[1] || 'general_studies';
  const subjectName = subjectSlug.replace(/_/g, ' ').replace(/\b\w/g, c => c.toUpperCase());

  const titleM = html.match(/<title[^>]*>(.*?)<\/title>/i);
  const topicTitle = titleM ? titleM[1].replace(/\s*-\s*UPSC.*/i, '').replace(/\s*\|\s*SJMaths/i, '').trim() : 'Study Material';

  const summaryBlock = `
    <!-- AI Deep Summary & Revision Overview Block -->
    <section class="ai-summary" style="max-width: 800px; margin: 24px auto; padding: 24px 28px; background: #ffffff; border-radius: 12px; border: 1px solid #e2e8f0; box-shadow: 0 4px 12px rgba(0,0,0,0.05);">
        <h2 style="font-size: 1.3rem; font-weight: 700; color: #0f172a; margin-bottom: 14px; display: flex; align-items: center; gap: 10px;">
            <i class="fas fa-graduation-cap" style="color: #4f46e5;"></i> ${isHindi ? `परीक्षा रिवीजन गाइड और अध्ययन नोट्स: ${topicTitle}` : `Comprehensive Study Guide & Revision Overview: ${topicTitle}`}
        </h2>
        <p style="color: #334155; font-size: 0.95rem; line-height: 1.7; margin-bottom: 12px;">
            ${isHindi 
              ? `SJMaths के इस विशेष यूपीएससी सिविल सेवा परीक्षा (IAS) स्टडी पोर्टल पर आपका स्वागत है। यहाँ <strong>${topicTitle}</strong> के बारे में महत्वपूर्ण तथ्य, माइंडमैप्स, परीक्षा-केंद्रित ऐतिहासिक विवरण और रिवीजन नोट्स प्रदान किए गए हैं जो परीक्षा की दृष्टि से अत्यंत उपयोगी हैं।`
              : `Welcome to the official <strong>${topicTitle}</strong> study portal on SJMaths, specially compiled for <strong>UPSC Civil Services / IAS</strong> candidates. This page features high-yielding study facts, interactive mindmaps, core concepts, and key historical points structured to maximize your exam preparation.`}
        </p>
        <p style="color: #475569; font-size: 0.95rem; line-height: 1.7; margin-bottom: 12px;">
            <strong>${isHindi ? 'मुख्य विशेषताएं और अध्ययन मॉड्यूल:' : 'Key Features & Study Highlights:'}</strong>
        </p>
        <ul style="color: #475569; font-size: 0.92rem; line-height: 1.6; margin-left: 20px; margin-bottom: 14px;">
            <li><strong>${isHindi ? 'इंटरैक्टिव माइंडमैप्स:' : 'Interactive Mindmaps:'}</strong> ${isHindi ? 'प्रत्येक विषय का दृश्य रूप से स्पष्ट और याद रखने में आसान माइंडमैप संरचना।' : 'Visually structured conceptual hierarchies for easy memory recall.'}</li>
            <li><strong>${isHindi ? 'महत्वपूर्ण तथ्य और विश्लेषण:' : 'Key Facts & Analysis:'}</strong> ${isHindi ? 'परीक्षा में पूछे जाने वाले संभावित प्रश्नों का गहराई से विश्लेषण और बिंदुवार नोट्स।' : 'High-yielding points and core facts tailored to UPSC exam specifications.'}</li>
        </ul>
    </section>\n`;

  let modified = false;

  if (html.includes('class="ai-summary"')) {
    html = html.replace(/<section class="ai-summary"[\s\S]*?<\/section>/i, summaryBlock.trim());
    modified = true;
  } else {
    if (html.includes('<main>')) {
      html = html.replace('<main>', `<main>\n${summaryBlock}`);
      modified = true;
    } else if (html.includes('<main')) {
      html = html.replace(/<main[^>]*>/i, `$&${summaryBlock}`);
      modified = true;
    } else if (html.includes('<body')) {
      html = html.replace(/<body[^>]*>/i, `$&${summaryBlock}`);
      modified = true;
    }
  }

  if (modified) {
    fs.writeFileSync(filePath, html, 'utf8');
    fixed++;
  }
}

console.log(`🎉 Remediated ${fixed} thin UPSC pages.`);
