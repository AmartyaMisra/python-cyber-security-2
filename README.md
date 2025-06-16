# 🛡️ WiFi Audit Ghost

> *A stealth-focused Python tool for wireless network auditing, cyber hygiene diagnostics, and ethical WiFi reconnaissance.*

---

## 📡 Overview

`WiFi Audit Ghost` is a lightweight yet potent Python script designed to scan, audit, and analyze WiFi connections for common vulnerabilities. It’s built for cybersecurity learners, ethical hackers, and analysts who want fast insights into WiFi behavior — from SSID exposure to weak encryption flags.

This is the **first deployment** in a larger series of tactical tools under [`python-cyber-security-2`](https://github.com/AmartyaMisra/python-cyber-security-2).

---

## 🧰 Features

- 🚨 Detect nearby SSIDs and hidden networks  
- 🔓 Flag open or weak encryption protocols (e.g., WEP/WPA)  
- 🧠 Checks for common misconfigurations (e.g., default gateways, weak passphrases)  
- 📜 Simple terminal-based interface (CLI)

---

## 📦 Tech Stack

- `Python 3.x`
- `subprocess`, `platform`, `os`
- Optional: `scapy`, `wifi`, `pywifi`, `colorama`

---

## 🚀 Installation

```bash
git clone https://github.com/AmartyaMisra/python-cyber-security-2.git
cd python-cyber-security-2/wifi
pip install -r requirements.txt
