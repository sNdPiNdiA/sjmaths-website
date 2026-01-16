// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyA0kGONQMQ3NBLfnOuDPTPN_tGCqM-ed2M",
  authDomain: "sjmaths-web.firebaseapp.com",
  projectId: "sjmaths-web",
  storageBucket: "sjmaths-web.firebasestorage.app",
  messagingSenderId: "168858335686",
  appId: "1:168858335686:web:9f9a87028b7b71db7e1ac7",
  measurementId: "G-K326N2KJ2G"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);