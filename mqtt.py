from flask_mqtt import Mqtt


mqtt = Mqtt()

@mqtt.on_connect()
def subscribe_on_broker(client, userdata, flags, rc):
    mqtt.subscribe('status-led')
