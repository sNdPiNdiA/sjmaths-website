/**
 * class12-physics.js
 * Unified Client-Side Engine for Class 12 Physics Chapter Pages
 * Handles: Tab Navigation, MathJax/KaTeX Auto-Render, Collapsible Stepwise Solutions,
 * Quiz Option Selection, Interactive Scoring, Test Engine, and PYQ Subtopic Jump Scrolling.
 */

let currentActiveTestLevel = 0;

/* 1. Tab Switching & Progress Bar */
function switchTab(tabId) {
  document.querySelectorAll('.tab').forEach(t => t.classList.toggle('active', t.id === tabId));
  document.querySelectorAll('.nav-btn').forEach(btn => btn.classList.toggle('active', btn.dataset.tab === tabId));
  
  const progMap = { learn: 16, quiz: 33, exercise: 50, revision: 66, pyqs: 83, tests: 100 };
  const pb = document.getElementById('progressBar');
  if (pb && progMap[tabId]) {
    pb.style.width = progMap[tabId] + '%';
  }

  window.scrollTo({ top: 0, behavior: 'smooth' });
}

/* 2. Direct Navigation to a Learn Section */
function openLearnSec(secId) {
  switchTab('learn');
  setTimeout(() => {
    const el = document.getElementById(secId);
    if (el) el.scrollIntoView({ behavior: 'smooth', block: 'start' });
  }, 100);
}

/* 3. Solved Examples Stepwise Toggle */
function toggleExample(btn) {
  const box = btn.nextElementSibling;
  if (!box) return;
  const isOpening = !box.classList.contains('open');
  box.classList.toggle('open', isOpening);
  btn.classList.toggle('active', isOpening);
  
  const bEl = btn.querySelector('b');
  const spanEl = btn.querySelector('span');
  if (bEl) bEl.textContent = isOpening ? '−' : '+';
  if (spanEl) spanEl.textContent = isOpening ? 'Hide Step-by-Step Solution' : 'View Step-by-Step Solution';
}

/* 4. Exercise & PYQ Stepwise Solution Toggle */
function toggleSolution(btn) {
  const content = btn.nextElementSibling;
  if (!content) return;
  const isOpening = !content.classList.contains('open');
  content.classList.toggle('open', isOpening);
  btn.classList.toggle('active', isOpening);
  
  const bEl = btn.querySelector('b');
  const spanEl = btn.querySelector('span');
  if (bEl) bEl.textContent = isOpening ? '−' : '+';
  if (spanEl) spanEl.textContent = isOpening ? 'Hide Step-by-Step Solution' : 'View Step-by-Step Solution';
}

/* 5. Filter Exercises */
function filterExercises(tag, chip) {
  document.querySelectorAll('#exercise .chip').forEach(c => c.classList.remove('active'));
  if (chip) chip.classList.add('active');

  document.querySelectorAll('.exercise-card').forEach(card => {
    if (!card.classList.contains('pyq-card')) {
      if (tag === 'all' || (card.dataset.tags && card.dataset.tags.includes(tag))) {
        card.style.display = 'block';
      } else {
        card.style.display = 'none';
      }
    }
  });
}

/* 6. Filter Quiz */
function filterQuiz(cat, chip) {
  document.querySelectorAll('#quiz .chip').forEach(c => c.classList.remove('active'));
  if (chip) chip.classList.add('active');

  document.querySelectorAll('.mcq-card').forEach(card => {
    if (cat === 'all' || card.dataset.cat === cat) {
      card.style.display = 'block';
    } else {
      card.style.display = 'none';
    }
  });
}

/* 7. Quiz Option Selection & Stepwise Explanation Reveal */
function initQuizHandlers() {
  document.querySelectorAll('.mcq-card').forEach(card => {
    const optionBtns = card.querySelectorAll('.mcq-option-btn');
    const explanations = card.querySelectorAll('.opt-explanation');
    const statusEl = card.querySelector('.mcq-status');
    const takeawayEl = card.querySelector('.mcq-takeaway');

    optionBtns.forEach(btn => {
      btn.addEventListener('click', () => {
        if (card.dataset.answered === 'true') return;
        card.dataset.answered = 'true';
        
        const isCorrect = btn.dataset.correct === 'true';
        card.dataset.isCorrect = isCorrect ? 'true' : 'false';

        optionBtns.forEach(b => b.disabled = true);
        btn.classList.add(isCorrect ? 'correct' : 'wrong');

        if (!isCorrect) {
          const correctBtn = Array.from(optionBtns).find(b => b.dataset.correct === 'true');
          if (correctBtn) correctBtn.classList.add('correct');
        }

        explanations.forEach(exp => exp.classList.add('show'));
        if (takeawayEl) takeawayEl.classList.add('show');

        if (statusEl) {
          statusEl.textContent = isCorrect ? 'CORRECT' : 'INCORRECT';
          statusEl.style.color = isCorrect ? 'var(--ok)' : 'var(--danger)';
        }

        updateQuizStats();
      });
    });
  });
}

