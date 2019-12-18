var CACHE_NAME = 'my-site-cache-v1';
var urlsToCache = [
    '/',
    '/static/core/css/bootstrap-grid.css',
    '/static/core/css/bootstrap-grid.css.map',
    '/static/core/css/bootstrap-grid.min.css',
    '/static/core/css/bootstrap-grid.min.css.map',
    '/static/core/css/bootstrap-reboot.css',
    '/static/core/css/bootstrap-reboot.css.map',
    '/static/core/css/bootstrap-reboot.min.css',
    '/static/core/css/bootstrap-reboot.min.css.map',
    '/static/core/css/bootstrap.css',
    '/static/core/css/bootstrap.css.map',
    '/static/core/css/bootstrap.min.css',
    '/static/core/css/bootstrap.min.css.map',
    '/static/core/css/estilo_floreria.css',
    '/static/core/img/flores_7.jpg',
    '/static/core/img/flores_8.jpg',
    '/static/core/img/logo-floreria.png',
    '/static/core/img/macro.png',
    '/static/core/img/ramo_5.jpg',
    '/static/core/img/ramo_6.jpg',
    '/static/core/img/ramo_flores_1.jpg',
    '/static/core/img/ramo_flores_2.jpg',
    '/static/core/img/ramo_flores_3.jpg',
    '/static/core/img/ramo_flores_4.jpg',
    '/static/core/img/rosa.jpg',
    '/static/core/img/Rosas.jpg',
];

self.addEventListener('install', function(event) {
  // Perform install steps
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(function(cache) {
        console.log('Opened cache');
        return cache.addAll(urlsToCache);
      })
  );
});

self.addEventListener('fetch', function(event) {
    event.respondWith(

      fetch(event.request)
      .then((result)=>{
        return caches.open(CACHE_NAME)
        .then(function(c) {
          c.put(event.request.url, result.clone())
          return result;
        })
    })
    .catch(function(e){
        return caches.match(event.request)
    })


   
  );
});

