/**
 * Mandatory Auth Gate for UPSSSC PET Current Affairs
 * Protects premium current affairs notes and quizzes behind Google Login.
 */

import { GoogleAuthProvider, signInWithPopup, onAuthStateChanged, setPersistence, browserLocalPersistence } from "https://www.gstatic.com/firebasejs/12.8.0/firebase-auth.js";
import { doc, setDoc, serverTimestamp } from "https://www.gstatic.com/firebasejs/12.8.0/firebase-firestore.js";
import { auth, db, analytics, logEvent } from "./firebase-config.js";

// Ensure Firebase Auth persists session across browser reopens & tabs
setPersistence(auth, browserLocalPersistence).catch(console.error);

const provider = new GoogleAuthProvider();

function injectAuthOverlay() {
    // If user is already remembered in localStorage, don't display overlay while Firebase re-initializes
    const storedUid = localStorage.getItem('sj_uid');
    if (storedUid && !storedUid.startsWith('user_')) {
        return; // User is remembered as logged in
    }

    if (document.getElementById('sj-auth-overlay')) return;

    // Blur / hide main content container across all page layouts
    const targetEl = document.querySelector('.topic-container, main, .main-content, #main-content, .container, body > div:not(#header-container):not(#sj-auth-overlay)');
    const allContainers = document.querySelectorAll('main, .topic-container, .main-content, .page-content, section');
    if (allContainers.length > 0) {
        allContainers.forEach(el => {
            el.style.filter = 'blur(12px)';
            el.style.pointerEvents = 'none';
            el.style.userSelect = 'none';
        });
    } else if (targetEl) {
        targetEl.style.filter = 'blur(12px)';
        targetEl.style.pointerEvents = 'none';
        targetEl.style.userSelect = 'none';
    }

    const overlay = document.createElement('div');
    overlay.id = 'sj-auth-overlay';
    overlay.style.cssText = `
        position: fixed;
        top: 0;
        left: 0;
        width: 100vw;
        height: 100vh;
        background: rgba(15, 23, 42, 0.85);
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
        z-index: 999999;
        display: flex;
        align-items: center;
        justify-content: center;
        padding: 1.5rem;
        font-family: 'Outfit', 'Inter', sans-serif;
    `;

    overlay.innerHTML = `
        <div style="
            background: #ffffff;
            border-radius: 24px;
            max-width: 460px;
            width: 100%;
            padding: 2.5rem 2rem;
            text-align: center;
            box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.35);
            border: 1px solid rgba(255, 255, 255, 0.2);
            animation: overlayPop 0.4s cubic-bezier(0.16, 1, 0.3, 1);
        ">
            <div style="
                width: 64px;
                height: 64px;
                background: rgba(41, 128, 185, 0.1);
                color: #2980b9;
                border-radius: 50%;
                display: inline-flex;
                align-items: center;
                justify-content: center;
                font-size: 1.75rem;
                margin-bottom: 1.25rem;
            ">
                <i class="fas fa-lock"></i>
            </div>
            
            <h2 style="
                margin: 0 0 0.5rem 0;
                font-size: 1.6rem;
                font-weight: 700;
                color: #0f172a;
            ">Login Required</h2>

            <p style="
                margin: 0 0 1.75rem 0;
                color: #64748b;
                font-size: 0.95rem;
                line-height: 1.5;
            ">Please sign in with your Google account to access premium study notes, memory tricks, and monthly practice quizzes.</p>

            <button id="sj-google-gate-btn" style="
                width: 100%;
                padding: 0.85rem 1.25rem;
                background: #0f172a;
                color: #ffffff;
                border: none;
                border-radius: 12px;
                font-size: 1rem;
                font-weight: 600;
                cursor: pointer;
                display: flex;
                align-items: center;
                justify-content: center;
                gap: 10px;
                transition: all 0.2s ease;
                box-shadow: 0 4px 12px rgba(15, 23, 42, 0.15);
            ">
                <i class="fab fa-google" style="color: #4285F4; font-size: 1.1rem;"></i>
                <span>Sign in with Google</span>
            </button>

            <div style="margin-top: 1.25rem; font-size: 0.8rem; color: #94a3b8;">
                Free instant access &bull; SJMaths Student Portal
            </div>
        </div>

        <style>
            @keyframes overlayPop {
                from { opacity: 0; transform: scale(0.92); }
                to { opacity: 1; transform: scale(1); }
            }
            #sj-google-gate-btn:hover {
                background: #1e293b !important;
                transform: translateY(-1px);
            }
        </style>
    `;

    document.body.appendChild(overlay);

    // Add event listener to login button
    const btn = document.getElementById('sj-google-gate-btn');
    btn.addEventListener('click', async () => {
        try {
            btn.disabled = true;
            btn.innerHTML = `<i class="fas fa-spinner fa-spin"></i> <span>Signing in...</span>`;

            const result = await signInWithPopup(auth, provider);
            const user = result.user;

            logEvent(analytics, "login", { method: "google_gate" });
            localStorage.setItem('sj_uid', user.uid);
            localStorage.setItem('sj_user_logged_in', 'true');

            await setDoc(doc(db, "users", user.uid), {
                displayName: user.displayName || "",
                email: user.email || "",
                photoURL: user.photoURL || "",
                lastLogin: serverTimestamp()
            }, { merge: true });

            removeAuthOverlay();
        } catch (error) {
            console.error("Gate Login Error:", error);
            btn.disabled = false;
            btn.innerHTML = `<i class="fab fa-google" style="color: #4285F4;"></i> <span>Sign in with Google</span>`;
            alert("Login failed: " + error.message);
        }
    });
}

function removeAuthOverlay() {
    const overlay = document.getElementById('sj-auth-overlay');
    if (overlay) overlay.remove();

    const allContainers = document.querySelectorAll('main, .topic-container, .main-content, .page-content, section, body > div');
    allContainers.forEach(el => {
        el.style.filter = 'none';
        el.style.pointerEvents = 'auto';
        el.style.userSelect = 'auto';
    });
}

// Check initial stored login state immediately to avoid initial overlay flash
const rememberedUid = localStorage.getItem('sj_uid');
if (!rememberedUid || rememberedUid.startsWith('user_')) {
    injectAuthOverlay();
}

// Sync with Firebase Auth state
onAuthStateChanged(auth, (user) => {
    if (user) {
        localStorage.setItem('sj_uid', user.uid);
        localStorage.setItem('sj_user_logged_in', 'true');
        removeAuthOverlay();
    } else {
        localStorage.removeItem('sj_user_logged_in');
        // Only clear sj_uid if it wasn't a guest ID or if user explicitly logged out
        if (localStorage.getItem('sj_uid') && !localStorage.getItem('sj_uid').startsWith('user_')) {
            localStorage.removeItem('sj_uid');
        }
        injectAuthOverlay();
    }
});
