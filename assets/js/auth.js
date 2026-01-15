// auth.js
import { initializeApp } from "https://www.gstatic.com/firebasejs/10.7.1/firebase-app.js";
import { getAuth, onAuthStateChanged, signOut } from "https://www.gstatic.com/firebasejs/10.7.1/firebase-auth.js";

import { firebaseConfig } from './firebase-config.js';

// Initialize Firebase safely
let auth;
try {
    const app = initializeApp(firebaseConfig);
    auth = getAuth(app);
} catch (e) {
    console.error("Firebase Initialization Error:", e);
}

// Toast Notification Utility
const injectToastStyles = () => {
    if (document.getElementById('toast-styles')) return;
    const style = document.createElement('style');
    style.id = 'toast-styles';
    style.textContent = `
        .toast-notification {
            position: fixed;
            bottom: 30px;
            left: 50%;
            transform: translateX(-50%) translateY(20px);
            background: #333;
            color: white;
            padding: 12px 24px;
            border-radius: 50px;
            box-shadow: 0 5px 15px rgba(0,0,0,0.2);
            z-index: 10000;
            opacity: 0;
            visibility: hidden;
            transition: all 0.3s ease;
            font-family: 'Poppins', sans-serif;
            font-size: 0.9rem;
            display: flex;
            align-items: center;
            gap: 8px;
        }
        .toast-notification.show {
            transform: translateX(-50%) translateY(0);
            opacity: 1;
            visibility: visible;
        }
        .toast-notification.error { background: #e74c3c; }
        .toast-notification.success { background: #2ecc71; }
    `;
    document.head.appendChild(style);
};

export const showToast = (message, type = 'info') => {
    injectToastStyles();
    
    const toast = document.createElement('div');
    toast.className = `toast-notification ${type}`;
    
    let icon = '';
    if (type === 'error') icon = '<i class="fas fa-exclamation-circle"></i>';
    else if (type === 'success') icon = '<i class="fas fa-check-circle"></i>';
    
    toast.innerHTML = `${icon}<span>${message}</span>`;
    document.body.appendChild(toast);

    // Trigger animation
    requestAnimationFrame(() => {
        toast.classList.add('show');
    });

    setTimeout(() => {
        toast.classList.remove('show');
        setTimeout(() => toast.remove(), 300);
    }, 3000);
};

// Make available globally for non-module scripts
window.showToast = showToast;

// Logic to update UI based on user state
const updateAuthButton = (user) => {
    const buttons = [
        document.getElementById('authBtn'),
        document.getElementById('mobileAuthBtn')
    ];

    buttons.forEach(loginBtn => {
        if (!loginBtn) return;

        if (user) {
            // --- LOGGED IN STATE ---
            loginBtn.textContent = "Logout";
            loginBtn.href = "#";
            loginBtn.setAttribute('role', 'button'); // Accessibility fix

            // Override click behavior for Logout
            loginBtn.onclick = async (e) => {
                e.preventDefault();

                if (confirm("Are you sure you want to logout?")) {
                    try {
                        await signOut(auth);
                        window.location.reload(); // Refresh to clear state
                    } catch (error) {
                        console.error("Logout failed", error);
                        showToast("Error logging out. Please try again.", "error");
                    }
                }
            };
        } else {
            // --- LOGGED OUT STATE ---
            loginBtn.textContent = "Login";
            loginBtn.href = "login.html";
            loginBtn.removeAttribute('role');

            // Remove the click handler so the link works normally
            loginBtn.onclick = null;
        }
    });
};

// Start Observer (Only if auth initialized)
if (auth) {
    onAuthStateChanged(auth, (user) => {
        // Try to update immediately
        updateAuthButton(user);

        // If button not found (header loading async), watch for it
        if (!document.getElementById('authBtn')) {
            const observer = new MutationObserver((mutations, obs) => {
                if (document.getElementById('authBtn')) {
                    updateAuthButton(user);
                    obs.disconnect();
                }
            });
            observer.observe(document.body, { childList: true, subtree: true });
        }
    });
}