/**
 * Lightweight Firebase Analytics Module
 * Only loads analytics SDK (~15KB) instead of full Firebase (~230KB+)
 * Use this on pages that only need page view tracking
 */

import { initializeApp, getApps, getApp } from "https://www.gstatic.com/firebasejs/12.8.0/firebase-app.js";
import { getAnalytics, logEvent } from "https://www.gstatic.com/firebasejs/12.8.0/firebase-analytics.js";

const firebaseConfig = {
    apiKey: "AIzaSyA0kGONQMQ3NBLfnOuDPTPN_tGCqM-ed2M",
    authDomain: "sjmaths-web.firebaseapp.com",
    projectId: "sjmaths-web",
    storageBucket: "sjmaths-web.firebasestorage.app",
    messagingSenderId: "168858335686",
    appId: "1:168858335686:web:9f9a87028b7b71db7e1ac7",
    measurementId: "G-K326N2KJ2G"
};

const app = getApps().length ? getApp() : initializeApp(firebaseConfig);
const analytics = getAnalytics(app);

export { analytics, logEvent };
