import { initializeApp, getApps, getApp } from "https://www.gstatic.com/firebasejs/10.7.1/firebase-app.js";
import { getAuth, onAuthStateChanged } from "https://www.gstatic.com/firebasejs/10.7.1/firebase-auth.js";
import { getFirestore, doc, setDoc } from "https://www.gstatic.com/firebasejs/10.7.1/firebase-firestore.js";
import { firebaseConfig } from "./firebase-config.js";

// Initialize Firebase only once
const app = getApps().length ? getApp() : initializeApp(firebaseConfig);
export const auth = getAuth(app);
export const db = getFirestore(app);

// Toast function
export function showToast(message, type = "info") {
    const toast = document.createElement("div");
    toast.textContent = message;
    toast.style.cssText = `
        position:fixed;
        bottom:30px;
        left:50%;
        transform:translateX(-50%);
        background:${type === "error" ? "#e74c3c" : "#2ecc71"};
        color:white;
        padding:12px 24px;
        border-radius:50px;
        z-index:9999;
        font-family:Poppins;
        font-size:14px;
    `;
    document.body.appendChild(toast);
    setTimeout(() => toast.remove(), 3000);
}

// Save logged-in user to Firestore
onAuthStateChanged(auth, async (user) => {
    if (user) {
        await setDoc(doc(db, "users", user.uid), {
            email: user.email,
            role: "student",
            createdAt: new Date()
        }, { merge: true });
    }
});
