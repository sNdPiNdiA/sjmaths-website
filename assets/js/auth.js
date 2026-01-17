import { initializeApp, getApps, getApp } from "https://www.gstatic.com/firebasejs/12.8.0/firebase-app.js";
import { 
  getAuth, 
  onAuthStateChanged, 
  signOut 
} from "https://www.gstatic.com/firebasejs/12.8.0/firebase-auth.js";
import { 
  getFirestore, 
  doc, 
  setDoc 
} from "https://www.gstatic.com/firebasejs/12.8.0/firebase-firestore.js";
import { 
  getAnalytics, 
  logEvent 
} from "https://www.gstatic.com/firebasejs/12.8.0/firebase-analytics.js";

import { firebaseConfig } from "./firebase-config.js";

/* -------------------- INITIALIZE FIREBASE -------------------- */
const app = getApps().length ? getApp() : initializeApp(firebaseConfig);
export const auth = getAuth(app);
export const db = getFirestore(app);
const analytics = getAnalytics(app);

/* -------------------- TOAST NOTIFICATION -------------------- */
export function showToast(message, type = "info") {
  const toast = document.createElement("div");
  toast.innerHTML = message;
  toast.style.cssText = `
    position: fixed;
    bottom: 30px;
    left: 50%;
    transform: translateX(-50%);
    background: ${type === "error" ? "#e74c3c" : type === "success" ? "#2ecc71" : "#333"};
    color: white;
    padding: 12px 24px;
    border-radius: 50px;
    z-index: 10000;
    font-family: Poppins, sans-serif;
    font-size: 14px;
  `;
  document.body.appendChild(toast);
  setTimeout(() => toast.remove(), 3000);
}

/* -------------------- SAVE VERIFIED USERS + ANALYTICS -------------------- */
onAuthStateChanged(auth, async (user) => {
  if (user && user.emailVerified) {
    await setDoc(doc(db, "users", user.uid), {
      email: user.email,
      role: "student",
      verified: true,
      lastLogin: new Date()
    }, { merge: true });

    // Analytics: login
    logEvent(analytics, "login", {
      method: user.providerData[0]?.providerId || "password"
    });

    // Analytics: verified
    logEvent(analytics, "email_verified");
  }
});

/* -------------------- PAGE PROTECTION -------------------- */
export function requireAuth() {
  onAuthStateChanged(auth, (user) => {
    if (!user) {
      sessionStorage.setItem("sjmaths_redirect", window.location.href);
      window.location.href = "/login.html";
      return;
    }

    if (!user.emailVerified) {
      showToast("Please verify your email before accessing this page.", "error");
      signOut(auth).then(() => {
        window.location.href = "/login.html";
      });
    }
  });
}
