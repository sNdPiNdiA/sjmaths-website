// assets/js/firebase-config.js
import { initializeApp, getApps, getApp } from "https://www.gstatic.com/firebasejs/10.7.1/firebase-app.js";
import { getAuth } from "https://www.gstatic.com/firebasejs/10.7.1/firebase-auth.js";
import { getFirestore } from "https://www.gstatic.com/firebasejs/10.7.1/firebase-firestore.js";

export const firebaseConfig = {
  apiKey: "AIzaSyAoKGON0Q3NBLfnOuDPTPN_tGCqM-ed2M",
  authDomain: "sjmaths-web.firebaseapp.com",
  projectId: "sjmaths-web",
  storageBucket: "sjmaths-web.appspot.com",
  messagingSenderId: "168858335686",
  appId: "1:168858335686:web:9fa87028b7b71db7e1ac7",
  measurementId: "G-K326N2KJ2G"
};

const app = getApps().length ? getApp() : initializeApp(firebaseConfig);

export const auth = getAuth(app);
export const db = getFirestore(app);
