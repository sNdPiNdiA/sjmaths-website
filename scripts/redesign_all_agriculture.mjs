import fs from 'fs';
import path from 'path';

const INVENTORY_FILE = 'scratch/agriculture_inventory.json';
if (!fs.existsSync(INVENTORY_FILE)) {
  console.error(`Inventory file ${INVENTORY_FILE} does not exist.`);
  process.exit(1);
}

const inventory = JSON.parse(fs.readFileSync(INVENTORY_FILE, 'utf8'));
console.log(`Starting redesign batch transformation for all ${inventory.length} Agriculture pages...`);

const customCss = `<style>
:root {
  --brand: #14532d;
  --brand-dark: #052e16;
  --brand-light: #16a34a;
  --accent: #15803d;
  --accent-hover: #166534;
  --accent-soft: rgba(21, 128, 61, 0.08);
  --accent-border: rgba(21, 128, 61, 0.24);
}
html.dark, body.dark-mode {
  --brand: #4ade80;
  --brand-dark: #86efac;
  --brand-light: #22c55e;
  --accent: #34d399;
  --accent-hover: #6ee7b7;
  --accent-soft: rgba(52, 211, 153, 0.14);
  --accent-border: rgba(52, 211, 153, 0.35);
}
.desk-only { display: none; }
@media (min-width: 640px) {
  .desk-only { display: inline; }
}
</style>`;

