let currentActiveTestLevel = 0;
let learnScrollTimer = null;

/* Tab Navigation */
function switchTab(tabId){
  clearTimeout(learnScrollTimer);
  learnScrollTimer = null;
  if (!document.getElementById(tabId)?.classList.contains('tab')) return;
  document.querySelectorAll('.tab').forEach(t => t.classList.toggle('active', t.id === tabId));
  document.querySelectorAll('.nav-btn').forEach(btn => btn.classList.toggle('active', btn.dataset.tab === tabId));

  const progMap = { learn: 20, quiz: 40, exercise: 60, revision: 80, tests: 100 };
  const pb = document.getElementById('progressBar');
  if(pb) pb.style.width = progMap[tabId] + '%';

  window.scrollTo({ top: 0, behavior: window.matchMedia('(prefers-reduced-motion: reduce)').matches ? 'instant' : 'smooth' });
}

function openLearnSec(secId){
  switchTab('learn');
  learnScrollTimer = setTimeout(() => {
    learnScrollTimer = null;
    if (!document.getElementById('learn').classList.contains('active')) return;
    const el = document.getElementById(secId);
    if(el) el.scrollIntoView({ behavior: window.matchMedia('(prefers-reduced-motion: reduce)').matches ? 'instant' : 'smooth' });
  }, 100);
}

/* Solution Toggle in Solved Examples */
function toggleExample(btn){
  const box = btn.nextElementSibling;
  const isOpening = !box.classList.contains('open');
  box.classList.toggle('open', isOpening);
  btn.classList.toggle('active', isOpening);
  btn.setAttribute('aria-expanded', String(isOpening));
  btn.querySelector('b').textContent = isOpening ? '−' : '+';
  btn.querySelector('span').textContent = isOpening ? 'Hide Step-by-Step Solution' : 'View Step-by-Step Solution';
}

/* Solution Toggle in Exercises */
function toggleSolution(btn){
  const content = btn.nextElementSibling;
  const isOpening = !content.classList.contains('open');
  content.classList.toggle('open', isOpening);
  btn.classList.toggle('active', isOpening);
  btn.setAttribute('aria-expanded', String(isOpening));
  btn.querySelector('b').textContent = isOpening ? '−' : '+';
  btn.querySelector('span').textContent = isOpening ? 'Hide Step-by-Step Solution' : 'View Step-by-Step Solution';
}

/* Filter Exercises */
function filterExercises(tag, chip){
  document.querySelectorAll('#exercise .chip').forEach(c => c.classList.remove('active'));
  chip.classList.add('active');

  document.querySelectorAll('.exercise-card').forEach(card => {
    if(tag === 'all' || card.dataset.tags.includes(tag)){
      card.style.display = 'block';
    } else {
      card.style.display = 'none';
    }
  });
}

/* Quiz Option Selection & Stepwise Explanation Reveal */
document.querySelectorAll('.mcq-card').forEach(card => {
  const optionBtns = card.querySelectorAll('.mcq-option-btn');
  const explanations = card.querySelectorAll('.opt-explanation');
  const statusEl = card.querySelector('.mcq-status');
  const takeawayEl = card.querySelector('.mcq-takeaway');

  optionBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      if(card.dataset.answered === 'true') return;
      card.dataset.answered = 'true';

      const isCorrect = btn.dataset.correct === 'true';
      card.dataset.isCorrect = isCorrect ? 'true' : 'false';

      optionBtns.forEach(b => b.disabled = true);
      btn.classList.add(isCorrect ? 'correct' : 'wrong');

      if(!isCorrect){
        const correctBtn = Array.from(optionBtns).find(b => b.dataset.correct === 'true');
        if(correctBtn) correctBtn.classList.add('correct');
      }

      explanations.forEach(exp => exp.classList.add('show'));
      if(takeawayEl) takeawayEl.classList.add('show');

      if(statusEl){
        statusEl.textContent = isCorrect ? 'CORRECT' : 'INCORRECT';
        statusEl.style.color = isCorrect ? 'var(--ok)' : 'var(--danger)';
      }

      updateQuizStats();
    });
  });
});

