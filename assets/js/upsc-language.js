(function () {
            const btnEn = document.getElementById('langEn');
            const btnHi = document.getElementById('langHi');
            const apply = (lang) => {
                document.documentElement.classList.toggle('lang-hi', lang === 'hi');
                document.documentElement.classList.toggle('lang-en', lang !== 'hi');
                document.body.classList.toggle('lang-hi', lang === 'hi');
                document.body.classList.toggle('lang-en', lang !== 'hi');
                if (btnEn) btnEn.classList.toggle('active', lang !== 'hi');
                if (btnHi) btnHi.classList.toggle('active', lang === 'hi');
                if (btnEn) btnEn.setAttribute('aria-pressed', String(lang !== 'hi'));
                if (btnHi) btnHi.setAttribute('aria-pressed', String(lang === 'hi'));
                try { localStorage.setItem('sj_pref_lang', lang); } catch (e) { }
            };
            document.addEventListener('DOMContentLoaded', () => {
                const pref = (localStorage.getItem('sj_pref_lang') || 'en');
                apply(pref);
                if (btnEn) btnEn.addEventListener('click', () => apply('en'));
                if (btnHi) btnHi.addEventListener('click', () => apply('hi'));
            });
        })();
