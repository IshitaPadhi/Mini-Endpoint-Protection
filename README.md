# 🛡️ Mini Endpoint Protection

A lightweight Endpoint Detection and Monitoring (EDR-inspired) project built in Python that demonstrates how modern endpoint protection solutions monitor processes, detect suspicious file activities, assess risk, and log security events.

> **Educational Project**
> This project is designed to simulate the core concepts behind Endpoint Detection & Response (EDR) solutions such as Microsoft Defender for Endpoint, CrowdStrike Falcon, and Elastic Defend.

---

## 📌 Overview

Traditional antivirus solutions rely heavily on malware signatures. Modern Endpoint Detection & Response (EDR) platforms continuously monitor endpoint activity to identify suspicious behavior in real time.

This project implements a simplified endpoint monitoring engine capable of:

- Monitoring newly launched processes
- Monitoring file creation events
- Performing rule-based risk analysis
- Logging security events
- Generating structured CSV reports for further analysis

The goal is to understand the fundamental building blocks of endpoint security through a hands-on implementation.

---

# ✨ Features

### 🖥️ Process Monitoring

- Learns existing running processes as a baseline
- Detects newly started processes
- Assigns a risk score
- Classifies processes as:
  - Low Risk
  - Medium Risk
  - High Risk

---

### 📂 File Monitoring

Monitors a specified directory in real time and detects:

- New file creation
- Suspicious executable files
- Script files
- Archive files
- Unknown file types

---

### ⚠️ Risk Engine

Every detected event passes through a simple rule-based risk engine.

Example checks include:

- Executable file detection
- Batch scripts
- PowerShell scripts
- Suspicious filenames
- Unknown processes

The engine assigns:

- Risk Level
- Risk Score
- Reason

---

### 📝 Event Logging

All detected events are automatically stored inside:

```
reports/events.csv
```

Each event contains:

- Timestamp
- Event Type
- Process/File Name
- Risk Level
- Reason

---

# 📁 Project Structure

```
Mini-Endpoint-Protection
│
├── app.py                 # Main application
├── process_monitor.py     # Process monitoring
├── file_monitor.py        # File system monitoring
├── risk_engine.py         # Risk evaluation engine
├── logger.py              # CSV event logger
├── config.py              # Configuration
│
├── watched_folder/        # Folder being monitored
│
├── reports/
│   └── events.csv         # Generated logs
│
├── README.md
│
└── requirements.txt
```

---

# ⚙️ Technologies Used

- Python 3.12
- psutil
- watchdog
- csv
- datetime
- threading

---

# 🚀 Installation

Clone the repository

```bash
git clone https://github.com/IshitaPadhi/Mini-Endpoint-Protection.git
```

Move into the project

```bash
cd Mini-Endpoint-Protection
```

Create a virtual environment

```bash
python -m venv venv
```

Activate it

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Running the Project

Start the application:

```bash
python app.py
```

The program will begin:

- Learning existing processes
- Monitoring new processes
- Watching the monitored folder
- Logging detected events

---

# 📊 Sample Output

```
Learning existing processes...

Monitoring processes...

New Process Detected!

Name:
powershell.exe

Risk Level:
HIGH

Reason:
PowerShell process detected
```

---

Example CSV Log

| Timestamp | Event | Name | Risk | Reason |
|-----------|------|------|------|--------|
| 2026-07-08 20:15 | Process | powershell.exe | HIGH | PowerShell detected |
| 2026-07-08 20:17 | File | malware.exe | HIGH | Executable detected |

---

# 🧠 How It Works

```
                 +------------------+
                 |     app.py       |
                 +------------------+
                          |
          -----------------------------------
          |                                 |
          v                                 v
+--------------------+          +--------------------+
| Process Monitor    |          | File Monitor       |
+--------------------+          +--------------------+
          |                                 |
          ----------- Risk Engine ----------
                          |
                          v
                 +----------------+
                 | Event Logger   |
                 +----------------+
                          |
                          v
                 reports/events.csv
```

---

# 📚 Learning Objectives

This project helped explore concepts such as:

- Endpoint Protection
- Endpoint Detection & Response (EDR)
- Process Monitoring
- File Monitoring
- Event Logging
- Threat Detection
- Risk Scoring
- Python System Programming

---

# 🔮 Future Improvements

Potential enhancements include:

- SIEM integration (Splunk / Elastic)
- Windows Event Log monitoring
- SHA-256 file hash analysis
- VirusTotal API integration
- YARA rule support
- Email or Slack alerts
- Machine Learning-based anomaly detection
- Real-time dashboard
- SQLite/PostgreSQL logging
- Process termination for high-risk threats

---

# 📖 Concepts Demonstrated

- Endpoint Security
- Security Monitoring
- Detection Engineering
- Behavioral Detection
- Threat Hunting Basics
- Incident Logging
- Rule-Based Detection
- Cybersecurity Automation

---

# 👩‍💻 Author

**Ishita Padhi**

Computer & Communication Engineering Student

Passionate about Cybersecurity, AI, Endpoint Security, and Detection Engineering.

GitHub:
https://github.com/IshitaPadhi

---

# ⭐ If you found this project useful...

Consider giving the repository a ⭐ to support the project!
