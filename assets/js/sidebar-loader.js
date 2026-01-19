import { signOut } from "https://www.gstatic.com/firebasejs/12.8.0/firebase-auth.js";
import { auth } from "./firebase-config.js";

/**
 * Dynamically loads the sidebar component and handles its logic.
 * @param {string} pathPrefix - Relative path to root (e.g., '../' or '../../') for fetching assets.
 */
export async function initSidebar(pathPrefix = '') {
    const sidebarContainerId = 'sidebar-container';

    try {
        // 1. Fetch Sidebar HTML
        const response = await fetch(`${pathPrefix}components/sidebar.html`);
        if (!response.ok) throw new Error(`Sidebar load failed: ${response.statusText}`);
        const html = await response.text();

        // 2. Inject into DOM
        let container = document.getElementById(sidebarContainerId);
        if (!container) {
            container = document.createElement('div');
            container.id = sidebarContainerId;
            // Prepend to body so it sits before main content
            document.body.prepend(container);
        }
        container.innerHTML = html;

        // 3. Initialize Logic
        highlightActiveLink();
        setupLogout(pathPrefix);
        setupMobileToggle();
        adjustLayout();

        // 4. Handle Window Resize for Layout
        window.addEventListener('resize', adjustLayout);

    } catch (error) {
        console.error("Error initializing sidebar:", error);
    }
}

function highlightActiveLink() {
    const currentPath = window.location.pathname;
    // Helper to normalize paths (remove trailing slash, index.html)
    const normalize = (p) => p.replace(/\/index\.html$/, '').replace(/\/$/, '').toLowerCase() || '/';
    const currentNorm = normalize(currentPath);

    const links = document.querySelectorAll('.sidebar-link');
    
    links.forEach(link => {
        try {
            const linkUrl = new URL(link.getAttribute('href'), window.location.origin);
            const linkNorm = normalize(linkUrl.pathname);

            // Exact match or parent match (e.g. /classes/class-9 matches /classes/class-9/notes)
            if (currentNorm === linkNorm || (linkNorm !== '/' && currentNorm.startsWith(linkNorm))) {
                link.classList.add('active');
            }
        } catch (e) {
            // Ignore invalid URLs
        }
    });
}

function setupLogout(pathPrefix) {
    const logoutBtn = document.getElementById('sidebarLogout');
    if (logoutBtn) {
        logoutBtn.addEventListener('click', async () => {
            try {
                await signOut(auth);
                window.location.href = `${pathPrefix}login.html`;
            } catch (error) {
                console.error("Logout failed:", error);
                alert("Failed to logout. Please try again.");
            }
        });
    }
}

function setupMobileToggle() {
    const sidebarContainer = document.querySelector('#sidebar-container .sidebar-container');
    if (!sidebarContainer) return;

    // 1. Create Toggle Button if not exists
    let toggleBtn = document.getElementById('sidebar-toggle');
    if (!toggleBtn) {
        toggleBtn = document.createElement('button');
        toggleBtn.id = 'sidebar-toggle';
        toggleBtn.innerHTML = '<i class="fas fa-bars"></i>';
        toggleBtn.setAttribute('aria-label', 'Toggle Sidebar');
        
        // Styles
        Object.assign(toggleBtn.style, {
            position: 'fixed',
            top: '20px',
            left: '20px',
            zIndex: '1200',
            background: 'var(--primary, #8e44ad)',
            color: 'white',
            border: 'none',
            borderRadius: '50%',
            width: '45px',
            height: '45px',
            cursor: 'pointer',
            display: 'none', // Controlled by resize
            alignItems: 'center',
            justifyContent: 'center',
            boxShadow: '0 4px 15px rgba(0,0,0,0.2)',
            fontSize: '1.2rem',
            transition: 'transform 0.2s'
        });
        
        document.body.appendChild(toggleBtn);
    }

    // 2. Inject Mobile Styles
    if (!document.getElementById('sidebar-mobile-styles')) {
        const style = document.createElement('style');
        style.id = 'sidebar-mobile-styles';
        style.textContent = `
            @media (max-width: 992px) {
                #sidebar-container .sidebar-container.active {
                    transform: translateX(0) !important;
                    box-shadow: 0 0 50px rgba(0,0,0,0.5);
                }
                .sidebar-overlay {
                    position: fixed; inset: 0; background: rgba(0,0,0,0.5); z-index: 999;
                    opacity: 0; transition: opacity 0.3s; pointer-events: none;
                }
                .sidebar-overlay.active { opacity: 1; pointer-events: auto; }
            }
        `;
        document.head.appendChild(style);
    }

    // 3. Create Overlay
    let overlay = document.querySelector('.sidebar-overlay');
    if (!overlay) {
        overlay = document.createElement('div');
        overlay.className = 'sidebar-overlay';
        document.body.appendChild(overlay);
    }

    // 4. Logic
    const toggleSidebar = (forceState) => {
        const isActive = typeof forceState === 'boolean' ? forceState : !sidebarContainer.classList.contains('active');
        sidebarContainer.classList.toggle('active', isActive);
        overlay.classList.toggle('active', isActive);
        toggleBtn.innerHTML = isActive ? '<i class="fas fa-times"></i>' : '<i class="fas fa-bars"></i>';
    };

    toggleBtn.addEventListener('click', (e) => {
        e.stopPropagation();
        toggleSidebar();
    });

    overlay.addEventListener('click', () => toggleSidebar(false));

    // Close on link click
    sidebarContainer.querySelectorAll('a').forEach(link => {
        link.addEventListener('click', () => {
            if (window.innerWidth <= 992) toggleSidebar(false);
        });
    });

    // 5. Visibility
    const handleResize = () => {
        if (window.innerWidth <= 992) {
            toggleBtn.style.display = 'flex';
        } else {
            toggleBtn.style.display = 'none';
            sidebarContainer.classList.remove('active');
            overlay.classList.remove('active');
        }
    };
    window.addEventListener('resize', handleResize);
    handleResize();
}

function adjustLayout() {
    // If sidebar exists and is visible (desktop), shift body content
    // The sidebar CSS has width: 280px
    const sidebarWidth = 280;
    const isDesktop = window.innerWidth > 992; // Standard breakpoint

    if (isDesktop) {
        document.body.style.paddingLeft = `${sidebarWidth}px`;
        document.body.style.transition = 'padding-left 0.3s ease';
    } else {
        document.body.style.paddingLeft = '0';
    }
}