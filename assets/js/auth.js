import { initializeApp, getApps, getApp } from "https://www.gstatic.com/firebasejs/12.8.0/firebase-app.js";
import { 
  getAuth, 
  onAuthStateChanged 
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
import { showToast } from "./utils.js";

/* -------------------- INITIALIZE FIREBASE -------------------- */
const app = getApps().length ? getApp() : initializeApp(firebaseConfig);
export const auth = getAuth(app);
export const db = getFirestore(app);
const analytics = getAnalytics(app);

export { showToast };

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
      method: "google"
    });

    // Analytics: verified
    logEvent(analytics, "email_verified");
  }
});
