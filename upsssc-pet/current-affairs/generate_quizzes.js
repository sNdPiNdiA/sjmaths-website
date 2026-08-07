import fs from 'fs';
import path from 'path';
import readline from 'readline';

const baseDir = 'c:\\Users\\sande\\Documents\\GitHub\\sjmaths-website\\upsssc-pet\\current-affairs';
const folders = [
  "appointments-and-persons",
  "awards-and-honors",
  "economic-updates",
  "government-schemes",
  "international-events",
  "national-events",
  "sports-and-games",
  "summits-and-conferences"
];

// Helper to load .env manually
function loadEnv() {
  const envPath = 'c:\\Users\\sande\\Documents\\GitHub\\sjmaths-website\\.env';
  if (fs.existsSync(envPath)) {
    const envLines = fs.readFileSync(envPath, 'utf8').split('\n');
    for (const line of envLines) {
      const match = line.match(/^\s*(GEMINI_API_KEY|GOOGLE_API_KEY)\s*=\s*(.*)\s*$/);
      if (match) {
        process.env[match[1]] = match[2].trim().replace(/^['"]|['"]$/g, '');
      }
    }
  }
}

loadEnv();

const apiKey = process.env.GEMINI_API_KEY || process.env.GOOGLE_API_KEY || "";

if (!apiKey) {
  console.error("ERROR: Please set the GEMINI_API_KEY environment variable.");
  process.exit(1);
}

const sleep = (ms) => new Promise(resolve => setTimeout(resolve, ms));

// Function to call Gemini API
async function generateQuizData(contentSnippet, categoryName, monthName) {
  const url = `https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash-lite:generateContent?key=${apiKey}`;
  
  const prompt = `You are a professional exam developer for the UPSSSC PET competitive exam.
Based on the following current affairs notes for the category "${categoryName}" in "${monthName}", generate exactly 30 high-quality practice questions.
Ensure the questions are diverse (about 20 MCQs and 10 True/False type questions).
Every question, option, correct answer, and explanation MUST be bilingual (English & Hindi).

Format the output strictly as a JSON array of objects, with NO markdown formatting (no \`\`\`json block, just raw JSON).
Each object in the array must follow this schema:
{
  "type": "mcq" or "tf",
  "question_en": "Question text in English",
  "question_hi": "हिंदी में प्रश्न",
  "options": [ // Only for MCQ type, provide exactly 4 options
    { "key": "A", "en": "Option A in English", "hi": "हिंदी में विकल्प A" },
    { "key": "B", "en": "Option B in English", "hi": "हिंदी में विकल्प B" },
    { "key": "C", "en": "Option C in English", "hi": "हिंदी में विकल्प C" },
    { "key": "D", "en": "Option D in English", "hi": "हिंदी में विकल्प D" }
  ],
  "correct_option": "A", // For MCQ, specify the correct option key (A, B, C, or D). For TF, specify "A" or "B" where A is True and B is False.
  "explanation_en": "Short explanation in English highlighting the correct fact",
  "explanation_hi": "हिंदी में संक्षिप्त व्याख्या सही तथ्य को स्पष्ट करते हुए"
}

Here is the current affairs content:
${contentSnippet}
`;

  for (let attempt = 1; attempt <= 4; attempt++) {
    try {
      const response = await fetch(url, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          contents: [{ parts: [{ text: prompt }] }],
          generationConfig: {
            responseMimeType: "application/json"
          }
        })
      });
      
      if (response.status === 429) {
        console.warn(`Rate limit hit (429) for ${categoryName} - ${monthName}. Waiting 60 seconds before retry (attempt ${attempt}/4)...`);
        await sleep(60000);
        continue;
      }
      
      if (!response.ok) {
        const errorText = await response.text();
        throw new Error(`Gemini API error: ${response.status} - ${errorText}`);
      }
      
      const resJson = await response.json();
      const rawText = resJson.candidates[0].content.parts[0].text;
      return JSON.parse(rawText.trim());
    } catch (err) {
      console.error(`Failed to generate quiz for ${categoryName} - ${monthName} (attempt ${attempt}/4):`, err.message);
      if (attempt < 4) {
        await sleep(5000);
      }
    }
  }
  return null;
}

