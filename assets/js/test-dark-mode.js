document.addEventListener('DOMContentLoaded', () => {
    // 1. Inject Styles for Timer and Dark Mode
    const style = document.createElement('style');
    style.textContent = `
        /* Timer Styling */
        .timer-badge {
            font-family: 'Inter', sans-serif;
            font-size: 1.1rem !important;
            font-weight: 700 !important;
            padding: 8px 15px !important;
            background: #fff !important;
            border: 2px solid #e9ecef !important;
            border-radius: 8px !important;
            color: #2c3e50 !important;
            box-shadow: 0 2px 5px rgba(0,0,0,0.05);
            transition: all 0.3s ease;
            display: flex;
            align-items: center;
            gap: 8px;
        }
        .timer-badge i {
            color: #e74c3c !important; /* Red clock icon */
        }
        
        /* Dark Mode Timer overrides */
        body.dark-mode .timer-badge,
        html.dark-mode .timer-badge {
            background: #1e293b !important;
            border-color: #334155 !important;
            color: #f8fafc !important;
        }
        
        /* Nav Button Alignment */
        .nav-panel {
            gap: 15px; 
        }
    `;
    document.head.appendChild(style);

    // 2. Delegate to global ThemeManager if available
    const getIsDark = () => {
        if (typeof window.isDarkMode === 'function') return window.isDarkMode();
        const sjDark = localStorage.getItem('sjmaths-dark');
        if (sjDark !== null) return sjDark === 'on';
        const legacyTheme = localStorage.getItem('theme');
        if (legacyTheme !== null) return legacyTheme === 'dark';
        const testDark = localStorage.getItem('sjmaths-test-dark');
        if (testDark !== null) return testDark === 'true';
        return window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches;
    };

    // If no dark mode toggle button exists on the page and none in main.js, ensure button exists
    let btn = document.getElementById('testThemeToggle') || document.getElementById('darkToggle');
    if (!btn) {
        btn = document.createElement('button');
        btn.id = 'testThemeToggle';
        btn.innerHTML = '<i class="fas fa-moon"></i>';
        btn.setAttribute('aria-label', 'Toggle Dark Mode');

        Object.assign(btn.style, {
            position: 'fixed',
            bottom: '30px',
            left: '30px',
            width: '50px',
            height: '50px',
            borderRadius: '50%',
            border: 'none',
            background: '#1e293b',
            color: '#fff',
            boxShadow: '0 4px 15px rgba(0,0,0,0.3)',
            zIndex: '10000',
            cursor: 'pointer',
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
            fontSize: '1.3rem',
            transition: 'all 0.3s ease'
        });

        document.body.appendChild(btn);
    }

    const updateBtn = (isDark) => {
        if (!btn) return;
        btn.innerHTML = isDark ? '<i class="fas fa-sun"></i>' : '<i class="fas fa-moon"></i>';
        btn.style.background = isDark ? '#ffffff' : '#1e293b';
        btn.style.color = isDark ? '#0f172a' : '#ffffff';
        btn.style.boxShadow = isDark ? '0 0 15px rgba(255, 255, 255, 0.3)' : '0 4px 15px rgba(0,0,0,0.3)';
    };

    const isCurrentDark = getIsDark();
    if (document.documentElement) {
        document.documentElement.classList.toggle('dark-mode', isCurrentDark);
        document.documentElement.setAttribute('data-theme', isCurrentDark ? 'dark' : 'light');
    }
    if (document.body) {
        document.body.classList.toggle('dark-mode', isCurrentDark);
    }
    updateBtn(isCurrentDark);

    btn.addEventListener('click', (e) => {
        e.preventDefault();
        if (typeof window.toggleDarkMode === 'function') {
            window.toggleDarkMode();
        } else {
            const nextDark = !document.body.classList.contains('dark-mode');
            document.documentElement.classList.toggle('dark-mode', nextDark);
            document.documentElement.setAttribute('data-theme', nextDark ? 'dark' : 'light');
            document.body.classList.toggle('dark-mode', nextDark);
            try {
                localStorage.setItem('sjmaths-dark', nextDark ? 'on' : 'off');
                localStorage.setItem('theme', nextDark ? 'dark' : 'light');
                localStorage.setItem('sjmaths-test-dark', nextDark ? 'true' : 'false');
            } catch(err) {}
            updateBtn(nextDark);
            window.dispatchEvent(new CustomEvent('themeChanged', { detail: { isDark: nextDark } }));
        }
    });

    window.addEventListener('themeChanged', (e) => {
        if (e && e.detail) {
            updateBtn(e.detail.isDark);
        }
    });
});
