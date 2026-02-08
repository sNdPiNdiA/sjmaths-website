class TestEngine {
    constructor(config) {
        this.config = config;
        this.storageKey = `sjmaths_test_${window.location.pathname}`;
        this.currentQuestionIndex = 0;
        this.answers = {}; // { qId: answer }
        this.visited = new Set();
        this.timeLeft = config.timeLimit * 60;
        this.timerInterval = null;
        this.isSubmitted = false;

        this.loadState();
        this.init();
    }

    loadState() {
        try {
            const saved = localStorage.getItem(this.storageKey);
            if (saved) {
                const data = JSON.parse(saved);
                this.answers = data.answers || {};
                this.isSubmitted = data.isSubmitted || false;
                if (data.visited) this.visited = new Set(data.visited);
                if (typeof data.timeLeft === 'number') this.timeLeft = data.timeLeft;
                if (typeof data.currentQuestionIndex === 'number') this.currentQuestionIndex = data.currentQuestionIndex;
            }
        } catch (e) { console.error("Load failed", e); }
    }

    saveState() {
        try {
            localStorage.setItem(this.storageKey, JSON.stringify({
                answers: this.answers,
                isSubmitted: this.isSubmitted,
                visited: Array.from(this.visited),
                timeLeft: this.timeLeft,
                currentQuestionIndex: this.currentQuestionIndex
            }));
        } catch (e) { console.error("Save failed", e); }
    }

    init() {
        this.renderPalette();
        this.loadQuestion(this.currentQuestionIndex);
        
        if (this.isSubmitted) {
            this.showResultModal();
            const display = document.getElementById('timerDisplay');
            if (display) display.textContent = "Finished";
        } else {
            this.startTimer();
        }
        
        this.attachEventListeners();
        this.injectResetButton();
    }

    startTimer() {
        const display = document.getElementById('timerDisplay');
        if (!display) return;
        
        const updateDisplay = () => {
            const m = Math.floor(this.timeLeft / 60);
            const s = this.timeLeft % 60;
            display.textContent = `${m}:${s < 10 ? '0' : ''}${s}`;
        };
        updateDisplay();

        this.timerInterval = setInterval(() => {
            if (this.timeLeft <= 0) {
                this.submitTest();
                return;
            }
            this.timeLeft--;
            if (this.timeLeft % 5 === 0) this.saveState();
            updateDisplay();
        }, 1000);
    }

    loadQuestion(index) {
        this.currentQuestionIndex = index;
        this.visited.add(index);
        this.saveState();
        const q = this.config.questions[index];

        // Update Header
        document.getElementById('qSection').textContent = q.section;
        document.getElementById('qNumber').textContent = `Question ${index + 1}`;
        document.getElementById('qMarks').textContent = `(${q.marks} Mark${q.marks > 1 ? 's' : ''})`;
        
        // Update Text
        document.getElementById('qText').innerHTML = q.question;

        // Render Input
        const inputArea = document.getElementById('inputArea');
        inputArea.innerHTML = '';

        if (q.type === 'mcq') {
            q.options.forEach((opt, i) => {
                const div = document.createElement('div');
                div.className = `mcq-option ${this.answers[q.id] === i ? 'selected' : ''}`;
                div.innerHTML = opt;
                div.onclick = () => this.selectOption(q.id, i, div);
                inputArea.appendChild(div);
            });
        } else {
            const textarea = document.createElement('textarea');
            textarea.style.width = '100%';
            textarea.style.height = '100px';
            textarea.style.padding = '10px';
            textarea.style.marginTop = '10px';
            textarea.style.borderRadius = '8px';
            textarea.style.border = '1px solid #ddd';
            textarea.placeholder = 'Type your answer here...';
            textarea.value = this.answers[q.id] || '';
            textarea.oninput = (e) => {
                this.answers[q.id] = e.target.value;
                this.saveState();
                this.updatePalette();
            };
            inputArea.appendChild(textarea);
        }

        // Show Solution if submitted
        const solArea = document.getElementById('solutionArea');
        if (this.isSubmitted) {
            solArea.style.display = 'block';
            solArea.innerHTML = `
                <strong>Correct Answer:</strong> ${q.finalAnswer}<br><br>
                <strong>Solution Steps:</strong>
                <ul>${q.solutionSteps.map(s => `<li>${s}</li>`).join('')}</ul>
            `;
            // Disable inputs
            const inputs = inputArea.querySelectorAll('textarea, .mcq-option');
            inputs.forEach(el => {
                el.style.pointerEvents = 'none';
                if (el.tagName === 'TEXTAREA') el.readOnly = true;
            });
        } else {
            solArea.style.display = 'none';
        }

        this.updatePalette();
        this.updateNavButtons();
        
        // Re-render MathJax
        if (window.MathJax && window.MathJax.typesetPromise) {
            MathJax.typesetPromise([
                document.getElementById('qText'),
                document.getElementById('inputArea'),
                document.getElementById('solutionArea')
            ]).catch(err => console.warn('MathJax error:', err));
        }

        // Scroll to top of question panel (helpful for mobile)
        const panel = document.querySelector('.question-panel');
        if (panel) panel.scrollTop = 0;
    }

    selectOption(qId, optionIndex, element) {
        if (this.isSubmitted) return;
        this.answers[qId] = optionIndex;
        this.saveState();
        
        // UI Update
        const options = document.querySelectorAll('.mcq-option');
        options.forEach(o => o.classList.remove('selected'));
        element.classList.add('selected');
        
        this.updatePalette();
    }

    renderPalette() {
        const palette = document.getElementById('questionPalette');
        palette.innerHTML = '';
        this.config.questions.forEach((q, i) => {
            const btn = document.createElement('button');
            btn.className = 'palette-btn';
            btn.textContent = i + 1;
            btn.onclick = () => this.loadQuestion(i);
            btn.id = `palette-${i}`;
            palette.appendChild(btn);
        });
    }

    updatePalette() {
        this.config.questions.forEach((q, i) => {
            const btn = document.getElementById(`palette-${i}`);
            if (!btn) return;
            
            btn.className = 'palette-btn';
            if (i === this.currentQuestionIndex) btn.classList.add('active');
            
            const hasAnswer = this.answers[q.id] !== undefined && this.answers[q.id] !== '';
            if (hasAnswer) btn.classList.add('answered');
            else if (this.visited.has(i)) btn.classList.add('visited');
        });
    }

    updateNavButtons() {
        document.getElementById('btnPrev').disabled = this.currentQuestionIndex === 0;
        const nextBtn = document.getElementById('btnNext');
        if (this.currentQuestionIndex === this.config.questions.length - 1) {
            nextBtn.textContent = this.isSubmitted ? 'Finish' : 'Submit Test';
            nextBtn.classList.add('btn-submit');
        } else {
            nextBtn.textContent = 'Next';
            nextBtn.classList.remove('btn-submit');
        }
    }

    attachEventListeners() {
        document.getElementById('btnPrev').onclick = () => {
            if (this.currentQuestionIndex > 0) this.loadQuestion(this.currentQuestionIndex - 1);
        };
        document.getElementById('btnNext').onclick = () => {
            if (this.currentQuestionIndex < this.config.questions.length - 1) {
                this.loadQuestion(this.currentQuestionIndex + 1);
            } else {
                if (!this.isSubmitted) this.submitTest();
                else window.location.href = this.config.exitUrl || '../index.html';
            }
        };
    }

    submitTest() {
        clearInterval(this.timerInterval);
        this.isSubmitted = true;
        this.saveState();
        
        this.showResultModal();
        
        // Refresh current question to show solutions immediately
        this.loadQuestion(this.currentQuestionIndex);
    }

    showResultModal() {
        let scoreInfo = { score: 0, total: 0 };
        
        // Calculate Score
        this.config.questions.forEach(q => {
            if (q.type === 'mcq') {
                scoreInfo.total += (q.marks || 1);
                const ans = this.answers[q.id];
                const match = q.finalAnswer && q.finalAnswer.match(/\(([a-z])\)/i);
                if (match && ans !== undefined) {
                    const correctIdx = match[1].toLowerCase().charCodeAt(0) - 97;
                    if (parseInt(ans) === correctIdx) scoreInfo.score += (q.marks || 1);
                }
            }
        });

        const modal = document.getElementById('resultModal');
        modal.style.display = 'flex';
        document.querySelector('.score-text').textContent = `${scoreInfo.score} / ${scoreInfo.total}`;
        document.getElementById('resultMessage').innerHTML = `
            <h3>Test Submitted!</h3>
            <p>You have completed this test.<br>Review the solutions below.</p>
        `;
    }

    injectResetButton() {
        const header = document.querySelector('.test-header');
        if (!header) return;

        const btn = document.createElement('button');
        btn.textContent = 'Reset';
        btn.className = 'btn-reset';
        btn.onclick = () => {
            if (confirm('Reset test progress? This will clear your answers.')) {
                localStorage.removeItem(this.storageKey);
                window.location.reload();
            }
        };
        
        if (header.lastElementChild) {
            header.insertBefore(btn, header.lastElementChild);
        } else {
            header.appendChild(btn);
        }
    }
}

// Global function for modal
window.closeResult = function() {
    document.getElementById('resultModal').style.display = 'none';
    // Trigger a refresh of the current question to show solutions
    const currentBtn = document.querySelector('.palette-btn.active');
    if(currentBtn) currentBtn.click();
};