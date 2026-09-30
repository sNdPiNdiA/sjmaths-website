/* Current unit papers reuse TestEngine without changing other classes' tests. */
(function () {
  'use strict';
  class CurrentUnitTestEngine extends TestEngine {
    loadState() {
      this.storageKey += '_' + this.config.version;
      super.loadState();
      this.currentQuestionIndex = Math.max(0, Math.min(this.currentQuestionIndex, this.config.questions.length - 1));
    }
    loadQuestion(index) {
      super.loadQuestion(index);
      const question = this.config.questions[index];
      const input = document.getElementById('inputArea');
      const title = document.getElementById('qNumber');
      title.setAttribute('tabindex', '-1');
      if (question.type === 'mcq') {
        input.replaceChildren();
        question.options.forEach((option, i) => {
          const button = document.createElement('button');
          button.type = 'button';
          button.className = 'mcq-option';
          button.textContent = option;
          button.classList.toggle('selected', this.answers[question.id] === i);
          button.setAttribute('aria-pressed', String(this.answers[question.id] === i));
          button.disabled = this.isSubmitted;
          button.addEventListener('click', () => {
            this.selectOption(question.id, i, button);
            input.querySelectorAll('button').forEach((item, optionIndex) => item.setAttribute('aria-pressed', String(i === optionIndex)));
          });
          input.appendChild(button);
        });
      } else {
        input.querySelector('textarea').setAttribute('aria-label', 'Your written answer to question ' + (index + 1));
      }
      if (this.isSubmitted) {
        const solution = document.getElementById('solutionArea');
        solution.replaceChildren();
        const answer = document.createElement('p');
        answer.textContent = 'Model answer: ' + question.finalAnswer;
        const steps = document.createElement('ol');
        question.solutionSteps.forEach(step => {
          const item = document.createElement('li');
          item.textContent = step;
          steps.appendChild(item);
        });
        solution.append(answer, steps);
        const diagram = document.querySelector('#paper-' + question.id + ' svg');
        if (diagram) solution.appendChild(diagram.cloneNode(true));
        if (question.type !== 'mcq') {
          const note = document.createElement('p');
          note.textContent = 'Written response: self-check or ask a teacher to assess the ' + question.marks + ' marks. It is not automatically scored.';
          solution.appendChild(note);
        }
      }
      document.querySelectorAll('.palette-btn').forEach((button, i) => {
        button.setAttribute('aria-label', 'Go to question ' + (i + 1));
        if (i === index) button.setAttribute('aria-current', 'step');
        else button.removeAttribute('aria-current');
      });
    }
    attachEventListeners() {
      super.attachEventListeners();
      document.getElementById('btnReset').addEventListener('click', () => {
        if (!window.confirm('Clear this paper’s saved answers and restart its timer?')) return;
        clearInterval(this.timerInterval);
        localStorage.removeItem(this.storageKey);
        window.location.reload();
      });
      const panel = document.querySelector('.nav-panel');
      const toggle = document.getElementById('paletteToggle');
      const sync = () => toggle.setAttribute('aria-expanded', String(!panel.classList.contains('collapsed')));
      sync();
      toggle.addEventListener('click', event => {
        event.stopPropagation();
        panel.classList.toggle('collapsed');
        sync();
      });
      document.querySelector('.nav-panel h3').style.cursor = 'default';
      document.querySelector('.nav-panel h3').onclick = null;
      const next = document.getElementById('btnNext');
      const previous = document.getElementById('btnPrev');
      [next, previous].forEach(button => button.addEventListener('click', () => {
        if (!this.isSubmitted) document.getElementById('qNumber').focus({ preventScroll: true });
      }));
      const review = document.querySelector('#resultModal .btn-submit');
      review.addEventListener('click', () => document.getElementById('qNumber').focus());
      this.previousFocus = null;
      document.getElementById('resultModal').addEventListener('keydown', event => {
        if (event.key !== 'Tab') return;
        const controls = [...document.querySelectorAll('#resultModal button, #resultModal a[href]')];
        if (event.shiftKey && document.activeElement === controls[0]) {
          event.preventDefault(); controls.at(-1).focus();
        } else if (!event.shiftKey && document.activeElement === controls.at(-1)) {
          event.preventDefault(); controls[0].focus();
        }
      });
    }
    showResultModal() {
      const auto = this.config.questions.filter(question => question.type === 'mcq');
      const total = auto.reduce((sum, question) => sum + question.marks, 0);
      const score = auto.reduce((sum, question) => sum + (this.answers[question.id] === question.correctOption ? question.marks : 0), 0);
      const writtenMarks = this.config.questions.filter(question => question.type !== 'mcq').reduce((sum, question) => sum + question.marks, 0);
      const modal = document.getElementById('resultModal');
      modal.style.display = 'flex';
      document.querySelector('.score-text').textContent = score + ' / ' + total;
      const message = document.getElementById('resultMessage');
      message.replaceChildren();
      const heading = document.createElement('h2');
      heading.id = 'result-heading';
      heading.textContent = 'MCQ score';
      const explanation = document.createElement('p');
      explanation.textContent = 'Automatically scored: ' + score + ' of ' + total + ' marks. Written questions carry a further ' + writtenMarks + ' marks for self- or teacher assessment. Review the step-wise model solutions.';
      message.append(heading, explanation);
      document.getElementById('timerDisplay').textContent = 'Finished';
      modal.querySelector('button').focus();
    }
  }
  const data = JSON.parse(document.getElementById('unit-test-data').textContent);
  document.getElementById('source-paper').removeAttribute('open');
  new CurrentUnitTestEngine(data);
  document.documentElement.classList.add('unit-test-ready');
}());
