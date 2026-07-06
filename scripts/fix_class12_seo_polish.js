const fs = require('fs');
const path = require('path');

const ROOT_DIR = path.join(__dirname, '..');
const CLASS12_DIR = path.join(ROOT_DIR, 'class-12-maths');

function getHtmlFiles(dir, fileList = []) {
  const files = fs.readdirSync(dir);
  for (const file of files) {
    const filePath = path.join(dir, file);
    if (fs.statSync(filePath).isDirectory()) {
      getHtmlFiles(filePath, fileList);
    } else if (file.endsWith('.html')) {
      fileList.push(filePath);
    }
  }
  return fileList;
}

const htmlFiles = getHtmlFiles(CLASS12_DIR);

let count = 0;

for (const filePath of htmlFiles) {
  let html = fs.readFileSync(filePath, 'utf8');
  let modified = false;

  // Skip noindex / redirect files
  if (/<meta\s+name=["']robots["']\s+content=["'][^"']*noindex/i.test(html) || /http-equiv=["']refresh["']/i.test(html)) {
    continue;
  }

  // 1. Fix long titles (> 70 chars)
  const titleM = html.match(/<title[^>]*>(.*?)<\/title>/i);
  if (titleM) {
    let title = titleM[1].trim();
    if (title.length > 70) {
      let trimmed = title.replace(/\s*\|\s*SJMaths/i, '').trim();
      if (trimmed.length > 55) {
        trimmed = trimmed.substring(0, 55).trim();
      }
      trimmed = `${trimmed} | SJMaths`;
      html = html.replace(/<title[^>]*>(.*?)<\/title>/i, `<title>${trimmed}</title>`);
      modified = true;
    }
  }

  // 2. Fix long meta descriptions (> 165 chars)
  const descM = html.match(/<meta\s+name=["']description["']\s+content=["'](.*?)["']/i);
  if (descM) {
    let desc = descM[1].trim();
    if (desc.length > 165) {
      let trimmedDesc = desc.substring(0, 155).trim();
      const lastSpace = trimmedDesc.lastIndexOf(' ');
      if (lastSpace > 120) trimmedDesc = trimmedDesc.substring(0, lastSpace);
      trimmedDesc += '.';
      html = html.replace(/<meta\s+name=["']description["']\s+content=["'](.*?)["']/i, `<meta name="description" content="${trimmedDesc}">`);
      modified = true;
    }
  }

  // 3. Add AI Summary / Overview block if thin content (< 100 words in body)
  const bodyM = html.match(/<body[^>]*>([\s\S]*?)<\/body>/i);
  if (bodyM) {
    const textOnly = bodyM[1]
      .replace(/<script[\s\S]*?<\/script>/gi, '')
      .replace(/<style[\s\S]*?<\/style>/gi, '')
      .replace(/<[^>]+>/g, ' ')
      .replace(/\s+/g, ' ')
      .trim();
    const wordCount = textOnly.split(/\s+/).filter(w => w.length > 0).length;

    if (wordCount < 100 && !html.includes('class="ai-summary"')) {
      const pageTitle = (titleM ? titleM[1] : 'Class 12 Maths').replace(/\s*\|\s*SJMaths/i, '');
      const summaryBlock = `
    <!-- AI Summary Block -->
    <section class="ai-summary" style="max-width: 800px; margin: 20px auto; padding: 20px; background: #f9fafb; border-radius: 12px; border: 1px solid #e5e7eb;">
        <h2 style="font-size: 1.2rem; color: #1f2937; margin-bottom: 10px;"><i class="fas fa-list-ul"></i> Overview & Revision Guide</h2>
        <p style="color: #4b5563; line-height: 1.6;">Access comprehensive <strong>${pageTitle}</strong> on SJMaths. Practice CBSE board exam previous year questions, NCERT solutions, key formulas, step-by-step proofs, and quick revision notes designed for Class 12 Mathematics preparation.</p>
    </section>\n`;

      if (html.includes('<main>')) {
        html = html.replace('<main>', `<main>\n${summaryBlock}`);
        modified = true;
      } else if (html.includes('<body')) {
        html = html.replace(/<body[^>]*>/i, `$&${summaryBlock}`);
        modified = true;
      }
    }
  }

  if (modified) {
    fs.writeFileSync(filePath, html, 'utf8');
    count++;
  }
}

console.log(`🎉 Polished Class 12 titles, descriptions, and static summaries in ${count} files.`);
