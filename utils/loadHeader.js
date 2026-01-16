/* ==========================================
   SJMATHS - DYNAMIC HEADER LOADER
   Loads header navigation across all pages
   ========================================== */

'use strict';

// Configuration: Single Source of Truth for Navigation
const navConfig = [
    { label: 'Home', href: '/index.html' },
    { label: 'Class 9', href: '/classes/class-9/index.html' },
    { label: 'Class 10', href: '/classes/class-10/index.html' },
    { label: 'Class 11', href: '/classes/class-11/index.html' },
    { label: 'Class 12', href: '/classes/class-12/index.html' },
    { label: 'About', href: '/pages/about.html' },
    { label: 'Contact', href: '/pages/contact.html' }
];

function loadHeader() {
    // Generate Desktop Navigation
    const desktopNavHTML = navConfig.map(item => {
        if (item.dropdown) {
            return `
                <li class="nav-item dropdown">
                    <a href="${item.href}" class="nav-link dropdown-toggle">
                        ${item.label} <span>▼</span>
                    </a>
                    <div class="dropdown-menu">
                        ${item.dropdown.map(sub => `<a href="${sub.href}" class="dropdown-item">${sub.label}</a>`).join('')}
                    </div>
                </li>`;
        }
        return `<li><a href="${item.href}" class="nav-link">${item.label}</a></li>`;
    }).join('');

    const headerHTML = `
        <style>
            /* Injected styles for better mobile responsiveness */
            .nav-container {
                display: flex;
                align-items: center;
                justify-content: space-between;
                width: 100%;
            }
            .nav-controls {
                display: flex;
                align-items: center;
                gap: 15px;
            }
            /* Mobile Drawer & Layout */
            @media (max-width: 768px) {
                .search-wrapper { display: none; } /* Hide search on mobile to prevent overflow */
                
                /* Install Button Mobile Styles */
                .install-app-btn .btn-text { display: none !important; }
                .install-app-btn {
                    width: 40px;
                    height: 40px;
                    padding: 0;
                    border-radius: 50%;
                    justify-content: center;
                    display: flex;
                    align-items: center;
                }
                .install-app-btn i { margin: 0 !important; }
                
                /* Reorder Header Elements: Hamburger Left, Logo Center/Left, Controls Right */
                .nav-controls {
                    display: contents; /* Allows children to be reordered in the main grid */
                }
                .mobile-toggle {
                    order: -1;
                    margin-right: 10px;
                    display: flex;
                    z-index: 1002; /* Ensure above drawer */
                }
                .logo {
                    margin-right: auto;
                }
                
                /* Mobile Drawer Styles */
                #mainNav {
                    position: fixed;
                    top: 0;
                    left: -100%;
                    width: 280px;
                    height: 100vh;
                    background: var(--bg-card, #ffffff);
                    box-shadow: 2px 0 10px rgba(0,0,0,0.1);
                    z-index: 1001;
                    transition: left 0.3s ease;
                    padding-top: 80px; /* Space for header */
                    display: flex;
                    flex-direction: column;
                }
                #mainNav.active {
                    left: 0;
                }
                #mainNav ul {
                    flex-direction: column;
                    gap: 0;
                }
                #mainNav a {
                    display: block;
                    padding: 15px 25px;
                    border-bottom: 1px solid rgba(0,0,0,0.05);
                }
            }
            @media (max-width: 360px) {
                .logo { font-size: 1.2rem; }
            }
        </style>
        <div class="container">
            <div class="nav-container">
                <!-- Logo -->
                <a href="/index.html" class="logo">
                    <span class="logo-icon">&int;</span>
                    <span>SJMaths</span>
                </a>

                <!-- Search Bar -->
                <div class="search-wrapper">
                    <div class="header-search">
                        <button><i class="fas fa-search"></i></button>
                        <label class="sr-only">Search</label>
                        <input type="text" placeholder="Search for chapters, notes...">
                        <div class="search-results"></div>
                    </div>
                </div>

                <!-- Unified Navigation -->
                <nav id="mainNav">
                    <ul>
                        ${desktopNavHTML}
                        <li><a href="/login.html" class="nav-btn" id="authBtn">Login</a></li>
                    </ul>
                </nav>

                <!-- Controls (Dark Mode & Mobile Toggle) -->
                <div class="nav-controls">
                    <button id="darkToggle" class="theme-toggle-btn" aria-label="Toggle Dark Mode">
                        <i class="fas fa-moon"></i>
                    </button>

                    <button class="mobile-toggle" id="mobileMenuToggle" aria-label="Toggle navigation menu">
                        <i class="fas fa-bars"></i>
                    </button>
                </div>
            </div>
        </div>
    `;

    // Insert header into the page
    const headerElement = document.getElementById('header');
    if (headerElement) {
        headerElement.innerHTML = headerHTML;
    }
}

// Global function for mobile dropdown toggle
window.toggleMobileDropdown = function (dropdownId) {
    const dropdown = document.getElementById(dropdownId);
    if (!dropdown) return;

    // Close other dropdowns
    document.querySelectorAll('.dropdown-menu-mobile.active').forEach(menu => {
        if (menu.id !== dropdownId) {
            menu.classList.remove('active');
            const button = menu.previousElementSibling;
            if (button) {
                const arrow = button.querySelector('span:last-child');
                if (arrow) arrow.textContent = '▼';
            }
        }
    });

    // Toggle current dropdown
    dropdown.classList.toggle('active');

    // Update arrow
    const button = dropdown.previousElementSibling;
    if (button) {
        const arrow = button.querySelector('span:last-child');
        if (arrow) {
            arrow.textContent = dropdown.classList.contains('active') ? '▲' : '▼';
        }
    }
};

if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', loadHeader);
} else {
    loadHeader();
}