import time
import paho.mqtt.client as mqtt
import random
import json

print('Conectando ao MQTT Broker...')
mqtt_client = mqtt.Client()
mqtt_client.connect('127.0.0.1', 1883)

pessoas = random.randint(0, 10)
print(pessoas)

mensagem = {
    'Entrada': 'Porta Principal',
    'Quantidade de pessoas': pessoas
   }

mqtt_client.publish('ProjetoIN242', json.dumps(mensagem))