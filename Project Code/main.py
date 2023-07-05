import dht
import machine
import time
import network
import boot
import lib.timeDiff as timeDiff
from lib.simple import MQTTClient
import lib.config as config

topic_1 = "sensor"
subtopic_1 = "Temp&Humid"
subtopic_2 = "PIR"
subtopic_3 = "Rain"
rain_t = 0
PIR_sensor_t = 0
PIR_value = 0
motor = machine.Pin(16, machine.Pin.OUT)
tempSensor = dht.DHT11(machine.Pin(28))     # DHT11 Constructor
PIR_sensor = machine.Pin(27, machine.Pin.IN, machine.Pin.PULL_UP)
adc = machine.ADC(26)
wlan = network.WLAN(network.STA_IF)
time_diff = timeDiff.TimeDiff(60)

# Send initial values when the Pico boot
def initialize():
    tempSensor.measure()
    temperature = tempSensor.temperature()
    humidity = tempSensor.humidity()
    mqtt_client.publish("{}/{}".format(topic_1, subtopic_1), '{{"Temp": {}, "Humid": {}}}'.format(temperature, humidity))
    mqtt_client.publish("{}/{}".format(topic_1, subtopic_2), "{}".format(PIR_value))
    rain = 100-(adc.read_u16()/369)
    if rain <= 1:
        rain_f = 0
    else:
        rain_f = "{:.0f}".format(rain)
    mqtt_client.publish("{}/{}".format(topic_1, subtopic_3), "{}".format(rain_f))


# Define MQTT client
mqtt_client = MQTTClient(config.MQTT_CLIENT_ID, config.MQTT_SERVER, config.MQTT_PORT)

# Connect to MQTT broker
mqtt_client.connect()

initialize()
start_time = time.ticks_ms()

while True:
    while not wlan.isconnected():
        boot.connect_to_wifi()

    try:
        tempSensor.measure()
        temperature = tempSensor.temperature()
        humidity = tempSensor.humidity()
        
        if time_diff.check():
            mqtt_client.publish("{}/{}".format(topic_1, subtopic_1), '{{"Temp": {}, "Humid": {}}}'.format(temperature, humidity))

        PIR_value = PIR_sensor.value()
        if PIR_value != PIR_sensor_t:
            mqtt_client.publish("{}/{}".format(topic_1, subtopic_2), "{}".format(PIR_value))
            PIR_sensor_t = PIR_value
        if PIR_value == 1:
            motor.value(1)
        else:
            motor.value(0)

        rain = 100-(adc.read_u16()/369)
        if rain <= 1:
            rain_f = 0
        else:
            rain_f = "{:.0f}".format(rain)

        if rain_f != rain_t:
            mqtt_client.publish("{}/{}".format(topic_1, subtopic_3), "{}".format(rain_f))
            rain_t = rain_f

    except Exception as error:
        print("Exception occurred", error)
    time.sleep(1)