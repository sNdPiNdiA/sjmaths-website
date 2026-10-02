import fs from 'fs';
import path from 'path';

const SOCIAL_STUDIES_DIR = path.resolve('up-upper-primary-teacher/social-studies');
const entries = fs.readdirSync(SOCIAL_STUDIES_DIR);

let modifiedCount = 0;

for (const entry of entries) {
  const fullPath = path.join(SOCIAL_STUDIES_DIR, entry, 'index.html');
  if (!fs.existsSync(fullPath)) continue;

  let html = fs.readFileSync(fullPath, 'utf8');

  // Regex to match the Curriculum Analysis Card that was placed between study-tabs-strip and TAB 1
  const cardRegex = /<!--\s*Curriculum Analysis Card[\s\S]*?<\/table>[\s\S]*?<\/div>\s*<\/div>\s*(?=<!--\s*={4,}\s*TAB 1)/i;

  if (cardRegex.test(html)) {
    // Extract exam focus/scope text if present
    const focusMatch = html.match(/<td><strong>Exam Focus &amp; Scope<\/strong><\/td>\s*<td>([\s\S]*?)<\/td>/i) ||
                       html.match(/<td><strong>पाठ्यक्रम फोकस<\/strong>[\s\S]*?<\/td>\s*<td>([\s\S]*?)<\/td>/i);
    let focusText = '';
    if (focusMatch) {
      focusText = focusMatch[1].replace(/<[^>]+>/g, ' ').replace(/\s+/g, ' ').trim();
    }

    // Remove the card from above the tabs
    html = html.replace(cardRegex, '');

    // If focusText exists, ensure tab-concepts has a nice clean strategy note at top if not already present
    if (focusText && !html.includes('Syllabus Focus &amp; High-Yield Strategy')) {
      const bannerHtml = `    <!-- ==================== TAB 1: CONCEPTS & THEORY ==================== -->\n    <div class="study-tab-pane active" id="tab-concepts">\n        <div style="background: var(--brand-emerald-subtle); border-left: 4px solid var(--brand-emerald); padding: 1rem 1.25rem; border-radius: 8px; margin-bottom: 1.5rem;">\n            <p style="margin: 0; font-size: 0.95rem; color: var(--text-headline); line-height: 1.6;">\n                <i class="fas fa-compass" style="color: var(--brand-emerald); margin-right: 0.4rem;"></i>\n                <strong>Syllabus Focus &amp; High-Yield Strategy:</strong> ${focusText}\n            </p>\n        </div>`;
      html = html.replace(/<!--\s*={4,}\s*TAB 1:\s*CONCEPTS & THEORY\s*={4,}\s*-->\s*<div\s+class="study-tab-pane active"\s+id="tab-concepts">/i, bannerHtml);
    }

    fs.writeFileSync(fullPath, html, 'utf8');
    modifiedCount++;
    console.log(`Cleaned up tabs in: ${entry}/index.html`);
  }
}

console.log(`\nSuccessfully cleaned ${modifiedCount} topic pages!`);
