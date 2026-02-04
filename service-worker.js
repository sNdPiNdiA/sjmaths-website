const CACHE_NAME = 'sjmaths-v1770187360';
const ASSETS = [
    './',
    './index.html',
    './offline.html',
    './assets/css/main.min.css?v=1770179813',
    './assets/css/layout.min.css?v=1770179813',
    './assets/css/component.min.css?v=1770179813',
    './assets/css/improved-ui.min.css?v=1770179813',
    './components/header.html',
    './components/footer.html'
];

self.addEventListener('install', (event) => {
    event.waitUntil(
        caches.open(CACHE_NAME).then((cache) => cache.addAll(ASSETS))
    );
});

self.addEventListener('activate', (event) => {
    event.waitUntil(
        caches.keys().then((keys) => Promise.all(
            keys.map((key) => {
                if (key !== CACHE_NAME) return caches.delete(key);
            })
        ))
    );
    self.clients.claim();
});

self.addEventListener('message', (event) => {
    if (event.data && event.data.type === 'SKIP_WAITING') {
        self.skipWaiting();
    }
});

self.addEventListener('fetch', (event) => {
    // 0. Bypass for non-GET requests (POST/PUT uploads) and external APIs (Firebase)
    if (event.request.method !== 'GET' ||
        event.request.url.includes('googleapis.com') ||
        event.request.url.includes('firebase')) {
        return;
    }

    const url = new URL(event.request.url);

    // 1. Stale-While-Revalidate for Components (Header/Footer)
    // This ensures instant loading while updating in the background
    if (url.pathname.includes('/components/')) {
        event.respondWith(
            caches.open(CACHE_NAME).then((cache) => {
                return cache.match(event.request).then((cachedResponse) => {
                    const fetchPromise = fetch(event.request).then((networkResponse) => {
                        cache.put(event.request, networkResponse.clone());
                        return networkResponse;
                    });
                    return cachedResponse || fetchPromise;
                });
            })
        );
        return;
    }

    // 2. Network First for HTML Navigation (ensures fresh content, falls back to offline)
    if (event.request.mode === 'navigate') {
        event.respondWith(
            fetch(event.request).catch(() => caches.match('/offline.html'))
        );
        return;
    }

    // 3. Cache First for Static Assets (CSS, JS, Images)
    event.respondWith(
        caches.match(event.request, { ignoreSearch: true }).then((response) => {
            return response || fetch(event.request);
        })
    );
});