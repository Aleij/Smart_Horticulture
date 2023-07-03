<h1 align="center">Smart Horticulture</h1>

<p align="center">
  <img src="images/banner.jpg" alt="Project Banner">
</p>

<p align="center">
  By: <a href="https://github.com/Aleij">Olle Jönsson</a> - Student ID: XX666X
</p>

## Project Overview

The Smart Horticulture project aims to build a system for monitoring temperature, humidity, rainfall, and motion in a horticulture environment. The project utilizes the Raspberry Pi Pico WH microcontroller along with a temperature and humidity sensor, a rain sensor, and a PIR motion sensor. The collected data provides insights into the environmental conditions and helps optimize plant growth and care.

## Objective

The main objective of the Smart Horticulture project is to create an automated monitoring system for horticulture environments. By utilizing sensors to collect data on temperature, humidity, rainfall, and motion, we aim to achieve the following:

- Monitor and maintain optimal environmental conditions for plant growth
- Detect and respond to changes in environmental parameters
- Provide insights for better plant care and resource management

## Materials

List of materials used in the project:

| Component                                 | Description                            | Purchase Link                                                        | Price ($) |
|-------------------------------------------|----------------------------------------|----------------------------------------------------------------------|-----------|
| <img src="images/PICO-Pi-HERO.jpg" width="100"> | Raspberry Pi Pico WH                   | [Link](https://example.com/pico-wh)                                  | 109 SEK   |
| <img src="images/dht11.jpg" width="100">   | DHT11 Temperature and Humidity Sensor   | [Link](https://example.com/dht11-sensor)                              | X         |
| <img src="images/rain-sensor.jpg" width="100">  | Rain Sensor                            | [Link](https://example.com/rain-sensor)                               | X         |
| <img src="images/pir-sensor.jpg" width="100">    | PIR (Passive Infrared) Motion Sensor    | [Link](https://example.com/pir-sensor)                                | X         |

Note: Provide brief specifications and cost information for each component.

## Computer Setup

To program the Raspberry Pi Pico WH microcontroller, follow these steps:

1. Flash the MicroPython firmware onto the Raspberry Pi Pico WH.
2. Install your preferred Integrated Development Environment (IDE) such as Visual Studio Code or Thonny.
3. Set up the necessary plugins and extensions for MicroPython development.
4. Connect the Raspberry Pi Pico WH to your computer using a USB cable.
5. Upload the code to the microcontroller and ensure proper communication is established.

## Ubuntu Server Setup

To set up the Ubuntu server for running Mosquitto MQTT protocol and Node-RED, follow these steps:

1. Install Ubuntu Server on your old laptop or a dedicated machine.
2. Install Mosquitto MQTT broker on the Ubuntu server for communication between devices.
3. Install Node-RED on the Ubuntu server for building the user interface and data flow management.
4. Configure Mosquitto MQTT and Node-RED to communicate with the Raspberry Pi Pico WH and other devices.
5. Ensure that the Ubuntu server is connected to the same network as the Raspberry Pi Pico WH.

## Data Transmission and Visualization

The Smart Horticulture project utilizes the MQTT protocol for data transmission and Node-RED for data visualization and user interface. The workflow is as follows:

1. The Raspberry Pi Pico WH collects sensor data and publishes it to specific MQTT topics.
2. The Ubuntu server, running Mosquitto MQTT broker, receives the published data.
3. Node-RED subscribes to the MQTT topics, retrieves the sensor data, and presents it on a user-friendly dashboard.
4. The dashboard displays real-time sensor readings, historical data, and provides control options for the horticulture system.

## Data Storage

To save data from the sensors on the Ubuntu server, we use the "ToFile" node in Node-RED. This node allows us to save the sensor data with timestamps into a text file on the server's local storage. We can configure the "ToFile" node to save the data at specific intervals, such as once every 30 minutes.

## Platform

The Smart Horticulture project utilizes a local installation of a cloud-based platform for data processing and visualization. The platform offers scalability and flexibility for future expansion of the project. Consider the following aspects:

- Data storage and retrieval
- Data visualization and dashboard creation
- Integration with other services or APIs
- Cost considerations for scaling the project

## The Code

The code for the Smart Horticulture project is written in MicroPython using Visual Studio Code with the PyMakr extension. The code includes the necessary setup for reading sensor data, connecting to the MQTT broker, and publishing the data. It also includes any specific functionalities for data processing and device control.

```python
# Add code snippets and explanations here

import this as that

def my_cool_function():
    print('not much here')

s.send(package)

# Explain your code!




