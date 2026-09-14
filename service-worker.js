const CACHE_NAME = 'sjmaths-v9ac6a61d';
const ASSETS = [
    './',
    './index.html',
    './offline.html',
    './assets/css/main.min.css?v=a88cc396',
    './assets/css/layout.min.css?v=e4922b08',
    './assets/css/component.min.css?v=2b8ae814',
    './assets/css/improved-ui.min.css?v=dd2cffe9',
    './assets/vendor/fontawesome/css/all.min.css?v=db73e473',
    './components/header.html',
    './components/footer.html'
];

self.addEventListener('install', (event) => {
    event.waitUntil(
        caches.open(CACHE_NAME)
            .then((cache) => cache.addAll(ASSETS))
            .then(() => self.skipWaiting())
    );
});

self.addEventListener('activate', (event) => {
    event.waitUntil(
        Promise.all([
            caches.keys().then((keys) => Promise.all(
                keys.map((key) => {
                    if (key !== CACHE_NAME) return caches.delete(key);
                })
            )),
            self.clients.claim()
        ])
    );
});

self.addEventListener('message', (event) => {
    if (event.data && event.data.type === 'SKIP_WAITING') {
        self.skipWaiting();
    }
});

self.addEventListener('fetch', (event) => {
    // 0. Bypass for non-GET requests (POST/PUT uploads) and external APIs (Firebase)
    if (event.request.method !== 'GET' ||
        !event.request.url.startsWith(self.location.origin) ||
        event.request.url.includes('googleapis.com') ||
        event.request.url.includes('firebase')) {
        return;
    }

    const url = new URL(event.request.url);

    // 1. Stale-While-Revalidate for Components (Header/Footer)
    // This ensures instant loading while updating in the background
    if (url.pathname.includes('/components/')) {
        const cachePromise = caches.open(CACHE_NAME);
        const cachedResponsePromise = cachePromise.then((cache) => cache.match(event.request));
        const networkResponsePromise = cachePromise.then((cache) =>
            fetch(event.request).then(async (networkResponse) => {
                if (networkResponse.ok) {
                    await cache.put(event.request, networkResponse.clone());
                }
                return networkResponse;
            })
        );

        event.respondWith(
            cachedResponsePromise.then((cachedResponse) => cachedResponse || networkResponsePromise)
        );
        event.waitUntil(networkResponsePromise.catch(() => undefined));
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
        caches.match(event.request).then((response) => {
            return response || fetch(event.request).catch((err) => {
                console.warn('SW Fetch fail:', event.request.url);
                return new Response('Network error happened', {
                    status: 408,
                    headers: { 'Content-Type': 'text/plain' },
                });
            });
        })
    );
});
