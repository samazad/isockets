#!/usr/bin/python

import paho.mqtt.client as paho
import time
import random
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-i','--mqttClientId',help='MQTT Client ID',required=True)
parser.add_argument('-t','--mqttTopic',help='MQTT Topic',required=True)
parser.add_argument('-b','--mqttBroker',help='MQTT Broker',required=True)
parser.add_argument('-p','--mqttPort',help='MQTT Broker Port',required=False,type=int,default=1883)

args = parser.parse_args()
 
mqtt_client_id = args.mqttClientId
mqtt_topic = args.mqttTopic
mqtt_broker = args.mqttBroker
mqtt_port = args.mqttPort

def on_publish(client, userdata, mid):
    print("Msg. ID: " + str(mid))

client = paho.Client(client_id=mqtt_client_id, clean_session=True, userdata=None, protocol=paho.MQTTv31)
client.on_publish = on_publish
client.connect(mqtt_broker, mqtt_port, keepalive=60, bind_address="")
client.loop_start()
 
while True:
    temperature = str(random.randint(75, 85)) + '.' + str(random.randint(0,9)) + '.. F' 
    print("Current Temperature = " + temperature)
    (rc, mid) = client.publish(mqtt_topic, temperature, qos=0)
    time.sleep(5)
