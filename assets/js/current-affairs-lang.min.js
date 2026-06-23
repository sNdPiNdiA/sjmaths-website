// Language management for SJMaths Current Affairs Platform
document.addEventListener('DOMContentLoaded', () => {
  initLanguageToggle();
});

// Global Google Translate Init Callback
window.googleTranslateElementInit = function() {
  new google.translate.TranslateElement({
    pageLanguage: 'en',
    includedLanguages: 'en,hi',
    layout: google.translate.TranslateElement.InlineLayout.SIMPLE,
    autoDisplay: false
  }, 'google_translate_element');
};

// Utility to set/clear translation cookies
function setGoogleTranslateCookie(lang) {
  const cookieValue = lang === 'hi' ? '/en/hi' : '/en/en';
  document.cookie = "googtrans=" + cookieValue + "; path=/";
  document.cookie = "googtrans=" + cookieValue + "; path=/; domain=" + window.location.hostname;
  
  if (lang === 'en') {
    document.cookie = "googtrans=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;";
    document.cookie = "googtrans=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/; domain=" + window.location.hostname;
  }
}

function initLanguageToggle() {
  // 1. Ensure hidden translate element container exists in body
  if (!document.getElementById('google_translate_element')) {
    const gtDiv = document.createElement('div');
    gtDiv.id = 'google_translate_element';
    gtDiv.style.display = 'none';
    document.body.appendChild(gtDiv);
  }

  let currentLang = localStorage.getItem('sjmaths_preferred_language') || localStorage.getItem('sjmaths_ca_lang') || 'hi';
  localStorage.setItem('sjmaths_preferred_language', currentLang);
  localStorage.setItem('sjmaths_ca_lang', currentLang);
  setGoogleTranslateCookie(currentLang);

  // 3. Inject Google Translate Script dynamically with fallback
  const gtScript = document.createElement('script');
  gtScript.src = 'https://translate.google.com/translate_a/element.js?cb=googleTranslateElementInit';
  gtScript.async = true;
  
  gtScript.onerror = () => {
    console.warn("SJMaths: Failed to load Google Translate from translate.google.com. Trying fallback translate.googleapis.com...");
    const fallbackScript = document.createElement('script');
    fallbackScript.src = 'https://translate.googleapis.com/translate_a/element.js?cb=googleTranslateElementInit';
    fallbackScript.async = true;
    document.body.appendChild(fallbackScript);
  };
  document.body.appendChild(gtScript);

  // 4. Apply current language configuration
  if (currentLang === 'hi') {
    document.body.classList.remove('lang-en');
    document.body.classList.add('lang-hi');
  } else {
    document.body.classList.remove('lang-hi');
    document.body.classList.add('lang-en');
  }

  // 5. Bind Toggle Button click listeners
  const toggleBtn = document.getElementById('ca-lang-toggle');
  if (toggleBtn) {
    const updateToggleUI = (lang) => {
      toggleBtn.querySelectorAll('.ca-lang-option').forEach(opt => {
        if (opt.dataset.lang === lang) {
          opt.classList.add('active');
        } else {
          opt.classList.remove('active');
        }
      });
    };

    updateToggleUI(currentLang);

    toggleBtn.addEventListener('click', (e) => {
      const option = e.target.closest('.ca-lang-option');
      if (!option) return;
      
      const selectedLang = option.dataset.lang;
      if (selectedLang !== currentLang) {
        localStorage.setItem('sjmaths_preferred_language', selectedLang);
        localStorage.setItem('sjmaths_ca_lang', selectedLang);
        localStorage.setItem('ssc-cgl-lang', selectedLang);
        setGoogleTranslateCookie(selectedLang);
        
        // Reload to apply translation reliably
        location.reload();
      }
    });
  }
}

