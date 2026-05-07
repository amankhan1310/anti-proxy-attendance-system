# Anti-Proxy Attendance System (APAS)

A biometric attendance system built using Raspberry Pi and fingerprint authentication to eliminate proxy attendance in classrooms and institutions. The system authenticates students using real-time fingerprint verification, enables faculty-controlled attendance sessions, and generates exportable attendance records for institutional use.

This project was developed as part of **Smart India Hackathon 2024**, where it secured **1st Place** for solving real-world attendance fraud challenges using affordable hardware and embedded AI-driven authentication workflows.

---

## Overview

Traditional attendance systems are vulnerable to proxy attendance and manual errors. APAS solves this problem by integrating biometric fingerprint authentication with Raspberry Pi–based edge hardware.

The system allows faculty to start attendance sessions securely, students to mark attendance using fingerprints, and institutions to generate accurate attendance logs instantly.

The architecture was designed to be:

* Low-cost
* Portable
* Scalable
* Fast for classroom environments
* Reliable under real-time usage

---

# Features

* Fingerprint-based student authentication
* Proxy attendance prevention
* Faculty-authenticated session control
* Real-time attendance marking
* CSV/Excel attendance export
* Lightweight Raspberry Pi deployment
* UART-based biometric communication
* Secure attendance logging

---

# Tech Stack

## Hardware

* Raspberry Pi 4
* R307 Fingerprint Sensor
* UART Serial Communication
* Optional Display Module

## Software

* Python
* PySerial
* Adafruit Fingerprint Library
* Pandas
* OpenPyXL
* ReportLab

## System & Tools

* Raspberry Pi OS
* Git
* GitHub
* Visual Studio Code

---

# System Architecture

1. Faculty starts attendance session
2. Faculty fingerprint is verified
3. Students scan fingerprints
4. System matches fingerprint templates
5. Attendance gets logged instantly
6. Faculty ends session securely
7. Attendance report exported as CSV/Excel

---

# Hardware Integration

The fingerprint sensor communicates with Raspberry Pi using UART serial communication.

### Wiring

| R307 Sensor | Raspberry Pi |
| ----------- | ------------ |
| TX          | GPIO15 (RX)  |
| RX          | GPIO14 (TX)  |
| VCC         | 5V           |
| GND         | GND          |

UART was enabled through Raspberry Pi configuration for serial communication with the biometric module.

---

# Core Functionalities

## Fingerprint Enrollment

* Captures multiple scans per student
* Stores fingerprint templates securely
* Generates unique IDs for matching

## Attendance Verification

* Real-time fingerprint matching
* Fast identification pipeline
* High accuracy verification system

## Faculty Authentication

* Faculty-only session control
* PIN-protected attendance termination
* Prevents unauthorized attendance marking

## Attendance Export

* Generates attendance logs
* CSV/Excel export support
* Structured attendance summaries

---

# Challenges Solved

* Eliminated manual attendance fraud
* Reduced proxy attendance
* Improved attendance accuracy
* Created low-cost deployable hardware solution
* Built scalable biometric attendance workflow

---

# Project Impact

* Successfully demonstrated at Smart India Hackathon 2024
* Recognized for practical real-world implementation
* Designed for deployment in schools and colleges
* Portable and cost-effective institutional solution

---

# Future Enhancements

* Face recognition integration
* Web dashboard for analytics
* Cloud synchronization
* LMS integration
* Multi-class attendance management
* AI-powered attendance insights

---

# Installation

## Clone Repository

```bash
git clone <repository-url>
cd anti-proxy-attendance-system
```

## Install Dependencies

```bash
pip install pyserial adafruit-circuitpython-fingerprint pandas openpyxl pillow reportlab
```

## Run Project

```bash
python apas.py
```

---

# Learning Outcomes

Through this project, key concepts learned include:

* Embedded AI systems
* Raspberry Pi hardware integration
* UART communication
* Biometric authentication systems
* Real-time verification pipelines
* Attendance automation workflows
* Python-based hardware programming

---

# Author

**Aman Yahya Khan**
AI & Machine Learning Engineer
Pune, Maharashtra, India

GitHub: github.com/amankhan1310
