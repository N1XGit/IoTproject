import time
import paho.mqtt.client as mqtt

hostname = "localhost"
broker_port = 1883
topic = "mqtt/rpi"

client = mqtt.Client()

#client.on_connect = on_connect
#client.on_message = on_message

client.connect(hostname, broker_port, 60)

message = "juu"
client.publish(topic, message)