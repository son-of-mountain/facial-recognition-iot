# Face Recognition IoT System with MQTT and Node-RED

This project implements a facial recognition system integrated with IoT technologies. It uses Python for facial detection and classification, MQTT for communication, Node-RED for orchestration, and ThingsBoard for data visualization. The system automates actions such as door access control and sends notifications via Telegram.

---

## Features

- **Real-Time Face Recognition:** Detect and identify faces using Python and OpenCV.
- **IoT Integration:** Publish detected data to an MQTT broker for further processing.
- **Node-RED Orchestration:** Process MQTT data and trigger actions (e.g., door control or notifications).
- **ThingsBoard Visualization:** Real-time monitoring of recognized individuals and system actions.
- **Telegram Notifications:** Alerts for recognized or unrecognized faces.

---

## Architecture

1. **Webcam:** Captures video feed in real-time.
2. **Python Module:** Detects faces, identifies individuals, and sends the data as MQTT messages.
3. **MQTT Broker (Mosquitto):** Facilitates communication between Python, Node-RED, and ThingsBoard.
4. **Node-RED:** Processes data, decides actions, and sends notifications.
5. **ThingsBoard:** Displays real-time data on interactive dashboards.

---

## Workflow

1. **Facial Recognition:**
   - Python captures video via OpenCV.
   - Identifies individuals using pre-trained models (face\_recognition library).
   - Sends structured data via MQTT to the `face-detection` topic.

2. **Node-RED:**
   - Subscribes to the MQTT topic.
   - Processes incoming data to determine actions (e.g., open or close a door).
   - Publishes actions and updates to ThingsBoard and sends Telegram notifications.

3. **ThingsBoard:**
   - Displays recognized faces and system actions (e.g., door open/closed).
   - Allows manual override of actions via widgets (e.g., toggle button).

---

## Installation

### Prerequisites
- Python 3.9+
- MQTT Broker (e.g., Mosquitto)
- Node-RED
- ThingsBoard Account

### Python Dependencies
Install the required Python libraries:
```bash
pip install paho-mqtt opencv-python face-recognition numpy
```