const upgradedScript = `<script>
document.addEventListener('DOMContentLoaded', () => {
  // Dual-Class Theme Toggle
  const themeToggleBtn = document.getElementById('btn-theme-toggle');
  const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
  const savedTheme = localStorage.getItem('sjmaths_theme') || localStorage.getItem('sj_theme');
  if (savedTheme === 'dark' || (!savedTheme && prefersDark)) {
    document.body.classList.add('dark-mode');
    document.documentElement.classList.add('dark');
    if (themeToggleBtn) themeToggleBtn.textContent = '☀️ Light Mode';
  }
  if (themeToggleBtn) {
    themeToggleBtn.addEventListener('click', () => {
      const isDark = document.body.classList.toggle('dark-mode');
      document.documentElement.classList.toggle('dark', isDark);
      localStorage.setItem('sjmaths_theme', isDark ? 'dark' : 'light');
      localStorage.setItem('sj_theme', isDark ? 'dark' : 'light');
      themeToggleBtn.textContent = isDark ? '☀️ Light Mode' : '🌙 Dark Mode';
    });
  }

  // 5-Tab Switching Logic
  const tabBtns = document.querySelectorAll('.tab-btn');
  const tabPanels = document.querySelectorAll('.tab-panel');

  tabBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      const targetId = btn.getAttribute('data-tab');
      tabBtns.forEach(b => {
        b.classList.remove('active');
        b.setAttribute('aria-selected', 'false');
      });
      tabPanels.forEach(p => {
        p.classList.remove('active');
        p.classList.add('hidden');
      });

      btn.classList.add('active');
      btn.setAttribute('aria-selected', 'true');
      const activePanel = document.getElementById(targetId);
      if (activePanel) {
        activePanel.classList.remove('hidden');
        activePanel.classList.add('active');
      }
      const stickyWrap = document.querySelector('.study-tabs-sticky-wrapper');
      if (stickyWrap) {
        window.scrollTo({ top: stickyWrap.offsetTop - 15, behavior: 'smooth' });
      }
    });
  });

  // Practice Quiz Interactive Verification
  let quizScore = 0;
  const answeredQuestions = new Set();
  const quizOptionBtns = document.querySelectorAll('.quiz-option-btn, .quiz-opt');

  quizOptionBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      const qIndex = parseInt(btn.getAttribute('data-qindex'), 10);
      const optIndex = parseInt(btn.getAttribute('data-optindex'), 10);
      const card = document.getElementById('q-card-' + qIndex);
      if (!card) return;
      const correctIndex = parseInt(card.getAttribute('data-correct'), 10);
      const feedback = document.getElementById('feedback-' + qIndex) || document.getElementById('q-feedback-' + qIndex);
      const statusIndicator = feedback ? (feedback.querySelector('.feedback-indicator') || feedback.querySelector('.feedback-status')) : null;

      if (answeredQuestions.has(qIndex)) return;
      answeredQuestions.add(qIndex);

      const allBtns = card.querySelectorAll('.quiz-option-btn, .quiz-opt');
      allBtns.forEach((b, idx) => {
        b.disabled = true;
        if (idx === correctIndex) b.classList.add('correct');
        else if (idx === optIndex && optIndex !== correctIndex) b.classList.add('incorrect');
      });

      const letters = ['A', 'B', 'C', 'D'];
      if (optIndex === correctIndex) {
        quizScore++;
        if (statusIndicator) {
          statusIndicator.textContent = '✓ Correct Answer!';
          statusIndicator.className = 'feedback-indicator correct';
        }
        if (feedback) {
          feedback.className = 'q-feedback quiz-feedback show correct';
        }
      } else {
        if (statusIndicator) {
          statusIndicator.textContent = '✗ Incorrect. Correct Option: ' + letters[correctIndex];
          statusIndicator.className = 'feedback-indicator incorrect';
        }
        if (feedback) {
          feedback.className = 'q-feedback quiz-feedback show incorrect';
        }
      }
      if (feedback) feedback.classList.remove('hidden');

      const scoreEl = document.getElementById('quizScore') || document.getElementById('quizScoreText');
      if (scoreEl) {
        scoreEl.textContent = scoreEl.id === 'quizScore' ? quizScore : 'Score: ' + quizScore + ' / ' + document.querySelectorAll('.quiz-question-card, .quiz-card').length;
      }
    });
  });

  const btnResetQuiz = document.getElementById('btnResetQuiz');
  if (btnResetQuiz) {
    btnResetQuiz.addEventListener('click', () => {
      quizScore = 0;
      answeredQuestions.clear();
      const scoreEl = document.getElementById('quizScore') || document.getElementById('quizScoreText');
      if (scoreEl) {
        scoreEl.textContent = scoreEl.id === 'quizScore' ? '0' : 'Score: 0 / ' + document.querySelectorAll('.quiz-question-card, .quiz-card').length;
      }
      document.querySelectorAll('.quiz-option-btn, .quiz-opt').forEach(b => {
        b.disabled = false;
        b.classList.remove('correct', 'incorrect');
      });
      document.querySelectorAll('.q-feedback, .quiz-feedback').forEach(f => {
        f.classList.add('hidden');
        f.classList.remove('show', 'correct', 'incorrect');
      });
    });
  }

  // Timed Topic Test Logic
  let testTimer = null;
  let secondsLeft = 600;
  const btnStartTest = document.getElementById('btnStartTest');
  const testStartWrap = document.getElementById('testStartWrap');
  const testActiveWrap = document.getElementById('testActiveWrap');
  const timerDisplay = document.getElementById('timerDisplay') || document.getElementById('testTimerDisplay');

  if (btnStartTest) {
    btnStartTest.addEventListener('click', () => {
      if (testStartWrap) testStartWrap.classList.add('hidden');
      if (testActiveWrap) testActiveWrap.classList.remove('hidden');
      testTimer = setInterval(() => {
        secondsLeft--;
        const mins = Math.floor(secondsLeft / 60);
        const secs = secondsLeft % 60;
        if (timerDisplay) {
          timerDisplay.textContent = (mins < 10 ? '0' : '') + mins + ':' + (secs < 10 ? '0' : '') + secs;
        }
        if (secondsLeft <= 0) {
          clearInterval(testTimer);
          submitTest();
        }
      }, 1000);
    });
  }

  const selectedTestAnswers = {};
  document.querySelectorAll('.test-option-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      const tIndex = parseInt(btn.getAttribute('data-tindex'), 10);
      const optIndex = parseInt(btn.getAttribute('data-optindex'), 10);
      selectedTestAnswers[tIndex] = optIndex;
      const card = document.getElementById('t-card-' + tIndex);
      if (card) {
        card.querySelectorAll('.test-option-btn').forEach(b => b.classList.remove('selected'));
      }
      btn.classList.add('selected');
    });
  });

  function submitTest() {
    if (testTimer) clearInterval(testTimer);
    let score = 0;
    const testCards = document.querySelectorAll('.test-question-card');
    testCards.forEach((card, idx) => {
      const correct = parseInt(card.getAttribute('data-correct'), 10);
      const userAns = selectedTestAnswers[idx];
      const feedback = document.getElementById('t-feedback-' + idx);
      const btns = card.querySelectorAll('.test-option-btn');
      btns.forEach((b, oIdx) => {
        b.disabled = true;
        if (oIdx === correct) b.classList.add('correct');
        else if (oIdx === userAns && userAns !== correct) b.classList.add('incorrect');
      });
      if (userAns === correct) score++;
      if (feedback) feedback.classList.remove('hidden');
    });
    const resScore = document.getElementById('resFinalScore');
    if (resScore) resScore.textContent = score;
    const resModal = document.getElementById('testResultModal');
    if (resModal) resModal.classList.remove('hidden');
    const btnSub = document.getElementById('btnSubmitTest');
    if (btnSub) btnSub.classList.add('hidden');
  }

  const btnSubmitTest = document.getElementById('btnSubmitTest');
  if (btnSubmitTest) btnSubmitTest.addEventListener('click', submitTest);

  const btnRetakeTest = document.getElementById('btnRetakeTest');
  if (btnRetakeTest) {
    btnRetakeTest.addEventListener('click', () => {
      location.reload();
    });
  }
});
</script>`;

