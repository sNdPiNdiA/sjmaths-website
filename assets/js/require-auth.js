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

const AUTH_OVERLAY_CSS = `
    #sj-auth-overlay {
        --auth-ink: #182e26;
        --auth-muted: #5d6d63;
        --auth-brand: #174b39;
        --auth-paper: #fffdf8;
        --auth-border: #d9ddd1;
        --auth-soft: #eaf0e7;
        position: fixed;
        inset: 0;
        z-index: 999999;
        display: flex;
        align-items: center;
        justify-content: center;
        min-height: 100vh;
        min-height: 100dvh;
        overflow-y: auto;
        overscroll-behavior: contain;
        padding: clamp(1rem, 4vw, 2rem);
        background: rgba(13, 24, 19, 0.74);
        backdrop-filter: blur(8px);
        -webkit-backdrop-filter: blur(8px);
        font-family: 'DM Sans', 'Segoe UI', sans-serif;
    }

    body.dark-mode #sj-auth-overlay {
        --auth-ink: #f4f2e7;
        --auth-muted: #b6c4b7;
        --auth-brand: #90c8a8;
        --auth-paper: #1d2d25;
        --auth-border: #415346;
        --auth-soft: #2b4335;
        color-scheme: dark;
    }

    #sj-auth-overlay *, #sj-auth-overlay *::before, #sj-auth-overlay *::after { box-sizing: border-box; }
    #sj-auth-overlay [hidden] { display: none !important; }

    #sj-auth-overlay .sj-auth-card {
        position: relative;
        width: min(100%, 448px);
        padding: clamp(1.5rem, 4vw, 2.25rem);
        border: 1px solid var(--auth-border);
        border-radius: 14px;
        background: var(--auth-paper);
        color: var(--auth-ink);
        box-shadow: 0 28px 72px rgba(0, 0, 0, 0.28);
        animation: sj-auth-enter 240ms cubic-bezier(.2, .7, .2, 1) both;
    }

    #sj-auth-overlay .sj-auth-card::before {
        position: absolute;
        top: 0;
        left: 2rem;
        width: 3.25rem;
        height: 3px;
        border-radius: 0 0 3px 3px;
        background: var(--auth-brand);
        content: '';
    }

    #sj-auth-overlay .sj-auth-brand-line { display: flex; align-items: center; gap: .75rem; margin-bottom: 1.75rem; }
    #sj-auth-overlay .sj-auth-mark {
        display: inline-grid;
        width: 42px;
        height: 42px;
        flex: 0 0 42px;
        place-items: center;
        border: 1px solid var(--auth-border);
        border-radius: 8px;
        background: var(--auth-soft);
        color: var(--auth-brand);
        font: 500 1.75rem/1 Georgia, serif;
    }
    #sj-auth-overlay .sj-auth-eyebrow { color: var(--auth-brand); font-size: .68rem; font-weight: 700; letter-spacing: .14em; text-transform: uppercase; }
    #sj-auth-overlay .sj-auth-rule { height: 1px; flex: 1; background: var(--auth-border); }
    #sj-auth-overlay .sj-auth-title { margin: 0 0 .65rem; color: var(--auth-ink); font-size: clamp(1.55rem, 5vw, 1.9rem); font-weight: 650; letter-spacing: -.035em; line-height: 1.15; text-wrap: balance; }
    #sj-auth-overlay .sj-auth-copy { margin: 0 0 1.5rem; color: var(--auth-muted); font-size: .96rem; line-height: 1.65; }

    #sj-auth-overlay .sj-auth-error {
        margin: 0 0 1rem;
        padding: .75rem .9rem;
        overflow-wrap: anywhere;
        border: 1px solid #e6b8a8;
        border-radius: 6px;
        background: #fbf0eb;
        color: #813c27;
        font-size: .875rem;
        line-height: 1.45;
        text-align: left;
    }

    #sj-auth-overlay .sj-auth-actions { display: grid; gap: .35rem; }
    #sj-auth-overlay .sj-auth-primary {
        display: inline-flex;
        min-height: 54px;
        align-items: center;
        justify-content: center;
        gap: .7rem;
        padding: .8rem 1rem;
        border: 1px solid var(--auth-brand);
        border-radius: 7px;
        background: var(--auth-brand);
        color: #fffdf8;
        cursor: pointer;
        font: 650 .98rem/1.3 'DM Sans', 'Segoe UI', sans-serif;
        transition: background-color 150ms ease, border-color 150ms ease, transform 150ms ease;
    }
    body.dark-mode #sj-auth-overlay .sj-auth-primary { color: #14241d; }
    #sj-auth-overlay .sj-auth-google-mark { width: 1.2rem; flex: 0 0 1.2rem; color: #4285f4; font: 700 1.1rem/1 Arial, sans-serif; text-align: center; }
    #sj-auth-overlay .sj-auth-primary:hover:not(:disabled) { border-color: #216b50; background: #216b50; transform: translateY(-1px); }
    body.dark-mode #sj-auth-overlay .sj-auth-primary:hover:not(:disabled) { border-color: #b0dec0; background: #b0dec0; }
    #sj-auth-overlay .sj-auth-primary:disabled { cursor: wait; opacity: .78; }
    #sj-auth-overlay .sj-auth-skip {
        min-height: 48px;
        padding: .65rem;
        border: 0;
        border-radius: 6px;
        background: transparent;
        color: var(--auth-muted);
        cursor: pointer;
        font: 600 .9rem/1.35 'DM Sans', 'Segoe UI', sans-serif;
        transition: background-color 150ms ease, color 150ms ease;
    }
    #sj-auth-overlay .sj-auth-skip:hover { background: var(--auth-soft); color: var(--auth-ink); }
    #sj-auth-overlay button:focus-visible { outline: 3px solid #cf9d52; outline-offset: 3px; }
    #sj-auth-overlay .sj-auth-note { display: flex; align-items: center; justify-content: center; gap: .5rem; margin: 1rem 0 0; padding-top: 1rem; border-top: 1px solid var(--auth-border); color: var(--auth-muted); font-size: .78rem; line-height: 1.45; }
    #sj-auth-overlay .sj-auth-note i { color: var(--auth-brand); }

    @keyframes sj-auth-enter { from { opacity: 0; transform: translateY(8px); } to { opacity: 1; transform: translateY(0); } }
    @media (max-width: 420px) {
        #sj-auth-overlay { padding: 1rem; }
        #sj-auth-overlay .sj-auth-card { border-radius: 11px; }
        #sj-auth-overlay .sj-auth-brand-line { margin-bottom: 1.35rem; }
    }
    @media (prefers-reduced-motion: reduce) {
        #sj-auth-overlay .sj-auth-card { animation: none; }
        #sj-auth-overlay .sj-auth-primary, #sj-auth-overlay .sj-auth-skip { transition: none; }
    }
`;

