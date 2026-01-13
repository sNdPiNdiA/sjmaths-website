// main.js

/* =========================================
   1. CONFIGURATION & STATE (Run Immediately)
   ========================================= */

// Theme Definitions (Keys match CSS variables directly)
const themes = {
    purple: { primary: '#8e44ad', 'primary-dark': '#6c3483', 'primary-light': '#a569bd', secondary: '#e74c3c', accent: '#f39c12' },
    blue: { primary: '#2563eb', 'primary-dark': '#1e40af', 'primary-light': '#60a5fa', secondary: '#0ea5e9', accent: '#22c55e' },
    green: { primary: '#16a34a', 'primary-dark': '#166534', 'primary-light': '#4ade80', secondary: '#22c55e', accent: '#facc15' },
    orange: { primary: '#f97316', 'primary-dark': '#c2410c', 'primary-light': '#fdba74', secondary: '#ef4444', accent: '#f59e0b' }
};

// Apply Saved States Immediately (Prevents FOUC)
const savedDark = localStorage.getItem('sjmaths-dark') === 'on';
if (savedDark) document.body.classList.add('dark-mode');

const savedTheme = localStorage.getItem('sjmaths-theme');
if (savedTheme && themes[savedTheme]) applyThemeVars(savedTheme);


/* =========================================
   2. THEME CONTROLLER
   ========================================= */

function applyThemeVars(themeName) {
    const theme = themes[themeName];
    if (!theme) return;

    const root = document.documentElement.style;
    Object.entries(theme).forEach(([key, value]) => {
        root.setProperty(`--${key}`, value);
    });
}

// Global function for UI buttons
window.setTheme = function (themeName) {
    applyThemeVars(themeName);
    localStorage.setItem('sjmaths-theme', themeName);
};


/* =========================================
   3. DARK MODE INTERACTION
   ========================================= */

document.addEventListener('DOMContentLoaded', () => {

    // Helper: Update Icon based on Body Class
    const updateToggleIcon = (btn) => {
        const icon = btn.querySelector('i');
        if (!icon) return;
        const isDark = document.body.classList.contains('dark-mode');
        icon.className = isDark ? 'fas fa-sun' : 'fas fa-moon';
    };

    // 1. Event Delegation: Handles clicks even if button loads late
    document.addEventListener('click', (e) => {
        const toggleBtn = e.target.closest('#darkToggle');
        if (!toggleBtn) return;

        // Toggle State
        const isDark = document.body.classList.toggle('dark-mode');
        localStorage.setItem('sjmaths-dark', isDark ? 'on' : 'off');

        // Update Icon
        updateToggleIcon(toggleBtn);
    });

    // 2. Initialization: Find button to set initial icon
    const initIconState = () => {
        const btn = document.getElementById('darkToggle');
        if (btn) {
            updateToggleIcon(btn);
            return true; // Found it
        }
        return false; // Not found
    };

    // Try immediately
    if (!initIconState()) {
        // If not found (e.g. loaded via component.js), wait for it
        const observer = new MutationObserver((mutations, obs) => {
            if (initIconState()) obs.disconnect(); // Stop watching once found
        });
        observer.observe(document.body, { childList: true, subtree: true });
    }
});