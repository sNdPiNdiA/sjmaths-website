/**
 * Guided Slide Deck (Minimal Scroll Study Deck) for SJMaths Chapter Notes
 * Supports keyboard navigation, tab switching, and mode toggling.
 */
(function() {
    let currentSlide = 0;
    let slides = [];
    let slideMeta = [];

    function initSlideDeck() {
        slides = Array.from(document.querySelectorAll('main .sj-card, .content-wrapper .note-section, .sj-container .sj-card, .sj-container section.sj-card'));
        if (slides.length === 0) return;

        const mainEl = document.querySelector('main') || document.querySelector('.content-wrapper') || document.querySelector('.sj-container');
        if (!mainEl) return;

        // Auto-detect Chapter Title
        const h1 = document.querySelector('h1');
        const chapterTitle = h1 ? h1.textContent.trim() : (document.title.split('|')[0].trim());

        // 1. Check preference or default to 'slide'
        const savedMode = localStorage.getItem('sjmaths_notes_mode') || 'slide';
        document.body.classList.add(savedMode === 'scroll' ? 'mode-scroll' : 'mode-slide');

        // 2. Inject Top Controls (Mode Bar, Header, Progress Track) if absent
        if (!document.getElementById('slideDeckHeader')) {
            const firstCard = slides[0];
            const topControls = document.createElement('div');
            topControls.id = 'slideDeckAutoTop';
            topControls.innerHTML = `
                <!-- VIEW MODE TOGGLE BAR -->
                <div class="notes-view-mode-bar">
                    <div style="font-size: 0.82rem; font-weight: 700; color: var(--slide-muted);">
                        <i class="fas fa-compass" style="color: var(--slide-accent);"></i> STUDY MODE
                    </div>
                    <div class="view-mode-toggle" id="viewModeToggle">
                        <button type="button" class="mode-btn ${savedMode !== 'scroll' ? 'active' : ''}" id="btnModeSlide" onclick="setNotesViewMode('slide')">
                            <i class="fas fa-layer-group"></i> 🎯 Slide Deck (Min Scroll)
                        </button>
                        <button type="button" class="mode-btn ${savedMode === 'scroll' ? 'active' : ''}" id="btnModeScroll" onclick="setNotesViewMode('scroll')">
                            <i class="fas fa-align-left"></i> 📜 Full Scroll
                        </button>
                    </div>
                </div>

                <!-- SLIDE DECK TOP FRAME -->
                <div class="slide-deck-header" id="slideDeckHeader">
                    <div class="slide-deck-top-row">
                        <div class="slide-deck-title">
                            <i class="fas fa-graduation-cap"></i>
                            <span>${chapterTitle} &mdash; Quick Master Deck</span>
                        </div>
                        <div class="slide-dot-indicators" id="slideDotContainer"></div>
                    </div>
                    <!-- Horizontal Module Tabs Strip -->
                    <div class="slide-tabs-strip" id="slideTabsStrip"></div>
                </div>

                <!-- Progress Track Bar with Navigation Chevrons -->
                <div class="slide-track-bar" id="slideTrackBar">
                    <button type="button" class="slide-track-nav-btn" id="trackPrevBtn" onclick="navigateSlide(-1)" title="Previous (Left Arrow)">
                        <i class="fas fa-chevron-left"></i>
                    </button>
                    <div class="slide-track-meter">
                        <div class="slide-track-meter-fill" id="slideTrackFill"></div>
                    </div>
                    <button type="button" class="slide-track-nav-btn" id="trackNextBtn" onclick="navigateSlide(1)" title="Next (Right Arrow)">
                        <i class="fas fa-chevron-right"></i>
                    </button>
                </div>
            `;
            firstCard.parentNode.insertBefore(topControls, firstCard);
        }

        // 3. Inject Bottom Footer Controls if absent
        if (!document.getElementById('slideDeckFooter')) {
            const footerEl = document.createElement('div');
            footerEl.className = 'slide-deck-footer';
            footerEl.id = 'slideDeckFooter';
            footerEl.innerHTML = `
                <button type="button" class="slide-deck-btn prev-btn" id="footerPrevBtn" onclick="navigateSlide(-1)">
                    <i class="fas fa-arrow-left"></i> Previous
                </button>
                <div style="text-align: center;">
                    <div class="slide-counter-badge" id="slideCounterText">Section <strong>1</strong> of <strong>${slides.length}</strong></div>
                    <div class="slide-key-hint" style="margin-top: 2px;">
                        Use <kbd>&larr;</kbd> <kbd>&rarr;</kbd> keys to flip
                    </div>
                </div>
                <button type="button" class="slide-deck-btn next-btn" id="footerNextBtn" onclick="navigateSlide(1)">
                    Next <i class="fas fa-arrow-right"></i>
                </button>
            `;
            mainEl.appendChild(footerEl);
        }

        // Build metadata from each card
        slideMeta = slides.map((card, idx) => {
            const stepNum = card.getAttribute('data-step') || ('0' + (idx + 1));
            const h2 = card.querySelector('h2');
            let title = h2 ? h2.textContent.replace(/[\u{1F300}-\u{1F9FF}]|[\u{2600}-\u{26FF}]|[\u{2700}-\u{27BF}]/gu, '').trim() : ('Module ' + stepNum);
            
            // Clean up long prefixes or board indicators
            title = title.replace(/^(\d+\.?\s*|Section\s*\d+:?\s*)/i, '').trim();

            // Intelligent shortening for tab pills
            if (title.toLowerCase().includes('weightage') || title.toLowerCase().includes('blueprint')) title = 'Blueprint';
            else if (title.toLowerCase().includes('basic') || title.toLowerCase().includes('concept')) title = 'Basics & Concepts';
            else if (title.toLowerCase().includes('formula') || title.toLowerCase().includes('identity') || title.toLowerCase().includes('theorems')) title = 'Key Formulas';
            else if (title.toLowerCase().includes('solved') || title.toLowerCase().includes('example') || title.toLowerCase().includes('pyq')) title = 'Solved Examples';
            else if (title.toLowerCase().includes('strategy') || title.toLowerCase().includes('mistake') || title.toLowerCase().includes('pitfall')) title = 'Mistake Bank';
            else if (title.toLowerCase().includes('assessment') || title.toLowerCase().includes('mock')) title = 'Mock Test';
            else if (title.toLowerCase().includes('graph')) title = 'Graphical Study';
            else if (title.toLowerCase().includes('checklist') || title.toLowerCase().includes('summary') || title.toLowerCase().includes('revision')) title = 'Checklist';
            else if (title.toLowerCase().includes('quiz')) title = 'Quiz';
            else if (title.length > 22) title = title.substring(0, 20) + '…';

            return { stepNum, title };
        });

        updateModeButtons(savedMode);

        // 4. Populate Slide Dots
        const dotContainer = document.getElementById('slideDotContainer');
        if (dotContainer) {
            dotContainer.innerHTML = slides.map((_, i) => 
                `<span class="slide-dot ${i === 0 ? 'active' : ''}" onclick="goToSlide(${i})" title="Slide ${i+1}"></span>`
            ).join('');
        }

        // 5. Populate Slide Tabs Strip
        const tabsStrip = document.getElementById('slideTabsStrip');
        if (tabsStrip) {
            tabsStrip.innerHTML = slideMeta.map((meta, i) =>
                `<button type="button" class="slide-tab-pill ${i === 0 ? 'active' : ''}" onclick="goToSlide(${i})">
                    <span class="slide-tab-num">${meta.stepNum}</span>
                    <span>${meta.title}</span>
                </button>`
            ).join('');
        }

        // 4. Activate initial slide (check URL hash or start at 0)
        let initialIndex = 0;
        if (window.location.hash && window.location.hash.startsWith('#slide-')) {
            const idx = parseInt(window.location.hash.replace('#slide-', ''), 10) - 1;
            if (!isNaN(idx) && idx >= 0 && idx < slides.length) initialIndex = idx;
        }

        goToSlide(initialIndex, false);

        // 5. Setup keyboard arrow navigation
        window.addEventListener('keydown', function(e) {
            if (!document.body.classList.contains('mode-slide')) return;
            // Ignore if typing inside input
            if (['INPUT', 'TEXTAREA'].includes(document.activeElement.tagName)) return;

            if (e.key === 'ArrowRight' || e.key === 'PageDown') {
                e.preventDefault();
                navigateSlide(1);
            } else if (e.key === 'ArrowLeft' || e.key === 'PageUp') {
                e.preventDefault();
                navigateSlide(-1);
            }
        });
    }

    window.goToSlide = function(index, scrollUp = true) {
        if (!slides || slides.length === 0) return;
        if (index < 0) index = 0;
        if (index >= slides.length) index = slides.length - 1;

        currentSlide = index;

        // Toggle active card
        slides.forEach((card, i) => {
            if (i === currentSlide) {
                card.classList.add('active-slide');
                // Ensure card animations are visible
                card.classList.add('anim-visible');
                const content = card.querySelector('.card-content');
                if (content) content.classList.add('anim-visible');
            } else {
                card.classList.remove('active-slide');
            }
        });

        // Update Dots
        const dots = document.querySelectorAll('.slide-dot');
        dots.forEach((dot, i) => {
            dot.classList.toggle('active', i === currentSlide);
        });

        // Update Tab Pills
        const pills = document.querySelectorAll('.slide-tab-pill');
        pills.forEach((pill, i) => {
            const isActive = i === currentSlide;
            pill.classList.toggle('active', isActive);
            if (isActive && pill.scrollIntoView) {
                pill.scrollIntoView({ behavior: 'smooth', block: 'nearest', inline: 'center' });
            }
        });

        // Update Progress Meter
        const fill = document.getElementById('slideTrackFill');
        if (fill) {
            const pct = ((currentSlide + 1) / slides.length) * 100;
            fill.style.width = pct + '%';
        }

        // Update Counter Text
        const counter = document.getElementById('slideCounterText');
        if (counter) {
            counter.innerHTML = `Section <strong>${currentSlide + 1}</strong> of <strong>${slides.length}</strong>`;
        }

        // Class 9 Chapters Navigation (Rendered at bottom of last slide)
        const isClass9 = window.location.pathname.includes('/class-9-maths/');
        const class9Nav = document.getElementById('slideChapterNavClass9');
        if (isClass9) {
            if (!class9Nav) {
                const class9Chapters = [
                    { num: 1, name: "The Use of Coordinates", slug: "chapter-1-use-of-coordinates" },
                    { num: 2, name: "Linear Polynomials", slug: "chapter-2-linear-polynomials" },
                    { num: 3, name: "The World of Numbers", slug: "chapter-3-world-of-numbers" },
                    { num: 4, name: "Algebraic Identities", slug: "chapter-4-algebraic-identities" },
                    { num: 5, name: "Circles", slug: "chapter-5-circles" },
                    { num: 6, name: "Perimeter and Area", slug: "chapter-6-perimeter-and-area" },
                    { num: 7, name: "Probability", slug: "chapter-7-probability" },
                    { num: 8, name: "Sequences & Progressions", slug: "chapter-8-sequences-and-progressions" },
                    { num: 9, name: "Triangles", slug: "chapter-9-triangles" },
                    { num: 10, name: "Heron's Formula", slug: "chapter-10-herons-formula" },
                    { num: 11, name: "Surface Areas & Volumes", slug: "chapter-11-surface-areas-and-volumes" },
                    { num: 12, name: "Statistics", slug: "chapter-12-statistics" }
                ];

                const currentSlug = window.location.pathname.split('/').filter(Boolean).pop();
                const curIdx = class9Chapters.findIndex(c => c.slug === currentSlug);

                if (curIdx !== -1) {
                    const prevCh = curIdx > 0 ? class9Chapters[curIdx - 1] : null;
                    const nextCh = curIdx < class9Chapters.length - 1 ? class9Chapters[curIdx + 1] : null;

                    const lastCard = slides[slides.length - 1];
                    const navBox = document.createElement('div');
                    navBox.id = 'slideChapterNavClass9';
                    navBox.className = 'slide-chapter-nav';
                    navBox.innerHTML = `
                        <div>
                            ${prevCh ? `<a href="/class-9-maths/chapter-wise-notes/${prevCh.slug}/" class="slide-chapter-nav-btn prev">
                                <i class="fas fa-arrow-left"></i> Ch ${prevCh.num}: ${prevCh.name}
                            </a>` : `<a href="/class-9-maths/chapter-wise-notes/" class="slide-chapter-nav-btn overview">
                                <i class="fas fa-th-large"></i> Class 9 Chapters
                            </a>`}
                        </div>
                        <div style="font-size:0.85rem; font-weight:700; color:var(--slide-muted);">
                            <i class="fas fa-flag-checkered" style="color:var(--slide-accent);"></i> Chapter Completed
                        </div>
                        <div>
                            ${nextCh ? `<a href="/class-9-maths/chapter-wise-notes/${nextCh.slug}/" class="slide-chapter-nav-btn next">
                                Next Ch ${nextCh.num}: ${nextCh.name} <i class="fas fa-arrow-right"></i>
                            </a>` : `<a href="/class-9-maths/chapter-wise-notes/" class="slide-chapter-nav-btn next">
                                All Class 9 Notes <i class="fas fa-check-circle"></i>
                            </a>`}
                        </div>
                    `;
                    lastCard.appendChild(navBox);
                }
            }
        }

        // Update Prev / Next Buttons disabled state
        const prevBtns = [document.getElementById('trackPrevBtn'), document.getElementById('footerPrevBtn')];
        const nextBtns = [document.getElementById('trackNextBtn'), document.getElementById('footerNextBtn')];

        prevBtns.forEach(btn => { if (btn) btn.disabled = (currentSlide === 0); });
        nextBtns.forEach(btn => { if (btn) btn.disabled = (currentSlide === slides.length - 1); });

        // Update URL hash without jumping page
        if (history.replaceState) {
            history.replaceState(null, null, '#slide-' + (currentSlide + 1));
        }

        // Smooth scroll viewport top if requested
        if (scrollUp) {
            const topBar = document.getElementById('slideDeckHeader');
            if (topBar) {
                const rect = topBar.getBoundingClientRect();
                if (rect.top < 0 || rect.top > 250) {
                    topBar.scrollIntoView({ behavior: 'smooth', block: 'start' });
                }
            }
        }
    };

    window.navigateSlide = function(delta) {
        goToSlide(currentSlide + delta, true);
    };

    window.setNotesViewMode = function(mode) {
        if (mode === 'scroll') {
            document.body.classList.remove('mode-slide');
            document.body.classList.add('mode-scroll');
            localStorage.setItem('sjmaths_notes_mode', 'scroll');
            updateModeButtons('scroll');
        } else {
            document.body.classList.remove('mode-scroll');
            document.body.classList.add('mode-slide');
            localStorage.setItem('sjmaths_notes_mode', 'slide');
            updateModeButtons('slide');
            goToSlide(currentSlide, false);
        }
    };

    function updateModeButtons(mode) {
        const btnSlide = document.getElementById('btnModeSlide');
        const btnScroll = document.getElementById('btnModeScroll');
        if (btnSlide && btnScroll) {
            btnSlide.classList.toggle('active', mode === 'slide');
            btnScroll.classList.toggle('active', mode === 'scroll');
        }
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initSlideDeck);
    } else {
        initSlideDeck();
    }
})();
