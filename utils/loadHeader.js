/* ==========================================
   SJMATHS - DYNAMIC HEADER LOADER
   Loads header navigation across all pages
   ========================================== */

'use strict';

document.addEventListener('DOMContentLoaded', function() {
    loadHeader();
});

function loadHeader() {
    const headerHTML = `
        <div class="container">
            <div class="nav-container">
                <!-- Logo -->
                <a href="/index.html" class="logo">
                    <span class="logo-icon">📐</span>
                    <span>SJMaths</span>
                </a>

                <!-- Desktop Navigation -->
                <nav class="nav-desktop">
                    <a href="/index.html" class="nav-link">
                        Home
                    </a>
                    
                    <!-- Class 9 Dropdown -->
                    <div class="nav-item dropdown">
                        <a href="/classes/class-9/index.html" class="nav-link dropdown-toggle">
                            Class 9 <span>▼</span>
                        </a>
                        <div class="dropdown-menu">
                            <a href="/classes/class-9/chapter-wise-notes/index.html" class="dropdown-item">Chapter-wise Notes</a>
                            <a href="/classes/class-9/ncert-exercise-practice/index.html" class="dropdown-item">NCERT Exercise Practice</a>
                            <a href="/classes/class-9/pyqs-chapter-wise/index.html" class="dropdown-item">PYQs Chapter-wise</a>
                            <a href="/classes/class-9/sample-papers/index.html" class="dropdown-item">Sample Papers</a>
                            <a href="/classes/class-9/worksheets/index.html" class="dropdown-item">Worksheets</a>
                        </div>
                    </div>
                    
                    <!-- Class 10 Dropdown -->
                    <div class="nav-item dropdown">
                        <a href="/classes/class-10/index.html" class="nav-link dropdown-toggle">
                            Class 10 <span>▼</span>
                        </a>
                        <div class="dropdown-menu">
                            <a href="/classes/class-10/chapter-wise-notes/index.html" class="dropdown-item">Chapter-wise Notes</a>
                            <a href="/classes/class-10/live-class/index.html" class="dropdown-item">Live Classes</a>
                            <a href="/classes/class-10/ncert-exercise-practice/index.html" class="dropdown-item">NCERT Exercise Practice</a>
                            <a href="/classes/class-10/pyqs-chapter-wise/index.html" class="dropdown-item">PYQs Chapter-wise</a>
                            <a href="/classes/class-10/quiz-based-on-pyqs/index.html" class="dropdown-item">Quiz Based on PYQs</a>
                            <a href="/classes/class-10/sample-papers/index.html" class="dropdown-item">Sample Papers</a>
                            <a href="/classes/class-10/unit-wise-and-full-length-test/index.html" class="dropdown-item">Unit & Full Tests</a>
                            <a href="/classes/class-10/worksheets/index.html" class="dropdown-item">Worksheets</a>
                        </div>
                    </div>
                    
                    <!-- Class 11 Dropdown -->
                    <div class="nav-item dropdown">
                        <a href="/classes/class-11/index.html" class="nav-link dropdown-toggle">
                            Class 11 <span>▼</span>
                        </a>
                        <div class="dropdown-menu">
                            <a href="/classes/class-11/chapter-wise-notes/index.html" class="dropdown-item">Chapter-wise Notes</a>
                            <a href="/classes/class-11/ncert-exercise-practice/index.html" class="dropdown-item">NCERT Solutions</a>
                            <a href="/classes/class-11/sample-papers/index.html" class="dropdown-item">Sample Papers</a>
                            <a href="/classes/class-11/worksheets/index.html" class="dropdown-item">Worksheets</a>
                        </div>
                    </div>
                    
                    <!-- Class 12 Dropdown -->
                    <div class="nav-item dropdown">
                        <a href="/classes/class-12/index.html" class="nav-link dropdown-toggle">
                            Class 12 <span>▼</span>
                        </a>
                        <div class="dropdown-menu">
                            <a href="/classes/class-12/chapter-wise-notes/index.html" class="dropdown-item">Chapter-wise Notes</a>
                            <a href="/classes/class-12/ncert-exercise-practice/index.html" class="dropdown-item">NCERT Solutions</a>
                            <a href="/classes/class-12/sample-papers/index.html" class="dropdown-item">Sample Papers</a>
                            <a href="/classes/class-12/worksheets/index.html" class="dropdown-item">Worksheets</a>
                        </div>
                    </div>
                    
                    <a href="/pages/about.html" class="nav-link">About</a>
                    <a href="/pages/contact.html" class="nav-link">Contact</a>
                </nav>

                <!-- Mobile Menu Toggle -->
                <button class="mobile-menu-toggle" id="mobileMenuToggle" aria-label="Toggle navigation menu">
                    <div class="hamburger" id="hamburger">
                        <span></span>
                        <span></span>
                        <span></span>
                    </div>
                </button>
            </div>

            <!-- Mobile Navigation -->
            <nav class="nav-mobile" id="mobileNav">
                <a href="/index.html" class="nav-mobile-link">Home</a>
                
                <!-- Class 9 Mobile Dropdown -->
                <div class="dropdown-mobile">
                    <button class="nav-mobile-link" onclick="toggleMobileDropdown('class9Dropdown')" type="button">
                        Class 9 <span>▼</span>
                    </button>
                    <div class="dropdown-menu-mobile" id="class9Dropdown">
                        <a href="/classes/class-9/chapter-wise-notes/index.html" class="dropdown-item">Chapter-wise Notes</a>
                        <a href="/classes/class-9/ncert-exercise-practice/index.html" class="dropdown-item">NCERT Exercise Practice</a>
                        <a href="/classes/class-9/pyqs-chapter-wise/index.html" class="dropdown-item">PYQs Chapter-wise</a>
                        <a href="/classes/class-9/sample-papers/index.html" class="dropdown-item">Sample Papers</a>
                        <a href="/classes/class-9/worksheets/index.html" class="dropdown-item">Worksheets</a>
                    </div>
                </div>
                
                <!-- Class 10 Mobile Dropdown -->
                <div class="dropdown-mobile">
                    <button class="nav-mobile-link" onclick="toggleMobileDropdown('class10Dropdown')" type="button">
                        Class 10 <span>▼</span>
                    </button>
                    <div class="dropdown-menu-mobile" id="class10Dropdown">
                        <a href="/classes/class-10/chapter-wise-notes/index.html" class="dropdown-item">Chapter-wise Notes</a>
                        <a href="/classes/class-10/live-class/index.html" class="dropdown-item">Live Classes</a>
                        <a href="/classes/class-10/ncert-exercise-practice/index.html" class="dropdown-item">NCERT Exercise Practice</a>
                        <a href="/classes/class-10/pyqs-chapter-wise/index.html" class="dropdown-item">PYQs Chapter-wise</a>
                        <a href="/classes/class-10/quiz-based-on-pyqs/index.html" class="dropdown-item">Quiz Based on PYQs</a>
                        <a href="/classes/class-10/sample-papers/index.html" class="dropdown-item">Sample Papers</a>
                        <a href="/classes/class-10/unit-wise-and-full-length-test/index.html" class="dropdown-item">Unit & Full Tests</a>
                        <a href="/classes/class-10/worksheets/index.html" class="dropdown-item">Worksheets</a>
                    </div>
                </div>
                
                <!-- Class 11 Mobile Dropdown -->
                <div class="dropdown-mobile">
                    <button class="nav-mobile-link" onclick="toggleMobileDropdown('class11Dropdown')" type="button">
                        Class 11 <span>▼</span>
                    </button>
                    <div class="dropdown-menu-mobile" id="class11Dropdown">
                        <a href="/classes/class-11/chapter-wise-notes/index.html" class="dropdown-item">Chapter-wise Notes</a>
                        <a href="/classes/class-11/ncert-exercise-practice/index.html" class="dropdown-item">NCERT Solutions</a>
                        <a href="/classes/class-11/sample-papers/index.html" class="dropdown-item">Sample Papers</a>
                        <a href="/classes/class-11/worksheets/index.html" class="dropdown-item">Worksheets</a>
                    </div>
                </div>
                
                <!-- Class 12 Mobile Dropdown -->
                <div class="dropdown-mobile">
                    <button class="nav-mobile-link" onclick="toggleMobileDropdown('class12Dropdown')" type="button">
                        Class 12 <span>▼</span>
                    </button>
                    <div class="dropdown-menu-mobile" id="class12Dropdown">
                        <a href="/classes/class-12/chapter-wise-notes/index.html" class="dropdown-item">Chapter-wise Notes</a>
                        <a href="/classes/class-12/ncert-exercise-practice/index.html" class="dropdown-item">NCERT Solutions</a>
                        <a href="/classes/class-12/sample-papers/index.html" class="dropdown-item">Sample Papers</a>
                        <a href="/classes/class-12/worksheets/index.html" class="dropdown-item">Worksheets</a>
                    </div>
                </div>
                
                <a href="/pages/about.html" class="nav-mobile-link">About</a>
                <a href="/pages/contact.html" class="nav-mobile-link">Contact</a>
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
    const hamburger = document.getElementById('hamburger');
    
    if (!toggle || !nav) return;
    
    // Toggle mobile menu
    toggle.addEventListener('click', (e) => {
        e.stopPropagation();
        nav.classList.toggle('active');
        if (hamburger) {
            hamburger.classList.toggle('active');
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
                if (hamburger) hamburger.classList.remove('active');
                document.body.style.overflow = '';
            }
        }
    });
    
    // Close menu on escape key
    document.addEventListener('keydown', (event) => {
        if (event.key === 'Escape') {
            if (nav.classList.contains('active')) {
                nav.classList.remove('active');
                if (hamburger) hamburger.classList.remove('active');
                document.body.style.overflow = '';
            }
        }
    });
}

// Global function for mobile dropdown toggle
window.toggleMobileDropdown = function(dropdownId) {
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