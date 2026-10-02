import fs from 'node:fs';
import path from 'node:path';

const GK_DIR = 'up-upper-primary-teacher/general-knowledge';
const subdirs = fs.readdirSync(GK_DIR, { withFileTypes: true }).filter(d => d.isDirectory());

let processed = 0;
let failed = 0;

for (const s of subdirs) {
  const filePath = path.join(GK_DIR, s.name, 'index.html');
  if (!fs.existsSync(filePath)) continue;

  let content = fs.readFileSync(filePath, 'utf8');
  const originalLength = content.length;

  // 1. Replace inline <style> with common CSS link
  if (content.includes('<style>')) {
    content = content.replace(/<style>[\s\S]*?<\/style>/i, '<link href="/assets/css/up-upper-primary-topic.min.css" rel="stylesheet"/>');
  } else if (!content.includes('up-upper-primary-topic.min.css') && !content.includes('up-upper-primary-topic.css')) {
    content = content.replace(
      /(<link href="\/assets\/css\/pages\.min\.css\?v=[^"]*" rel="stylesheet"\/>)/,
      '$1\n<link href="/assets/css/up-upper-primary-topic.min.css" rel="stylesheet"/>'
    );
  }

  // 2. Replace duplicated inline <script> engine with common JS runtime link
  const scriptMatch = content.match(/<script>([\s\S]*?const TOPIC_STORAGE_KEY[\s\S]*?)<\/script>/i);
  if (scriptMatch) {
    const scriptBlock = scriptMatch[1];
    const storageMatch = scriptBlock.match(/const\s+TOPIC_STORAGE_KEY\s*=\s*['"]([^'"]+)['"]/);
    const checkboxMatch = scriptBlock.match(/const\s+TOPIC_CHECKBOX_ID\s*=\s*['"]([^'"]+)['"]/);
    const testDataMatch = scriptBlock.match(/const\s+testData\s*=\s*(\[[\s\S]*?\]);/);

    const storageKey = storageMatch ? storageMatch[1] : 'up-upper-primary-teacher-checklist-v2';
    const checkboxId = checkboxMatch ? checkboxMatch[1] : '';
    const testDataJson = testDataMatch ? testDataMatch[1] : '[]';

    const newScriptBlock = `<!-- Interactive Logic -->
<script>
    window.TOPIC_STORAGE_KEY = '${storageKey}';
    window.TOPIC_CHECKBOX_ID = '${checkboxId}';
    window.testData = ${testDataJson};
</script>
<script data-cfasync="false" defer="" src="/assets/js/up-upper-primary-topic.min.js"></script>`;

    content = content.replace(/<!-- Interactive Logic -->[\s\S]*?<script>[\s\S]*?const TOPIC_STORAGE_KEY[\s\S]*?<\/script>/i, newScriptBlock);
  } else if (s.name === 'current-events-national-international') {
    // Coming soon placeholder page
    if (!content.includes('up-upper-primary-topic.min.js')) {
      content = content.replace('</body>', '<script data-cfasync="false" defer="" src="/assets/js/up-upper-primary-topic.min.js"></script>\n</body>');
    }
  }

  // 3. Remove AI-tell text & Robotic phrasing
  // Duplicate Module pill
  content = content.replace(/Module\s*(\d+)\s*:\s*Module\s*\1\s*:\s*/gi, 'Module $1: ');

  // Robotic section headers
  content = content.replace(/1\.\s*Foundational Framework &amp; Core Principles\s*\(Pointwise Breakdown\)/gi, '1. Core Concepts &amp; Foundational Principles');
  content = content.replace(/1\.\s*Foundational Framework & Core Principles\s*\(Pointwise Breakdown\)/gi, '1. Core Concepts & Foundational Principles');
  content = content.replace(/\(Pointwise Breakdown\)/gi, '');
  content = content.replace(/2\.\s*Structural Dynamics,\s*Classifications &amp; Formulae\/Rules/gi, '2. Structural Dynamics &amp; High-Yield Classifications');
  content = content.replace(/2\.\s*Structural Dynamics,\s*Classifications & Formulae\/Rules/gi, '2. Structural Dynamics & High-Yield Classifications');
  content = content.replace(/3\.\s*Uttar Pradesh Context,\s*Applied Dimensions &amp; Case Studies/gi, '3. Uttar Pradesh Regional Perspective &amp; Sites');
  content = content.replace(/3\.\s*Uttar Pradesh Context,\s*Applied Dimensions & Case Studies/gi, '3. Uttar Pradesh Regional Perspective & Sites');
  content = content.replace(/4\.\s*Comparative Matrix,\s*Edge Cases &amp; Trap Prevention/gi, '4. Comparative Analysis &amp; Exam Pitfalls');
  content = content.replace(/4\.\s*Comparative Matrix,\s*Edge Cases & Trap Prevention/gi, '4. Comparative Analysis & Exam Pitfalls');

  // Meta-prompt leaks
  content = content.replace(/\s*,?\s*and zero narrative paragraphs\.?/gi, '.');
  content = content.replace(/\s*,?\s*with zero narrative paragraphs\.?/gi, '.');
  content = content.replace(/zero narrative paragraphs/gi, '');

  // Robotic lead description opening
  content = content.replace(/This module provides exhaustive,\s*pointwise study material on/gi, 'Comprehensive syllabus study notes, key principles, and practice material on');
  content = content.replace(/This module provides exhaustive study material on/gi, 'Comprehensive syllabus study notes on');

  fs.writeFileSync(filePath, content, 'utf8');
  processed++;
  console.log(`[REFACTORED] ${s.name} (${originalLength} -> ${content.length} bytes, -${Math.round((originalLength - content.length)/1024)} KB)`);
}

console.log(`\nRefactoring Complete! Successfully refactored ${processed} files.`);
