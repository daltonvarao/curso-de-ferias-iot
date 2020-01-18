from flask import Flask, render_template

from mqtt import mqtt
from socket_io import socketio
import service


app = Flask(
    __name__,
    static_folder='static',
    static_url_path=''
    )

app.config['SECRET_KEY'] = 'ih6cep2-s1dck4n-in89ons-d2dd3fn-ws3dj0s'
app.config['DEBUG'] = True


mqtt.init_app(app)
socketio.init_app(app)

@app.route('/')
def index():
    return render_template('index.html')

socketio.run(app)
