<h1 align="center">Smart Horticulture</h1>

<p align="center">
  <img src="images/IoT_CHILLI_2.png" alt="Project Banner">
</p>

<p align="center">
  By: <a href="https://github.com/Aleij">Olle Jönsson</a> - Student ID: oj222iu
</p>

## Project Overview

The Smart Horticulture project aims to build a system for monitoring a horticulture environment. The project utilizes the Raspberry Pi Pico WH microcontroller along with a temperature and humidity sensor, a rain sensor, and a PIR motion sensor for controlling a motor. The collected data provides insights into the environmental conditions and helps optimize plant growth and care.

### Estimated time needed for this project: 6 hours

## Objective

The main objective of the Smart Horticulture project is to create an automated monitoring system for horticulture environments. By utilizing sensors to collect data on temperature, humidity, rainfall, and motion, we aim to achieve the following:

- Monitor and maintain optimal environmental conditions for plant growth
- Detect and respond to changes in environmental parameters
- Provide insights for better plant care and resource management
- Survailance of the plants for bird intruders

## Materials

List of materials used in the project:

| Component                                 | Description                            | Purchase Link                                                        | Price (SEK) |
|-------------------------------------------|----------------------------------------|----------------------------------------------------------------------|-----------|
| <img src="images/PICO-WH.jpg" width="150"> | Raspberry Pi Pico WH                   | [Link](https://www.electrokit.com/produkt/raspberry-pi-pico-wh/)                                  | 109   |
| <img src="images/DHT11.jpg" width="150">   | DHT11 Temperature and Humidity Sensor   | [Link](https://www.electrokit.com/produkt/digital-temperatur-och-fuktsensor-dht11/)                              | 49  |
| <img src="images/RAIN.jpg" width="150">  | Rain Sensor                            | [Link](https://www.electrokit.com/produkt/regnsensor/)                               | 39         |
| <img src="images/PIR.jpg" width="150">    | PIR (Passive Infrared) Motion Sensor    | [Link](https://www.electrokit.com/produkt/pir-rorelsedetektor-hc-sr501/)                                | 49         |
| <img src="images/RELAY.jpg" width="150">    | Relay module 3.3V (5V)    | [Link](https://www.electrokit.com/produkt/relamodul-5v/)                                | 39         |
| <img src="images/DC-MOTOR.jpg" width="150">    | DC Motor    | [Link](https://www.electrokit.com/produkt/labbsladd-20-pin-15cm-hona-hane/)                                | -         |
| <img src="images/BREADBOARD.jpg" width="150">    | Breadboard    | [Link](https://www.electrokit.com/produkt-kategori/kretskort-2/kopplingsdack-2/)                                | 69         |
| <img src="images/CABLE_MM.jpg" width="150">    | Jumper Wire Male to Male    | [Link](https://www.electrokit.com/produkt/labbsladd-20-pin-15cm-hane-hane/)                                | 29         |
| <img src="images/CABLE_MF.jpg" width="150">    | Jumper Wire Male to Female    | [Link](https://www.electrokit.com/produkt/labbsladd-20-pin-15cm-hona-hane/)                                | 29         |

## Computer Setup

### Programming the Raspberry Pi Pico WH Microcontroller

To program the Raspberry Pi Pico WH microcontroller on a Windows computer using Visual Studio Code, follow these steps:

1. **Flash the MicroPython firmware onto the Raspberry Pi Pico WH.**

   - Download the latest MicroPython firmware for Raspberry Pi Pico from the official [website](https://micropython.org/download/rp2-pico-w/).
   - Press and hold the BOOTSEL button on the Raspberry Pi Pico WH.
   - While holding the BOOTSEL button, connect the Raspberry Pi Pico WH to your computer using a USB cable.
   - The Raspberry Pi Pico WH will now appear as a mass storage device on your computer.
   - Copy the downloaded firmware (.uf2 file) and paste it into the mass storage device (Raspberry Pi Pico WH).

2. **Install Visual Studio Code.**

   - Download Visual Studio Code from the official website.
   - Run the installer and follow the on-screen instructions to complete the installation.

3. **Install the necessary extensions for MicroPython development in Visual Studio Code.**

   - Launch Visual Studio Code.
   - Open the Extensions view by clicking on the square icon on the left sidebar or by pressing `Ctrl+Shift+X`.
   - Search for the following extensions and install them:
   
     - MicroPython by Microsoft
     - PyMakr by Pycom

   ![Installing necessary extensions](images/INSTALL_PYMAKR.png)



### Ubuntu Server Setup

To set up the Ubuntu server for running the Mosquitto MQTT protocol and Node Red, follow these steps:

1. **Install Ubuntu Server on your old laptop or a dedicated machine.**

   - Download the Ubuntu Server ISO from the official [website](https://ubuntu.com/download/server).
   - Create a bootable USB drive using software like Rufus or BalenaEtcher.
   - Boot your laptop or dedicated machine from the USB drive and follow the installation wizard to install Ubuntu Server.
   - Create an admin user and password.
   - Update the software package.
     ```powershell
     sudo apt update -y
     sudo apt upgrade -y
     ```

2. **Install Mosquitto MQTT broker on the Ubuntu server for communication between devices.**

   - Open PowerShell on your Windows computer.
   - Connect to the Ubuntu server via SSH:
     ```powershell
     ssh ubuntu_server_ip_address
     ```
   - Update the package lists and install Mosquitto and Mosquitto-clients:
     ```shell
     sudo apt install -y mosquitto mosquitto-clients
     ```
   - Enable autostart at server boot.
     ```shell
     sudo systemctl enable mosquitto.service
     ```
   - Test Mosquitto configuration:
     Open up two PowerShells and ssh into the server on both.
     In the first one:
     ```shell
     mosquitto_sub -t test/topic
     ```
     In the second one
     ```shell
     mosquitto_pub -t test/topic -m "Hello, MQTT!"
     ```
     If everything is set up correctly, you should see the published message appear in the terminal where you subscribed.

3. **Install Node Red on the Ubuntu server for building the user interface and data flow management.**

   - Install Node.js and npm:
     ```shell
     sudo apt install nodejs npm
     ```
   - Verify the Node.js and npm installations:
     ```shell
     node --version
     npm --version
     ```
   - Install Node-red:
     ```shell
     sudo npm install node-red
     ```
   - Enable autostart at server boot.
     ```shell
     sudo systemctl enable nodered.service
     ```
      
4. **Configure Mosquitto MQTT to communicate with the Raspberry Pi Pico WH, dissable local-only mode.**

   - Locate the mosquitto.conf file. It's usually at /etc/mosquitto/
     ```shell
     sudo nano /etc/mosquitto/mosquitto.conf
     ```
   - Add listener 1883 and allow_anonymous true
     
     ![Mosquitto conf file](images/M_conf.png)


## Putting Everything Together

You can arrange the components as desired, but make sure to connect everything correctly.

![Final design diagram](images/DIAGRAM.png)

## Data Transmission and Visualization

The Smart Horticulture project utilizes the MQTT protocol for data transmission and Node Red for data visualization and user interface. The workflow is as follows:

1. The Raspberry Pi Pico collects sensor data and publishes it to specific MQTT topics.
2. The Ubuntu server, running Mosquitto MQTT broker, receives the published data.
3. Node Red subscribes to the MQTT topics, retrieves the sensor data, and presents it on a user-friendly dashboard.
4. The dashboard displays real-time sensor readings.

    ![User interface, Node Red](images/NODE_RED_UI.png)

    <p align="center">
    <img src="images/MOVEMENT.png" alt="Image" />
    </p>

## Data Storage

To save data from the sensors on the Ubuntu server, the "ToFile" node in Node Red is used. This node allows us to save the sensor data with timestamps into a text file on the server's local storage. We can configure to save the data at specific intervals, such as once every 30 minutes. 

### Create a data file

- Choose your preferred location for storing the data file and create a directory and the data file:
  ```shell
     sudo mkdir /preferred-file-path/data
     sudo touch /preferred-file-path/data/datafile.txt
     ```
- Setup permissions to allow Node Red "ToFile" node to write to the file:
  ```shell
     sudo chown *username* /preferred-file-path/data/datafile.txt
     sudo chmod u+w /home/data/datafile.txt
     ```

## Platform

The Smart Horticulture project utilizes a local installation of a cloud-based platform for data processing and visualization. The platform offers scalability and flexibility for future expansion of the project. Consider the following aspects:

- Data storage and retrieval
- Data visualization and dashboard creation
- Integration with other services or APIs
- Cost considerations for scaling the project

## The Code

The code files provided in this project serve the purpose of collecting sensor data, establishing a connection to Wi-Fi, and transmitting the data to an MQTT broker.

- `boot.py` handles the Wi-Fi connection.
- `main.py` contains the core functionalities of collecting and sending data to the broker.
- `timeDiff.py` includes a helper class for managing time intervals.
- `config.py` stores the credentials and configurations related to Wi-Fi and MQTT.
- `simple.py` provides the implementation of the MQTT client.

## Transmitting the Data

The data collected from the sensors is transmitted to an MQTT broker using the MQTT protocol. The choice of MQTT as the transport protocol offers lightweight and efficient messaging, reducing data overhead and conserving battery life. The MQTT client implementation provided in `simple.py` facilitates the communication with the MQTT broker.

The data transmission interval is controlled by the `time_diff` object in `main.py`, which uses the `TimeDiff` class from `timeDiff.py` to check if the specified time interval has passed. Adjusting the timer value in `time_diff = timeDiff.TimeDiff(60)` allows you to modify the frequency of data updates.

The wireless protocol used in this project is Wi-Fi, which enables relatively long-range and reliable communication within a local network. The code establishes a Wi-Fi connection by calling the `connect_to_wifi()` function from `boot.py`. The Wi-Fi credentials (SSID and password) should be updated in the `config.py` file to match your network settings.

### Node Red Backend

![Node Red Backend](images/UI.png)

## Finilizing the Design

![The project including plants](images/PROJECT_PLANTS.jpg)
![The project](images/PROJECT.jpg)
