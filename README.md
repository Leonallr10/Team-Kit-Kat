# Team-Kit-Kat
### From Amrita School of Engineering
## Detective Dustbin

![Detective Dustbin](https://github.com/Leonallr10/Team-Kit-Kat/assets/118210551/dea43ef5-17ed-4c86-a66c-39ae459dc308)

### Table of Contents
- [Team Members](#team-members)
- [Introduction](#introduction)
- [Components](#components)
- [Functionality](#functionality)
  - [Automatic Open and Close](#automatic-open-and-close)
  - [Motion Detection](#motion-detection)
  - [Quantity Measurement](#quantity-measurement)
  - [Bluetooth Connectivity](#bluetooth-connectivity)
- [Usage Instructions](#usage-instructions)
- [Pin Numbers](#pin-numbers)
- [Software Used](#software-used)
- [Conclusion](#conclusion)
- [YouTube Link](#youtube-link)

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

### Pin Numbers:

#### Raspberry Pi Pico:
![Raspberry Pi Pico](https://github.com/Leonallr10/Team-Kit-Kat/assets/118210551/6a8e9105-78b7-45e3-a088-3f979f7bab66)

#### Ultrasonic Sensor:
![Ultrasonic Sensor](https://github.com/Leonallr10/Team-Kit-Kat/assets/118210551/10bf6c50-b2af-4005-a209-3346a8d01b59)

#### Motion Sensor:
![Motion Sensor](https://github.com/Leonallr10/Team-Kit-Kat/assets/118210551/e6f8d103-54f1-42df-95ac-befba7e48ea3)

#### Buzzer:
![Buzzer](https://github.com/Leonallr10/Team-Kit-Kat/assets/118210551/f4793156-fbd1-447a-8a30-f28e25eac407)

#### Bluetooth Module:
![Bluetooth Module](https://github.com/Leonallr10/Team-Kit-Kat/assets/118210551/f387224f-430e-4088-86f1-d0e94322f124)

#### Servo motor:
![WhatsApp Image 2023-12-07 at 14 28 01_fc144ebf](https://github.com/Leonallr10/Team-Kit-Kat/assets/118210551/79a0bc3f-d9fa-416b-9ce5-6e60a663ccc6)


### Software Used:

#### Bluetooth Terminal App (Android):

- **App:** Android Bluetooth Terminal App
- **Usage:** Control the dustbin remotely and receive Bluetooth notifications.
- **Download:** [Android Bluetooth Terminal App](https://appinventor.mit.edu/)

#### MIT App Inventor:

- **Platform:** MIT App Inventor
- **Link:** [MIT App Inventor on Google Play](https://play.google.com/store/apps/details?id=de.kai_morich.serial_bluetooth_terminal&pcampaignid=web_share)
- **Purpose:** Develop custom mobile applications for Bluetooth control and data reception.

#### Raspberry Pi Pico Python Software:

- **Language:** Python
- **Function:** Enables programming and integration of the Raspberry Pi Pico microcontroller.
- **Note:** Ensure proper configuration for seamless communication with sensors and Bluetooth module.
- **Link:** [Getting Started with Raspberry Pi Pico (Python)](https://projects.raspberrypi.org/en/projects/getting-started-with-the-pico/2)

### Conclusion:

The Detective Dustbin combines automation and security features to enhance waste management. With its advanced sensors and Bluetooth connectivity, it provides a smart solution for homes, ensuring convenience and safety in waste disposal.

### YouTube Link:
[Watch the Detective Dustbin in action](https://youtu.be/30gV1dWLi8w)