function updateQuizStats(){
  const allCards = document.querySelectorAll('.mcq-card');
  const answered = Array.from(allCards).filter(c => c.dataset.answered === 'true');
  const correct = Array.from(allCards).filter(c => c.dataset.isCorrect === 'true');

  const countEl = document.getElementById('quizProgressCount');
  const scoreEl = document.getElementById('quizScoreCount');

  if(countEl) countEl.textContent = answered.length + ' / ' + allCards.length + ' Answered';
  if(scoreEl) scoreEl.textContent = correct.length + ' (' + Math.round((correct.length / allCards.length)*100) + '%)';
}

/* Test Engine Handling */
function switchTestLevel(levelIdx, btn){
  currentActiveTestLevel = levelIdx;
  document.querySelectorAll('.test-tab-btn').forEach(b => b.classList.remove('active'));
  btn.classList.add('active');

  for(let i=0; i<3; i++){
    const panel = document.getElementById('testLevel' + i);
    if(panel) panel.style.display = (i === levelIdx) ? 'block' : 'none';
  }

  const res = document.getElementById('testResultBox');
  if(res) res.classList.remove('show');
}

document.querySelectorAll('.test-panel-wrap .test-card').forEach(card => {
  const opts = card.querySelectorAll('.mcq-option-btn');
  opts.forEach(opt => {
    opt.addEventListener('click', () => {
      opts.forEach(o => o.classList.remove('selected'));
      opt.classList.add('selected');
      card.dataset.selected = opt.dataset.idx;
      const panel = card.closest('.test-panel-wrap');
      panel.querySelectorAll('.mcq-option-btn').forEach(o => o.classList.remove('correct', 'wrong'));
      const result = document.getElementById('testResultBox');
      if (result) result.classList.remove('show');
    });
  });
});

function submitActiveTest(){
  const panel = document.getElementById('testLevel' + currentActiveTestLevel);
  if(!panel) return;

  const cards = panel.querySelectorAll('.test-card');
  let score = 0;

  cards.forEach(card => {
    const ans = parseInt(card.dataset.ans);
    const selected = parseInt(card.dataset.selected);
    const opts = card.querySelectorAll('.mcq-option-btn');

    opts.forEach(o => o.classList.remove('correct', 'wrong'));

    if(!isNaN(selected)){
      if(selected === ans){
        score++;
        opts[selected].classList.add('correct');
      } else {
        opts[selected].classList.add('wrong');
        opts[ans].classList.add('correct');
      }
    } else {
      opts[ans].classList.add('correct');
    }
  });

  const resBox = document.getElementById('testResultBox');
  if(resBox){
    resBox.classList.add('show');
    resBox.innerHTML = 'Your Score for Level ' + (currentActiveTestLevel + 1) + ': <strong>' + score + ' / ' + cards.length + '</strong> (' + Math.round((score/cards.length)*100) + '%)<br><small style="font-weight:normal;color:#047857">' + (score / cards.length >= 0.8 ? 'Excellent understanding of this chapter!' : 'Revise the Learn section and try again.') + '</small>';
    resBox.scrollIntoView({ behavior: window.matchMedia('(prefers-reduced-motion: reduce)').matches ? 'instant' : 'smooth', block: 'nearest' });
  }
}

function resetActiveTest(){
  const panel = document.getElementById('testLevel' + currentActiveTestLevel);
  if(!panel) return;

  panel.querySelectorAll('.test-card').forEach(card => {
    delete card.dataset.selected;
    card.querySelectorAll('.mcq-option-btn').forEach(o => o.classList.remove('selected', 'correct', 'wrong'));
  });

  const resBox = document.getElementById('testResultBox');
  if(resBox) resBox.classList.remove('show');
}

// Direct links to a concept or exercise open the containing tab before scrolling.
function openChapterHash() {
  let id;
  try { id = decodeURIComponent(location.hash.slice(1)); }
  catch { return; } // A malformed URL fragment cannot identify a chapter section.
  const target = document.getElementById(id);
  const tab = target?.closest('.tab');
  if (!tab) return;
  switchTab(tab.id);
  target.scrollIntoView({ block: 'start', behavior: 'instant' });
}
window.addEventListener('hashchange', openChapterHash);
if (location.hash) openChapterHash();
