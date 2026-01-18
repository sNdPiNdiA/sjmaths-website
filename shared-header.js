import { onAuthStateChanged } from "https://www.gstatic.com/firebasejs/12.8.0/firebase-auth.js";
import { auth } from "./assets/js/firebase-config.js";
import { getSearchConfig } from "./search.js";
import { handleUserProfile } from "./user-profile.js";


export async function initSharedHeader(customHandler = null, componentPathPrefix = '../../') {
    // Load Components
    try {
        const [headerRes, footerRes] = await Promise.all([
            fetch(`${componentPathPrefix}components/header.html`),
            fetch(`${componentPathPrefix}components/footer.html`)
        ]);

        if (headerRes.ok) document.getElementById('header-container').innerHTML = await headerRes.text();
        if (footerRes.ok) document.getElementById('footer-container').innerHTML = await footerRes.text();

        // Initialize Logic after DOM injection
        initializeLogic(customHandler || getSearchConfig(), componentPathPrefix);
    } catch (error) {
        console.error("Error loading components:", error);
    }
}

function initializeLogic(searchHandler, componentPathPrefix) {
    // 1. Highlight Active Link
    const currentPath = window.location.pathname;
    document.querySelectorAll('nav a').forEach(link => {
        if (link.getAttribute('href') === currentPath) {
            link.classList.add('active');
        }
    });

    // 2. Firebase Auth
    try {
        const loginBtn = document.getElementById('authBtn');

        onAuthStateChanged(auth, (user) => {
            if (user) {
                handleUserProfile(user, auth);
            } else if (loginBtn) {
                // Ensure default state
                loginBtn.innerText = "Login";
                loginBtn.href = `${componentPathPrefix}login.html`;
            }
        });
    } catch (e) { /* Firebase not configured */ }

    // 3. Mobile Menu
    const mobileToggle = document.querySelector('.mobile-toggle');
    const navMenu = document.querySelector('nav');
    if (mobileToggle && navMenu) {
        const toggleIcon = mobileToggle.querySelector('i');
        mobileToggle.addEventListener('click', (e) => {
            e.stopPropagation(); // Prevent conflict with global navigation scripts
            const isOpen = navMenu.classList.toggle('active');
            if (toggleIcon) {
                toggleIcon.classList.toggle('fa-bars', !isOpen);
                toggleIcon.classList.toggle('fa-times', isOpen);
            }
            mobileToggle.setAttribute('aria-expanded', isOpen);
        });
    }

    // 4. Search Logic
    const searchInput = document.querySelector('.header-search input');
    const searchBtn = document.querySelector('.header-search button');

    if (searchInput && searchBtn && searchHandler) {
        if (searchHandler.placeholder) searchInput.placeholder = searchHandler.placeholder;

        const performSearch = () => {
            const query = searchInput.value.toLowerCase().trim();
            if (query === "") return;
            searchHandler.onSearch(query);
        };

        searchBtn.addEventListener('click', performSearch);
        searchInput.addEventListener('keypress', (e) => { if (e.key === 'Enter') performSearch(); });
    }
}