/* --- 1. DARK MODE LOGIC --- */
function toggleTheme() {
    if (typeof window.toggleDarkMode === 'function') {
        window.toggleDarkMode();
        return;
    }

    const nextDark = !document.body.classList.contains('dark-mode');
    if (document.documentElement) {
        document.documentElement.classList.toggle('dark-mode', nextDark);
        document.documentElement.setAttribute('data-theme', nextDark ? 'dark' : 'light');
    }
    if (document.body) {
        document.body.classList.toggle('dark-mode', nextDark);
    }

    const btn = document.getElementById('themeToggle');
    if (btn) {
        btn.innerHTML = nextDark ? '☀' : '🌙';
    }

    try {
        localStorage.setItem('sjmaths-dark', nextDark ? 'on' : 'off');
        localStorage.setItem('theme', nextDark ? 'dark' : 'light');
        localStorage.setItem('sjmaths-test-dark', nextDark ? 'true' : 'false');
    } catch (e) {}

    window.dispatchEvent(new CustomEvent('themeChanged', { detail: { isDark: nextDark } }));
}