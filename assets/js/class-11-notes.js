/**
 * class-11-notes.js  •  SJMaths Class 11
 * World-Class Interactivity:
 *   3D Card Tilt · Multi-direction Reveals · MathJax Scroll Wrapper
 *   Adaptive Header · Floating TOC · Confetti · Parallax Depth
 */
(function () {
    'use strict';

    /* ── Single throttled scroll handler ──── */
    let _raf = null;
    const _scrollFns = [];
    let _totalScrollHeight = 0;
    const _headingsOffsetMap = [];

    function _onScroll() {
        if (_raf) return;
        _raf = requestAnimationFrame(() => {
            const sy = window.scrollY;
            _scrollFns.forEach(fn => fn(sy));
            _raf = null;
        });
    }

    function onScroll(fn) { _scrollFns.push(fn); }

    function _updateCachedDimensions() {
        _totalScrollHeight = document.documentElement.scrollHeight - window.innerHeight;

        // Refresh TOC offsets
        const headings = document.querySelectorAll('.note-section h2');
        _headingsOffsetMap.length = 0;
        headings.forEach((h, i) => {
            // Ensure ID exists (in case TOC init didn't run or missed it)
            if (!h.id) h.id = `section-${i}`;

            // Get absolute offset from top of document
            const rect = h.getBoundingClientRect();
            const absoluteTop = rect.top + window.scrollY;
            _headingsOffsetMap.push({ id: h.id, offset: absoluteTop });
        });

        // Sort by offset just in case
        _headingsOffsetMap.sort((a, b) => a.offset - b.offset);
    }



    /* ── Boot ──────────────────────────────── */
    document.addEventListener('DOMContentLoaded', () => {
        _initAdaptiveHeader();
        _initMultiReveal();
        _initProgressBar();
        _initScrollToTop();
        _addReadingTime();
        _initFloatingTOC();
        _initFloatingControls();
        _initWidgetInteractions();
        _init3DTilt();

        // Initial cache update
        _updateCachedDimensions();

        // Delay MathJax check slightly to allow layout to settle
        setTimeout(() => {
            _wrapMathJax();
            _updateCachedDimensions(); // Re-cache after MathJax possible expansion
        }, 300);

        window.addEventListener('scroll', _onScroll, { passive: true });
        window.addEventListener('resize', _updateCachedDimensions, { passive: true });
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
       §2  ADAPTIVE HEADER
       ═══════════════════════════════════════════ */
    function _initAdaptiveHeader() {
        const header = document.querySelector('header') || document.getElementById('site-header');
        if (!header) return;
        onScroll(sy => header.classList.toggle('scrolled', sy > 50));
    }

    /* ═══════════════════════════════════════════
       §3  MULTI-DIRECTION REVEAL
       Cards fly in from different angles for variety
       ═══════════════════════════════════════════ */
    function _initMultiReveal() {
        const variants = ['reveal-up', 'reveal-up', 'reveal-left', 'reveal-right', 'reveal-zoom', 'reveal-rotate'];

        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('active');
                    observer.unobserve(entry.target);
                }
            });
        }, {
            threshold: 0.06,
            rootMargin: '0px 0px -30px 0px'
        });

        const targets = document.querySelectorAll(
            '.note-section, .calc-box, .accordion-item, .quiz-container, .table-container'
        );

        targets.forEach((el, i) => {
            const variant = variants[i % variants.length];
            el.classList.add('reveal', variant);
            el.style.transitionDelay = `${(i % 4) * 0.08}s`;
            observer.observe(el);
        });
    }

    /* ═══════════════════════════════════════════
       §4  PROGRESS BAR + PERCENTAGE
       ═══════════════════════════════════════════ */
    function _initProgressBar() {
        const container = document.querySelector('.progress-container');
        const bar = document.getElementById('progressBar');
        if (!container || !bar) return;

        const perc = document.createElement('span');
        perc.className = 'progress-perc';
        container.appendChild(perc);

        onScroll(sy => {
            if (_totalScrollHeight <= 0) return;
            const pct = Math.min(Math.round((sy / _totalScrollHeight) * 100), 100);
            bar.style.width = pct + '%';
            perc.textContent = pct + '%';
            perc.style.opacity = pct > 1 ? '1' : '0';
        });

    }

    /* ═══════════════════════════════════════════
       §5  FLOATING TABLE OF CONTENTS
       ═══════════════════════════════════════════ */
    function _initFloatingTOC() {
        const headings = document.querySelectorAll('.note-section h2');
        if (headings.length < 2) return;

        const toc = document.createElement('nav');
        toc.className = 'floating-toc';
        toc.id = 'floatingToC';

        const list = document.createElement('ul');

        // TOC Header with Close button
        const header = document.createElement('div');
        header.className = 'toc-header';
        header.innerHTML = `<span>Quick Nav</span><i class="fas fa-times" id="closeToC"></i>`;
        toc.appendChild(header);

        headings.forEach((h, i) => {
            if (!h.id) h.id = `section-${i}`;
            const id = h.id;

            const li = document.createElement('li');
            const a = document.createElement('a');
            a.href = `#${id}`;
            let text = h.textContent.replace(/^Step \d+:/, '').replace(/^Q\d+\./, '').trim();
            if (text.length > 35) text = text.substring(0, 32) + '...';

            a.innerHTML = `<span class="toc-num">${i + 1}</span><span class="toc-text">${text}</span>`;

            a.addEventListener('click', e => {
                e.preventDefault();
                const target = document.getElementById(id);
                const headerOffset = 100;
                const elementPosition = target.getBoundingClientRect().top;
                const offsetPosition = elementPosition + window.scrollY - headerOffset;

                window.scrollTo({
                    top: offsetPosition,
                    behavior: "smooth"
                });

                // Hide TOC after clicking on mobile or small screens
                if (window.innerWidth < 1200) {
                    toc.classList.remove('active');
                }
            });

            li.appendChild(a);
            list.appendChild(li);
        });

        toc.appendChild(list);
        document.body.appendChild(toc);

        // Add Toggle Button
        const toggleBtn = document.createElement('div');
        toggleBtn.className = 'toc-toggle';
        toggleBtn.id = 'tocToggle';
        toggleBtn.innerHTML = '<i class="fas fa-list-ul"></i>';
        toggleBtn.title = "Table of Contents";
        document.body.appendChild(toggleBtn);

        // Toggle logic
        const toggle = () => toc.classList.toggle('active');
        toggleBtn.addEventListener('click', toggle);
        header.querySelector('#closeToC').addEventListener('click', toggle);

        const links = toc.querySelectorAll('a');
        onScroll(sy => {
            let currentId = '';
            for (let i = 0; i < _headingsOffsetMap.length; i++) {
                if (sy >= _headingsOffsetMap[i].offset - 150) {
                    currentId = _headingsOffsetMap[i].id;
                } else {
                    break;
                }
            }
            links.forEach(link => {
                link.classList.toggle('active', link.getAttribute('href') === `#${currentId}`);
            });
        });

    }

    /* ═══════════════════════════════════════════
       §5.5  FLOATING CONTROLS (Back Button)
       ═══════════════════════════════════════════ */
    function _initFloatingControls() {
        if (document.querySelector('.floating-controls')) return;

        const div = document.createElement('div');
        div.className = 'floating-controls';
        // Class 12 style: includes span (text hidden by CSS usually but keeps DOM structure)
        div.innerHTML = `
            <a href="../" class="back-btn-floating" aria-label="Back to Chapters">
                <i class="fas fa-arrow-left"></i> <span>Back</span>
            </a>
        `;
        document.body.appendChild(div);
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
       §7  3D TILT ON NOTE SECTIONS
       Mouse-follow perspective tilt for premium feel
       ═══════════════════════════════════════════ */
    function _init3DTilt() {
        if (window.innerWidth < 768) return; // Disable on mobile

        document.querySelectorAll('.note-section').forEach(card => {
            card.classList.add('tilt-card');
            let rect = null;

            card.addEventListener('mouseenter', () => {
                rect = card.getBoundingClientRect();
            });

            card.addEventListener('mousemove', e => {
                if (!rect) rect = card.getBoundingClientRect();
                const x = e.clientX - rect.left;
                const y = e.clientY - rect.top;
                const centerX = rect.width / 2;
                const centerY = rect.height / 2;
                const rotateX = ((y - centerY) / centerY) * -3;
                const rotateY = ((x - centerX) / centerX) * 3;

                card.style.transform = `perspective(1000px) rotateX(${rotateX}deg) rotateY(${rotateY}deg) translateY(-6px)`;
            });

            card.addEventListener('mouseleave', () => {
                card.style.transform = '';
                rect = null;
            });
        });

    }

    /* ═══════════════════════════════════════════
       §8  SCROLL-TO-TOP BUTTON
       ═══════════════════════════════════════════ */
    function _initScrollToTop() {
        const btn = document.createElement('button');
        btn.className = 'scroll-top-btn';
        btn.setAttribute('aria-label', 'Scroll to top');
        btn.innerHTML = '<i class="fas fa-arrow-up"></i>';
        document.body.appendChild(btn);

        onScroll(sy => btn.classList.toggle('visible', sy > 400));

        btn.addEventListener('click', () => {
            window.scrollTo({ top: 0, behavior: 'smooth' });
        });
    }

    /* ═══════════════════════════════════════════
       §9  READING TIME
       ═══════════════════════════════════════════ */
    function _addReadingTime() {
        const wrapper = document.querySelector('.content-wrapper');
        const subtitle = document.querySelector('.chapter-subtitle');
        if (!wrapper || !subtitle) return;

        const text = wrapper.innerText || '';
        const words = text.trim().split(/\s+/).length;
        const mins = Math.max(1, Math.ceil(words / 200));

        const badge = document.createElement('div');
        badge.className = 'reading-time';
        badge.innerHTML = `<i class="fas fa-clock"></i> ${mins} min read &nbsp;&middot;&nbsp; <i class="fas fa-book-open"></i> ${words.toLocaleString()} words`;
        badge.style.cssText = 'text-align:center; width:fit-content; margin-left:auto; margin-right:auto; display:block;';
        subtitle.insertAdjacentElement('afterend', badge);
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

        if (window.MathJax) MathJax.typeset();
    };

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
