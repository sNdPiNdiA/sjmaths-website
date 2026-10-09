function switchTab(tabId) {
    document.querySelectorAll('.sub-nav-item').forEach(btn => {
        btn.classList.toggle('active', btn.getAttribute('data-tab') === tabId);
    });
    document.querySelectorAll('.tab-content').forEach(content => {
        content.style.display = (content.id === `tab-${tabId}`) ? 'block' : 'none';
    });
    window.scrollTo({ top: document.querySelector('.subject-nav').offsetTop - 80, behavior: 'smooth' });
    if (window.MathJax && window.MathJax.typesetPromise) {
        window.MathJax.typesetPromise();
    }
}

function bindTabs() {
    document.querySelectorAll('.sub-nav-item').forEach(btn => {
        btn.addEventListener('click', () => switchTab(btn.getAttribute('data-tab')));
    });
}

if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', bindTabs);
} else {
    bindTabs();
}
