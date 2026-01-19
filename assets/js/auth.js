// assets/js/auth.js

import { GoogleAuthProvider, signInWithPopup } from "https://www.gstatic.com/firebasejs/12.8.0/firebase-auth.js";
import { auth, analytics, logEvent } from "./firebase-config.js";
import { showToast } from "./utils.js";

const provider = new GoogleAuthProvider();

document.addEventListener("DOMContentLoaded", () => {
    const googleBtn = document.getElementById("googleLoginBtn");

    if (!googleBtn) return;

    googleBtn.addEventListener("click", async () => {
        try {
            const result = await signInWithPopup(auth, provider);

            logEvent(analytics, "login", { method: "google" });

            // Success redirect
            window.location.href = "/profile.html";

        } catch (error) {
            console.error("Google Login Error:", error);
            showToast(error.message, "error");
        }
    });
});

logEvent(analytics, "page_view", {
    page_title: document.title,
    page_path: window.location.pathname
});
