document.addEventListener('DOMContentLoaded', () => {
    // Create Toggle Button
    const btn = document.createElement('button');
    btn.id = 'testThemeToggle';
    btn.innerHTML = '<i class="fas fa-moon"></i>';
    btn.setAttribute('aria-label', 'Toggle Dark Mode');
    
    // Style the button
    Object.assign(btn.style, {
        position: 'fixed',
        bottom: '80px', // Positioned above footer/nav buttons
        left: '20px',
        width: '45px',
        height: '45px',
        borderRadius: '50%',
        border: 'none',
        background: '#2c3e50',
        color: '#fff',
        boxShadow: '0 4px 10px rgba(0,0,0,0.2)',
        zIndex: '10000',
        cursor: 'pointer',
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'center',
        fontSize: '1.2rem',
        transition: 'all 0.3s ease'
    });

    document.body.appendChild(btn);

    // Function to set theme
    const setTheme = (isDark) => {
        if (isDark) {
            document.body.classList.add('dark-mode');
            btn.innerHTML = '<i class="fas fa-sun"></i>';
            btn.style.background = '#fff';
            btn.style.color = '#2c3e50';
        } else {
            document.body.classList.remove('dark-mode');
            btn.innerHTML = '<i class="fas fa-moon"></i>';
            btn.style.background = '#2c3e50';
            btn.style.color = '#fff';
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