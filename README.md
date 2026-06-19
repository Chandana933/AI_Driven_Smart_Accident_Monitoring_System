# AI Smart Driven Accident Detection System

## 🚗 Project Overview

The AI Smart Driven Accident Detection System is an IoT and Machine Learning based vehicle safety solution designed to detect alcohol consumption and road accidents in real time. The system uses gas and MEMS sensors connected to a microcontroller to monitor vehicle conditions. Sensor data is analyzed using a Random Forest Machine Learning model, and emergency alerts are sent through Email while live sensor values are uploaded to the ThingSpeak cloud platform.

---

## 🎯 Objectives

* Detect alcohol consumption by the driver.
* Detect vehicle accidents using MEMS sensor data.
* Send automatic email alerts during emergencies.
* Upload real-time sensor readings to ThingSpeak.
* Improve road safety through intelligent monitoring.

---

## 🛠 Hardware Components

* ESP32 / Arduino Uno
* MQ-3 Alcohol Sensor
* MEMS Accelerometer Sensor
* USB Cable
* Breadboard and Jumper Wires
* Laptop/PC

---

## 💻 Software Requirements

* Python 3.10+
* Arduino IDE
* Visual Studio Code
* ThingSpeak Cloud Platform

### Python Libraries

* NumPy
* Pandas
* Scikit-Learn
* PySerial
* Requests
* OpenPyXL
* Python-Dotenv

---

## 🤖 Machine Learning Model

### Algorithm Used

* Random Forest Classifier

### Features

* Gas Sensor Value (MQ-3)
* X-axis MEMS Value
* Y-axis MEMS Value

### Output Labels

#### Alcohol Detection

| Label | Meaning          |
| ----- | ---------------- |
| 0     | No Alcohol       |
| 1     | Alcohol Detected |

#### Accident Detection

| Label | Meaning           |
| ----- | ----------------- |
| 1     | Safe              |
| 0     | Accident Detected |

---

## 🔄 System Workflow

1. Sensor values are collected from the vehicle.
2. Data is transmitted through serial communication.
3. Random Forest model predicts accident and alcohol conditions.
4. Emergency email alerts are generated when required.
5. Sensor data is uploaded to ThingSpeak cloud.
6. Results are displayed and monitored in real time.

---

## 📁 Project Structure

AI-Smart-Driven-Accident-Detection-System/

├── data/

├── src/

├── arduino/

├── models/

├── docs/

├── images/

├── .env.example

├── requirements.txt

├── README.md

└── LICENSE

---

## ▶️ How to Run

### Clone Repository

```bash
git clone https://github.com/yourusername/AI-Smart-Driven-Accident-Detection-System.git
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Train Model

```bash
python src/train_model.py
```

### Run System

```bash
python src/main.py
```

---

## ☁️ ThingSpeak Integration

The system uploads:

* Gas Sensor Value
* X-axis MEMS Value
* Y-axis MEMS Value

to the ThingSpeak cloud platform for remote monitoring and analysis.

---

## 📧 Email Alert System

Automatic email notifications are sent when:

* Alcohol is detected.
* Vehicle accident is detected.

---

## 📊 Results

* Real-time alcohol detection.
* Real-time accident prediction.
* Email notification system.
* Cloud-based monitoring through ThingSpeak.
* Improved vehicle safety monitoring.

---

## 🚀 Future Enhancements

* GPS location tracking
* SMS emergency alerts
* Mobile application integration
* Deep Learning based accident prediction
* Live dashboard monitoring

---

## 👩‍💻 Author

**Banka Chandana**

B.Tech – Computer Science Engineering (IoT & Automation)

Siddartha Institute of Science and Technology

CGPA: 8.51
