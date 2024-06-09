### This repository was developed as part of the evaluation criteria for the IoT for Embedded Devices classes on the UNESP-ICTS, teached by the Professor Dhiego Fernandes Carvalho.
### The authors of this project are Christian and Thiago (mainly Christian), studens of the Control and Automation Engineering course, who joined in 2020.

# Smart Door: Face Recognition Home Automation

This project demonstrates a simple home automation system using face recognition to unlock your front door. 

### Architecture

* **Raspberry Pi 4:** Runs the facial recognition logic using Python with the "face-recognition" and "face-detection" libraries. 
* **Camera:** Captures images for face detection and recognition.
* **TV Box:** Stores facial data in a MySQL database.
* **Door Actuator:**  Opens/closes the door based on recognition results (implementation details left to the user).

### Connection

1. **Raspberry Pi:** Connects to the camera for image capture.
2. **Raspberry Pi:** Connects to the TV Box via TCP/IP using MySQL connector library to access the facial database and check against recognized faces.
3. **Raspberry Pi:** Connects to the door actuator (implementation details left to the user) to control the door based on the recognition result.

### Features

* **Face Recognition:** Utilizes the "face-recognition" and "face-detection" Python libraries to accurately identify individuals.
* **Secure Database:** Stores facial data securely on a separate TV Box, accessed through the "MySQL Connector" library via a TCP/IP connection with authentication.
* **Automatic Door Control:** Upon successful recognition, the system triggers the front door to open automatically.
* **Raspberry Pi Based:**  Runs on the versatile Raspberry Pi 4 platform, enabling a cost-effective and customizable solution.
* **Open-Source:** The code is open-source, allowing for customization, improvement, and adaptation to specific needs.

### Setup and Configuration

Detailed instructions for setup, configuration, and installation can be found in the corresponding folders and files within the repository.

### Note

This project is a basic implementation. Further development is required for robust functionality and security.
