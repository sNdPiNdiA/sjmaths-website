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
        body.dark-mode .timer-badge {
            background: #2c3e50 !important;
            border-color: #4a6278 !important;
            color: #ecf0f1 !important;
        }
        
        /* Nav Button Alignment */
        .nav-panel {
            gap: 15px; 
        }
        
        /* Hide potential duplicate toggles from main.js if they lack our ID */
        .theme-toggle:not(#testThemeToggle),
        button[aria-label="Toggle Dark Mode"]:not(#testThemeToggle) {
            display: none !important;
        }
    `;
    document.head.appendChild(style);

    // 2. Remove existing duplicate buttons (cleanup)
    const existingButtons = document.querySelectorAll('button[aria-label="Toggle Dark Mode"], .theme-toggle');
    existingButtons.forEach(btn => {
        if (btn.id !== 'testThemeToggle') {
            btn.style.display = 'none'; // Hide instead of remove to avoid JS errors in other scripts
            btn.setAttribute('aria-hidden', 'true');
        }
    });

    // 3. Create Toggle Button (if not already present with our ID)
    if (document.getElementById('testThemeToggle')) return;

    const btn = document.createElement('button');
    btn.id = 'testThemeToggle';
    btn.innerHTML = '<i class="fas fa-moon"></i>';
    btn.setAttribute('aria-label', 'Toggle Dark Mode');

    // Style the button
    Object.assign(btn.style, {
        position: 'fixed',
        bottom: '30px', /* Moved down to avoid overlapping with content */
        left: '30px',
        width: '50px',
        height: '50px',
        borderRadius: '50%',
        border: 'none',
        background: '#2c3e50',
        color: '#fff',
        boxShadow: '0 4px 15px rgba(0,0,0,0.3)',
        zIndex: '10000',
        cursor: 'pointer',
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'center',
        fontSize: '1.4rem',
        transition: 'all 0.3s ease'
    });

    document.body.appendChild(btn);

    // Function to set theme
    const setTheme = (isDark) => {
        if (isDark) {
            document.body.classList.add('dark-mode');
            btn.innerHTML = '<i class="fas fa-sun"></i>';
            btn.style.background = '#f1c40f'; // Yellow sun bg
            btn.style.color = '#2c3e50';
            btn.style.boxShadow = '0 0 15px rgba(241, 196, 15, 0.5)';
        } else {
            document.body.classList.remove('dark-mode');
            btn.innerHTML = '<i class="fas fa-moon"></i>';
            btn.style.background = '#2c3e50';
            btn.style.color = '#fff';
            btn.style.boxShadow = '0 4px 15px rgba(0,0,0,0.3)';
        }
        localStorage.setItem('sjmaths-test-dark', isDark);
    };

    // Initialize
    const savedTheme = localStorage.getItem('sjmaths-test-dark') === 'true';
    setTheme(savedTheme);

    // Event Listener
    btn.addEventListener('click', () => {
        const isDark = !document.body.classList.contains('dark-mode');
        setTheme(isDark);
    });
});
