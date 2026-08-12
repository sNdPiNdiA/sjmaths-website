// assets/js/auth.js

import { GoogleAuthProvider, signInWithPopup, onAuthStateChanged, signOut, setPersistence, browserLocalPersistence } from "https://www.gstatic.com/firebasejs/12.8.0/firebase-auth.js";
import { doc, setDoc, serverTimestamp } from "https://www.gstatic.com/firebasejs/12.8.0/firebase-firestore.js";
import { auth, db, analytics, logEvent } from "./firebase-config.js";
import { showToast } from "./utils.js";

const provider = new GoogleAuthProvider();

function getPostLoginTarget() {
    const params = new URLSearchParams(window.location.search);
    const returnTo = params.get("returnTo");

    if (!returnTo) {
        return "/profile.html";
    }

    if (!returnTo.startsWith("/") || returnTo.startsWith("//")) {
        return "/profile.html";
    }

    return returnTo;
}

export function saveUserSession(user) {
    if (!user) return;
    localStorage.setItem('sj_uid', user.uid);
    localStorage.setItem('sj_user_logged_in', 'true');
    if (user.displayName) localStorage.setItem('sj_user_name', user.displayName);
    if (user.email) localStorage.setItem('sj_user_email', user.email);
    if (user.photoURL) localStorage.setItem('sj_user_photo', user.photoURL);
}

export function clearUserSession() {
    localStorage.removeItem('sj_user_logged_in');
    localStorage.removeItem('sj_user_name');
    localStorage.removeItem('sj_user_email');
    localStorage.removeItem('sj_user_photo');
    if (localStorage.getItem('sj_uid') && !localStorage.getItem('sj_uid').startsWith('user_')) {
        localStorage.removeItem('sj_uid');
    }
}

document.addEventListener("DOMContentLoaded", () => {
    // If user is already remembered in localStorage, show spinner/forward to target
    if (window.location.pathname.includes('login.html')) {
        const isRemembered = localStorage.getItem('sj_user_logged_in') === 'true' && 
                             localStorage.getItem('sj_uid') && 
                             !localStorage.getItem('sj_uid').startsWith('user_');
        
        if (isRemembered) {
            const formContent = document.querySelector('.form-content');
            if (formContent) {
                formContent.innerHTML = `
                    <h1>Welcome Back!</h1>
                    <p class="subtitle">You are already signed in. Redirecting to your dashboard...</p>
                    <div style="margin: 2rem 0; text-align: center; color: var(--primary);">
                        <i class="fas fa-spinner fa-spin" style="font-size: 2rem;"></i>
                    </div>
                `;
            }
        }
    }

    // Listen for auth state to auto-redirect if already logged in on login page
    onAuthStateChanged(auth, (user) => {
        if (user) {
            saveUserSession(user);
            if (window.location.pathname.includes('login.html')) {
                window.location.replace(getPostLoginTarget());
            }
        }
    });

    const googleBtn = document.getElementById("googleLoginBtn");
    if (!googleBtn) return;

    googleBtn.addEventListener("click", async () => {
        try {
            googleBtn.disabled = true;
            googleBtn.innerHTML = `<i class="fas fa-spinner fa-spin"></i> Signing in...`;

            // Explicitly set persistent browser session storage before signing in
            await setPersistence(auth, browserLocalPersistence);

            const result = await signInWithPopup(auth, provider);
            const user = result.user;

            logEvent(analytics, "login", { method: "google" });

            // Store user session across browser tabs and sessions
            saveUserSession(user);

            // Create/update user document in Firestore (merge to preserve existing fields)
            await setDoc(doc(db, "users", user.uid), {
                displayName: user.displayName || "",
                email: user.email || "",
                photoURL: user.photoURL || "",
                lastLogin: serverTimestamp()
            }, { merge: true });

            window.location.replace(getPostLoginTarget());

        } catch (error) {
            console.error("Google Login Error:", error);
            googleBtn.disabled = false;
            googleBtn.innerHTML = `<i class="fab fa-google"></i> Sign in with Google`;
            showToast(error.message, "error");
        }
    });
});

// Exported Auth Functions
export const checkAuth = () => {
    return new Promise((resolve) => {
        const unsubscribe = onAuthStateChanged(auth, (user) => {
            unsubscribe();
            // Ensure local storage syncs with actual auth state
            if (user) {
                saveUserSession(user);
            }
            resolve(user);
        });
    });
};

export const logout = async () => {
    try {
        await signOut(auth);
        clearUserSession();
        window.location.href = '/login.html';
    } catch (error) {
        console.error("Logout Error:", error);
    }
};