function transformHtml(html) {
  let updated = html;

  // 1. Clean raw LaTeX dollars in text ($2n$ -> 2n, $A$ -> A)
  updated = updated.replace(/\$([^\$]+)\$/g, '$1');

  // 2. Replace brand mark SJ with mathematical integral symbol &int;
  updated = updated.replace(
    /<span class="brand-mark"[^>]*>SJ<\/span>/g,
    '<span class="brand-mark" style="background: linear-gradient(145deg, #14532d, #16a34a); font-family: serif; font-size: 1.35rem; font-style: italic; display: flex; align-items: center; justify-content: center;">&int;</span>'
  );

  // 3. Responsive header buttons
  updated = updated.replace(
    /<div class="header-actions">[\s\S]*?<\/div>\s*<\/div>\s*<\/header>/,
    `<div class="header-actions">
      <button type="button" class="theme-toggle-btn" id="btn-theme-toggle" aria-label="Toggle Dark Mode">🌙 Dark Mode</button>
      <a class="back-btn" href="/up-pgt-agriculture/" title="UP PGT Agriculture Tracker">← UP PGT<span class="desk-only"> Agriculture</span></a>
      <a class="back-btn" href="/up-tgt-agriculture/" title="UP TGT Agriculture Tracker">← UP TGT<span class="desk-only"> Agriculture</span></a>
    </div>
  </div>
</header>`
  );

  // 4. Ensure root CSS includes dark mode variables and desk-only helper
  if (!updated.includes('html.dark, body.dark-mode')) {
    updated = updated.replace(/<style>[\s\S]*?<\/style>/, customCss);
  }

  // 5. Replace script tag at bottom of body
  updated = updated.replace(/<script>[\s\S]*?<\/script>\s*<\/body>/, `${upgradedScript}\n</body>`);

  return updated;
}

let successCount = 0;
let missingCount = 0;

for (let i = 0; i < inventory.length; i++) {
  const item = inventory[i];
  const htmlPath = path.join(path.resolve(item.dir), 'index.html');

  if (!fs.existsSync(htmlPath)) {
    missingCount++;
    console.warn(`[WARNING] File missing: ${htmlPath}`);
    continue;
  }

  try {
    const rawHtml = fs.readFileSync(htmlPath, 'utf8');
    const transformed = transformHtml(rawHtml);
    fs.writeFileSync(htmlPath, transformed, 'utf8');
    successCount++;
  } catch (err) {
    console.error(`[ERROR] Failed to transform ${htmlPath}:`, err.message);
  }

  if ((i + 1) % 50 === 0 || i === inventory.length - 1) {
    console.log(`Progress: [${i + 1}/${inventory.length}] files processed (${successCount} successful).`);
  }
}

console.log(`\n============================================================`);
console.log(`Batch Redesign Complete!`);
console.log(`Total Inventory: ${inventory.length}`);
console.log(`Successfully Redesigned: ${successCount}`);
console.log(`Missing Files: ${missingCount}`);
console.log(`============================================================`);
