from flask import Flask
from flask import render_template
from flask_socketio import SocketIO
from flask_mqtt import Mqtt

app = Flask(
    __name__,
    static_folder='static',
    static_url_path=''
    )


app.config['SECRET_KEY'] = 'ih6cep2-s1dck4n-in89ons-d2dd3fn-ws3dj0s'
app.config['DEBUG'] = True

mqtt = Mqtt(app)
socketio = SocketIO(app)
status_led = 'off'

# rotas
@app.route('/')
def index():
    return render_template('index.html')

# connection with socket.io
@socketio.on('action')
def on_message(message):
    mqtt.publish('action-led', message)


@socketio.on('connect')
def on_connect():
    global status_led
    socketio.emit('status-led', status_led)

# connection with MQTT
@mqtt.on_message()
def on_status_message(client, userdata, message):
    global status_led
    status_led = message.payload.decode()
    socketio.emit('status-led', status_led)


@mqtt.on_connect()
def subscribe_on_broker(client, userdata, flags, rc):
    mqtt.subscribe('status-led')


if __name__ == "__main__":
    socketio.run(app, debug=True)