// Generate the script and CSS styles for the quiz UI
const quizUiCss = `
    /* NotebookLLM Quiz Style CSS */
    .month-sub-nav {
      display: flex;
      gap: 0.5rem;
      margin-bottom: 1.25rem;
      border-bottom: 1px solid var(--glass-border);
      padding-bottom: 0.5rem;
    }
    .sub-tab-btn {
      background: transparent;
      border: 1px solid transparent;
      color: #64748b;
      padding: 0.4rem 0.8rem;
      border-radius: 6px;
      font-size: 0.85rem;
      font-weight: 600;
      cursor: pointer;
      transition: all 0.2s;
    }
    .sub-tab-btn:hover {
      color: var(--up-accent-purple);
      background: rgba(41, 128, 185, 0.05);
    }
    .sub-tab-btn.active {
      background: rgba(41, 128, 185, 0.1);
      color: var(--up-accent-purple);
      border-color: rgba(41, 128, 185, 0.2);
    }
    .sub-tab-panel {
      display: none;
    }
    .sub-tab-panel.active {
      display: block;
    }
    .quiz-container {
      background: #ffffff;
      border: 1px solid var(--glass-border);
      border-radius: var(--up-radius-lg);
      padding: 2rem;
      box-shadow: 0 10px 30px rgba(0,0,0,0.02);
      margin-bottom: 2rem;
      max-width: 750px;
      margin-left: auto;
      margin-right: auto;
      transition: background-color 0.3s;
    }
    body.dark-mode .quiz-container {
      background: #1e293b;
      border-color: rgba(255, 255, 255, 0.1);
    }
    .quiz-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 1rem;
      font-weight: 700;
      font-size: 0.95rem;
      color: var(--up-primary);
    }
    .quiz-progress-bar {
      width: 100%;
      height: 6px;
      background: #f1f5f9;
      border-radius: 999px;
      overflow: hidden;
      margin-bottom: 1.5rem;
    }
    body.dark-mode .quiz-progress-bar {
      background: #334155;
    }
    .quiz-progress-fill {
      height: 100%;
      background: var(--up-accent-purple);
      width: 0%;
      transition: width 0.3s ease;
    }
    .quiz-question-card {
      margin-bottom: 1.5rem;
    }
    .quiz-question-text {
      font-size: 1.15rem;
      font-weight: 700;
      line-height: 1.5;
      margin-bottom: 1rem;
    }
    .quiz-options-list {
      display: flex;
      flex-direction: column;
      gap: 0.75rem;
    }
    .quiz-option-btn {
      display: flex;
      align-items: center;
      width: 100%;
      text-align: left;
      padding: 1rem;
      border: 1px solid var(--glass-border);
      border-radius: var(--up-radius-lg);
      background: #f8fafc;
      cursor: pointer;
      transition: all 0.25s;
      font-family: inherit;
      font-size: 0.98rem;
    }
    body.dark-mode .quiz-option-btn {
      background: #0f172a;
      border-color: rgba(255, 255, 255, 0.1);
    }
    .quiz-option-btn:hover:not(:disabled) {
      border-color: var(--up-accent-purple);
      background: rgba(41, 128, 185, 0.03);
    }
    body.dark-mode .quiz-option-btn:hover:not(:disabled) {
      background: rgba(255, 255, 255, 0.02);
    }
    .option-marker {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      width: 32px;
      height: 32px;
      border-radius: 8px;
      background: rgba(100, 116, 139, 0.1);
      color: #64748b;
      font-weight: 700;
      margin-right: 1rem;
      flex-shrink: 0;
    }
    .quiz-option-btn.correct {
      border-color: #10b981 !important;
      background: rgba(16, 185, 129, 0.05) !important;
    }
    .quiz-option-btn.correct .option-marker {
      background: #10b981 !important;
      color: #ffffff !important;
    }
    .quiz-option-btn.wrong {
      border-color: #ef4444 !important;
      background: rgba(239, 68, 68, 0.05) !important;
    }
    .quiz-option-btn.wrong .option-marker {
      background: #ef4444 !important;
      color: #ffffff !important;
    }
    .quiz-explanation-box {
      margin-top: 1.5rem;
      padding: 1.25rem;
      border-radius: 12px;
      background: rgba(41, 128, 185, 0.03);
      border-left: 4px solid var(--up-accent-purple);
      animation: upFadeIn 0.3s ease-out;
    }
    body.dark-mode .quiz-explanation-box {
      background: rgba(255, 255, 255, 0.02);
    }
    .explanation-title {
      font-weight: 700;
      font-size: 0.9rem;
      color: var(--up-accent-purple);
      margin-bottom: 0.35rem;
    }
    .quiz-navigation {
      display: flex;
      justify-content: space-between;
      margin-top: 1.5rem;
      border-top: 1px solid var(--glass-border);
      padding-top: 1.25rem;
    }
    .quiz-nav-btn {
      padding: 0.6rem 1.2rem;
      border-radius: 8px;
      font-weight: 600;
      font-size: 0.9rem;
      cursor: pointer;
      transition: all 0.2s;
      border: 1px solid var(--glass-border);
      background: #ffffff;
      color: var(--up-primary);
    }
    body.dark-mode .quiz-nav-btn {
      background: #0f172a;
      border-color: rgba(255, 255, 255, 0.1);
      color: #f8fafc;
    }
    .quiz-nav-btn:hover:not(:disabled) {
      background: #f1f5f9;
    }
    body.dark-mode .quiz-nav-btn:hover:not(:disabled) {
      background: #1e293b;
    }
    .quiz-nav-btn:disabled {
      opacity: 0.5;
      cursor: not-allowed;
    }
`;

