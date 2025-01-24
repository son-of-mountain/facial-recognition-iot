# Face Recognition IoT System with MQTT and Node-RED

This project implements a facial recognition system integrated with IoT technologies, it uses:

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
<p align="center">
  <img src="https://github.com/user-attachments/assets/8041880b-0572-49c9-a66b-c38c86635fd8" alt="Oracle DBA" width="800"/>
</p>

---

## Workflow

1. **Facial Recognition:**
   - Python captures video via OpenCV.
   - Identifies individuals using pre-trained models (face\_recognition library).
   - Sends structured data via MQTT to the `face-detection` topic.

<p align="center">
  <img src="https://github.com/user-attachments/assets/210e9721-bf43-45a8-8a64-6d54f40915ff" alt="Oracle DBA" width="800"/>
</p>


2. **Node-RED:**
   - Subscribes to the MQTT topic.
   - Processes incoming data to determine actions (e.g., open or close a door).
   - Publishes actions and updates to ThingsBoard and sends Telegram notifications.
<p align="center">
  <img src="https://github.com/user-attachments/assets/0774c698-929c-4242-9810-3551f3e6432a" alt="Oracle DBA" width="800"/>
</p>

3. **ThingsBoard:**
   - Displays recognized faces and system actions (e.g., door open/closed).
   - Allows manual override of actions via widgets (e.g., toggle button).
<p align="center">
  <img src="https://github.com/user-attachments/assets/1add2ed3-6d39-47c1-b5a0-724879b64146" alt="Oracle DBA" width="800"/>
</p>

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

## Built by 

<table align="center">
  <tbody>
    <tr>
      <td align="center" valign="top" width="50%">
        <a href="https://github.com/son-of-mountain" target="_blank">
          <img src="https://avatars.githubusercontent.com/u/173689605?v=4" width="100px;" alt="Mouaad ELHANSALI" style="border-radius: 50%;"/>
          <br />
          <sub><b>Mouaad ELHANSALI</b></sub>
        </a>
      </td>
      <td align="center" valign="top" width="70%">
        <a href="https://github.com/MohamedBarbych" target="_blank">
          <img src="https://avatars.githubusercontent.com/u/146338565?v=4" width="100px;" alt="Mohamed BARBYCH" style="border-radius: 50%;"/>
          <br />
          <sub><b>Mohamed BARBYCH</b></sub>
        </a>
      </td>
    </tr>
  </tbody>
</table>
