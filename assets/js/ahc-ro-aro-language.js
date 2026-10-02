function toggleLanguage() {
            const currentLang = localStorage.getItem('sjmaths_preferred_language') === 'hi' ? 'en' : 'hi';
            localStorage.setItem('sjmaths_preferred_language', currentLang);
            document.documentElement.lang = currentLang;
            if (currentLang === 'hi') {
                document.body.classList.add('lang-mode-hi');
                document.body.classList.remove('lang-mode-en');
            } else {
                document.body.classList.add('lang-mode-en');
                document.body.classList.remove('lang-mode-hi');
            }
            const btnTexts = document.querySelectorAll('#langBtnText, #mobileLangBtnText, #navLangText');
            btnTexts.forEach(el => el.textContent = currentLang === 'hi' ? 'English' : 'हिन्दी');
            if (window.location.reload) {
                window.location.reload();
            }
        }
        document.addEventListener('DOMContentLoaded', () => {
            const prefLang = localStorage.getItem('sjmaths_preferred_language') || 'en';
            document.documentElement.lang = prefLang;
            if (prefLang === 'hi') {
                document.body.classList.add('lang-mode-hi');
            }
            const btnTexts = document.querySelectorAll('#langBtnText, #mobileLangBtnText, #navLangText');
            btnTexts.forEach(el => el.textContent = prefLang === 'hi' ? 'English' : 'हिन्दी');
        });
