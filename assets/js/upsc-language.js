(function () {
            const btnEn = document.getElementById('langEn');
            const btnHi = document.getElementById('langHi');
            const examUI = document.body.classList.contains('exam-ui');
            const pathname = typeof window !== 'undefined' && window.location ? window.location.pathname : '';
            const devanagariOnly = /^\/up-assistant-teacher\/(?:hindi|sanskrit)(?:\/|$)/i.test(pathname);
            const pageLanguage = /^\/up-assistant-teacher\/sanskrit(?:\/|$)/i.test(pathname) ? 'sa' : 'hi';
            const apply = (lang) => {
                if (devanagariOnly) lang = 'hi';
                document.documentElement.classList.toggle('lang-hi', lang === 'hi');
                document.documentElement.classList.toggle('lang-en', lang !== 'hi');
                document.body.classList.toggle('lang-hi', lang === 'hi');
                document.body.classList.toggle('lang-en', lang !== 'hi');
                if (examUI) {
                    document.querySelectorAll('.lang-hi, .lang-en').forEach(element => {
                        if (element.style.display === 'none') element.style.removeProperty('display');
                    });
                    document.body.classList.toggle('lang-mode-hi', lang === 'hi');
                    document.documentElement.lang = lang;
                }
                if (btnEn) btnEn.classList.toggle('active', lang !== 'hi');
                if (btnHi) btnHi.classList.toggle('active', lang === 'hi');
                if (btnEn) btnEn.setAttribute('aria-pressed', String(lang !== 'hi'));
                if (btnHi) btnHi.setAttribute('aria-pressed', String(lang === 'hi'));
                if (devanagariOnly) {
                    document.body.classList.add('devanagari-only');
                    document.documentElement.lang = pageLanguage;
                    document.querySelectorAll('#langEn, #langHi, #headerLangToggleBtn, .lang-toggle, .lang-toggle-btn').forEach(control => control.remove());
                } else {
                    try { localStorage.setItem('sj_pref_lang', lang); } catch (e) { }
                }
                if (examUI) {
                    if (!devanagariOnly) {
                        try { localStorage.setItem('sjmaths_preferred_language', lang); } catch (e) { }
                    }
                    const headerText = document.getElementById('headerLangText');
                    if (headerText) headerText.textContent = lang === 'hi' ? 'English' : 'हिन्दी';
                    const headerButton = document.getElementById('headerLangToggleBtn');
                    if (headerButton) headerButton.setAttribute('aria-label', lang === 'hi' ? 'Switch to English' : 'हिन्दी में पढ़ें');
                }
            };
            document.addEventListener('DOMContentLoaded', () => {
                let pref = 'en';
                try { pref = ((examUI && localStorage.getItem('sjmaths_preferred_language')) || localStorage.getItem('sj_pref_lang') || 'en'); } catch (e) { }
                pref = pref === 'hi' ? 'hi' : 'en';
                apply(pref);
                if (examUI) document.addEventListener('sjmaths:component-loaded', () => apply(document.body.classList.contains('lang-hi') ? 'hi' : 'en'));
                if (examUI) {
                    // One active controller for these exams, including content
                    // added by the renderer after the initial language selection.
                    document.addEventListener('click', (event) => {
                        const control = event.target.closest('#headerLangToggleBtn, #langEn, #langHi, .syllabus-container .lang-toggle-btn');
                        if (!control) return;
                        event.preventDefault();
                        event.stopImmediatePropagation();
                        const previousLang = document.body.classList.contains('lang-hi') ? 'hi' : 'en';
                        const lang = control.id === 'langEn' ? 'en' : control.id === 'langHi' ? 'hi' : document.body.classList.contains('lang-hi') ? 'en' : 'hi';
                        apply(lang);
                        if (lang !== previousLang) {
                            document.dispatchEvent(new CustomEvent('sjmaths:language-changed', { detail: { language: lang } }));
                        }
                    }, true);
                    return;
                }
                if (btnEn) btnEn.addEventListener('click', () => apply('en'));
                if (btnHi) btnHi.addEventListener('click', () => apply('hi'));
            });
        })();
