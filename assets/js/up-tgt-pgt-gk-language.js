(function () {
  function initLanguage() {
    if (document.body.dataset.gkLanguageReady) return;
    const element = document.getElementById('bilingual-data');
    if (!element) return;
    document.body.dataset.gkLanguageReady = 'true';
    const data = JSON.parse(element.textContent || '{}');
    let preference = new URL(location.href).searchParams.get('lang');
    if (!['en', 'hi'].includes(preference)) {
      try { preference = localStorage.getItem('sjmaths_language'); } catch (error) {}
    }
    const language = preference === 'en' ? 'en' : 'hi';
    document.documentElement.lang = language;
    document.body.classList.toggle('language-hi', language === 'hi');
    if (language === 'hi') {
      Object.entries(data.elements || {}).forEach(([id, text]) => {
        const el = document.querySelector('[data-bilingual-id="' + id + '"]');
        if (el && text) el.textContent = text;
      });
      if (data.meta?.title) document.title = data.meta.title;
      if (data.meta?.description) {
        const meta = document.querySelector('meta[name="description"]');
        if (meta) meta.setAttribute('content', data.meta.description);
      }
    }
    const button = document.getElementById('btn-language-toggle');
    if (button) {
      button.textContent = language === 'hi' ? 'English' : 'हिन्दी';
      button.setAttribute('aria-label', language === 'hi' ? 'Switch to English' : 'हिन्दी में देखें');
      button.addEventListener('click', () => {
        if (button.disabled) return;
        button.disabled = true;
        const next = language === 'hi' ? 'en' : 'hi';
        const url = new URL(location.href);
        try {
          localStorage.setItem('sjmaths_language', next);
          url.searchParams.delete('lang');
        } catch (error) {
          // Preserve the requested language when browser storage is unavailable.
          url.searchParams.set('lang', next);
        }
        location.replace(url.href);
      });
    }
  }
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initLanguage, { once: true });
  } else initLanguage();
})();
