// Firebase Cloud Messaging Service Worker
// This file MUST be at the root and named firebase-messaging-sw.js for FCM to work.

importScripts('https://www.gstatic.com/firebasejs/8.10.1/firebase-app.js');
importScripts('https://www.gstatic.com/firebasejs/8.10.1/firebase-messaging.js');

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

// Handle background push messages (when site is not in foreground)
messaging.onBackgroundMessage((payload) => {
    console.log('[firebase-messaging-sw.js] Background message received:', payload);

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
