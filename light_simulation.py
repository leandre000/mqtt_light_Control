import paho.mqtt.client as mqtt

# MQTT broker details
BROKER = "test.mosquitto.org"
TOPIC = "/student_group/light_control"

# Callback for when a message is received
def on_message(client, userdata, message):
    payload = message.payload.decode()
    if payload == "ON":
        print("💡 Light is TURNED ON")
    elif payload == "OFF":
        print("💡 Light is TURNED OFF")

# Set up MQTT client
client = mqtt.Client()
client.on_message = on_message

# Connect to the MQTT broker
client.connect(BROKER, 1883, 60)
client.subscribe(TOPIC)

print("Listening for messages... Press Ctrl+C to exit.")
client.loop_forever()