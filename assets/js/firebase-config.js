import { initializeApp, getApps, getApp } from "https://www.gstatic.com/firebasejs/12.8.0/firebase-app.js";
import { getAuth } from "https://www.gstatic.com/firebasejs/12.8.0/firebase-auth.js";
import { getFirestore } from "https://www.gstatic.com/firebasejs/12.8.0/firebase-firestore.js";

export const firebaseConfig = {
  apiKey: "AIzaSyA0kGONQM03NBLfnOuDPTPN_tGCqM-ed2M",
  authDomain: "sjmaths-web.firebaseapp.com",
  projectId: "sjmaths-web",
  storageBucket: "sjmaths-web.firebasestorage.app",
  messagingSenderId: "168858335686",
  appId: "1:168858335686:web:9f9a87028b7b71db7e1ac7",
  measurementId: "G-K326N2KJ2G"
};

const app = getApps().length ? getApp() : initializeApp(firebaseConfig);

export const auth = getAuth(app);
export const db = getFirestore(app);
