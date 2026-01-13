/* ==========================================
   SJMATHS - DYNAMIC FOOTER LOADER
   Loads footer across all pages
   ========================================== */

'use strict';

document.addEventListener('DOMContentLoaded', function() {
    loadFooter();
});

function loadFooter() {
    const currentYear = new Date().getFullYear();
    
    const footerHTML = `
        <div class="container">
            <div class="footer-content">
                <!-- About Section -->
                <div class="footer-section">
                    <div class="footer-logo">
                        <span class="logo-icon">📐</span>
                        <span>SJMaths</span>
                    </div>
                    <p style="color: var(--gray-400); line-height: 1.6; margin-top: 1rem;">
                        Making mathematics accessible, engaging, and easy to learn for all students. 
                        Comprehensive study materials for Class 9, 10, 11 & 12.
                    </p>
                    <div style="margin-top: 1rem;">
                        <p style="color: var(--gray-400); font-size: 0.875rem;">
                            📧 Email: contact@sjmaths.com<br>
                            📱 Phone: +91 12345 67890
                        </p>
                    </div>
                </div>

                <!-- Quick Links -->
                <div class="footer-section">
                    <h3>Quick Links</h3>
                    <ul class="footer-links">
                        <li><a href="/index.html">Home</a></li>
                        <li><a href="/pages/about.html">About Us</a></li>
                        <li><a href="/pages/contact.html">Contact</a></li>
                        <li><a href="/pages/faq.html">FAQ</a></li>
                        <li><a href="/pages/support.html">Support</a></li>
                    </ul>
                </div>

                <!-- Classes -->
                <div class="footer-section">
                    <h3>Classes</h3>
                    <ul class="footer-links">
                        <li><a href="/classes/class-9/index.html">Class 9 Mathematics</a></li>
                        <li><a href="/classes/class-10/index.html">Class 10 Mathematics</a></li>
                        <li><a href="/classes/class-11/index.html">Class 11 Mathematics</a></li>
                        <li><a href="/classes/class-12/index.html">Class 12 Mathematics</a></li>
                    </ul>
                </div>

                <!-- Resources & Legal -->
                <div class="footer-section">
                    <h3>Resources</h3>
                    <ul class="footer-links">
                        <li><a href="/pages/sample-papers.html">Sample Papers</a></li>
                        <li><a href="/pages/previous-years.html">Previous Years</a></li>
                        <li><a href="/pages/formulas.html">Important Formulas</a></li>
                    </ul>
                    <h3 style="margin-top: 1.5rem;">Legal</h3>
                    <ul class="footer-links">
                        <li><a href="/pages/privacy-policy.html">Privacy Policy</a></li>
                        <li><a href="/pages/terms.html">Terms of Service</a></li>
                        <li><a href="/pages/disclaimer.html">Disclaimer</a></li>
                    </ul>
                </div>
            </div>

            <!-- Footer Bottom -->
            <div class="footer-bottom">
                <p>&copy; ${currentYear} SJMaths. All rights reserved. Made with ❤️ for students by passionate educators.</p>
                <div style="margin-top: 0.5rem;">
                    <a href="#" style="color: var(--gray-500); text-decoration: none; margin: 0 0.5rem; transition: color 0.3s;" 
                       onmouseover="this.style.color='white'" 
                       onmouseout="this.style.color='var(--gray-500)'">Facebook</a>
                    <span style="color: var(--gray-700);">|</span>
                    <a href="#" style="color: var(--gray-500); text-decoration: none; margin: 0 0.5rem; transition: color 0.3s;"
                       onmouseover="this.style.color='white'" 
                       onmouseout="this.style.color='var(--gray-500)'">Twitter</a>
                    <span style="color: var(--gray-700);">|</span>
                    <a href="#" style="color: var(--gray-500); text-decoration: none; margin: 0 0.5rem; transition: color 0.3s;"
                       onmouseover="this.style.color='white'" 
                       onmouseout="this.style.color='var(--gray-500)'">Instagram</a>
                    <span style="color: var(--gray-700);">|</span>
                    <a href="#" style="color: var(--gray-500); text-decoration: none; margin: 0 0.5rem; transition: color 0.3s;"
                       onmouseover="this.style.color='white'" 
                       onmouseout="this.style.color='var(--gray-500)'">YouTube</a>
                </div>
            </div>
        </div>
    `;

    // Insert footer into the page
    const footerElement = document.getElementById('footer');
    if (footerElement) {
        footerElement.innerHTML = footerHTML;
    }
    
    // Initialize footer animations
    initFooterAnimations();
}

function initFooterAnimations() {
    // Animate footer links on hover
    const footerLinks = document.querySelectorAll('.footer-links a');
    footerLinks.forEach(link => {
        link.addEventListener('mouseenter', function() {
            this.style.transform = 'translateX(5px)';
            this.style.color = 'var(--text-white)';
        });
        
        link.addEventListener('mouseleave', function() {
            this.style.transform = 'translateX(0)';
            this.style.color = 'var(--gray-400)';
        });
    });
    
    // Add scroll reveal animation to footer
    const footer = document.querySelector('footer');
    if (footer) {
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.style.animation = 'fadeInUp 0.8s ease-out';
                    observer.unobserve(entry.target);
                }
            });
        }, { threshold: 0.1 });
        
        observer.observe(footer);
    }
}