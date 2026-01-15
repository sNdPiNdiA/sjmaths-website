import { initializeApp } from "https://www.gstatic.com/firebasejs/10.7.1/firebase-app.js";
import { initializeAppCheck, ReCaptchaV3Provider } from "https://www.gstatic.com/firebasejs/10.7.1/firebase-app-check.js";

export const firebaseConfig = {
  apiKey: "AIzaSyAoKGON0Q3NBLfnOuDPTPN_tGCqM-ed2M",
  authDomain: "sjmaths-web.firebaseapp.com",
  projectId: "sjmaths-web",
  storageBucket: "sjmaths-web.firebasestorage.app",
  messagingSenderId: "168858335686",
  appId: "1:168858335686:web:9f9a87028b7b71db7e1ac7",
  measurementId: "G-K326N2KJ2G"
};

const app = initializeApp(firebaseConfig);

// 🔐 App Check (replace with your SITE KEY, not secret key)
const appCheck = initializeAppCheck(app, {
  provider: new ReCaptchaV3Provider("6LeFxEssAAAAAIG-gA4fjxsR-V6t2hjvH0esO217"),
  isTokenAutoRefreshEnabled: true
});
