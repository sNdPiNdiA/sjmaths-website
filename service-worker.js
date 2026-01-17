const CACHE_NAME = 'sjmaths-v5';
const ASSETS_TO_CACHE = [
    '/',
    '/index.html',
    '/manifest.json',
    '/offline.html',
    '/pages/coming-soon.html',
    '/assets/css/main.css',
    '/assets/css/layout.css',
    '/assets/css/component.css',
    '/assets/css/hero.css',
    '/assets/css/auth.css',
    '/assets/css/dashboard.css',
    '/assets/css/error.css',
    '/assets/css/improved-ui.css',
    '/assets/css/pages.css',
    '/assets/js/main.js',
    '/assets/js/navigation.js',
    '/assets/js/search.js',
    '/assets/js/auth.js',
    '/assets/js/firebase-config.js',
    '/shared-header.js',
    '/user-profile.js',
    '/search.js',
    '/assets/favicon.svg'
];

// Install Event: Cache core assets
self.addEventListener('install', (event) => {
    event.waitUntil(
        caches.open(CACHE_NAME)
            .then((cache) => {
                return cache.addAll(ASSETS_TO_CACHE);
            })
    );
});

// Message Event: Listen for "SKIP_WAITING" to force update
self.addEventListener('message', (event) => {
    if (event.data && event.data.type === 'SKIP_WAITING') {
        self.skipWaiting();
    }
});

// Activate Event: Clean up old caches
self.addEventListener('activate', (event) => {
    event.waitUntil(
        caches.keys().then((cacheNames) => {
            return Promise.all(
                cacheNames.map((cache) => {
                    if (cache !== CACHE_NAME) {
                        return caches.delete(cache);
                    }
                })
            );
        })
    );
});

// Fetch Event: Stale-While-Revalidate / Dynamic Caching
self.addEventListener('fetch', (event) => {
    // Skip cross-origin requests (like Firebase, Google Fonts) from caching logic if needed, 
    // or handle them. For now, we focus on same-origin.
    if (!event.request.url.startsWith(self.location.origin)) {
        return;
    }

    event.respondWith(
        caches.match(event.request)
            .then((response) => {
                // Return cached response if found
                if (response) {
                    return response;
                }

                // If not in cache, fetch from network
                return fetch(event.request)
                    .then((networkResponse) => {
                        // Check if we received a valid response
                        if (!networkResponse || networkResponse.status !== 200 || networkResponse.type !== 'basic') {
                            return networkResponse;
                        }

                        // Clone the response to cache it (Dynamic Caching)
                        const responseToCache = networkResponse.clone();

                        caches.open(CACHE_NAME)
                            .then((cache) => {
                                cache.put(event.request, responseToCache);
                            });

                        return networkResponse;
                    })
                    .catch(() => {
                        // If network fails and request is for an HTML page, show offline page
                        if (event.request.headers.get('accept').includes('text/html')) {
                            return caches.match('/offline.html');
                        }
                    });
            })
    );
});