function injectAuthOverlay() {
    // Respect the student's choice for the current browser session.
    if (sessionStorage.getItem('sj_auth_gate_skipped') === 'true') return;

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
    overlay.className = 'mathjax_ignore';
    overlay.setAttribute('role', 'dialog');
    overlay.setAttribute('aria-modal', 'true');
    overlay.setAttribute('aria-labelledby', 'sj-auth-title');
    overlay.setAttribute('aria-describedby', 'sj-auth-copy');
    overlay.tabIndex = -1;

    if (!document.getElementById('sj-auth-overlay-styles')) {
        const styles = document.createElement('style');
        styles.id = 'sj-auth-overlay-styles';
        styles.textContent = AUTH_OVERLAY_CSS;
        document.head.appendChild(styles);
    }

    overlay.innerHTML = `
        <div class="sj-auth-card">
            <div class="sj-auth-brand-line">
                <span class="sj-auth-mark" aria-hidden="true">&int;</span>
                <span class="sj-auth-eyebrow">SJMaths Student Access</span>
                <span class="sj-auth-rule" aria-hidden="true"></span>
            </div>

            <h2 class="sj-auth-title" id="sj-auth-title">Sign in to continue</h2>
            <p class="sj-auth-copy" id="sj-auth-copy">Use your Google account to open premium notes, memory tricks, and monthly practice quizzes.</p>

            <div id="sj-auth-error" class="sj-auth-error" role="alert" aria-live="assertive" hidden></div>

            <div class="sj-auth-actions">
                <button id="sj-google-gate-btn" class="sj-auth-primary" type="button">
                    <span class="sj-auth-google-mark" aria-hidden="true">G</span>
                    <span>Continue with Google</span>
                </button>
                <button id="sj-skip-gate-btn" class="sj-auth-skip" type="button">Skip for now</button>
            </div>

            <p class="sj-auth-note"><i class="fas fa-key" aria-hidden="true"></i><span>No separate SJMaths password needed</span></p>
        </div>
    `;

    document.body.appendChild(overlay);
    document.getElementById('sj-google-gate-btn').focus({ preventScroll: true });

    overlay.addEventListener('keydown', (event) => {
        if (event.key !== 'Tab') return;
        const focusable = [...overlay.querySelectorAll('button:not(:disabled):not([hidden]), [href], input:not(:disabled), [tabindex]:not([tabindex="-1"])')]
            .filter(element => element.getClientRects().length > 0);
        if (!focusable.length) return;
        const first = focusable[0];
        const last = focusable[focusable.length - 1];
        if (event.shiftKey && (document.activeElement === first || document.activeElement === overlay)) {
            event.preventDefault();
            last.focus();
        } else if (!event.shiftKey && document.activeElement === last) {
            event.preventDefault();
            first.focus();
        }
    });

    // Add event listener to login button
    const btn = document.getElementById('sj-google-gate-btn');
    const skipBtn = document.getElementById('sj-skip-gate-btn');
    skipBtn.addEventListener('click', () => {
        sessionStorage.setItem('sj_auth_gate_skipped', 'true');
        removeAuthOverlay();
    });

    btn.addEventListener('click', async () => {
        try {
            btn.disabled = true;
            btn.setAttribute('aria-busy', 'true');
            const authError = document.getElementById('sj-auth-error');
            if (authError) {
                authError.hidden = true;
                authError.textContent = '';
            }
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
            btn.removeAttribute('aria-busy');
            btn.innerHTML = `<span class="sj-auth-google-mark" aria-hidden="true">G</span> <span>Continue with Google</span>`;
            const authError = document.getElementById('sj-auth-error');
            if (authError) {
                authError.textContent = `Sign-in failed: ${error.message || 'Please try again.'}`;
                authError.hidden = false;
            }
        }
    });
}

