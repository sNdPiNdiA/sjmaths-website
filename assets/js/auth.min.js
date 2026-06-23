// assets/js/auth.js

import { GoogleAuthProvider, signInWithPopup, onAuthStateChanged, signOut } from "https://www.gstatic.com/firebasejs/12.8.0/firebase-auth.js";
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

document.addEventListener("DOMContentLoaded", () => {
    const googleBtn = document.getElementById("googleLoginBtn");

    if (!googleBtn) return;

    googleBtn.addEventListener("click", async () => {
        try {
            const result = await signInWithPopup(auth, provider);
            const user = result.user;

            logEvent(analytics, "login", { method: "google" });

            // Create/update user document in Firestore (merge to preserve existing fields)
            await setDoc(doc(db, "users", user.uid), {
                displayName: user.displayName || "",
                email: user.email || "",
                photoURL: user.photoURL || "",
                lastLogin: serverTimestamp()
            }, { merge: true });

            window.location.href = getPostLoginTarget();

        } catch (error) {
            console.error("Google Login Error:", error);
            showToast(error.message, "error");
        }
    });
});

// Exported Auth Functions
export const checkAuth = () => {
    return new Promise((resolve) => {
        const unsubscribe = onAuthStateChanged(auth, (user) => {
            unsubscribe();
            resolve(user);
        });
    });
};

export const logout = async () => {
    try {
        await signOut(auth);
        window.location.reload();
    } catch (error) {
        console.error("Logout Error:", error);
    }
};
