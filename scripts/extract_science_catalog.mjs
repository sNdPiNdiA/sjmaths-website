import fs from 'fs';
import path from 'path';

const htmlHub = fs.readFileSync(path.join(process.cwd(), 'up-upper-primary-teacher', 'science', 'index.html'), 'utf8');
const regex = /href="\/up-upper-primary-teacher\/science\/([a-zA-Z0-9\-_]+)\/?"/g;
const linkedSlugs = [];
let m;
while ((m = regex.exec(htmlHub)) !== null) {
    if (m[1] && !linkedSlugs.includes(m[1])) linkedSlugs.push(m[1]);
}

const list = linkedSlugs.map((slug, i) => {
    const fPath = path.join(process.cwd(), 'up-upper-primary-teacher', 'science', slug, 'index.html');
    const content = fs.readFileSync(fPath, 'utf8');
    
    // Extract titles
    let titleEn = '';
    let titleHi = '';
    const h1Match = content.match(/<h1>([\s\S]*?)<\/h1>/);
    if (h1Match) {
        const enM = h1Match[1].match(/class="lang-en"[^>]*>([\s\S]*?)<\/span>/);
        const hiM = h1Match[1].match(/class="lang-hi"[^>]*>([\s\S]*?)<\/span>/);
        if (enM) titleEn = enM[1].replace(/&amp;/g, '&').trim();
        if (hiM) titleHi = hiM[1].replace(/&amp;/g, '&').trim();
    }
    
    // Extract key focus / syllabus focus
    let focusEn = '';
    let focusHi = '';
    const focusMatch = content.match(/<div style="background:\s*var\(--brand-emerald-subtle\)[\s\S]*?<p[\s\S]*?>([\s\S]*?)<\/p>/);
    if (focusMatch) {
        const enM = focusMatch[1].match(/class="lang-en"[^>]*>([\s\S]*?)<\/span>/g);
        const hiM = focusMatch[1].match(/class="lang-hi"[^>]*>([\s\S]*?)<\/span>/g);
        if (enM && enM.length > 1) focusEn = enM[1].replace(/<[^>]+>/g, '').trim();
        if (hiM && hiM.length > 1) focusHi = hiM[1].replace(/<[^>]+>/g, '').trim();
    }
    
    // Extract the headings of the concept cards
    const cardHeadings = [];
    const h2Regex = /<div class="prep-card">\s*<h2>([\s\S]*?)<\/h2>/g;
    let h2M;
    while ((h2M = h2Regex.exec(content)) !== null) {
        const hText = h2M[1].replace(/<[^>]+>/g, '').trim();
        if (hText && !hText.includes('प्रश्नोत्तरी') && !hText.includes('टेस्ट')) {
            cardHeadings.push(hText);
        }
    }

    return {
        num: i + 1,
        slug,
        titleEn,
        titleHi,
        focusEn,
        focusHi,
        cardHeadings
    };
});

fs.writeFileSync(path.join(process.cwd(), 'scripts', 'science_topics_catalog.json'), JSON.stringify(list, null, 2), 'utf8');
console.log(`Extracted catalog of ${list.length} official Science topics.`);
list.forEach(t => console.log(`#${t.num}. [${t.slug}] -> ${t.titleEn} | ${t.titleHi}`));
