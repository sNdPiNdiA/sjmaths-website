/**
 * class-11-notes.js  •  SJMaths Class 11
 * Shared Class 11 note functionality:
 *   MathJax overflow handling · accordions · calculators · quizzes.
 */
(function () {
    'use strict';

    /* ── Boot ──────────────────────────────── */
    document.addEventListener('DOMContentLoaded', () => {
        _initWidgetInteractions();

        // Delay MathJax check slightly to allow layout to settle
        setTimeout(() => {
            _wrapMathJax();
        }, 300);
    });


    /* Also wrap MathJax after it finishes rendering */
    if (window.MathJax) {
        const origReady = window.MathJax.startup?.ready;
        if (origReady) {
            window.MathJax.startup.ready = () => {
                origReady();
                // Batch wrap to avoid thrashing
                setTimeout(_wrapMathJax, 500);
            };
        } else {
            document.addEventListener('DOMContentLoaded', () => {
                setTimeout(_wrapMathJax, 2000);
            });
        }
    }

    /* ═══════════════════════════════════════════
       §1  MATHJAX SCROLL WRAPPER (Optimized)
       Batched reads/writes to prevent layout thrashing.
       ═══════════════════════════════════════════ */
    function _wrapMathJax() {
        // Collect all candidates first
        const displayMath = Array.from(document.querySelectorAll('mjx-container[display="true"]'));
        const inlineMath = Array.from(document.querySelectorAll('mjx-container:not([display="true"])'));

        const toWrap = [];

        // 1. READ PHASE: Measure without modifying DOM
        // Display math is always wrapped for consistent styling
        displayMath.forEach(el => toWrap.push({ el, type: 'display' }));

        // Inline math: check if it actually overflows
        inlineMath.forEach(el => {
            // Only wrap if significantly overflowing (tolerance 2px)
            // Combined with current clientWidth to avoid layout cycles
            const sw = el.scrollWidth;
            const cw = el.clientWidth;
            if (sw > cw + 2) {
                toWrap.push({ el, type: 'inline' });
            }
        });

        // 2. WRITE PHASE: Modify DOM in single batch
        if (toWrap.length > 0) {
            requestAnimationFrame(() => {
                toWrap.forEach(item => _wrapEl(item.el, item.type));

                // 3. POST-WRITE READ PHASE: Check overflow after some delay
                // to avoid immediate thrashing in the same frame
                setTimeout(() => {
                    requestAnimationFrame(() => {
                        document.querySelectorAll('.math-scroll').forEach(wrapper => {
                            if (wrapper.scrollWidth > wrapper.clientWidth) {
                                wrapper.classList.add('has-overflow');
                            }
                        });
                    });
                }, 100);
            });
        }
    }


    function _wrapEl(container, type) {
        // Skip if already wrapped
        if (container.parentElement?.classList.contains('math-scroll')) return;

        const wrapper = document.createElement('div');
        wrapper.className = 'math-scroll';

        // Apply appropriate display mode
        if (type === 'display') {
            wrapper.style.display = 'block';
        } else {
            wrapper.style.display = 'inline-block';
            wrapper.style.verticalAlign = 'middle';
            wrapper.style.maxWidth = '100%';
        }

        container.parentNode.insertBefore(wrapper, container);
        wrapper.appendChild(container);
    }


    /* ═══════════════════════════════════════════
       §6  WIDGET INTERACTIONS
       ═══════════════════════════════════════════ */
    function _initWidgetInteractions() {
        // Copy button
        document.querySelectorAll('.result-panel').forEach(panel => {
            const btn = document.createElement('button');
            btn.className = 'copy-btn';
            btn.innerHTML = '<i class="far fa-copy"></i>';
            btn.title = 'Copy Result';
            panel.style.position = 'relative';
            panel.appendChild(btn);

            btn.addEventListener('click', () => {
                const text = panel.textContent.replace('\uf0c5', '').trim();
                navigator.clipboard.writeText(text).then(() => {
                    btn.innerHTML = '<i class="fas fa-check"></i>';
                    btn.style.background = 'var(--success)';
                    btn.style.color = '#fff';
                    setTimeout(() => {
                        btn.innerHTML = '<i class="far fa-copy"></i>';
                        btn.style.background = '';
                        btn.style.color = '';
                    }, 2000);
                });
            });
        });

        // Ripple
        document.querySelectorAll('.calc-btn, .nav-btn, .quiz-option').forEach(el => {
            el.addEventListener('click', function (e) {
                const ripple = document.createElement('span');
                ripple.className = 'ripple';
                this.appendChild(ripple);
                const d = Math.max(this.clientWidth, this.clientHeight);
                ripple.style.width = ripple.style.height = d + 'px';
                ripple.style.left = (e.offsetX - d / 2) + 'px';
                ripple.style.top = (e.offsetY - d / 2) + 'px';
                setTimeout(() => ripple.remove(), 600);
            });
        });
    }

    /* ═══════════════════════════════════════════
       §10  ACCORDION  (Global)
       ═══════════════════════════════════════════ */
    window.toggleAccordion = function (header) {
        const body = header.nextElementSibling;
        if (!body) return;
        const isOpen = body.classList.contains('open');

        const parent = header.closest('.note-section') || header.parentElement?.parentElement;
        if (parent) {
            parent.querySelectorAll('.accordion-body.open').forEach(other => {
                if (other !== body) {
                    other.classList.remove('open');
                    other.style.maxHeight = null;
                    const h = other.previousElementSibling;
                    if (h) {
                        h.classList.remove('active');
                        h.setAttribute('aria-expanded', 'false');
                    }
                }
            });
        }

        if (isOpen) {
            body.classList.remove('open');
            body.style.maxHeight = null;
            header.classList.remove('active');
            header.setAttribute('aria-expanded', 'false');
        } else {
            // Read height first to avoid forced reflow
            const height = body.scrollHeight;

            // Ensure display is reset in case inline styles blocked it
            body.style.display = '';
            body.classList.add('open');
            header.classList.add('active');
            header.setAttribute('aria-expanded', 'true');
            // Set dynamic height for transition (with buffer)
            body.style.maxHeight = (height + 40) + "px";
        }
    };

    /* ═══════════════════════════════════════════
       §11  TAB SWITCHER  (Global)
       ═══════════════════════════════════════════ */
    let _mathTypesetQueue = Promise.resolve();
    window.sjTypesetMath = function (elements) {
        const run = () => new Promise(resolve => {
            const started = performance.now();
            const waitForMathJax = () => {
                if (window.MathJax?.typesetPromise) {
                    const ready = window.MathJax.startup?.promise || Promise.resolve();
                    ready
                        .then(() => elements
                            ? window.MathJax.typesetPromise([elements])
                            : window.MathJax.typesetPromise())
                        .then(resolve)
                        .catch(error => {
                            console.error('SJMaths MathJax update failed:', error);
                            resolve();
                        });
                    return;
                }

                if (performance.now() - started >= 5000) {
                    resolve();
                    return;
                }

                setTimeout(waitForMathJax, 50);
            };

            waitForMathJax();
        });

        _mathTypesetQueue = _mathTypesetQueue.then(run, run);
        return _mathTypesetQueue;
    };

    // Keep page-owned tab handlers intact. Chapter-note pages define their
    // resource switcher before this deferred shared script executes.
    if (typeof window.switchTab !== 'function') {
        window.switchTab = function (tabId) {
            document.querySelectorAll('.tab-content').forEach(t => t.classList.remove('active'));
            document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));

            const target = document.getElementById(tabId);
            if (target) target.classList.add('active');

            document.querySelectorAll('.tab-btn').forEach(b => {
                if (b.getAttribute('onclick')?.includes(`'${tabId}'`)) {
                    b.classList.add('active');
                }
            });

            window.sjTypesetMath();
        };
    }

    /* ═══════════════════════════════════════════
       §12  QUIZ + CONFETTI  (Global)
       ═══════════════════════════════════════════ */
    window.checkQuiz = function (element, isCorrect) {
        const parent = element.parentElement;
        const options = parent.querySelectorAll('.quiz-option');
        options.forEach(opt => { opt.style.pointerEvents = 'none'; });

        if (isCorrect) {
            element.classList.add('correct', 'pop');
            element.innerHTML += ' <i class="fas fa-check-circle"></i>';
            _burstConfetti(element);
        } else {
            element.classList.add('wrong', 'shake');
            element.innerHTML += ' <i class="fas fa-times-circle"></i>';
            setTimeout(() => {
                const correct = Array.from(options).find(
                    opt => opt.getAttribute('onclick')?.includes('true')
                );
                if (correct && !correct.classList.contains('correct')) {
                    correct.classList.add('correct', 'pop');
                    correct.innerHTML += ' <i class="fas fa-check-circle"></i>';
                }
            }, 600);
        }
    };

    function _burstConfetti(anchor) {
        const colors = ['#10b981', '#f59e0b', '#7c3aed', '#ef4444', '#3b82f6', '#ec4899'];
        const rect = anchor.getBoundingClientRect();
        const cx = rect.left + rect.width / 2;
        const cy = rect.top + rect.height / 2;

        for (let i = 0; i < 24; i++) {
            const dot = document.createElement('div');
            const angle = (Math.PI * 2 * i) / 24;
            const dist = Math.random() * 100 + 40;
            const color = colors[Math.floor(Math.random() * colors.length)];
            const size = (Math.random() * 8 + 4) + 'px';

            Object.assign(dot.style, {
                position: 'fixed',
                left: cx + 'px',
                top: cy + 'px',
                width: size,
                height: size,
                borderRadius: Math.random() > 0.4 ? '50%' : '3px',
                background: color,
                pointerEvents: 'none',
                zIndex: '9999',
                transition: 'all 1s cubic-bezier(0.2, 0.6, 0.4, 1)',
                opacity: '1',
                boxShadow: `0 0 6px ${color}`
            });

            document.body.appendChild(dot);

            requestAnimationFrame(() => {
                dot.style.left = (cx + Math.cos(angle) * dist) + 'px';
                dot.style.top = (cy + Math.sin(angle) * dist - 40) + 'px';
                dot.style.opacity = '0';
                dot.style.transform = `scale(0) rotate(${Math.random() * 540}deg)`;
            });

            setTimeout(() => dot.remove(), 1200);
        }
    }

})();