function updateQuizStats() {
  const allCards = document.querySelectorAll('.mcq-card');
  const answered = Array.from(allCards).filter(c => c.dataset.answered === 'true');
  const correct = Array.from(allCards).filter(c => c.dataset.isCorrect === 'true');

  const countEl = document.getElementById('quizProgressCount');
  const scoreEl = document.getElementById('quizScoreCount');

  if (countEl) countEl.textContent = answered.length + ' / ' + allCards.length + ' Answered';
  if (scoreEl) scoreEl.textContent = correct.length + ' (' + Math.round((correct.length / (allCards.length || 1)) * 100) + '%)';
}

/* 8. Practice Test Engine Handling */
function switchTestLevel(levelIdx, btn) {
  currentActiveTestLevel = levelIdx;
  document.querySelectorAll('.test-tab-btn').forEach(b => b.classList.remove('active'));
  if (btn) btn.classList.add('active');

  for (let i = 0; i < 3; i++) {
    const panel = document.getElementById('testLevel' + i);
    if (panel) panel.style.display = (i === levelIdx) ? 'block' : 'none';
  }

  const res = document.getElementById('testResultBox');
  if (res) res.classList.remove('show');
}

function initTestHandlers() {
  document.querySelectorAll('.test-panel-wrap .test-card').forEach(card => {
    const opts = card.querySelectorAll('.mcq-option-btn');
    opts.forEach(opt => {
      opt.addEventListener('click', () => {
        opts.forEach(o => o.classList.remove('selected'));
        opt.classList.add('selected');
        card.dataset.selected = opt.dataset.idx;
      });
    });
  });
}

function submitActiveTest() {
  const panel = document.getElementById('testLevel' + currentActiveTestLevel);
  if (!panel) return;

  const cards = panel.querySelectorAll('.test-card');
  let score = 0;

  cards.forEach(card => {
    const ans = parseInt(card.dataset.ans);
    const selected = parseInt(card.dataset.selected);
    const opts = card.querySelectorAll('.mcq-option-btn');

    opts.forEach(o => o.classList.remove('correct', 'wrong'));

    if (!isNaN(selected)) {
      if (selected === ans) {
        score++;
        if (opts[selected]) opts[selected].classList.add('correct');
      } else {
        if (opts[selected]) opts[selected].classList.add('wrong');
        if (opts[ans]) opts[ans].classList.add('correct');
      }
    } else {
      if (opts[ans]) opts[ans].classList.add('correct');
    }
  });

  const resBox = document.getElementById('testResultBox');
  if (resBox && cards.length > 0) {
    resBox.classList.add('show');
    const percent = Math.round((score / cards.length) * 100);
    resBox.innerHTML = 'Your Score for Level ' + (currentActiveTestLevel + 1) + ': <strong>' + score + ' / ' + cards.length + '</strong> (' + percent + '%)<br><small style="font-weight:normal;color:#0e7490">' + (score >= (cards.length * 0.8) ? 'Outstanding mastery!' : score >= (cards.length * 0.5) ? 'Good job! Review questions marked in red.' : 'Revise the Learn section and retry!') + '</small>';
    resBox.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
  }
}

function resetActiveTest() {
  const panel = document.getElementById('testLevel' + currentActiveTestLevel);
  if (!panel) return;

  panel.querySelectorAll('.test-card').forEach(card => {
    delete card.dataset.selected;
    card.querySelectorAll('.mcq-option-btn').forEach(o => o.classList.remove('selected', 'correct', 'wrong'));
  });

  const resBox = document.getElementById('testResultBox');
  if (resBox) resBox.classList.remove('show');
}

/* 9. PYQ Subtopic Scroll & Auto-Spy */
function scrollToPyqTopic(topicId, chip) {
  document.querySelectorAll('#pyqs .chip').forEach(c => c.classList.remove('active'));
  if (chip) chip.classList.add('active');

  if (topicId === 'all') {
    const container = document.getElementById('pyqContainer');
    if (container) container.scrollIntoView({ behavior: 'smooth', block: 'start' });
    return;
  }

  const targetEl = document.getElementById('pyq-' + topicId);
  if (targetEl) {
    targetEl.scrollIntoView({ behavior: 'smooth', block: 'start' });
  }
}

