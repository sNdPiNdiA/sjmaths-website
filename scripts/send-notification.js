// This is a sample script to demonstrate how to add a notification to your Firestore database.
// You would typically run this from a secure environment like a Cloud Function or a server.
// For testing, you can run this in your browser's developer console on a page where Firebase is initialized.

// Make sure you have Firebase initialized in your project.
// You should have a script that looks something like this:
/*
const firebaseConfig = {
  apiKey: "YOUR_API_KEY",
  authDomain: "YOUR_AUTH_DOMAIN",
  projectId: "YOUR_PROJECT_ID",
  storageBucket: "YOUR_STORAGE_BUCKET",
  messagingSenderId: "YOUR_MESSAGING_SENDER_ID",
  appId: "YOUR_APP_ID"
};
firebase.initializeApp(firebaseConfig);
*/

// Get a reference to the Firestore database.
const db = firebase.firestore();

// The new notification you want to add.
const newNotification = {
    id: 'n' + new Date().getTime(), // A unique ID for the notification
    title: 'New Feature Alert!',
    body: 'We have just launched a new dark mode feature. Check it out in the settings.',
    date: new Date().toISOString().split('T')[0], // e.g., '2026-01-31'
    type: 'system', // 'content', 'announcement', 'system'
    icon: 'fa-star', // Font Awesome icon class
    color: '#e3f2fd',
    iconColor: '#1976d2'
};

// Add the new notification to the 'notifications' collection.
db.collection('notifications').doc(newNotification.id).set(newNotification)
    .then(() => {
        console.log('Notification sent successfully!');
    })
    .catch((error) => {
        console.error('Error sending notification: ', error);
    });
