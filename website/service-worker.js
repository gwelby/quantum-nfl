// Quantum NFL Service Worker
const CACHE_NAME = 'nfl-quantum-v1';
const ASSETS = [
    '/',
    '/index.html',
    '/app.js',
    '/styles/main.css',
    '/styles/quantum-demos.css',
    '/styles/quantum-experience.css',
    '/styles/celebrations.css',
    '/js/quantum-demos.js',
    '/js/mobile-quantum.js',
    '/js/nfl-quantum-clock.js',
    '/js/quantum-teams.js',
    '/js/quantum-celebrations.js',
    '/sounds/effects/touchdown.mp3',
    '/sounds/effects/field_goal.mp3',
    '/sounds/effects/interception.mp3',
    '/sounds/effects/sack.mp3'
];

// Install Service Worker
self.addEventListener('install', (event) => {
    event.waitUntil(
        caches.open(CACHE_NAME)
            .then((cache) => cache.addAll(ASSETS))
            .then(() => self.skipWaiting())
    );
});

// Activate Service Worker
self.addEventListener('activate', (event) => {
    event.waitUntil(
        caches.keys().then((cacheNames) => {
            return Promise.all(
                cacheNames.map((cacheName) => {
                    if (cacheName !== CACHE_NAME) {
                        return caches.delete(cacheName);
                    }
                })
            );
        })
    );
});

// Fetch Event Handler
self.addEventListener('fetch', (event) => {
    event.respondWith(
        caches.match(event.request)
            .then((response) => {
                if (response) {
                    return response;
                }
                return fetch(event.request)
                    .then((response) => {
                        if (!response || response.status !== 200 || response.type !== 'basic') {
                            return response;
                        }
                        const responseToCache = response.clone();
                        caches.open(CACHE_NAME)
                            .then((cache) => {
                                cache.put(event.request, responseToCache);
                            });
                        return response;
                    });
            })
    );
});

// Background sync
self.addEventListener('sync', (event) => {
    if (event.tag === 'quantum-sync') {
        event.waitUntil(
            // Sync quantum data
            syncQuantumData()
        );
    }
});

// Push notification
self.addEventListener('push', (event) => {
    const options = {
        body: event.data.text(),
        icon: '/icons/icon-512x512.png',
        badge: '/icons/badge-96x96.png',
        vibrate: [100, 50, 100],
        data: {
            dateOfArrival: Date.now(),
            primaryKey: 1
        },
        actions: [
            {
                action: 'explore',
                title: 'View Prediction',
                icon: '/icons/checkmark.png'
            },
            {
                action: 'close',
                title: 'Close',
                icon: '/icons/xmark.png'
            }
        ]
    };

    event.waitUntil(
        self.registration.showNotification('Quantum NFL Update', options)
    );
});

// Notification click
self.addEventListener('notificationclick', (event) => {
    event.notification.close();

    if (event.action === 'explore') {
        event.waitUntil(
            clients.openWindow('/')
        );
    }
});

// Helper function to sync quantum data
async function syncQuantumData() {
    try {
        const response = await fetch('/api/quantum-sync');
        if (!response.ok) {
            throw new Error('Quantum sync failed');
        }
        const data = await response.json();
        
        // Process quantum data
        await processQuantumData(data);
        
        return true;
    } catch (error) {
        console.error('Quantum sync error:', error);
        return false;
    }
}

// Helper function to process quantum data
async function processQuantumData(data) {
    // Process and store quantum data
    const cache = await caches.open(CACHE_NAME);
    await cache.put('/api/quantum-data', new Response(JSON.stringify(data)));
}
