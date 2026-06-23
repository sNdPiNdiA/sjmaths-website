/**
 * Exercise Footer Component - Aligned with SJMaths Website Design
 * Creates a clean footer for all exercise pages with navigation
 */

(function () {
    'use strict';

    function initExerciseFooter() {
        // Check if footer already exists
        if (document.getElementById('exercise-page-footer')) return;

        // Build the footer
        const footer = document.createElement('footer');
        footer.id = 'exercise-page-footer';
        footer.className = 'exercise-page-footer';

        footer.innerHTML = `
            <div class="footer-nav" id="footerNav">
                <!-- Navigation populated from existing nav or empty -->
            </div>
            <div class="footer-brand">
                <a href="/" class="logo">
                    <span class="logo-symbol">&int;</span> SJMaths
                </a>
                <p class="copyright">&copy; ${new Date().getFullYear()} SJMaths. All Rights Reserved.</p>
            </div>
        `;

        // Insert before closing body
        document.body.appendChild(footer);

        // Try to move existing nav buttons into footer
        const existingNav = document.querySelector('.nav-buttons-container, .bottom-nav');
        const footerNav = document.getElementById('footerNav');
        if (existingNav && footerNav) {
            footerNav.innerHTML = existingNav.innerHTML;
            existingNav.remove();
        }

        // Add CSS - Aligned with SJMaths design
        if (!document.getElementById('exercise-footer-styles')) {
            const style = document.createElement('style');
            style.id = 'exercise-footer-styles';
            style.textContent = `
                /* ==== EXERCISE FOOTER - COMPACT DESIGN ==== */
                .exercise-page-footer {
                    background-color: #ffffff;
                    border-top: 1px solid rgba(0,0,0,0.05);
                    padding: 1rem 1rem;
                    margin-top: 1.5rem;
                    font-family: 'Poppins', 'Segoe UI', sans-serif;
                }
                
                .exercise-page-footer .footer-nav {
                    display: flex;
                    justify-content: center;
                    gap: 8px;
                    max-width: 700px;
                    margin: 0 auto 1rem;
                    padding-bottom: 1rem;
                    border-bottom: 1px solid rgba(0, 0, 0, 0.05);
                    flex-wrap: wrap;
                }
                
                .exercise-page-footer .footer-nav a,
                .exercise-page-footer .footer-nav .nav-btn {
                    display: inline-flex;
                    align-items: center;
                    gap: 6px;
                    padding: 8px 16px;
                    border-radius: 20px;
                    text-decoration: none;
                    font-weight: 600;
                    font-size: 0.85rem;
                    transition: all 0.25s ease;
                }
                
                .exercise-page-footer .btn-prev,
                .exercise-page-footer .footer-nav a:first-child {
                    background: #f5f5f5;
                    color: #555;
                    border: 1px solid #e0e0e0;
                }
                
                .exercise-page-footer .btn-prev:hover,
                .exercise-page-footer .footer-nav a:first-child:hover {
                    background: #eee;
                    border-color: #8e44ad;
                    color: #8e44ad;
                    transform: translateY(-1px);
                }
                
                .exercise-page-footer .btn-next,
                .exercise-page-footer .footer-nav a:last-child {
                    background: linear-gradient(135deg, #8e44ad, #9b59b6);
                    color: white;
                    border: none;
                    box-shadow: 0 4px 10px rgba(142, 68, 173, 0.2);
                }
                
                .exercise-page-footer .btn-next:hover,
                .exercise-page-footer .footer-nav a:last-child:hover {
                    background: linear-gradient(135deg, #9b59b6, #a569bd);
                    transform: translateY(-1px);
                    box-shadow: 0 6px 15px rgba(142, 68, 173, 0.3);
                }
                
                .exercise-page-footer .footer-brand {
                    text-align: center;
                }
                
                .exercise-page-footer .footer-brand .logo {
                    display: inline-flex;
                    align-items: center;
                    gap: 0.3rem;
                    font-size: 1.1rem;
                    font-weight: 800;
                    color: #8e44ad;
                    text-decoration: none;
                    margin-bottom: 0.2rem;
                }
                
                .exercise-page-footer .logo-symbol {
                    font-size: 1.3rem;
                    font-family: 'Times New Roman', serif;
                    line-height: 1;
                }
                
                .exercise-page-footer .copyright {
                    color: #6b7280;
                    font-size: 0.75rem;
                    margin: 0;
                }
                
                /* Dark mode */
                body.dark-mode .exercise-page-footer {
                    background-color: #1a1a1a;
                    border-top-color: rgba(255, 255, 255, 0.05);
                }
                
                body.dark-mode .exercise-page-footer .btn-prev,
                body.dark-mode .exercise-page-footer .footer-nav a:first-child {
                    background: #2d2d2d;
                    color: #ddd;
                    border-color: #444;
                }
                
                body.dark-mode .exercise-page-footer .btn-prev:hover,
                body.dark-mode .exercise-page-footer .footer-nav a:first-child:hover {
                    background: #333;
                    border-color: #bb86fc;
                    color: #bb86fc;
                }
                
                body.dark-mode .exercise-page-footer .footer-nav {
                    border-bottom-color: rgba(255, 255, 255, 0.05);
                }
                
                body.dark-mode .exercise-page-footer .footer-brand .logo {
                    color: #bb86fc;
                }
                
                body.dark-mode .exercise-page-footer .copyright {
                    color: #666;
                }
                
                /* Mobile */
                @media (max-width: 768px) {
                    .exercise-page-footer {
                        padding: 0.8rem 0.8rem;
                    }
                    
                    .exercise-page-footer .footer-nav {
                        flex-direction: column;
                        gap: 6px;
                        margin-bottom: 0.8rem;
                        padding-bottom: 0.8rem;
                    }
                    
                    .exercise-page-footer .footer-nav a,
                    .exercise-page-footer .footer-nav .nav-btn {
                        justify-content: center;
                        width: 100%;
                        padding: 10px;
                    }
                }
            `;
            document.head.appendChild(style);
        }
    }

    // Initialize when DOM is ready
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initExerciseFooter);
    } else {
        initExerciseFooter();
    }
})();