function initPyqObserver() {
  const observerOptions = {
    root: null,
    rootMargin: '-20% 0px -70% 0px',
    threshold: 0
  };

  const pyqObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const topicId = entry.target.id.replace('pyq-', '');
        const targetChip = document.getElementById('chip-' + topicId);
        if (targetChip) {
          document.querySelectorAll('#pyqs .chip').forEach(c => c.classList.remove('active'));
          targetChip.classList.add('active');
        }
      }
    });
  }, observerOptions);

  document.querySelectorAll('.pyq-topic-section-header').forEach(header => {
    pyqObserver.observe(header);
  });
}

/* 10. KaTeX Auto-Renderer */
function initKaTeXRenderer() {
  function renderMath() {
    if (typeof renderMathInElement === "function") {
      renderMathInElement(document.body, {
        delimiters: [
          { left: '$$', right: '$$', display: true },
          { left: '$', right: '$', display: false }
        ],
        throwOnError: false
      });
    } else {
      setTimeout(renderMath, 50);
    }
  }
  renderMath();
}

function initPyqQuizHandlers() {
  document.querySelectorAll('.pyq-card').forEach(card => {
    // Find a grid container that contains option divs
    const grids = card.querySelectorAll('.ex-body > div');
    let optionContainer = null;
    let options = [];
    
    for (const grid of grids) {
      const divs = Array.from(grid.children);
      if (divs.length >= 2 && divs.some(d => d.textContent.trim().startsWith('(a)'))) {
        optionContainer = grid;
        options = divs;
        break;
      }
    }
    
    if (!optionContainer || options.length === 0) return; // Not an MCQ
    
    // Find correct answer from final-ans-box
    const finalAnsBox = card.querySelector('.final-ans-box');
    if (!finalAnsBox) return;
    
    const match = finalAnsBox.textContent.match(/\(([a-d])\)/i);
    if (!match) return;
    
    const correctLetter = match[1].toLowerCase();
    
    // Style and add click/hover event listeners to options
    options.forEach(opt => {
      opt.style.cursor = 'pointer';
      opt.style.transition = 'all 0.2s ease';
      
      opt.addEventListener('mouseenter', () => {
        if (card.dataset.answered === 'true') return;
        opt.style.borderColor = 'var(--pyq, #ea580c)';
        opt.style.background = '#fff7ed';
      });
      opt.addEventListener('mouseleave', () => {
        if (card.dataset.answered === 'true') return;
        opt.style.borderColor = 'var(--line)';
        opt.style.background = '#f8fafc';
      });
      
      opt.addEventListener('click', () => {
        if (card.dataset.answered === 'true') return;
        card.dataset.answered = 'true';
        
        const optText = opt.textContent.trim();
        const optLetterMatch = optText.match(/^\(([a-d])\)/i);
        if (!optLetterMatch) return;
        
        const clickedLetter = optLetterMatch[1].toLowerCase();
        const isCorrect = clickedLetter === correctLetter;
        
        if (isCorrect) {
          opt.style.borderColor = '#059669';
          opt.style.background = '#ecfdf5';
          opt.style.color = '#065f46';
          opt.style.fontWeight = '700';
        } else {
          opt.style.borderColor = '#e11d48';
          opt.style.background = '#fff1f2';
          opt.style.color = '#9f1239';
          opt.style.fontWeight = '700';
          
          const correctOpt = options.find(o => {
            const m = o.textContent.trim().match(/^\(([a-d])\)/i);
            return m && m[1].toLowerCase() === correctLetter;
          });
          if (correctOpt) {
            correctOpt.style.borderColor = '#059669';
            correctOpt.style.background = '#ecfdf5';
            correctOpt.style.color = '#065f46';
            correctOpt.style.fontWeight = '700';
          }
        }
        
        // Auto-reveal the solution
        const solBtn = card.querySelector('.sol-toggle-btn');
        const solContent = card.querySelector('.ex-solution-content');
        if (solBtn && solContent && !solContent.classList.contains('open')) {
          toggleSolution(solBtn);
        }
      });
    });
  });
}

/* Initialise on DOM Ready */
document.addEventListener('DOMContentLoaded', () => {
  initKaTeXRenderer();
  initQuizHandlers();
  initTestHandlers();
  initPyqQuizHandlers();
  initPyqObserver();
});
