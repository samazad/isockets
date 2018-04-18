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

def payload():

    timeOut = int((time.time() + 0.5) * 1000)
    pTime = timeOut - 1

    device_id = D0000000000000000000000000000001

    p = '{"optCode":"0030","errCode":"9999","timeOut":"' + str(timeOut) + '","devArray":[{"devID":"D1C726BF635E4AC73D9F711CDF4378DD","numOfSen":"1","senArray":[{"senID":"1","senType":"0005","numOfParam":"4","paramArray":[{"paramType":"0055","paramValue":"0.2","paramValueType":"float","paramUnit":"V","paramTime":"946710009444","paramPre":"0.1"},{"paramType":"0060","paramValue":"0.0","paramValueType":"float","paramUnit":"A","paramTime":"946710009445","paramPre":"0.01"},{"paramType":"0065","paramValue":"0.0","paramValueType":"float","paramUnit":"W","paramTime":"946710009445","paramPre":"0.1"},{"paramType":"0070","paramValue":"0.0","paramValueType":"float","paramUnit":"KW.h","paramTime":"946710009445","paramPre":"0.1"}]}]}]}}'
    return(p)

while True:
    p = payload()
    print("Payload: " + p)
    (rc, mid) = client.publish(mqtt_topic, p, qos=0)
    time.sleep(5)
