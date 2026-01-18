const CACHE_NAME = 'sjmaths-no-cache-v1';

// Install Event: Skip waiting to activate immediately
self.addEventListener('install', (event) => {
    self.skipWaiting();
});

// Activate Event: Delete all existing caches to ensure fresh load
self.addEventListener('activate', (event) => {
    event.waitUntil(
        caches.keys().then((cacheNames) => {
            return Promise.all(
                cacheNames.map((cache) => caches.delete(cache))
            );
        })
    );
    self.clients.claim();
});

// Fetch Event: Network Only (No Caching)
self.addEventListener('fetch', (event) => {
    event.respondWith(fetch(event.request));
});