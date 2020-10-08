import paho.mqtt.client as mqtt
from pymongo import MongoClient
import json
from datetime import date
#import datetime

mongo_client = MongoClient('localhost', 27018)
mongo_db = mongo_client['ProjetoIN242']
mongo_collection = mongo_db['contadorpessoas']


def msg_recebida(mqtt_client, obj, msg):
    print('recebendo mensagem...')
    print(msg.payload)
    msg_formatada = json.loads(msg.payload)
    msg_formatada['Dia'] = date.today().strftime('%d/%m/%Y')#datetime.datetime.now()
    mongo_collection.insert_one(msg_formatada)
    print('mensagem inserida...')

print('Conectando ao broker MQTT...')
mqtt_client = mqtt.Client()
mqtt_client.connect('127.0.0.1', 1883)
mqtt_client.on_message = msg_recebida
mqtt_client.subscribe('ProjetoIN242')
mqtt_client.loop_forever()

