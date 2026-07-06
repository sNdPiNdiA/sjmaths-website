const fs = require('fs');
const path = require('path');

const ROOT_DIR = path.join(__dirname, '..');
const PYQ_DIR = path.join(ROOT_DIR, 'class-12-maths', 'previous-years-questions-chapter-wise', 'chapter-wise');

function getHtmlFiles(dir, fileList = []) {
  if (!fs.existsSync(dir)) return fileList;
  const files = fs.readdirSync(dir);
  for (const file of files) {
    const filePath = path.join(dir, file);
    const stat = fs.statSync(filePath);
    if (stat.isDirectory()) {
      getHtmlFiles(filePath, fileList);
    } else if (file.endsWith('.html') && file !== 'index.html') {
      fileList.push(filePath);
    }
  }
  return fileList;
}

function formatContent(text) {
  if (text === null || text === undefined) return "";
  let content = String(text);
  return content
    .replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>')
    .replace(/\[(\d+)\s*marks?\]/gi, (match, n) => `<span class="q-marks">${n} Mark${n > 1 ? 's' : ''}</span>`)
    .replace(/\*\*OR\*\*/g, '<span class="q-or">OR</span>');
}

function renderQuestionCard(q) {
  let questionHTML = formatContent(q.question || q.case_study || "");
  if (q.parts) {
    Object.entries(q.parts).forEach(([k, v]) => {
      questionHTML += `<br><strong>(${k})</strong> ${formatContent(v)}`;
    });
  }

  let optionsHTML = "";
  if (q.options) {
    if (Array.isArray(q.options)) {
      optionsHTML = `<div class="q-options-grid" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 12px; margin-top: 16px;">` +
        q.options.map((o, i) => `<div class="q-option-item" style="display: flex; align-items: flex-start; gap: 10px; padding: 12px 16px; background: rgba(0,0,0,0.02); border: 1px solid rgba(0,0,0,0.08); border-radius: 8px;"><span style="font-weight: 600; color: var(--primary, #2c3e50);">(${String.fromCharCode(97 + i)})</span><span style="flex: 1;">${formatContent(o)}</span></div>`).join("") +
        `</div>`;
    } else {
      optionsHTML = `<div class="q-options-text" style="margin-top: 16px; padding: 12px 16px; background: rgba(0,0,0,0.02); border: 1px solid rgba(0,0,0,0.08); border-radius: 8px;">${formatContent(q.options)}</div>`;
    }
  }

  return `
        <div class="question-card" id="q_${q.id}">
            <div class="q-header">
                <div style="display:flex; align-items:center; gap:8px;">
                    <span class="q-badge">Q${q.id}</span>
                    ${q.year ? `<span class="q-year" style="font-size:0.8rem; font-weight:600; color:#666; background:#f3f4f6; padding:2px 8px; border-radius:12px;">${q.year}</span>` : ""}
                </div>
                <span class="q-timer">00:00</span>
            </div>

            <div class="question-text">
                ${questionHTML}
                ${optionsHTML}
            </div>

            ${q.diagram ? `<div class="question-diagram">${q.diagram}</div>` : ""}
            ${q.graphRef ? `<div class="graph-container" data-ref="${q.graphRef}"></div>` : ""}

            ${q.solutionSteps ? `
                <button class="solution-btn" onclick="toggleSol('sol_${q.id}', this)">Show Solution ▼</button>
                <div id="sol_${q.id}" class="solution-content">
                    ${q.solutionSteps.map(s => `<div class="step">${formatContent(s)}</div>`).join("")}
                    ${q.finalAnswer ? `<div class="final-ans"><strong>${formatContent(q.finalAnswer)}</strong></div>` : ""}
                </div>` : ""}
        </div>`;
}

const htmlFiles = getHtmlFiles(PYQ_DIR);
console.log(`Found ${htmlFiles.length} Class 12 PYQ HTML files to process.`);

let prerenderedCount = 0;

for (const filePath of htmlFiles) {
  let html = fs.readFileSync(filePath, 'utf8');

  // Fix stray double angle bracket if present
  if (html.includes('.html">>')) {
    html = html.replace(/\.html">>/g, '.html">');
  }

  // Extract QUESTIONS_JSON path
  const jsonMatch = html.match(/window\.QUESTIONS_JSON\s*=\s*["']([^"']+)["']/);
  if (!jsonMatch) continue;

  const jsonRelPath = jsonMatch[1].replace(/^\//, '');
  const jsonFullPath = path.join(ROOT_DIR, jsonRelPath);

  if (!fs.existsSync(jsonFullPath)) {
    console.log(`⚠️ JSON file missing for ${filePath}: ${jsonFullPath}`);
    continue;
  }

  const rawJson = fs.readFileSync(jsonFullPath, 'utf8');
  let data;
  try {
    data = JSON.parse(rawJson);
  } catch (e) {
    console.log(`⚠️ JSON parse error for ${jsonFullPath}: ${e.message}`);
    continue;
  }

  const questions = Array.isArray(data) ? data : (data.sections ? data.sections.flatMap(s => s.questions || []) : []);
  if (!questions.length) continue;

  const cardsHtml = questions.map(q => renderQuestionCard(q)).join('\n');

  // Replace <div id="questionContainer"></div> or <div id="questionContainer">...</div>
  if (html.includes('<div id="questionContainer">')) {
    html = html.replace(
      /<div id="questionContainer">[\s\S]*?<\/div>/i,
      `<div id="questionContainer">\n${cardsHtml}\n        </div>`
    );
    fs.writeFileSync(filePath, html, 'utf8');
    prerenderedCount++;
  }
}

console.log(`🎉 Successfully pre-rendered static HTML question cards into ${prerenderedCount} Class 12 PYQ pages.`);