function removeAuthOverlay() {
    const overlay = document.getElementById('sj-auth-overlay');
    if (overlay) {
        // Hide immediately, but wait for MathJax's initial document pass before
        // removing the node. Removing it mid-pass can make MathJax replace a
        // child whose parent has already disappeared on slower/mobile devices.
        if (overlay.dataset.sjRemovalPending === 'true') return;
        overlay.dataset.sjRemovalPending = 'true';
        overlay.style.display = 'none';
        const finishRemoval = () => overlay.remove();
        const mathJaxStartup = window.MathJax?.startup?.promise;
        if (mathJaxStartup && typeof mathJaxStartup.then === 'function') {
            mathJaxStartup.then(finishRemoval, finishRemoval);
        } else {
            requestAnimationFrame(finishRemoval);
        }
    }

    const allContainers = document.querySelectorAll('main, .topic-container, .main-content, .page-content, section, body > div');
    allContainers.forEach(el => {
        el.style.filter = 'none';
        el.style.pointerEvents = 'auto';
        el.style.userSelect = 'auto';
    });
}

let authOverlaySchedulePending = false;

function scheduleAuthOverlay() {
    if (authOverlaySchedulePending || document.getElementById('sj-auth-overlay')) return;
    authOverlaySchedulePending = true;

    const showOverlay = () => {
        authOverlaySchedulePending = false;
        injectAuthOverlay();
    };
    const mathJaxStartup = window.MathJax?.startup?.promise;
    if (mathJaxStartup && typeof mathJaxStartup.then === 'function') {
        mathJaxStartup.then(showOverlay, showOverlay);
    } else if (document.readyState === 'complete') {
        requestAnimationFrame(showOverlay);
    } else {
        window.addEventListener('load', showOverlay, { once: true });
    }
}

// Do not decide from localStorage before Firebase has restored its persisted
// session.  Firebase briefly reports no user during startup; showing the gate
// here causes a login overlay flash on refresh/back/navigation for logged-in
// users.  The first auth-state callback is the single source of truth.
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
        scheduleAuthOverlay();
    }
});
