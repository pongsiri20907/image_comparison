from http import client
import paho.mqtt.client as paho
from random import randrange, uniform
import time
import sys

client = paho.Client()

if client.connect("localhost", 1883, 60) != 0:
    print("Cannot connect to Mqtt Broker !")
    sys.exit(-1)

while True:
    client.publish("test", "HELLO NODE RED !", 0)
    time.sleep(3)




