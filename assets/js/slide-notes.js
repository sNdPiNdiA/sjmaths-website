/**
 * Guided Slide Deck (Minimal Scroll Study Deck) for SJMaths Chapter Notes
 * Supports keyboard navigation, tab switching, and mode toggling.
 */
(function() {
    let currentSlide = 0;
    let slides = [];
    let slideMeta = [];

    // Keep chapter navigation in the reader itself. The reader is shared by all
    // Class 11 chapter-note pages, so this avoids relying on the hidden mobile
    // site header for the next learning destination.
    const class11Chapters = Object.freeze([
        { num: 1, name: 'Sets', slug: 'chapter-1-sets' },
        { num: 2, name: 'Relations and Functions', slug: 'chapter-2-relations-and-functions' },
        { num: 3, name: 'Trigonometric Functions', slug: 'chapter-3-trigonometric-functions' },
        { num: 4, name: 'Complex Numbers and Quadratic Equations', slug: 'chapter-4-complex-numbers-and-quadratic-equations' },
        { num: 5, name: 'Linear Inequalities', slug: 'chapter-5-linear-inequalities' },
        { num: 6, name: 'Permutations and Combinations', slug: 'chapter-6-permutations-and-combinations' },
        { num: 7, name: 'Binomial Theorem', slug: 'chapter-7-binomial-theorem' },
        { num: 8, name: 'Sequences and Series', slug: 'chapter-8-sequences-and-series' },
        { num: 9, name: 'Straight Lines', slug: 'chapter-9-straight-lines' },
        { num: 10, name: 'Conic Sections', slug: 'chapter-10-conic-sections' },
        { num: 11, name: 'Introduction to Three-dimensional Geometry', slug: 'chapter-11-introduction-to-three-dimensional-geometry' },
        { num: 12, name: 'Limits and Derivatives', slug: 'chapter-12-limits-and-derivatives' },
        { num: 13, name: 'Statistics', slug: 'chapter-13-statistics' },
        { num: 14, name: 'Probability', slug: 'chapter-14-probability' }
    ]);

    function getCurrentClass11Chapter() {
        if (!window.location.pathname.includes('/class-11-maths/chapter-wise-notes/')) return null;
        const slug = window.location.pathname.split('/').filter(Boolean).pop();
        const index = class11Chapters.findIndex(chapter => chapter.slug === slug);
        return index === -1 ? null : { index, chapter: class11Chapters[index] };
    }

    function getClass11ChapterNavigation() {
        const current = getCurrentClass11Chapter();
        if (!current) return '';
        const previous = class11Chapters[current.index - 1];
        const next = class11Chapters[current.index + 1];
        const basePath = '/class-11-maths/chapter-wise-notes/';
        const previousLink = previous
            ? `<a href="${basePath}${previous.slug}/"><i class="fas fa-arrow-left" aria-hidden="true"></i><span>Ch ${previous.num}: ${previous.name}</span></a>`
            : `<a href="${basePath}"><i class="fas fa-table-cells-large" aria-hidden="true"></i><span>All Class 11 notes</span></a>`;
        const nextLink = next
            ? `<a href="${basePath}${next.slug}/"><span>Ch ${next.num}: ${next.name}</span><i class="fas fa-arrow-right" aria-hidden="true"></i></a>`
            : `<a href="${basePath}"><span>All Class 11 notes</span><i class="fas fa-check" aria-hidden="true"></i></a>`;

        return `
            <nav class="notebook-chapter-switcher" aria-label="Class 11 chapter navigation">
                <p><i class="fas fa-bookmark" aria-hidden="true"></i> Switch chapter</p>
                <div class="notebook-chapter-links">
                    ${previousLink}
                    ${nextLink}
                </div>
            </nav>`;
    }

    function getSlideTone(title) {
        const value = (title || '').toLowerCase();
        if (/(mistake|pitfall|trap|avoid)/.test(value)) return { id: 'review', label: 'Watch for this', icon: 'fa-shield-halved' };
        if (/(quiz|assessment|mock|practice|test|challenge|exam)/.test(value)) return { id: 'practice', label: 'Try this', icon: 'fa-pen-ruler' };
        if (/(solved|example|application|illustration)/.test(value)) return { id: 'example', label: 'Worked example', icon: 'fa-lightbulb' };
        if (/(formula|identity|theorem|result|properties|rule)/.test(value)) return { id: 'formula', label: 'Key formula', icon: 'fa-swatchbook' };
        if (/(summary|checklist|revision|recap)/.test(value)) return { id: 'revision', label: 'Revision', icon: 'fa-flag-checkered' };
        return { id: 'foundation', label: 'Concept', icon: 'fa-compass' };
    }

    function updateNotebookThemeToggle(isDark = document.body.classList.contains('dark-mode')) {
        const button = document.getElementById('notebookThemeToggle');
        if (!button) return;
        const icon = button.querySelector('i');
        if (icon) icon.className = isDark ? 'fas fa-sun' : 'fas fa-moon';
        button.setAttribute('aria-pressed', String(isDark));
        button.setAttribute('aria-label', isDark ? 'Switch to light notebook' : 'Switch to dark notebook');
        button.title = isDark ? 'Light notebook' : 'Dark notebook';
    }

    // The focused reader hides the legacy site-header controls. Give it its
    // own theme control while delegating to the shared theme API when present.
    window.toggleNotebookTheme = function() {
        if (typeof window.toggleDarkMode === 'function') {
            const isDark = window.toggleDarkMode();
            updateNotebookThemeToggle(isDark);
            return;
        }
        const isDark = !document.body.classList.contains('dark-mode');
        document.documentElement.classList.toggle('dark-mode', isDark);
        document.documentElement.setAttribute('data-theme', isDark ? 'dark' : 'light');
        document.body.classList.toggle('dark-mode', isDark);
        try {
            localStorage.setItem('sjmaths-dark', isDark ? 'on' : 'off');
            localStorage.setItem('theme', isDark ? 'dark' : 'light');
            localStorage.setItem('sjmaths-test-dark', isDark ? 'true' : 'false');
        } catch (error) {}
        window.dispatchEvent(new CustomEvent('themeChanged', { detail: { isDark } }));
        updateNotebookThemeToggle(isDark);
    };

    window.addEventListener('themeChanged', event => {
        const isDark = event?.detail?.isDark ?? document.body.classList.contains('dark-mode');
        updateNotebookThemeToggle(isDark);
        // The chapter's Argand graph reads its palette when it draws, so redraw
        // it after a theme change when that widget is present.
        if (typeof window.plotArgand === 'function' && document.getElementById('argandSvg')) {
            window.plotArgand();
        }
    });

    function initSlideDeck() {
        const lessonSelector = 'main .sj-card, .content-wrapper .note-section, .sj-container .sj-card, .sj-container section.sj-card';
        let slideCandidates = Array.from(document.querySelectorAll(lessonSelector));

        // Promote nested authored lesson sections before building the reader.
        // This corrects malformed nested sections without removing their HTML:
        // each subsection becomes a real page instead of being hidden inside an
        // inactive parent card. Process each group in reverse to retain order.
        const candidateSet = new Set(slideCandidates);
        const nestedByParent = new Map();
        slideCandidates.forEach(card => {
            const parent = card.parentElement?.closest('.note-section, .sj-card');
            if (!parent || !candidateSet.has(parent)) return;
            const children = nestedByParent.get(parent) || [];
            children.push(card);
            nestedByParent.set(parent, children);
        });
        nestedByParent.forEach((children, parent) => {
            children.reverse().forEach(child => parent.insertAdjacentElement('afterend', child));
        });

        slideCandidates = Array.from(document.querySelectorAll(lessonSelector));
        // A few authored notes contain a subsection inside its parent note.
        // Rendering both as independent pages hides the child whenever its
        // parent page is inactive, producing a visually empty slide. Keep only
        // top-level lesson cards; nested learning material remains visible in
        // its parent paper sheet instead of becoming an unreachable page.
        slides = slideCandidates.filter(card => !slideCandidates.some(candidate => candidate !== card && candidate.contains(card)));
        if (slides.length === 0) return;

        const mainEl = document.querySelector('main') || document.querySelector('.content-wrapper') || document.querySelector('.sj-container');
        if (!mainEl) return;

        // Auto-detect Chapter Title
        const h1 = document.querySelector('h1');
        const chapterTitle = h1 ? h1.textContent.trim() : (document.title.split('|')[0].trim());
        const currentClass11Chapter = getCurrentClass11Chapter();
        if (h1 && currentClass11Chapter) {
            h1.dataset.notebookKicker = `Class 11 Mathematics · Chapter ${String(currentClass11Chapter.chapter.num).padStart(2, '0')}`;
        }

        // The notebook always opens as a page reader. Read-all remains available
        // for accessibility, but a stale preference must not restore the legacy UI.
        const savedMode = 'slide';
        document.body.classList.add('mode-slide');

        // 2. Inject the minimal notebook controls. Content cards remain authored HTML.
        if (!document.getElementById('slideDeckHeader')) {
            const firstCard = slides[0];
            const topControls = document.createElement('div');
            topControls.id = 'slideDeckAutoTop';
            topControls.innerHTML = `
                <nav class="notebook-reader-controls" id="slideDeckHeader" aria-label="Notebook reader controls">
                    <button type="button" class="notebook-control-btn notebook-pages-btn" id="notebookDrawerButton" aria-haspopup="dialog" aria-expanded="false" aria-controls="notebookChapterDrawer" onclick="setNotebookDrawer()">
                        <i class="fas fa-book-open" aria-hidden="true"></i><span>Chapters</span>
                    </button>
                    <span class="notebook-page-counter" id="slideProgressLabel" aria-live="polite">Page 1 of ${slides.length}</span>
                    <div class="notebook-reader-actions">
                        <button type="button" class="notebook-control-btn notebook-theme-toggle" id="notebookThemeToggle" aria-pressed="false" onclick="toggleNotebookTheme()" title="Dark notebook" aria-label="Switch to dark notebook">
                            <i class="fas fa-moon" aria-hidden="true"></i><span class="sr-only">Toggle dark notebook</span>
                        </button>
                        <button type="button" class="notebook-control-btn notebook-read-all ${savedMode === 'scroll' ? 'active' : ''}" id="btnModeScroll" aria-pressed="${savedMode === 'scroll'}" onclick="setNotesViewMode(document.body.classList.contains('mode-scroll') ? 'slide' : 'scroll')">
                            <i class="fas fa-align-left" aria-hidden="true"></i><span>Read all</span>
                        </button>
                        <button type="button" class="notebook-control-btn notebook-arrow" id="trackPrevBtn" onclick="navigateSlide(-1)" title="Previous page (Left Arrow)" aria-label="Previous page"><i class="fas fa-chevron-left" aria-hidden="true"></i></button>
                        <button type="button" class="notebook-control-btn notebook-arrow" id="trackNextBtn" onclick="navigateSlide(1)" title="Next page (Right Arrow)" aria-label="Next page"><i class="fas fa-chevron-right" aria-hidden="true"></i></button>
                    </div>
                </nav>
                <aside class="notebook-chapter-drawer" id="notebookChapterDrawer" role="dialog" aria-modal="false" aria-label="Choose a chapter or notebook page" hidden>
                    <div class="notebook-drawer-heading">
                        <div><span>Class 11 Mathematics</span><strong>${chapterTitle}</strong></div>
                        <button type="button" class="notebook-drawer-close" onclick="setNotebookDrawer(false)" aria-label="Close page list"><i class="fas fa-times" aria-hidden="true"></i></button>
                    </div>
                    ${getClass11ChapterNavigation()}
                    <p class="notebook-page-list-label">Pages in this chapter</p>
                    <div class="slide-tabs-strip notebook-page-list" id="slideTabsStrip" role="tablist" aria-label="Chapter pages"></div>
                    <label class="mobile-slide-selector-label" for="mobileSlideSelect">Choose a page</label>
                    <select class="mobile-slide-selector" id="mobileSlideSelect" aria-label="Choose a notebook page"></select>
                </aside>
            `;
            firstCard.parentNode.insertBefore(topControls, firstCard);
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

            const tone = getSlideTone(title);
            const panelId = card.id || `slide-section-${idx + 1}`;
            card.id = panelId;
            card.setAttribute('role', 'tabpanel');
            card.setAttribute('aria-labelledby', `slide-tab-${idx + 1}`);
            card.setAttribute('tabindex', '-1');
            card.dataset.slideTone = tone.id;
            card.dataset.notebookLayout = 'study-note';
            card.classList.add(`tone-${tone.id}`);
            if (!card.querySelector('.slide-learning-marker')) {
                const marker = document.createElement('div');
                marker.className = 'slide-learning-marker';
                marker.innerHTML = `<i class="fas ${tone.icon}" aria-hidden="true"></i><span>${tone.label}</span>`;
                card.insertBefore(marker, h2 || card.firstChild);
            }

            // Retain the authored learning content, but give the recurring
            // structures a consistent handwritten-notebook hierarchy.
            const directLead = Array.from(card.children).find(element =>
                element.tagName === 'P' && element.textContent.trim().length > 0
            );
            if (directLead) directLead.classList.add('notebook-lead');
            Array.from(card.children).forEach(element => {
                if (/^H[3-4]$/.test(element.tagName)) element.classList.add('notebook-subheading');
            });
            card.querySelectorAll('table').forEach(table => {
                table.closest('.table-container')?.classList.add('notebook-reference-table');
            });
            card.querySelectorAll('ul, ol').forEach(list => list.classList.add('notebook-list'));
            card.querySelectorAll('.calc-box, .simulator-container, .interactive-widget').forEach(widget => {
                widget.classList.add('notebook-try-it');
            });
            return { stepNum, title, panelId, tone };
        });

        updateModeButtons(savedMode);
        updateNotebookThemeToggle();

        // 3. Populate the notebook drawer.
        const tabsStrip = document.getElementById('slideTabsStrip');
        if (tabsStrip) {
            tabsStrip.innerHTML = slideMeta.map((meta, i) =>
                `<button type="button" class="slide-tab-pill tone-${meta.tone.id} ${i === 0 ? 'active' : ''}" data-slide-tone="${meta.tone.id}" id="slide-tab-${i + 1}" role="tab" aria-controls="${meta.panelId}" aria-selected="${i === 0}" onclick="goToSlide(${i})">
                    <span class="slide-tab-num">${meta.stepNum}</span>
                    <span>${meta.title}</span>
                </button>`
            ).join('');
        }
        const mobileSelect = document.getElementById('mobileSlideSelect');
        if (mobileSelect) {
            mobileSelect.innerHTML = slideMeta.map((meta, i) =>
                `<option value="${i}">${meta.stepNum}. ${meta.title}</option>`
            ).join('');
            mobileSelect.addEventListener('change', event => {
                goToSlide(Number(event.target.value));
                setNotebookDrawer(false);
            });
        }

        // 4. Activate initial page (check URL hash or start at 0)
        let initialIndex = 0;
        if (window.location.hash && window.location.hash.startsWith('#slide-')) {
            const idx = parseInt(window.location.hash.replace('#slide-', ''), 10) - 1;
            if (!isNaN(idx) && idx >= 0 && idx < slides.length) initialIndex = idx;
        }

        goToSlide(initialIndex, false);

        // 5. Setup keyboard and swipe page navigation.
        window.addEventListener('keydown', function(e) {
            if (e.key === 'Escape' && !document.getElementById('notebookChapterDrawer')?.hidden) {
                setNotebookDrawer(false);
                document.getElementById('notebookDrawerButton')?.focus({ preventScroll: true });
                return;
            }
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

        let touchStartX = 0;
        let touchStartY = 0;
        mainEl.addEventListener('touchstart', function(event) {
            if (!document.body.classList.contains('mode-slide') || event.touches.length !== 1) return;
            touchStartX = event.touches[0].clientX;
            touchStartY = event.touches[0].clientY;
        }, { passive: true });
        mainEl.addEventListener('touchend', function(event) {
            if (!document.body.classList.contains('mode-slide') || !touchStartX) return;
            const touch = event.changedTouches[0];
            const deltaX = touch.clientX - touchStartX;
            const deltaY = touch.clientY - touchStartY;
            touchStartX = 0;
            if (Math.abs(deltaX) < 64 || Math.abs(deltaX) < Math.abs(deltaY) * 1.25) return;
            navigateSlide(deltaX < 0 ? 1 : -1);
        }, { passive: true });

        let resizeTimer;
        window.addEventListener('resize', function() {
            clearTimeout(resizeTimer);
            resizeTimer = setTimeout(() => goToSlide(currentSlide, false), 120);
        });
    }

    window.goToSlide = function(index, scrollUp = true) {
        if (!slides || slides.length === 0) return;
        if (index < 0) index = 0;
        if (index >= slides.length) index = slides.length - 1;

        const previousSlide = currentSlide;
        const didChangePage = index !== previousSlide;
        currentSlide = index;
        const isSlideMode = document.body.classList.contains('mode-slide');
        // A single focused page is easier to read and mirrors a student's
        // notebook. The next page is reached through the page controls.
        const showDesktopCompanion = false;
        const activeMeta = slideMeta[currentSlide];
        const deckHeader = document.getElementById('slideDeckHeader');
        const trackBar = document.getElementById('slideTrackBar');
        const deckFooter = document.getElementById('slideDeckFooter');
        const toneClasses = ['tone-foundation', 'tone-formula', 'tone-example', 'tone-practice', 'tone-revision', 'tone-review'];
        [deckHeader, trackBar, deckFooter].forEach(element => {
            if (element && activeMeta) {
                element.dataset.activeTone = activeMeta.tone.id;
                element.classList.remove(...toneClasses);
                element.classList.add(`tone-${activeMeta.tone.id}`);
            }
        });
        const progressLabel = document.getElementById('slideProgressLabel');
        if (progressLabel) progressLabel.textContent = `Page ${currentSlide + 1} of ${slides.length}`;
        const mobileSelect = document.getElementById('mobileSlideSelect');
        if (mobileSelect) mobileSelect.value = String(currentSlide);

        // Toggle the active notebook page and, on wide screens, its facing page.
        slides.forEach((card, i) => {
            const isActive = i === currentSlide;
            const isCompanion = showDesktopCompanion && i === currentSlide + 1;
            card.classList.toggle('active-slide', isActive);
            card.classList.toggle('notebook-companion', isCompanion);
            card.dataset.notebookPageSide = isCompanion ? 'right' : (isActive ? 'left' : '');
            if (isActive || isCompanion) {
                card.setAttribute('aria-hidden', 'false');
                card.classList.add('anim-visible');
                const content = card.querySelector('.card-content');
                if (content) content.classList.add('anim-visible');
            } else {
                card.setAttribute('aria-hidden', String(isSlideMode));
            }
        });

        if (didChangePage && isSlideMode) {
            const page = slides[currentSlide];
            const turnClass = index > previousSlide ? 'notebook-page-turn-forward' : 'notebook-page-turn-back';
            page.classList.remove('notebook-page-turn-forward', 'notebook-page-turn-back');
            requestAnimationFrame(() => {
                page.classList.add(turnClass);
                window.setTimeout(() => page.classList.remove(turnClass), 520);
            });
        }

        // Update notebook page list.
        const pills = document.querySelectorAll('.slide-tab-pill');
        pills.forEach((pill, i) => {
            const isActive = i === currentSlide;
            pill.classList.toggle('active', isActive);
            pill.setAttribute('aria-selected', String(isActive));
            if (isActive && pill.scrollIntoView) {
                pill.scrollIntoView({ behavior: 'smooth', block: 'nearest', inline: 'center' });
            }
        });

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
        const previousMeta = slideMeta[currentSlide - 1];
        const nextMeta = slideMeta[currentSlide + 1];
        const prevTitle = document.getElementById('footerPrevTitle');
        const nextTitle = document.getElementById('footerNextTitle');
        if (prevTitle) prevTitle.textContent = previousMeta ? previousMeta.title : 'Start of chapter';
        if (nextTitle) nextTitle.textContent = nextMeta ? nextMeta.title : 'Chapter complete';
        const footerPrev = document.getElementById('footerPrevBtn');
        const footerNext = document.getElementById('footerNextBtn');
        if (footerPrev) footerPrev.setAttribute('aria-label', previousMeta ? `Previous section: ${previousMeta.title}` : 'Start of chapter');
        if (footerNext) footerNext.setAttribute('aria-label', nextMeta ? `Next section: ${nextMeta.title}` : 'Chapter complete');
        setNotebookDrawer(false);

        // Update URL hash without jumping page
        if (history.replaceState) {
            history.replaceState(null, null, '#slide-' + (currentSlide + 1));
        }

        // The controls are fixed to the viewport. Scroll the lesson itself so
        // a page change never leaves the reader at the previous page's bottom.
        if (scrollUp) {
            slides[currentSlide].scrollIntoView({
                behavior: window.matchMedia('(prefers-reduced-motion: reduce)').matches ? 'auto' : 'smooth',
                block: 'start'
            });
        }
    };

    window.navigateSlide = function(delta) {
        goToSlide(currentSlide + delta, true);
    };

    window.setNotebookDrawer = function(forceOpen) {
        const drawer = document.getElementById('notebookChapterDrawer');
        const trigger = document.getElementById('notebookDrawerButton');
        if (!drawer || !trigger) return;
        const isOpen = !drawer.hidden;
        const shouldOpen = typeof forceOpen === 'boolean' ? forceOpen : !isOpen;
        drawer.hidden = !shouldOpen;
        trigger.setAttribute('aria-expanded', String(shouldOpen));
        if (shouldOpen) {
            const selected = drawer.querySelector('.slide-tab-pill.active');
            if (selected) selected.focus({ preventScroll: true });
        }
    };

    window.setNotesViewMode = function(mode) {
        if (mode === 'scroll') {
            document.body.classList.remove('mode-slide');
            document.body.classList.add('mode-scroll');
            updateModeButtons('scroll');
            slides.forEach(card => card.setAttribute('aria-hidden', 'false'));
        } else {
            document.body.classList.remove('mode-scroll');
            document.body.classList.add('mode-slide');
            updateModeButtons('slide');
            goToSlide(currentSlide, false);
        }
    };

    function updateModeButtons(mode) {
        const btnSlide = document.getElementById('btnModeSlide');
        const btnScroll = document.getElementById('btnModeScroll');
        if (btnScroll) {
            const controls = document.getElementById('slideDeckHeader');
            if (controls) controls.classList.toggle('notebook-read-all-mode', mode === 'scroll');
            if (btnSlide) {
            btnSlide.classList.toggle('active', mode === 'slide');
            btnScroll.classList.toggle('active', mode === 'scroll');
            btnSlide.setAttribute('aria-pressed', String(mode === 'slide'));
            }
            btnScroll.classList.toggle('active', mode === 'scroll');
            btnScroll.setAttribute('aria-pressed', String(mode === 'scroll'));
            const label = btnScroll.querySelector('span');
            if (label) label.textContent = mode === 'scroll' ? 'Page view' : 'Read all';
            const icon = btnScroll.querySelector('i');
            if (icon) icon.className = mode === 'scroll' ? 'fas fa-book-open' : 'fas fa-align-left';
        }
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initSlideDeck);
    } else {
        initSlideDeck();
    }
})();
