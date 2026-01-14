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
                        alert("Error logging out. Please try again.");
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