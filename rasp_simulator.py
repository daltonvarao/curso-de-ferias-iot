import paho.mqtt.client as mqtt


def on_message(client, userdata, message):
    acao = message.payload.decode()
    if acao == 'on':
        print('Led on')
        client.publish('status-led', 'on')
    elif acao == 'off':
        client.publish('status-led', 'off')
        print('Led off')


def on_connect(client, userdata, flags, rc):
    print(f'connected with code {rc}')
    client.subscribe('action-led')


client = mqtt.Client()

client.on_connect = on_connect
client.on_message = on_message

client.connect(host='localhost', port=1883, keepalive=60)
client.loop_forever()
