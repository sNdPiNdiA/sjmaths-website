// auth.js
import { initializeApp } from "https://www.gstatic.com/firebasejs/10.7.1/firebase-app.js";
import { getAuth, onAuthStateChanged, signOut } from "https://www.gstatic.com/firebasejs/10.7.1/firebase-auth.js";

// Configuration
const firebaseConfig = {
    apiKey: "AIzaSyA0kGONQMQ3NBLfnOuDPTPN_tGCqM-ed2M",
    authDomain: "sjmaths-web.firebaseapp.com",
    projectId: "sjmaths-web",
    storageBucket: "sjmaths-web.firebasestorage.app",
    messagingSenderId: "168858335686",
    appId: "1:168858335686:web:9f9a87028b7b71db7e1ac7",
    measurementId: "G-K326N2KJ2G"
};

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
    const loginBtn = document.getElementById('authBtn');

    // Guard Clause: If button doesn't exist on this page, stop.
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
};

// Start Observer (Only if auth initialized)
if (auth) {
    onAuthStateChanged(auth, (user) => {
        // We wait for DOMContentLoaded to ensure the button exists
        if (document.readyState === 'loading') {
            document.addEventListener('DOMContentLoaded', () => updateAuthButton(user));
        } else {
            updateAuthButton(user);
        }
    });
}