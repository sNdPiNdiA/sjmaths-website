const CACHE_NAME = 'sjmaths-v3';
const ASSETS_TO_CACHE = [
    '/',
    '/index.html',
    '/offline.html',
    '/assets/css/main.css',
    '/assets/css/layout.css',
    '/assets/css/component.css',
    '/assets/css/hero.css',
    '/assets/js/main.js',
    '/assets/js/navigation.js',
    '/assets/js/search.js',
    '/assets/js/auth.js',
    '/assets/js/firebase-config.js',
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

// Fetch Event: Serve from cache, fall back to network, then offline page
self.addEventListener('fetch', (event) => {
    event.respondWith(
        caches.match(event.request)
            .then((response) => {
                // Return cached response if found, else fetch from network
                return response || fetch(event.request)
                    .catch(() => {
                        // If network fails and request is for an HTML page, show offline page
                        if (event.request.headers.get('accept').includes('text/html')) {
                            return caches.match('/offline.html');
                        }
                    });
            })
    );
});