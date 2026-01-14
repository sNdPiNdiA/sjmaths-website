/* ==========================================
   SJMATHS - DYNAMIC FOOTER LOADER
   Loads footer across all pages
   ========================================== */

'use strict';

document.addEventListener('DOMContentLoaded', function () {
    loadFooter();
});

// Configuration: Single Source of Truth for Footer
const footerConfig = {
    about: {
        logoIcon: '&int;',
        logoText: 'SJMaths',
        description: 'Making mathematics accessible, engaging, and easy to learn for all students. Comprehensive study materials for Class 9, 10, 11 & 12.',
        contact: {
            email: 'contact@sjmaths.com',
            phone: '+91 12345 67890'
        }
    },
    sections: [
        {
            groups: [
                {
                    title: 'Quick Links',
                    links: [
                        { label: 'Home', href: '/index.html' },
                        { label: 'About Us', href: '/pages/about.html' },
                        { label: 'Contact', href: '/pages/contact.html' },
                        { label: 'FAQ', href: '/pages/faq.html' },
                        { label: 'Support', href: '/pages/support.html' }
                    ]
                }
            ]
        },
        {
            groups: [
                {
                    title: 'Classes',
                    links: [
                        { label: 'Class 9 Mathematics', href: '/classes/class-9/index.html' },
                        { label: 'Class 10 Mathematics', href: '/classes/class-10/index.html' },
                        { label: 'Class 11 Mathematics', href: '/classes/class-11/index.html' },
                        { label: 'Class 12 Mathematics', href: '/classes/class-12/index.html' }
                    ]
                }
            ]
        },
        {
            groups: [
                {
                    title: 'Resources',
                    links: [
                        { label: 'Sample Papers', href: '/pages/sample-papers.html' },
                        { label: 'Previous Years', href: '/pages/previous-years.html' },
                        { label: 'Important Formulas', href: '/pages/formulas.html' }
                    ]
                },
                {
                    title: 'Legal',
                    marginTop: '1.5rem',
                    links: [
                        { label: 'Privacy Policy', href: '/pages/privacy-policy.html' },
                        { label: 'Terms of Service', href: '/pages/terms.html' },
                        { label: 'Disclaimer', href: '/pages/disclaimer.html' }
                    ]
                }
            ]
        }
    ],
    social: [
        { label: 'Facebook', href: '#' },
        { label: 'Twitter', href: '#' },
        { label: 'Instagram', href: '#' },
        { label: 'YouTube', href: '#' }
    ]
};

function loadFooter() {
    const currentYear = new Date().getFullYear();

    // Generate Sections HTML
    const sectionsHTML = footerConfig.sections.map(section => {
        const groupsHTML = section.groups.map(group => {
            const style = group.marginTop ? `style="margin-top: ${group.marginTop}"` : '';
            const linksHTML = group.links.map(link =>
                `<li><a href="${link.href}">${link.label}</a></li>`
            ).join('');

            return `
                <h3 ${style}>${group.title}</h3>
                <ul class="footer-links">
                    ${linksHTML}
                </ul>
            `;
        }).join('');

        return `<div class="footer-col">${groupsHTML}</div>`;
    }).join('');

    // Generate Social Links HTML
    const socialHTML = footerConfig.social.map((link, index) => {
        const separator = index < footerConfig.social.length - 1
            ? `<span style="color: var(--gray-700);">|</span>`
            : '';
        return `
            <a href="${link.href}" style="color: var(--gray-500); text-decoration: none; margin: 0 0.5rem; transition: color 0.3s;" 
               onmouseover="this.style.color='white'" 
               onmouseout="this.style.color='var(--gray-500)'">${link.label}</a>
            ${separator}
        `;
    }).join('');

    const footerHTML = `
        <div class="container">
            <div class="footer-grid">
                <!-- About Section -->
                <div class="footer-col footer-brand">
                    <h2>
                        <span class="logo-icon">${footerConfig.about.logoIcon}</span>
                        <span>${footerConfig.about.logoText}</span>
                    </h2>
                    <p style="color: var(--gray-400); line-height: 1.6; margin-top: 1rem;">
                        ${footerConfig.about.description}
                    </p>
                    <div style="margin-top: 1rem;">
                        <p style="color: var(--gray-400); font-size: 0.875rem;">
                            📧 Email: ${footerConfig.about.contact.email}<br>
                            📱 Phone: ${footerConfig.about.contact.phone}
                        </p>
                    </div>
                </div>

                ${sectionsHTML}
            </div>

            <!-- Footer Bottom -->
            <div class="footer-bottom">
                <p>&copy; ${currentYear} ${footerConfig.about.logoText}. All rights reserved. Made with ❤️ for students by passionate educators.</p>
                <div style="margin-top: 0.5rem;">
                    ${socialHTML}
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
        link.addEventListener('mouseenter', function () {
            this.style.transform = 'translateX(5px)';
            this.style.color = 'var(--text-white)';
        });

        link.addEventListener('mouseleave', function () {
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