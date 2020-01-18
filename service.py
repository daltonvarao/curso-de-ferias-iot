from mqtt import mqtt
from socket_io import socketio


status_led = 'off'

@socketio.on('connect')
def on_connect():
    global status_led
    socketio.emit('status-led', status_led)

@mqtt.on_message()
def on_status_message(client, userdata, message):
    global status_led
    status_led = message.payload.decode()
    socketio.emit('status-led', status_led)

@socketio.on('action')
def on_message(message):
    mqtt.publish('action-led', message)