const quizControllerJs = `
  <script>
    document.addEventListener('DOMContentLoaded', () => {
      // Set up sub-tab navigation inside month panels
      const months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul'];
      months.forEach(month => {
        const panel = document.getElementById(month);
        if (!panel) return;
        
        const subNav = panel.querySelector('.month-sub-nav');
        if (!subNav) return;
        
        const subTabButtons = subNav.querySelectorAll('.sub-tab-btn');
        const subTabPanels = panel.querySelectorAll('.sub-tab-panel');
        
        subTabButtons.forEach(button => {
          button.addEventListener('click', () => {
            subTabButtons.forEach(btn => btn.classList.remove('active'));
            button.classList.add('active');
            
            const targetId = button.getAttribute('data-subtab');
            subTabPanels.forEach(p => p.classList.remove('active'));
            const targetPanel = panel.querySelector('#' + targetId);
            if (targetPanel) {
              targetPanel.classList.add('active');
              if (targetId.endsWith('-quiz')) {
                initQuiz(month);
              }
            }
          });
        });
      });

      // Quiz controller state
      const quizStates = {};

      function initQuiz(month) {
        if (quizStates[month]) return; // Already initialized
        
        const questions = window.quizData ? window.quizData[month] : [];
        if (!questions || questions.length === 0) return;
        
        quizStates[month] = {
          currentIndex: 0,
          score: 0,
          answers: new Array(questions.length).fill(null),
          questions: questions
        };
        
        renderQuestion(month);
      }

      function renderQuestion(month) {
        const state = quizStates[month];
        const q = state.questions[state.currentIndex];
        const panel = document.getElementById(month);
        const quizPanel = panel.querySelector('#' + month + '-quiz');
        
        // Update header and progress
        quizPanel.querySelector('.quiz-progress').textContent = \`Question \${state.currentIndex + 1} of \${state.questions.length}\`;
        quizPanel.querySelector('.quiz-score').textContent = \`Score: \${state.score}/\${state.answers.filter(a => a !== null).length}\`;
        quizPanel.querySelector('.quiz-progress-fill').style.width = \`\${((state.currentIndex + 1) / state.questions.length) * 100}%\`;
        
        // Set question text
        quizPanel.querySelector('.quiz-question-text.en-text').innerHTML = q.question_en;
        quizPanel.querySelector('.quiz-question-text.hi-text').innerHTML = q.question_hi;
        
        // Render options list
        const optionsList = quizPanel.querySelector('.quiz-options-list');
        optionsList.innerHTML = '';
        
        const options = q.type === 'tf' 
          ? [{ key: 'A', en: 'True', hi: 'सत्य' }, { key: 'B', en: 'False', hi: 'असत्य' }]
          : q.options;
          
        options.forEach(opt => {
          const btn = document.createElement('button');
          btn.className = 'quiz-option-btn';
          btn.innerHTML = \`<span class="option-marker">\${opt.key}</span>
            <div>
              <span class="en-text">\${opt.en}</span>
              <span class="hi-text">\${opt.hi}</span>
            </div>\`;
            
          // If already answered this question
          const previousAnswer = state.answers[state.currentIndex];
          if (previousAnswer !== null) {
            btn.disabled = true;
            if (opt.key === q.correct_option) {
              btn.classList.add('correct');
            } else if (opt.key === previousAnswer) {
              btn.classList.add('wrong');
            }
          } else {
            btn.addEventListener('click', () => selectOption(month, opt.key));
          }
          optionsList.appendChild(btn);
        });
        
        // Render explanation box
        const expBox = quizPanel.querySelector('.quiz-explanation-box');
        if (state.answers[state.currentIndex] !== null) {
          expBox.style.display = 'block';
          expBox.querySelector('.explanation-text.en-text').textContent = q.explanation_en;
          expBox.querySelector('.explanation-text.hi-text').textContent = q.explanation_hi;
        } else {
          expBox.style.display = 'none';
        }
        
        // Navigation buttons state
        quizPanel.querySelector('.prev-btn').disabled = state.currentIndex === 0;
        quizPanel.querySelector('.next-btn').disabled = state.currentIndex === state.questions.length - 1;
      }

      function selectOption(month, key) {
        const state = quizStates[month];
        const q = state.questions[state.currentIndex];
        
        state.answers[state.currentIndex] = key;
        const isCorrect = key === q.correct_option;
        if (isCorrect) {
          state.score++;
        }
        
        renderQuestion(month);
      }

      // Handle navigation clicks
      document.addEventListener('click', (e) => {
        const prevBtn = e.target.closest('.prev-btn');
        const nextBtn = e.target.closest('.next-btn');
        
        if (prevBtn) {
          const panel = prevBtn.closest('.tab-panel');
          const month = panel.id;
          const state = quizStates[month];
          if (state && state.currentIndex > 0) {
            state.currentIndex--;
            renderQuestion(month);
          }
        }
        
        if (nextBtn) {
          const panel = nextBtn.closest('.tab-panel');
          const month = panel.id;
          const state = quizStates[month];
          if (state && state.currentIndex < state.questions.length - 1) {
            state.currentIndex++;
            renderQuestion(month);
          }
        }
      });
    });
  </script>
`;

