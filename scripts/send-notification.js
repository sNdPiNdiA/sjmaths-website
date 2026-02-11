// ====================================================
// SJMaths - Send Notification to Firestore
// ====================================================
// HOW TO USE:
// 1. Open your live site (https://www.sjmaths.com) in Chrome
// 2. Make sure you are logged in (Firebase must be initialized)
// 3. Open the browser's Developer Console (F12 → Console)
// 4. Paste this entire script and press Enter
//
// NOTE: This adds a notification to the Firestore 'notifications' collection.
// Users will see it on the notifications page. To also send a PUSH notification,
// use Firebase Console → Cloud Messaging → "Send your first message".
// ====================================================

// Get a reference to the Firestore database (v8 compat is loaded on the site)
const db = firebase.firestore();

// Customize your notification below:
const newNotification = {
    id: 'n' + Date.now(),
    title: 'New Feature Alert!',
    body: 'We have just launched a new dark mode feature. Check it out in the settings.',
    date: new Date().toISOString().split('T')[0],  // e.g., '2026-02-10'
    type: 'system',         // 'content', 'announcement', 'system'
    icon: 'fa-star',        // Font Awesome icon class
    color: '#e3f2fd',       // Icon background color
    iconColor: '#1976d2'    // Icon foreground color
};

// Add to Firestore
db.collection('notifications').doc(newNotification.id).set(newNotification)
    .then(() => console.log('✅ Notification sent successfully!'))
    .catch((error) => console.error('❌ Error sending notification:', error));
