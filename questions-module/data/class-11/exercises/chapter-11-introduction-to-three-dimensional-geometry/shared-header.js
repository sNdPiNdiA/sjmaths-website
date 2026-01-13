import { initializeApp } from "https://www.gstatic.com/firebasejs/10.7.1/firebase-app.js";
import { getAuth, onAuthStateChanged, signOut } from "https://www.gstatic.com/firebasejs/10.7.1/firebase-auth.js";

const firebaseConfig = {
    apiKey: "AIzaSyA0kGONQMQ3NBLfnOuDPTPN_tGCqM-ed2M",
    authDomain: "sjmaths-web.firebaseapp.com",
    projectId: "sjmaths-web",
    storageBucket: "sjmaths-web.firebasestorage.app",
    messagingSenderId: "168858335686",
    appId: "1:168858335686:web:9f9a87028b7b71db7e1ac7",
    measurementId: "G-K326N2KJ2G"
};

export async function initSharedHeader(searchHandler, componentPathPrefix = '../../') {
    // Load Components
    try {
        const [headerRes, footerRes] = await Promise.all([
            fetch(`${componentPathPrefix}components/header.html`),
            fetch(`${componentPathPrefix}components/footer.html`)
        ]);

        if (headerRes.ok) document.getElementById('header-container').innerHTML = await headerRes.text();
        if (footerRes.ok) document.getElementById('footer-container').innerHTML = await footerRes.text();

        // Initialize Logic after DOM injection
        initializeLogic(searchHandler);
    } catch (error) {
        console.error("Error loading components:", error);
    }
}

function initializeLogic(searchHandler) {
    // 1. Highlight Active Link
    const currentPath = window.location.pathname;
    document.querySelectorAll('nav a').forEach(link => {
        if (link.getAttribute('href') === currentPath) {
            link.classList.add('active');
        }
    });

    // 2. Firebase Auth
    try {
        const app = initializeApp(firebaseConfig);
        const auth = getAuth(app);
        const loginBtn = document.getElementById('authBtn');

        onAuthStateChanged(auth, (user) => {
            if (user && loginBtn) {
                loginBtn.innerText = "Logout";
                loginBtn.href = "#";
                loginBtn.onclick = (e) => {
                    e.preventDefault();
                    if (confirm("Logout?")) {
                        signOut(auth).then(() => window.location.reload());
                    }
                };
            }
        });
    } catch (e) { console.log("Firebase not configured."); }

    // 3. Mobile Menu
    const mobileToggle = document.querySelector('.mobile-toggle');
    const navMenu = document.querySelector('nav');
    if (mobileToggle && navMenu) {
        const toggleIcon = mobileToggle.querySelector('i');
        mobileToggle.addEventListener('click', () => {
            navMenu.classList.toggle('active');
            toggleIcon.classList.toggle('fa-bars');
            toggleIcon.classList.toggle('fa-times');
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