// auth.js
import { initializeApp, getApps, getApp } from "https://www.gstatic.com/firebasejs/10.7.1/firebase-app.js";
import { getAuth, onAuthStateChanged, signOut } from "https://www.gstatic.com/firebasejs/10.7.1/firebase-auth.js";
import { getFirestore, doc, setDoc } from "https://www.gstatic.com/firebasejs/10.7.1/firebase-firestore.js";

import { handleUserProfile } from '../../user-profile.js';
import { firebaseConfig } from './firebase-config.js';

// Initialize Firebase
let auth, db;
try {
    let app;
    if (getApps().length > 0) {
        app = getApp();
    } else {
        app = initializeApp(firebaseConfig);
    }
    auth = getAuth(app);
    db = getFirestore(app);
} catch (e) {
    console.error("Firebase Initialization Error:", e);
}

// Save user to Firestore
async function saveUserToFirestore(user) {
    try {
        await setDoc(doc(db, "users", user.uid), {
            name: user.displayName || "Student",
            email: user.email,
            role: "student",
            createdAt: new Date()
        }, { merge: true });
        console.log("User saved to Firestore:", user.email);
    } catch (error) {
        console.error("Error saving user:", error);
    }
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

    requestAnimationFrame(() => toast.classList.add('show'));

    setTimeout(() => {
        toast.classList.remove('show');
        setTimeout(() => toast.remove(), 300);
    }, 3000);
};

window.showToast = showToast;

// Global Auth Check Function
export const checkAuth = () => {
    return new Promise((resolve) => {
        const unsubscribe = onAuthStateChanged(auth, (user) => {
            unsubscribe();
            resolve(user);
        });
    });
};

window.checkAuth = checkAuth;

// Logic to update UI based on user state
const updateAuthButton = (user) => {
    if (user) {
        handleUserProfile(user, auth);
    } else {
        const buttons = [
            document.getElementById('authBtn'),
            document.getElementById('mobileAuthBtn')
        ];
        
        buttons.forEach(loginBtn => {
            if (!loginBtn) return;

            // Clone to remove event listeners
            const newBtn = loginBtn.cloneNode(true);
            loginBtn.parentNode.replaceChild(newBtn, loginBtn);

            newBtn.innerHTML = "Login";
            newBtn.href = "/login.html";
            newBtn.removeAttribute('role');
            newBtn.onclick = null;
        });
    }
};

// Start Observer (Only if auth initialized)
if (auth) {
    onAuthStateChanged(auth, (user) => {

        // 🔥 SAVE USER TO FIRESTORE WHEN LOGGED IN
        if (user) {
            saveUserToFirestore(user);
        }

        updateAuthButton(user);

        if (!document.getElementById('authBtn') || !document.getElementById('mobileAuthBtn')) {
            const observer = new MutationObserver((mutations, obs) => {
                if (document.getElementById('authBtn') || document.getElementById('mobileAuthBtn')) {
                    updateAuthButton(user);
                    obs.disconnect();
                }
            });
            observer.observe(document.body, { childList: true, subtree: true });
        }
    });
}
