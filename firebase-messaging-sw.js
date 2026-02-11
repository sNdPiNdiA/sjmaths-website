// Firebase Cloud Messaging Service Worker
// This file MUST be at the root and named firebase-messaging-sw.js for FCM to work.

importScripts('https://www.gstatic.com/firebasejs/8.10.1/firebase-app.js');
importScripts('https://www.gstatic.com/firebasejs/8.10.1/firebase-messaging.js');
importScripts('https://www.gstatic.com/firebasejs/8.10.1/firebase-firestore.js');

firebase.initializeApp({
    apiKey: "AIzaSyA0kGONQMQ3NBLfnOuDPTPN_tGCqM-ed2M",
    authDomain: "sjmaths-web.firebaseapp.com",
    projectId: "sjmaths-web",
    storageBucket: "sjmaths-web.firebasestorage.app",
    messagingSenderId: "168858335686",
    appId: "1:168858335686:web:9f9a87028b7b71db7e1ac7",
    measurementId: "G-K326N2KJ2G"
});

const messaging = firebase.messaging();
const db = firebase.firestore();

// Save notification to Firestore so it appears on the notifications page
function saveNotificationToFirestore(payload) {
    const title = payload.notification?.title || payload.data?.title || 'SJMaths';
    const body = payload.notification?.body || payload.data?.body || 'You have a new notification.';
    const notifId = payload.data?.tag || ('push_' + Date.now());

    return db.collection('notifications').doc(notifId).set({
        id: notifId,
        title: title,
        body: body,
        date: new Date().toISOString().split('T')[0],
        type: payload.data?.type || 'announcement',
        icon: payload.data?.icon || 'fa-bell',
        color: payload.data?.color || '#e3f2fd',
        iconColor: payload.data?.iconColor || '#1976d2',
        source: 'fcm',
        timestamp: firebase.firestore.FieldValue.serverTimestamp()
    }, { merge: true }).then(() => {
        console.log('[firebase-messaging-sw.js] Notification saved to Firestore');
    }).catch(err => {
        console.error('[firebase-messaging-sw.js] Failed to save notification:', err);
    });
}

// Handle background push messages (when site is not in foreground)
messaging.onBackgroundMessage((payload) => {
    console.log('[firebase-messaging-sw.js] Background message received:', payload);

    // Save to Firestore for the notifications page
    saveNotificationToFirestore(payload);

    const notificationTitle = payload.notification?.title || payload.data?.title || 'SJMaths';
    const notificationOptions = {
        body: payload.notification?.body || payload.data?.body || 'You have a new notification.',
        icon: '/assets/icons/icon-192x192.png',
        badge: '/assets/icons/icon-192x192.png',
        tag: payload.data?.tag || 'sjmaths-notification',
        data: {
            url: payload.data?.url || '/notifications.html'
        }
    };

    return self.registration.showNotification(notificationTitle, notificationOptions);
});

// Handle notification click — open the relevant page
self.addEventListener('notificationclick', (event) => {
    event.notification.close();

    const targetUrl = event.notification.data?.url || '/notifications.html';

    event.waitUntil(
        clients.matchAll({ type: 'window', includeUncontrolled: true }).then((windowClients) => {
            for (const client of windowClients) {
                if (client.url.includes(self.location.origin) && 'focus' in client) {
                    client.navigate(targetUrl);
                    return client.focus();
                }
            }
            return clients.openWindow(targetUrl);
        })
    );
});
