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

//codigo para notificaciones push

importScripts('https://www.gstatic.com/firebasejs/3.9.0/firebase-app.js');
importScripts('https://www.gstatic.com/firebasejs/3.9.0/firebase-messaging.js');

var firebaseConfig = {
  apiKey: "AIzaSyCWK6nju5QShdQVtv955jKCg0p2rY0tntk",
  authDomain: "floreriapetalos-161a3.firebaseapp.com",
  databaseURL: "https://floreriapetalos-161a3.firebaseio.com",
  projectId: "floreriapetalos-161a3",
  storageBucket: "floreriapetalos-161a3.appspot.com",
  messagingSenderId: "410885916020",
  appId: "1:410885916020:web:e7561e888a069e64071821"
};
// Initialize Firebase
firebase.initializeApp(firebaseConfig);

let messaging = firebase.messaging();

messaging.setBackgroundMessageHandler(function(payload){

  let title = 'titulo de la notificacion';

  let options = {
      body:'este es el mensaje',
      icon: '/static/core/img/logo-floreria.png'
  }

  self.registration.showNotification(title, options);


});