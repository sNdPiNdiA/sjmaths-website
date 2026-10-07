import fs from 'fs';
import path from 'path';

const file = path.resolve('upsssc-pet/history/swadeshi-civil-disobedience-gandhi/index.html');
let content = fs.readFileSync(file, 'utf8');

const cssToInsert = `
    /* Visual Roadmap & Mind Map Styles */
    .visual-roadmap-card { background: var(--up-surface, #ffffff); border: 1px solid rgba(59, 130, 246, 0.12); border-radius: var(--up-radius-xl, 20px); padding: 1.5rem; margin-bottom: 2rem; box-shadow: 0 10px 30px -5px rgba(0, 0, 0, 0.04); backdrop-filter: blur(12px); -webkit-backdrop-filter: blur(12px); transition: border-color 0.25s ease, box-shadow 0.25s ease; }
    .visual-roadmap-card:hover { border-color: rgba(59, 130, 246, 0.25); box-shadow: 0 14px 35px -5px rgba(59, 130, 246, 0.08); }
    .visual-roadmap-header { display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 0.75rem; margin-bottom: 1.1rem; }
    .visual-roadmap-title { font-family: 'Outfit', 'Inter', system-ui, sans-serif; font-size: 1.15rem; font-weight: 700; color: var(--up-primary); display: flex; align-items: center; gap: 0.6rem; margin: 0; }
    .visual-roadmap-title i { color: var(--up-accent); }
    .visual-chip { font-size: 0.78rem; font-weight: 700; padding: 0.35rem 0.85rem; border-radius: 999px; background: rgba(59, 130, 246, 0.08); color: var(--up-accent); border: 1px solid rgba(59, 130, 246, 0.18); }
    .visual-map-wrapper { display: flex; flex-direction: column; align-items: center; width: 100%; }
    .visual-map-wrapper picture { width: 100%; display: block; }
    .visual-roadmap-img { cursor: zoom-in; width: 100%; max-width: 100%; height: auto; display: block; border-radius: 14px; border: 1px solid rgba(0, 0, 0, 0.06); box-shadow: 0 4px 20px rgba(0, 0, 0, 0.04); background: #f8fafc; }
  </style>`;

if (!content.includes('visual-roadmap-card')) {
  content = content.replace(/\s*<\/style>/, cssToInsert);
}

const htmlToInsert = `</div>
<!-- Visual Concept Roadmap & Mind Map (Responsive & Bilingual) -->
<section class="visual-roadmap-card" aria-label="Visual Concept Roadmap">
  <div class="visual-roadmap-header">
    <h2 class="visual-roadmap-title">
      <i class="fas fa-diagram-project"></i>
      <span class="lang-en">Visual Concept Roadmap &amp; Mind Map</span>
      <span class="lang-hi">दृश्यक संकल्पना मानचित्र एवं माइंड मैप</span>
    </h2>
    <span class="visual-chip">
      <span class="lang-en">1905 – 1934 Timeline</span>
      <span class="lang-hi">1905 – 1934 कालक्रम</span>
    </span>
  </div>

  <!-- English Mind Map (Responsive: 9x16 on mobile, 16:9 on desktop) -->
  <div class="lang-en visual-map-wrapper">
    <a href="swadeshi-civil-disobedience-english-1600.webp" target="_blank" rel="noopener" class="visual-map-link" title="Click to view full resolution" style="display:block; width:100%; text-decoration:none;">
      <picture>
        <source media="(max-width: 768px)" srcset="swadeshi-civil-disobedience-english-9x16-1080x1920.webp" type="image/webp"/>
        <source media="(min-width: 769px)" srcset="swadeshi-civil-disobedience-english-1600.webp" type="image/webp"/>
        <img src="swadeshi-civil-disobedience-english-1600.webp" 
             alt="Swadeshi &amp; Civil Disobedience Movement Mind Map &amp; Visual Roadmap" 
             class="visual-roadmap-img" 
             loading="eager" 
             fetchpriority="high"
             width="1600" 
             height="900"/>
      </picture>
    </a>
  </div>

  <!-- Hindi Mind Map (Responsive: 9x16 on mobile, 16:9 on desktop) -->
  <div class="lang-hi visual-map-wrapper">
    <a href="swadeshi-civil-disobedience-hindi-1600.webp" target="_blank" rel="noopener" class="visual-map-link" title="पूर्ण आकार में देखने के लिए क्लिक करें" style="display:block; width:100%; text-decoration:none;">
      <picture>
        <source media="(max-width: 768px)" srcset="swadeshi-civil-disobedience-hindi-9x16-1080x1920.webp" type="image/webp"/>
        <source media="(min-width: 769px)" srcset="swadeshi-civil-disobedience-hindi-1600.webp" type="image/webp"/>
        <img src="swadeshi-civil-disobedience-hindi-1600.webp" 
             alt="स्वदेशी तथा सविनय अवज्ञा आंदोलन माइंड मैप एवं दृश्यक सारांश" 
             class="visual-roadmap-img" 
             loading="eager" 
             fetchpriority="high"
             width="1600" 
             height="900"/>
      </picture>
    </a>
  </div>
</section>
<div aria-label="Topic resources" class="study-tabs" role="tablist">`;

const marker = /<\/div>\s*<div aria-label="Topic resources" class="study-tabs" role="tablist">/;
if (marker.test(content) && !content.includes('aria-label="Visual Concept Roadmap"')) {
  content = content.replace(marker, htmlToInsert);
}

const ogPattern = /<meta content="https:\/\/sjmaths\.com\/assets\/icons\/icon-512x512\.png" property="og:image"\/>/;
content = content.replace(ogPattern, '<meta content="https://sjmaths.com/upsssc-pet/history/swadeshi-civil-disobedience-gandhi/swadeshi-civil-disobedience-english-1600.webp" property="og:image"/>');

const twPattern = /<meta content="https:\/\/sjmaths\.com\/assets\/icons\/icon-512x512\.png" name="twitter:image"\/>/;
content = content.replace(twPattern, '<meta content="https://sjmaths.com/upsssc-pet/history/swadeshi-civil-disobedience-gandhi/swadeshi-civil-disobedience-english-1600.webp" name="twitter:image"/>');

const schemaPattern = /"description": "Complete UPSSSC PET guide on Gandhian movements: Non-Cooperation, Civil Disobedience, Salt Satyagraha, Dandi March, and Round Table Conferences\.",/;
if (!content.includes('swadeshi-civil-disobedience-english-1600.webp",')) {
  content = content.replace(schemaPattern, `"description": "Complete UPSSSC PET guide on Gandhian movements: Non-Cooperation, Civil Disobedience, Salt Satyagraha, Dandi March, and Round Table Conferences.",\n      "image": "https://sjmaths.com/upsssc-pet/history/swadeshi-civil-disobedience-gandhi/swadeshi-civil-disobedience-english-1600.webp",`);
}

fs.writeFileSync(file, content, 'utf8');
console.log('✅ Successfully embedded visual-roadmap-card and updated meta tags in swadeshi index.html');
