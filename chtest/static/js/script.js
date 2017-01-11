var ReconnectingWebSocket = require('reconnecting-websocket');

var wsuri = "ws://" + window.location.host + "/datastream/?session_key=" + window.django.session_key;

var app = {}

var socket = new ReconnectingWebSocket(wsuri) ;
socket.onmessage = function(e) {
    console.log('class onmessage', e.data);
}
socket.onopen = function() {
    console.log('socket opened');
}
app.socketsend = function(x){
  console.log('sending via ws', JSON.stringify(x));
  socket.send(JSON.stringify(x));
}

if (socket.readyState == WebSocket.OPEN) socket.onopen();
window.app = app;
