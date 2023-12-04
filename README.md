# Team-Kit-Kat
## Detective Dustbin

![Detective Dustbin](https://github.com/Leonallr10/Team-Kit-Kat/assets/118210551/dea43ef5-17ed-4c86-a66c-39ae459dc308)

### Team Members:

- CB.EN.U4CSE21301 Aaditya E.R Menon
- CB.EN.U4CSE21310 Dhayanandh
- CB.EN.U4CSE21325 K Sai Tharun Aditya
- CB.EN.U4CSE21327 Karthie Krishna K
- CB.EN.U4CSE21331 Leonal Robin D

### Introduction:

The Detective Dustbin is an intelligent waste management system designed to provide automated functionality and security features. It employs various components, including a Raspberry Pi Pico microcontroller, ultrasonic sensors, motion sensors, a buzzer, LED, and a Bluetooth module (HC-05).

### Components:

- Raspberry Pi Pico - 1
- Ultrasonic Sensor - 2
- Motion Sensor - 1
- Buzzer - 1
- LED - 1
- Bluetooth Module HC-05 - 1

### Functionality:

#### Automatic Open and Close:

The dustbin is equipped with two ultrasonic sensors to detect the proximity of an object. When someone approaches the dustbin within a minimum distance of 15cm, the ultrasonic sensor triggers the dustbin to automatically open. The dustbin will close automatically after 5 seconds.

#### Motion Detection:

The motion sensor serves as a security feature. It detects motion in front of the dustbin, acting as a spy-like system. If anyone crosses the dustbin, the buzzer is activated, providing an alert.

#### Quantity Measurement:

The ultrasonic sensor is utilized not only for proximity detection but also to measure the percentage of the dustbin's capacity filled. This feature helps users monitor the waste level in real-time.

#### Bluetooth Connectivity:

The Bluetooth module (HC-05) enables remote control and monitoring. Users can switch on/off the ultrasonic sensor for the automatic open-close function using a mobile application. Additionally, the motion sensor's data is transmitted via Bluetooth to a paired device, allowing users to receive alerts about detected motion.

### Usage Instructions:

- **Proximity Detection:** Stand within 15cm of the dustbin to trigger automatic open-close functionality.
- **Motion Detection:** The motion sensor detects and alerts if anyone crosses in front of the dustbin.
- **Quantity Measurement:** The ultrasonic sensor measures the percentage of the dustbin's capacity filled.
- **Bluetooth Control:** Use the Bluetooth-connected mobile application to toggle the ultrasonic sensor on/off for automatic open-close and receive motion detection alerts as notifications.

### Conclusion:

The Detective Dustbin combines automation and security features to enhance waste management. With its advanced sensors and Bluetooth connectivity, it provides a smart solution for homes, ensuring convenience and safety in waste disposal.
