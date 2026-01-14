/* ==========================================
   SJMATHS - DYNAMIC HEADER LOADER
   Loads header navigation across all pages
   ========================================== */

'use strict';

document.addEventListener('DOMContentLoaded', function () {
    loadHeader();
});

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

    // Generate Mobile Navigation
    const mobileNavHTML = navConfig.map(item => {
        if (item.dropdown) {
            return `
                <div class="dropdown-mobile">
                    <button class="nav-mobile-link" onclick="toggleMobileDropdown('${item.id}Dropdown')" type="button">
                        ${item.label} <span>▼</span>
                    </button>
                    <div class="dropdown-menu-mobile" id="${item.id}Dropdown">
                        ${item.dropdown.map(sub => `<a href="${sub.href}" class="dropdown-item">${sub.label}</a>`).join('')}
                    </div>
                </div>`;
        }
        return `<li><a href="${item.href}" class="nav-mobile-link">${item.label}</a></li>`;
    }).join('');

    const headerHTML = `
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

                <!-- Desktop Navigation -->
                <nav class="nav-desktop">
                    <ul>
                        ${desktopNavHTML}
                        <li><a href="/login.html" class="nav-btn" id="authBtn">Login</a></li>
                    </ul>
                </nav>

                <!-- Controls (Dark Mode & Mobile Toggle) -->
                <div style="display: flex; align-items: center; gap: 15px;">
                    <button id="darkToggle" class="theme-toggle-btn" aria-label="Toggle Dark Mode">
                        <i class="fas fa-moon"></i>
                    </button>

                    <button class="mobile-menu-toggle" id="mobileMenuToggle" aria-label="Toggle navigation menu">
                        <i class="fas fa-bars"></i>
                    </button>
                </div>
            </div>

            <!-- Mobile Navigation -->
            <nav class="nav-mobile" id="mobileNav">
                <ul>
                    ${mobileNavHTML}
                    <li><a href="/login.html" class="nav-mobile-link" id="mobileAuthBtn">Login</a></li>
                </ul>
            </nav>
        </div>
    `;

    // Insert header into the page
    const headerElement = document.getElementById('header');
    if (headerElement) {
        headerElement.innerHTML = headerHTML;
    }

    // Initialize mobile menu after header is loaded
    initializeMobileMenuAfterLoad();
}

function initializeMobileMenuAfterLoad() {
    const toggle = document.getElementById('mobileMenuToggle');
    const nav = document.getElementById('mobileNav');

    if (!toggle || !nav) return;

    const icon = toggle.querySelector('i');

    // Toggle mobile menu
    toggle.addEventListener('click', (e) => {
        e.stopPropagation();
        nav.classList.toggle('active');

        if (icon) {
            icon.classList.toggle('fa-bars');
            icon.classList.toggle('fa-times');
        }

        // Prevent body scroll when menu is open
        if (nav.classList.contains('active')) {
            document.body.style.overflow = 'hidden';
        } else {
            document.body.style.overflow = '';
        }
    });

    // Close menu when clicking outside
    document.addEventListener('click', (event) => {
        if (!nav.contains(event.target) && !toggle.contains(event.target)) {
            if (nav.classList.contains('active')) {
                nav.classList.remove('active');
                if (icon) {
                    icon.classList.add('fa-bars');
                    icon.classList.remove('fa-times');
                }
                document.body.style.overflow = '';
            }
        }
    });

    // Close menu on escape key
    document.addEventListener('keydown', (event) => {
        if (event.key === 'Escape') {
            if (nav.classList.contains('active')) {
                nav.classList.remove('active');
                if (icon) {
                    icon.classList.add('fa-bars');
                    icon.classList.remove('fa-times');
                }
                document.body.style.overflow = '';
            }
        }
    });
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