// Helper to extract clean text context from month tabs
function extractTextForMonth(htmlContent, monthId) {
  const months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'revision'];
  const startIndex = htmlContent.search(new RegExp(`id="${monthId}"`, 'i'));
  if (startIndex === -1) return "";
  
  let endIndex = htmlContent.length;
  const currentMonthIndex = months.indexOf(monthId);
  for (let i = currentMonthIndex + 1; i < months.length; i++) {
    const nextMonthId = months[i];
    const idx = htmlContent.search(new RegExp(`id="${nextMonthId}"`, 'i'));
    if (idx !== -1 && idx > startIndex) {
      endIndex = idx;
      break;
    }
  }
  
  const rawChunk = htmlContent.substring(startIndex, endIndex);
  return rawChunk.replace(/<[^>]*>/g, ' ').replace(/\s+/g, ' ').trim().substring(0, 5000);
}

// Main execution block
async function run() {
  for (const folder of folders) {
    const filePath = path.join(baseDir, folder, 'index.html');
    if (!fs.existsSync(filePath)) continue;

    console.log(`\n======================================`);
    console.log(`Processing folder: ${folder}`);
    console.log(`======================================`);

    let content = fs.readFileSync(filePath, 'utf8');

    // Append CSS to style tag
    if (!content.includes('.month-sub-nav')) {
      content = content.replace('</style>', `${quizUiCss}\n  </style>`);
    }

    const months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul'];
    const allQuizData = {};

    for (const month of months) {
      console.log(`Generating quiz for ${month}...`);
      const textContext = extractTextForMonth(content, month);
      
      if (!textContext.trim()) {
        console.log(`Empty content for ${month}, skipping.`);
        continue;
      }

      const questions = await generateQuizData(textContext, folder, month);
      if (questions && questions.length > 0) {
        allQuizData[month] = questions;
        console.log(`Successfully generated ${questions.length} questions.`);
      } else {
        console.log(`Failed to get quiz questions for ${month}.`);
      }
      
      // Proactive delay to avoid rate limits
      await sleep(5000);
    }

    // Embed data in HTML
    const dataScript = `
  <!-- QUIZ DATA -->
  <script>
    window.quizData = ${JSON.stringify(allQuizData, null, 2)};
  </script>`;

    // Remove old data script if present
    content = content.replace(/<!-- QUIZ DATA -->[\s\S]*?<\/script>/, '');

    // Inject data script before the main script tag
    content = content.replace('<script src="/assets/js/main.min.js', `${dataScript}\n  <script src="/assets/js/main.min.js`);
    content = content.replace('<script defer="" src="/assets/js/main.min.js', `${dataScript}\n  <script defer="" src="/assets/js/main.min.js`);

    // Inject controller script if not present
    if (!content.includes('month-sub-nav')) {
      content = content.replace('</body>', `${quizControllerJs}\n</body>`);
    }

    // Now wrap each month's panels with sub-nav tabs
    for (const month of months) {
      const monthRegex = new RegExp(`(<div [^>]*id="${month}"[^>]*>)([\\s\\S]*?)(</div>\\s*(<!-- (FEBRUARY|MARCH|APRIL|MAY|JUNE|JULY|REVISION) PANEL|</div>\\s*</div>))`, 'i');
      const match = content.match(monthRegex);
      
      if (match && !match[2].includes('month-sub-nav')) {
        const innerContent = match[2];
        const wrappedContent = `
      <div class="month-sub-nav">
        <button class="sub-tab-btn active" data-subtab="${month}-study">Study Notes / अध्ययन सामग्री</button>
        <button class="sub-tab-btn" data-subtab="${month}-quiz">Practice Quiz / अभ्यास क्विज</button>
      </div>

      <div id="${month}-study" class="sub-tab-panel active">
        ${innerContent}
      </div>

      <div id="${month}-quiz" class="sub-tab-panel">
        <div class="quiz-container">
          <div class="quiz-header">
            <span class="quiz-progress">Question 1 of 30</span>
            <span class="quiz-score">Score: 0/0</span>
          </div>
          <div class="quiz-progress-bar">
            <div class="quiz-progress-fill" style="width: 3.33%;"></div>
          </div>
          <div class="quiz-question-card">
            <p class="quiz-question-text en-text"></p>
            <p class="quiz-question-text hi-text"></p>
            <div class="quiz-options-list"></div>
            <div class="quiz-explanation-box" style="display: none;">
              <p class="explanation-title">Explanation / व्याख्या:</p>
              <p class="explanation-text en-text"></p>
              <p class="explanation-text hi-text"></p>
            </div>
          </div>
          <div class="quiz-navigation">
            <button class="quiz-nav-btn prev-btn" disabled>Previous / पिछला</button>
            <button class="quiz-nav-btn next-btn">Next / अगला</button>
          </div>
        </div>
      </div>
`;
        content = content.replace(match[0], `${match[1]}${wrappedContent}${match[3]}`);
      }
    }

    fs.writeFileSync(filePath, content, 'utf8');
    console.log(`Completed folder: ${folder}`);
  }
}

run();
