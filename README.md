# 🛡️ AI-Cybersecurity-Lab 2.0
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

**AI-Cybersecurity-Lab 2.0** is an advanced, modular cybersecurity laboratory integrating **Artificial Intelligence (AI)**, **Suricata**, **Zeek**, and **Ethereum smart contract auditing**. It is designed to simulate real-world cyber environments, evaluate threats, and test defense strategies.

---

## 🎯 Target Users
This lab is ideal for:
- 🧠 AI & Cybersecurity Students and Researchers
- 🕵️‍♂️ SOC Analysts and Threat Hunters
- 🔴🔵 Red/Blue Teams
- 🏢 Enterprises evaluating scalable defense platforms
- 💡 Developers building intelligent security tools

---
```
## 📁 Project Tree Overview

AI-Cybersecurity-lab-2.0/
├── ai_alert_scoring/ # AI/ML-based alert scoring
│ ├── ai_model.py # Trained ML model for threat prioritization
│ └── feature_extractor.py # Extracts features from parsed alerts
│
├── suricata_alerts/ # Suricata log parsing
│ ├── parse_suricata.py # Parses Suricata JSON logs
│ └── sample_suricata.json # Sample Suricata alert file
│
├── zeek_alerts/ # Zeek log analysis
│ ├── parse_zeek.py # Parses Zeek conn.log data
│ └── sample_conn.log # Sample Zeek connection log
│
├── smart_contract_audit/ # Smart contract security tools
│ ├── audit_with_mythril.py # Audit script using Mythril
│ ├── audit_with_slither.py # Audit script using Slither
│ └── vulnerable_contract.sol # Sample vulnerable Solidity contract
│
├── visualization/ # Visualization & dashboard
│ ├── dashboard.py # Python dashboard using matplotlib/seaborn
│ └── alert_data.csv # Sample data for visualizing alerts
│
├── Dockerfile # Builds the lab environment container
├── docker-compose.yml # Launches all services with one command
├── requirements.txt # Python package dependencies
├── LICENSE # MIT License
└── README.md # Project overview, setup guide, and usage

```
---

## 🚀 How to Run

Clone and launch with Docker Compose:

```bash
git clone https://github.com/ivonexauce/AI-Cybersecurity-lab-2.0.git
cd AI-Cybersecurity-lab-2.0
docker-compose up --build
```

This sets up a ready-to-use environment with AI scoring, log parsing, and smart contract auditing tools pre-installed.

---


🧠 AI Model Details
```
| Component     | Description                                      |
| ------------- | ------------------------------------------------ |
| Algorithms    | Logistic Regression, Random Forest, XGBoost      |
| Training Data | Labeled Suricata & Zeek logs                     |
| Output        | Alert Priority: **High**, **Medium**, or **Low** |
```


Usage example:

```
from ai_alert_scoring.ai_model import load_model, predict_threat
from ai_alert_scoring.feature_extractor import extract_features
from suricata_alerts.parse_suricata import load_suricata_alerts

model = load_model('model.pkl')
alert = load_suricata_alerts('suricata_alerts/sample_suricata.json')[0]
features = extract_features(alert)
print("Threat Level:", predict_threat(features, model))
```
---

🧪 Smart Contract Tools
```
| Tool    | Purpose                      | Supported Format |
| ------- | ---------------------------- | ---------------- |
| Mythril | Symbolic execution engine    | `.sol`           |
| Slither | Static analysis and bug scan | `.sol`           |

```

Run audits like this:
```
python smart_contract_audit/audit_with_mythril.py
python smart_contract_audit/audit_with_slither.py
```
---

📊 Visual Dashboard
Visualize alert severity distribution:
```
python visualization/dashboard.py
```
A bar graph of severity levels will appear using matplotlib.
---

📦 Requirements
🐍 Python 3.10+

🐳 Docker & Docker Compose

🧰 Suricata & Zeek (pre-configured or via container)

🔧 Node.js (for optional Solidity compilation)

Install Python packages manually if needed:
```
pip install -r requirements.txt

```
---
🔍 Feature Summary

| Feature                     | Description                                                    |
| --------------------------- | -------------------------------------------------------------- |
| 🧠 AI Alert Scoring         | Uses machine learning to prioritize alerts intelligently.      |
| 📡 Suricata IDS Integration | Monitors traffic using signature-based intrusion detection.    |
| 🔬 Zeek IDS Integration     | Captures behavioral traffic logs for analysis.                 |
| 🔐 Smart Contract Auditing  | Audits Ethereum smart contracts using industry-standard tools. |
| 📊 Data Visualization       | Provides plots and dashboards for alert analytics.             |
| 🐳 Docker Support           | Simple and isolated deployment using Docker Compose.           |

---
📜 License
This project is licensed under the MIT License — free to use, distribute, and modify.
---
🙌 Contributors & Community
Author: UMBA YANGA IVON EXAUCE
🎓 AI & Blockchain Security
🌐 umbaconsulting.com
📧 umbayanga6bio@gmail.com

“Combining AI and cybersecurity isn't just a trend—it's a necessity for modern digital defense.” – Ivon Exauce Umba
