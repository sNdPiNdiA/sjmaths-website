/**
 * chapter-learning.js  —  Premium Single-Card Wizard
 */
(function () {
    'use strict';

    var KEY = window.CL_KEY || 'sjmaths_c9_ch_unknown';
    var TOTAL = 24;
    var progress = parseInt(localStorage.getItem(KEY) || '1', 10);
    var DATA = null;
    var SPC = 4; /* Steps Per Concept: 4 or 5 (when PYQ exists) */
    var SUB_LABELS = ['Check', 'Learn', 'Practice', 'Test'];
    var viewStep = null; /* null = follow progress, number = reviewing a specific step */

    function $(id) { return document.getElementById(id); }
    function setProgress(n) { progress = n; localStorage.setItem(KEY, n); renderUI(); }
    function stepInfo(s) { return { ci: Math.floor((s - 1) / SPC), si: (s - 1) % SPC }; }

    /* ══════════ RENDER ══════════ */
    function renderUI() {
        var pct = Math.min(100, Math.round(((progress - 1) / TOTAL) * 100));
        var fill = $('cl-progress-fill');
        var label = $('cl-progress-label');
        if (fill) fill.style.width = pct + '%';
        if (label) label.textContent = pct >= 100 ? '🎉 100%' : pct + '%';
        if (!DATA) return;

        var info = stepInfo(Math.min(progress, TOTAL));

        var completed = progress > TOTAL;
        var activeStep = viewStep || progress;

        /* Roadmap */
        var activeInfo = stepInfo(Math.min(activeStep, TOTAL));
        DATA.concepts.forEach(function (c, ci) {
            var row = $('cl-rm-' + ci);
            if (!row) return;
            var first = ci * SPC + 1, last = ci * SPC + SPC;
            row.classList.remove('rm-done', 'rm-active', 'rm-locked');
            var icon = row.querySelector('.rm-icon');
            if (completed) {
                /* All done — highlight the one being viewed */
                row.classList.add(ci === activeInfo.ci ? 'rm-active' : 'rm-done');
                if (icon) icon.innerHTML = ci === activeInfo.ci ? '<i class="fas fa-eye"></i>' : '<i class="fas fa-check-circle"></i>';
                row.style.cursor = 'pointer';
            } else if (progress > last) {
                row.classList.add('rm-done');
                if (icon) icon.innerHTML = '<i class="fas fa-check-circle"></i>';
            } else if (progress >= first) {
                row.classList.add('rm-active');
                if (icon) icon.innerHTML = '<i class="fas fa-circle-dot"></i>';
            } else {
                row.classList.add('rm-locked');
                if (icon) icon.innerHTML = '<i class="fas fa-lock"></i>';
            }
        });

        /* Roadmap header */
        var rmHeader = $('cl-rm-header');
        var conceptCount = DATA.concepts.length;
        var conceptSteps = conceptCount * SPC;
        var isChapterTest = DATA.chapterTest && activeStep === conceptSteps + 1;
        if (rmHeader) {
            if (completed && !viewStep) {
                rmHeader.querySelector('.rm-current-text').textContent = '✅ Completed — tap a concept to review';
                rmHeader.querySelector('.rm-counter').textContent = '🎉';
            } else if (isChapterTest) {
                rmHeader.querySelector('.rm-current-text').textContent = '\ud83d\udcdd Chapter Test';
                rmHeader.querySelector('.rm-counter').textContent = 'Final';
            } else {
                var c = DATA.concepts[activeInfo.ci];
                rmHeader.querySelector('.rm-current-text').textContent = c.icon + ' ' + c.title;
                rmHeader.querySelector('.rm-counter').textContent = (activeInfo.ci + 1) + ' / ' + conceptCount;
            }
        }

        /* Text stepper */
        var stepper = $('cl-stepper');
        if (isChapterTest || (completed && !viewStep)) {
            if (stepper) stepper.style.display = 'none';
        } else {
            if (stepper) stepper.style.display = '';
            for (var si = 0; si < SPC; si++) {
                var item = $('cl-st-' + si);
                if (!item) continue;
                item.classList.remove('st-done', 'st-active');
                if (completed) {
                    /* In review mode, make stepper items clickable */
                    item.classList.add(si === activeInfo.si ? 'st-active' : 'st-done');
                } else {
                    if (si < info.si) item.classList.add('st-done');
                    else if (si === info.si) item.classList.add('st-active');
                }
            }
        }

        /* Active card — always show only ONE */
        for (var i = 1; i <= TOTAL; i++) {
            var mod = $('step' + i);
            if (!mod) continue;
            mod.classList.remove('active-module');
            if (i === activeStep) mod.classList.add('active-module');
        }

        /* Completion */
        var banner = $('cl-completion-banner');
        if (banner) {
            if (completed && !viewStep) { banner.classList.add('show'); launchConfetti(); }
            else banner.classList.remove('show');
        }

        /* Render math with KaTeX */
        if (window.renderMathInElement) {
            renderMathInElement(document.body, {
                delimiters: [
                    { left: '$$', right: '$$', display: true },
                    { left: '$', right: '$', display: false },
                    { left: '\\(', right: '\\)', display: false },
                    { left: '\\[', right: '\\]', display: true },
                    { left: '\\\\(', right: '\\\\)', display: false },
                    { left: '\\\\[', right: '\\\\]', display: true }
                ],
                throwOnError: false
            });
        }
    }

    /* Jump to any step (review mode) */
    function jumpTo(step) {
        if (progress <= TOTAL) return; /* only after completion */
        viewStep = step || null;
        renderUI();
        window.scrollTo({ top: 0, behavior: 'smooth' });
    }

    /* ══════════ ACTIONS ══════════ */
    function completeStep(n) {
        if (progress > TOTAL) {
            /* Review mode — navigate to next step */
            jumpTo(n + 1 <= TOTAL ? n + 1 : null);
            return;
        }
        if (progress <= n) {
            viewStep = null;
            setProgress(n + 1);
            window.scrollTo({ top: 0, behavior: 'smooth' });
        }
    }

    function selectOpt(cid, el, correct, btnId, fbId) {
        var c = $(cid); if (!c) return;
        c.querySelectorAll('.opt-item').forEach(function (o) { o.classList.remove('opt-correct', 'opt-wrong'); });
        el.classList.add(correct ? 'opt-correct' : 'opt-wrong');
        /* Show hint on wrong answer */
        var hintEl = $('hint-' + cid);
        if (hintEl && !correct) hintEl.style.display = 'block';
        /* Show solution on correct answer */
        var solEl = $('sol-' + cid);
        if (solEl && correct) {
            solEl.classList.add('show');
            if (window.renderMathInElement) renderMathInElement(solEl);
        }
        if (fbId) {
            var fb = $(fbId);
            if (fb) { fb.className = 'opt-feedback show ' + (correct ? 'fb-ok' : 'fb-err'); fb.textContent = correct ? '✅ Correct!' : '❌ Try again!'; }
        }
        if (btnId) { var b = $(btnId); if (b) b.style.display = correct ? 'flex' : 'none'; }
    }

    function selectPrecheck(cid, el, correct, stepNum, fbId) {
        var c = $(cid); if (!c) return;
        c.querySelectorAll('.opt-item').forEach(function (o) { o.classList.remove('opt-precheck'); });
        el.classList.add('opt-precheck');
        if (fbId) {
            var fb = $(fbId);
            var concept = DATA.concepts[stepInfo(stepNum).ci];
            fb.className = 'opt-feedback show fb-pre';
            fb.textContent = correct ? concept.precheck.passMessage : concept.precheck.failMessage;
        }
        var btn = $('btn-step' + stepNum);
        if (btn) btn.style.display = 'flex';
    }

    /* ══════════ BUILD ══════════ */
    function loadChapter(url) {
        fetch(url).then(function (r) { return r.json(); }).then(function (data) {
            DATA = data;
            /* Detect if any concept has PYQ data */
            var hasPyq = data.concepts.some(function (c) { return c.pyq && c.pyq.length > 0; });
            SPC = hasPyq ? 5 : 4;
            SUB_LABELS = hasPyq ? ['Check', 'Learn', 'Practice', 'PYQ', 'Test'] : ['Check', 'Learn', 'Practice', 'Test'];
            TOTAL = data.concepts.length * SPC + (data.chapterTest ? 1 : 0);
            buildRoadmap(data);
            buildStepper();
            buildModules(data);
            if (data.chapterTest) buildChapterTest(data);
            buildCompletion(data.completion);
            renderUI();
        });
    }

    function buildRoadmap(data) {
        var wrap = $('cl-roadmap-wrap'); if (!wrap) return;
        wrap.innerHTML = '';

        var header = document.createElement('div');
        header.className = 'rm-header'; header.id = 'cl-rm-header';
        header.innerHTML = '<span class="rm-current-text rm-header-left"></span><div class="rm-header-right"><span class="rm-counter"></span><i class="fas fa-chevron-down rm-chevron"></i></div>';
        header.addEventListener('click', function () {
            var list = $('cl-rm-list');
            var chev = header.querySelector('.rm-chevron');
            list.classList.toggle('rm-open');
            chev.classList.toggle('rm-chev-up');
        });
        wrap.appendChild(header);

        var list = document.createElement('div');
        list.className = 'rm-list'; list.id = 'cl-rm-list';
        data.concepts.forEach(function (c, ci) {
            var row = document.createElement('div');
            row.className = 'rm-row'; row.id = 'cl-rm-' + ci;
            row.innerHTML = '<span class="rm-icon"></span><span class="rm-name">' + c.icon + ' ' + c.title + '</span>';
            row.addEventListener('click', function () {
                if (progress > TOTAL) { jumpTo(ci * SPC + 2); } /* jump to Learn step */
            });
            list.appendChild(row);
        });
        wrap.appendChild(list);
    }

    function buildStepper() {
        var card = document.querySelector('.cl-progress-card'); if (!card) return;
        var row = document.createElement('div');
        row.className = 'cl-stepper'; row.id = 'cl-stepper';
        for (var si = 0; si < SPC; si++) {
            if (si > 0) { var sep = document.createElement('span'); sep.className = 'cl-stepper-sep'; sep.textContent = '›'; row.appendChild(sep); }
            var item = document.createElement('span');
            item.className = 'cl-stepper-item'; item.id = 'cl-st-' + si;
            item.textContent = SUB_LABELS[si];
            (function (idx) {
                item.addEventListener('click', function () {
                    if (progress > TOTAL && viewStep) {
                        var ci = stepInfo(viewStep).ci;
                        jumpTo(ci * SPC + idx + 1);
                    }
                });
            })(si);
            row.appendChild(item);
        }
        card.appendChild(row);
    }

    function buildModules(data) {
        var container = $('cl-wizard'); if (!container) return;
        var loading = container.querySelector('.cl-loading');
        if (loading) loading.remove();
        data.concepts.forEach(function (concept, ci) {
            var base = ci * SPC;
            container.appendChild(makePrecheck(concept, base + 1));
            container.appendChild(makeLearn(concept, base + 2));
            container.appendChild(makeQuiz(concept.practice, base + 3, 'Practice', 'fas fa-pen-nib', concept.title));
            if (SPC === 5) {
                container.appendChild(makeQuiz(concept.pyq || [], base + 4, 'Previous Year Qs', 'fas fa-history', concept.title));
                container.appendChild(makeQuiz(concept.test, base + 5, 'Test', 'fas fa-flask', concept.title));
            } else {
                container.appendChild(makeQuiz(concept.test, base + 4, 'Test', 'fas fa-flask', concept.title));
            }
        });
    }

    function mkCard(stepNum, title, icon) {
        var div = document.createElement('div');
        div.id = 'step' + stepNum;
        div.className = 'path-module';
        div.innerHTML = '<div class="module-header"><div class="step-badge"><i class="' + icon + '"></i></div><h2>' + title + '</h2></div><div class="content-area"></div>';
        return div;
    }

    function makePrecheck(concept, sn) {
        var d = mkCard(sn, 'Pre-check', 'fas fa-brain');
        var pc = concept.precheck;
        var h = '<p>Before <strong>' + concept.title + '</strong>, let\'s check what you know.</p>';
        h += '<div class="quiz-block"><div class="quiz-q">' + pc.question + '</div>';
        h += '<div class="options-list" id="pc' + sn + '">';
        pc.options.forEach(function (opt, oi) {
            h += '<div class="opt-item" onclick="CL.selectPrecheck(\'pc' + sn + '\',this,' + (oi === pc.correctIndex) + ',' + sn + ',\'fb-pc' + sn + '\')">' + opt + '</div>';
        });
        h += '</div><div class="opt-feedback" id="fb-pc' + sn + '"></div></div>';
        h += '<button class="action-btn btn-primary" id="btn-step' + sn + '" style="display:none" onclick="CL.completeStep(' + sn + ')">Let\'s Learn <i class="fas fa-arrow-right"></i></button>';
        d.querySelector('.content-area').innerHTML = h;
        return d;
    }

    /* Convert **bold** and *italic* markdown to HTML */
    function mdInline(s) {
        return s.replace(/\*\*(.+?)\*\*/g, '<strong>$1</strong>').replace(/\*(.+?)\*/g, '<em>$1</em>');
    }

    function hasMathDelimiters(s) {
        return /\$\$[\s\S]*\$\$|\$[^$]+\$|\\\([\s\S]*\\\)|\\\[[\s\S]*\\\]/.test(s);
    }

    function mathCardText(s) {
        if (!s) return '';
        return hasMathDelimiters(s) ? s : '\\(' + s + '\\)';
    }

    function makeLearn(concept, sn) {
        var d = mkCard(sn, concept.title, 'fas fa-book-open');
        var lrn = concept.learn, h = '';
        if (lrn.paragraphs) lrn.paragraphs.forEach(function (p) { h += '<p>' + mdInline(p) + '</p>'; });
        if (lrn.tree) {
            h += '<div class="number-tree">';
            lrn.tree.forEach(function (t) { h += '<div class="nt-level"><span class="nt-chip ' + t.class + '">' + t.symbol + ' ' + t.label + '</span><span class="nt-desc">' + t.desc + '</span></div>'; });
            h += '</div>';
        }
        if (lrn.formulas) {
            h += '<div class="formula-grid">';
            lrn.formulas.forEach(function (f) {
                h += '<div class="formula-card"><div class="fc-name">' + f.rule + '</div><div class="fc-formula">' + mathCardText(f.formula) + '</div><div class="fc-example">' + mathCardText(f.example) + '</div></div>';
            });
            h += '</div>';
        }
        if (lrn.algorithms) {
            lrn.algorithms.forEach(function (algo) {
                h += '<div class="algorithm-block">';
                algo.steps.forEach(function (step, idx) {
                    h += '<div class="algo-step"><span class="algo-num">' + (idx + 1) + '.</span><span class="algo-text">' + mdInline(step) + '</span></div>';
                });
                h += '</div>';
            });
        }
        if (lrn.interactiveGraph) {
            h += '<div class="cl-graph-container">';
            h += '<canvas id="graph-' + sn + '" width="400" height="400" class="cl-interactive-graph"></canvas>';
            h += '<div class="cl-graph-controls">';
            h += '<div class="cl-graph-info" id="ginfo-' + sn + '">Hover or tap on the graph...</div>';
            if (lrn.interactiveGraph.clickable) {
                h += '<button class="action-btn btn-sm" onclick="CL.clearGraph(\'graph-' + sn + '\')">Clear All</button>';
            }
            if (lrn.interactiveGraph.spiral) {
                h += '<button class="action-btn btn-sm" id="spiral-next-' + sn + '">Next Step</button>';
            }
            h += '</div>';
            if (lrn.interactiveGraph.spiral) {
                h += '<div class="spiral-stats"><div class="stat-item"><div class="stat-label">Hypotenuse</div><div class="stat-value" id="spiral-hyp-' + sn + '">-</div></div><div class="stat-item"><div class="stat-label">Irrational</div><div class="stat-value" id="spiral-irr-' + sn + '">-</div></div></div>';
            }
            h += '</div>';
            /* Draw graph after DOM update */
            setTimeout(function () {
                if (lrn.interactiveGraph.spiral) CL.initSpiral('graph-' + sn, 'ginfo-' + sn, sn);
                else CL.initGraph('graph-' + sn, 'ginfo-' + sn, lrn.interactiveGraph);
            }, 50);
        }
        if (lrn.boxes) lrn.boxes.forEach(function (b) { h += '<div class="box-' + b.type + '">' + b.html + '</div>'; });
        if (lrn.decomposition) {
            lrn.decomposition.forEach(function (d) {
                h += '<div class="box-decomposition"><strong>🧩 Problem Decomposition:</strong><br>' + mdInline(d) + '</div>';
            });
        }
        h += '<button class="action-btn btn-primary" onclick="CL.completeStep(' + sn + ')">Got it <i class="fas fa-arrow-right"></i></button>';
        d.querySelector('.content-area').innerHTML = h;
        return d;
    }

    function makeQuiz(questions, sn, title, icon, conceptTitle) {
        var d = mkCard(sn, title + ': ' + conceptTitle, icon);
        var btnId = 'btn-step' + sn;
        var isTest = title === 'Test';
        var h = '';
        questions.forEach(function (q, qi) {
            var qid = 's' + sn + 'q' + qi;
            if (qi > 0) h += '<div class="quiz-divider"></div>';
            h += '<div class="quiz-block"><div class="quiz-q">' + (qi + 1) + '. ' + q.question + '</div>';

            if (q.interactiveGraph) {
                h += '<div class="cl-graph-container" style="margin: 10px 0;">';
                h += '<canvas id="graph-' + qid + '" width="300" height="300" class="cl-interactive-graph"></canvas>';
                h += '<div class="cl-graph-controls">';
                h += '<div class="cl-graph-info" id="ginfo-' + qid + '">Hover to see details...</div>';
                if (q.interactiveGraph.clickable) {
                    h += '<button class="action-btn btn-sm" onclick="CL.clearGraph(\'graph-' + qid + '\')">Clear</button>';
                }
                h += '</div></div>';
                setTimeout(function () { CL.initGraph('graph-' + qid, 'ginfo-' + qid, q.interactiveGraph); }, 50);
            }

            if (q.hint) h += '<div class="quiz-hint" id="hint-' + qid + '" style="display:none">💡 ' + q.hint + '</div>';
            h += '<div class="options-list" id="' + qid + '">';
            q.options.forEach(function (opt, oi) {
                h += '<div class="opt-item" onclick="CL.selectOpt(\'' + qid + '\',this,' + (oi === q.correctIndex) + ',\'' + btnId + '\',\'fb-' + qid + '\')">' + opt + '</div>';
            });
            h += '</div><div class="opt-feedback" id="fb-' + qid + '"></div>';
            if (q.solution) {
                h += '<div class="quiz-solution" id="sol-' + qid + '">';
                h += '<div class="sol-title"><i class="fas fa-lightbulb"></i> Stepwise Solution</div>';
                h += '<div class="sol-content">' + q.solution + '</div></div>';
            }
            h += '</div>';
        });
        h += '<button class="action-btn btn-orange" id="' + btnId + '" style="display:none" onclick="CL.completeStep(' + sn + ')">' + (isTest ? 'Complete ✓' : 'Next →') + '</button>';
        d.querySelector('.content-area').innerHTML = h;
        return d;
    }

    function buildChapterTest(data) {
        var container = $('cl-wizard'); if (!container || !data.chapterTest) return;
        var ct = data.chapterTest;
        var sn = data.concepts.length * 4 + 1;
        var d = mkCard(sn, ct.title, 'fas fa-award');
        d.classList.add('chapter-test-card');
        var h = '<p class="ct-desc">' + ct.description + '</p>';
        h += '<div class="ct-score-bar" id="ct-score-bar"><span class="ct-answered">0 / ' + ct.questions.length + ' answered</span></div>';
        ct.questions.forEach(function (q, qi) {
            var qid = 'ct-q' + qi;
            if (qi > 0) h += '<div class="quiz-divider"></div>';
            h += '<div class="quiz-block">';
            h += '<div class="ct-concept-tag">' + q.concept + '</div>';
            h += '<div class="quiz-q">' + (qi + 1) + '. ' + q.question + '</div>';

            if (q.interactiveGraph) {
                h += '<div class="cl-graph-container" style="margin: 10px 0;">';
                h += '<canvas id="graph-' + qid + '" width="300" height="300" class="cl-interactive-graph"></canvas>';
                h += '<div class="cl-graph-controls">';
                h += '<div class="cl-graph-info" id="ginfo-' + qid + '">Hover to see details...</div>';
                if (q.interactiveGraph.clickable) {
                    h += '<button class="action-btn btn-sm" onclick="CL.clearGraph(\'graph-' + qid + '\')">Clear</button>';
                }
                h += '</div></div>';
                setTimeout(function () { CL.initGraph('graph-' + qid, 'ginfo-' + qid, q.interactiveGraph); }, 50);
            }

            h += '<div class="options-list" id="' + qid + '">';
            q.options.forEach(function (opt, oi) {
                h += '<div class="opt-item" onclick="CL.selectChapterTest(\'' + qid + '\',this,' + (oi === q.correctIndex) + ',' + qi + ')">' + opt + '</div>';
            });
            h += '</div><div class="opt-feedback" id="fb-' + qid + '"></div></div>';
        });
        h += '<div class="ct-result" id="ct-result" style="display:none"></div>';
        h += '<button class="action-btn btn-orange" id="btn-step' + sn + '" style="display:none" onclick="CL.completeStep(' + sn + ')">Complete Chapter ✓</button>';
        d.querySelector('.content-area').innerHTML = h;
        container.appendChild(d);
    }

    /* Chapter test answer tracking */
    var ctAnswers = {};
    function selectChapterTest(qid, el, correct, qi) {
        var c = $(qid); if (!c) return;
        /* Lock after answer */
        if (ctAnswers[qi] !== undefined) return;
        ctAnswers[qi] = correct;
        c.querySelectorAll('.opt-item').forEach(function (o) { o.style.pointerEvents = 'none'; });
        el.classList.add(correct ? 'opt-correct' : 'opt-wrong');
        /* Show correct if wrong */
        if (!correct) {
            var correctIdx = DATA.chapterTest.questions[qi].correctIndex;
            c.querySelectorAll('.opt-item')[correctIdx].classList.add('opt-correct');
        }
        /* Update score bar */
        var total = DATA.chapterTest.questions.length;
        var answered = Object.keys(ctAnswers).length;
        var correctCount = 0;
        for (var k in ctAnswers) if (ctAnswers[k]) correctCount++;
        var bar = $('ct-score-bar');
        if (bar) bar.querySelector('.ct-answered').textContent = answered + ' / ' + total + ' answered';
        /* If all answered, show result */
        if (answered >= total) {
            var pct = Math.round((correctCount / total) * 100);
            var pass = pct >= (DATA.chapterTest.passPercent || 70);
            var result = $('ct-result');
            if (result) {
                result.style.display = 'block';
                result.className = 'ct-result ' + (pass ? 'ct-pass' : 'ct-fail');
                result.innerHTML = '<div class="ct-result-icon">' + (pass ? '🏆' : '📖') + '</div>' +
                    '<div class="ct-result-score">' + correctCount + ' / ' + total + ' correct (' + pct + '%)</div>' +
                    '<div class="ct-result-msg">' + (pass ? 'Excellent! You passed the Chapter Test!' : 'Keep learning! Review the concepts and try again.') + '</div>';
            }
            if (pass) {
                var btn = $('btn-step' + (DATA.concepts.length * 4 + 1));
                if (btn) btn.style.display = 'flex';
            }
        }
    }

    function buildCompletion(c) {
        var container = $('cl-wizard'); if (!container || !c) return;
        var div = document.createElement('div');
        div.className = 'completion-banner'; div.id = 'cl-completion-banner';
        div.innerHTML = '<h2>' + c.title + '</h2><p>' + c.message + '</p>' +
            (c.nextChapter ? '<a href="' + c.nextChapter.url + '" class="next-link">' + c.nextChapter.label + ' <i class="fas fa-arrow-right"></i></a>' : '');
        container.appendChild(div);
    }

    /* ── Confetti ── */
    function launchConfetti() {
        var cv = $('cl-confetti'); if (!cv) return;
        var ctx = cv.getContext('2d'); cv.width = innerWidth; cv.height = innerHeight;
        var cols = ['#f44336', '#e91e63', '#9c27b0', '#4f46e5', '#2196f3', '#10b981', '#ffeb3b', '#f97316'];
        var pcs = []; for (var i = 0; i < 100; i++) pcs.push({ x: cv.width * Math.random(), y: -10, vx: (Math.random() - .5) * 5, vy: Math.random() * 3 + 2, s: Math.random() * 8 + 3, c: cols[i % cols.length], r: Math.random() * 360, rs: (Math.random() - .5) * 5 });
        var aid; function draw() { ctx.clearRect(0, 0, cv.width, cv.height); var a = false; pcs.forEach(function (p) { p.x += p.vx; p.y += p.vy; p.r += p.rs; if (p.y < cv.height + 20) a = true; ctx.save(); ctx.translate(p.x, p.y); ctx.rotate(p.r * Math.PI / 180); ctx.fillStyle = p.c; ctx.fillRect(-p.s / 2, -p.s / 2, p.s, p.s); ctx.restore() }); if (a) aid = requestAnimationFrame(draw) } draw();
        setTimeout(function () { cancelAnimationFrame(aid); ctx.clearRect(0, 0, cv.width, cv.height) }, 4000);
    }

    /* ── Interactive Graph ── */
    var activeGraphs = {};
    function initGraph(canvasId, infoId, config) {
        var cv = $(canvasId); if (!cv) return;
        var ctx = cv.getContext('2d');
        var info = $(infoId);

        var w = cv.width, h = cv.height;
        var rangeX = config.rangeX || [-10, 10];
        var rangeY = config.rangeY || [-10, 10];
        var ppuX = w / (rangeX[1] - rangeX[0]); /* pixels per unit */
        var ppuY = h / (rangeY[1] - rangeY[0]);
        var originX = -rangeX[0] * ppuX;
        var originY = rangeY[1] * ppuY;

        var points = config.points ? JSON.parse(JSON.stringify(config.points)) : [];
        activeGraphs[canvasId] = { points: points };

        function drawGraph() {
            ctx.clearRect(0, 0, w, h);

            /* Fill background */
            ctx.fillStyle = '#1e293b'; /* dark background */
            ctx.fillRect(0, 0, w, h);

            /* Draw grid */
            ctx.strokeStyle = 'rgba(255,255,255,0.05)';
            ctx.lineWidth = 1;
            ctx.beginPath();
            for (var x = Math.ceil(rangeX[0]); x <= rangeX[1]; x++) {
                var px = originX + x * ppuX;
                ctx.moveTo(px, 0); ctx.lineTo(px, h);
            }
            for (var y = Math.ceil(rangeY[0]); y <= rangeY[1]; y++) {
                var py = originY - y * ppuY;
                ctx.moveTo(0, py); ctx.lineTo(w, py);
            }
            ctx.stroke();

            /* Draw Axes */
            ctx.strokeStyle = 'rgba(255,255,255,0.3)';
            ctx.lineWidth = 2;
            ctx.beginPath();
            ctx.moveTo(0, originY); ctx.lineTo(w, originY); /* X axis */
            ctx.moveTo(originX, 0); ctx.lineTo(originX, h); /* Y axis */
            ctx.stroke();

            /* Draw ticks & labels */
            ctx.fillStyle = 'rgba(255,255,255,0.6)';
            ctx.font = '12px Courier New';
            ctx.textAlign = 'center';
            ctx.textBaseline = 'top';
            for (var x = Math.ceil(rangeX[0]); x <= rangeX[1]; x++) {
                if (x === 0) continue;
                var px = originX + x * ppuX;
                ctx.beginPath(); ctx.moveTo(px, originY - 4); ctx.lineTo(px, originY + 4); ctx.stroke();
                ctx.fillText(x, px, originY + 8);
            }
            ctx.textAlign = 'right';
            ctx.textBaseline = 'middle';
            for (var y = Math.ceil(rangeY[0]); y <= rangeY[1]; y++) {
                if (y === 0) continue;
                var py = originY - y * ppuY;
                ctx.beginPath(); ctx.moveTo(originX - 4, py); ctx.lineTo(originX + 4, py); ctx.stroke();
                ctx.fillText(y, originX - 8, py);
            }
            /* Origin */
            ctx.fillText('0', originX - 8, originY + 10);

            /* Helper function to draw lines */
            function drawGeoLine(x1, y1, x2, y2, color, isRay, isSegment) {
                var px1 = originX + x1 * ppuX, py1 = originY - y1 * ppuY;
                var px2 = originX + x2 * ppuX, py2 = originY - y2 * ppuY;
                ctx.strokeStyle = color || '#38bdf8';
                ctx.lineWidth = 2;
                ctx.beginPath();

                if (isSegment) {
                    ctx.moveTo(px1, py1); ctx.lineTo(px2, py2);
                } else {
                    var dx = px2 - px1, dy = py2 - py1;
                    if (dx === 0 && dy === 0) return;
                    var len = Math.hypot(dx, dy);
                    var nx = dx / len * 2000, ny = dy / len * 2000;
                    if (isRay) {
                        ctx.moveTo(px1, py1); ctx.lineTo(px1 + nx, py1 + ny);
                    } else {
                        ctx.moveTo(px1 - nx, py1 - ny); ctx.lineTo(px1 + nx, py1 + ny);
                    }
                }
                ctx.stroke();
            }

            /* Draw Lines, Rays, Segments */
            if (config.lines) config.lines.forEach(function (l) { drawGeoLine(l.x1, l.y1, l.x2, l.y2, l.color, false, false); });
            if (config.rays) config.rays.forEach(function (r) { drawGeoLine(r.x1, r.y1, r.x2, r.y2, r.color, true, false); });
            if (config.segments) config.segments.forEach(function (s) { drawGeoLine(s.x1, s.y1, s.x2, s.y2, s.color, false, true); });

            /* Draw Angles (Arcs) */
            if (config.angles) config.angles.forEach(function (a) {
                var cx = originX + a.x * ppuX, cy = originY - a.y * ppuY;
                var r = a.radius ? a.radius * ppuX : 30;
                ctx.beginPath();
                ctx.arc(cx, cy, r, -a.startAngle * Math.PI / 180, -a.endAngle * Math.PI / 180, true);
                ctx.strokeStyle = a.color || '#f59e0b';
                ctx.lineWidth = 3;
                ctx.stroke();
                if (a.fill) {
                    ctx.lineTo(cx, cy); ctx.fillStyle = a.fill; ctx.fill();
                }
                if (a.label) {
                    var midAngle = -(a.startAngle + a.endAngle) / 2 * Math.PI / 180;
                    ctx.fillStyle = a.color || '#f59e0b';
                    ctx.font = 'bold 12px sans-serif';
                    ctx.fillText(a.label, cx + Math.cos(midAngle) * (r + 15), cy + Math.sin(midAngle) * (r + 15));
                }
            });

            /* Draw Points */
            points.forEach(function (pt) {
                var px = originX + pt.x * ppuX;
                var py = originY - pt.y * ppuY;

                /* Draw dashed lines to axes */
                if (pt.showLines) {
                    ctx.strokeStyle = 'rgba(56, 189, 248, 0.4)';
                    ctx.setLineDash([4, 4]);
                    ctx.lineWidth = 1;
                    ctx.beginPath();
                    ctx.moveTo(px, py); ctx.lineTo(px, originY);
                    ctx.moveTo(px, py); ctx.lineTo(originX, py);
                    ctx.stroke();
                    ctx.setLineDash([]);
                }

                ctx.beginPath();
                ctx.arc(px, py, 6, 0, Math.PI * 2);
                ctx.fillStyle = pt.color || '#38bdf8';
                ctx.fill();
                ctx.strokeStyle = '#fff';
                ctx.lineWidth = 2;
                ctx.stroke();

                if (pt.label) {
                    ctx.fillStyle = '#fff';
                    ctx.font = 'bold 14px "Inter", sans-serif';
                    ctx.textAlign = 'left';
                    var labelText = config.hideCoords ? pt.label : pt.label + ' (' + pt.x + ', ' + pt.y + ')';
                    ctx.fillText(labelText, px + 10, py - 10);
                }
            });
        }

        drawGraph();

        function getCoords(e) {
            var rect = cv.getBoundingClientRect();
            var mx = e.clientX - rect.left;
            var my = e.clientY - rect.top;
            var rx = (mx - originX) / ppuX;
            var ry = (originY - my) / ppuY;
            return { rawX: rx, rawY: ry, roundX: Math.round(rx), roundY: Math.round(ry), mx: mx, my: my };
        }

        if (config.clickable || config.hoverable) {
            cv.addEventListener('mousemove', function (e) {
                var c = getCoords(e);
                /* Find if hovering near a point */
                var hovered = null;
                points.forEach(function (pt) {
                    var px = originX + pt.x * ppuX;
                    var py = originY - pt.y * ppuY;
                    var dist = Math.hypot(c.mx - px, c.my - py);
                    if (dist < 15) hovered = pt;
                });

                if (hovered) {
                    cv.style.cursor = 'pointer';
                    if (info) {
                        if (hovered.hoverText) {
                            info.innerHTML = hovered.hoverText;
                        } else {
                            var quad = '';
                            if (hovered.x > 0 && hovered.y > 0) quad = 'Quadrant I (+, +)';
                            else if (hovered.x < 0 && hovered.y > 0) quad = 'Quadrant II (-, +)';
                            else if (hovered.x < 0 && hovered.y < 0) quad = 'Quadrant III (-, -)';
                            else if (hovered.x > 0 && hovered.y < 0) quad = 'Quadrant IV (+, -)';
                            else if (hovered.y === 0 && hovered.x !== 0) quad = 'x-axis';
                            else if (hovered.x === 0 && hovered.y !== 0) quad = 'y-axis';
                            else quad = 'Origin (0,0)';
                            info.innerHTML = '<strong>' + (hovered.label || 'Point') + ' (' + hovered.x + ', ' + hovered.y + ')</strong> lies in ' + quad;
                        }
                        info.className = 'cl-graph-info info-active';
                    }
                } else {
                    cv.style.cursor = config.clickable ? 'crosshair' : 'default';
                    if (info) {
                        info.innerHTML = config.clickable ? 'Click to plot a point at (' + c.roundX + ', ' + c.roundY + ')' : 'Hover over points to see details.';
                        info.className = 'cl-graph-info';
                    }
                }
            });
        }

        if (config.clickable) {
            cv.addEventListener('click', function (e) {
                var c = getCoords(e);
                var nx = c.roundX, ny = c.roundY;
                /* check if removing */
                var removed = false;
                for (var i = 0; i < points.length; i++) {
                    if (points[i].x === nx && points[i].y === ny) { points.splice(i, 1); removed = true; break; }
                }
                if (!removed) {
                    points.push({ x: nx, y: ny, color: '#f59e0b', showLines: true });
                }
                drawGraph();

                /* Update info */
                if (info && !removed) {
                    var quad = '';
                    if (nx > 0 && ny > 0) quad = 'Quadrant I (+, +)';
                    else if (nx < 0 && ny > 0) quad = 'Quadrant II (-, +)';
                    else if (nx < 0 && ny < 0) quad = 'Quadrant III (-, -)';
                    else if (nx > 0 && ny < 0) quad = 'Quadrant IV (+, -)';
                    else if (ny === 0 && nx !== 0) quad = 'x-axis';
                    else if (nx === 0 && ny !== 0) quad = 'y-axis';
                    else quad = 'Origin (0,0)';
                    info.innerHTML = '✅ Plotted <strong>(' + nx + ', ' + ny + ')</strong> in ' + quad;
                    info.className = 'cl-graph-info info-success';
                }
            });
        }
    }

    function clearGraph(canvasId) {
        if (activeGraphs[canvasId]) {
            activeGraphs[canvasId].points = [];
            /* Re-trigger the whole init to redraw blank */
            var infoId = canvasId.replace('graph-', 'ginfo-');
            initGraph(canvasId, infoId, { clickable: true, rangeX: [-10, 10], rangeY: [-10, 10] });
        }
    }

    function initSpiral(canvasId, infoId, sn) {
        var cv = $(canvasId); if (!cv) return;
        var ctx = cv.getContext('2d');
        var info = $(infoId);
        var btn = $('spiral-next-' + sn);
        var hypVal = $('spiral-hyp-' + sn);
        var irrVal = $('spiral-irr-' + sn);

        var w = cv.width, h = cv.height;
        var scale = 80;
        var centerX = w / 2 - 50, centerY = h / 2 + 50;
        var steps = 1;
        var maxSteps = 10;

        function draw() {
            ctx.clearRect(0, 0, w, h);
            ctx.fillStyle = '#1e293b'; ctx.fillRect(0, 0, w, h);

            /* Axes */
            ctx.strokeStyle = 'rgba(255,255,255,0.1)';
            ctx.beginPath(); ctx.moveTo(0, centerY); ctx.lineTo(w, centerY); ctx.moveTo(centerX, 0); ctx.lineTo(centerX, h); ctx.stroke();

            var x = 1, y = 0;
            var prevX = 0, prevY = 0;

            for (var i = 1; i <= steps; i++) {
                var angle = Math.atan2(y, x);
                var nextAngle = angle + Math.atan2(1, Math.sqrt(i));
                var nextLen = Math.sqrt(i + 1);
                var nx = nextLen * Math.cos(nextAngle);
                var ny = nextLen * Math.sin(nextAngle);

                /* Triangle */
                ctx.beginPath();
                ctx.moveTo(centerX, centerY);
                ctx.lineTo(centerX + x * scale, centerY - y * scale);
                ctx.lineTo(centerX + nx * scale, centerY - ny * scale);
                ctx.closePath();
                ctx.fillStyle = 'rgba(124, 58, 237, ' + (0.1 + i * 0.05) + ')';
                ctx.fill();
                ctx.strokeStyle = i === steps ? '#a78bfa' : 'rgba(167, 139, 250, 0.3)';
                ctx.stroke();

                /* Project to number line if last step */
                if (i === steps) {
                    ctx.setLineDash([5, 5]);
                    ctx.beginPath();
                    ctx.arc(centerX, centerY, nextLen * scale, 0, Math.PI * 2);
                    ctx.strokeStyle = 'rgba(16, 185, 129, 0.3)';
                    ctx.stroke();
                    ctx.setLineDash([]);

                    ctx.beginPath();
                    ctx.moveTo(centerX + nextLen * scale, centerY - 10);
                    ctx.lineTo(centerX + nextLen * scale, centerY + 10);
                    ctx.strokeStyle = '#10b981';
                    ctx.lineWidth = 3;
                    ctx.stroke();
                    ctx.lineWidth = 1;

                    if (hypVal) hypVal.textContent = '√' + (i + 1);
                    if (irrVal) irrVal.textContent = (Math.sqrt(i + 1)).toFixed(4) + '...';
                }

                x = nx; y = ny;
            }

            if (info) info.innerHTML = 'Showing <strong>√' + (steps + 1) + '</strong> construction step.';
        }

        if (btn) {
            btn.onclick = function () {
                steps = (steps % maxSteps) + 1;
                draw();
            };
        }
        draw();
    }

    function init() { renderUI(); }
    if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init);
    else init();

    window.CL = { completeStep: completeStep, selectOpt: selectOpt, selectPrecheck: selectPrecheck, selectChapterTest: selectChapterTest, loadChapter: loadChapter, initGraph: initGraph, clearGraph: clearGraph, initSpiral: initSpiral };
})();
