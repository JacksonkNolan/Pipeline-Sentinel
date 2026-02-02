# Pipeline-Sentinel 🛢️🛡️

**A specialized ICS/SCADA Honeypot for Critical Infrastructure Security**

## 📌 The Problem
As the oil and gas industry digitizes its mapping and remote monitoring (wells, pipelines, and pumping stations), these assets become targets for cyber-sabotage. Many industrial devices use the **Modbus TCP** protocol, which is often unencrypted and lacks built-in authentication.

## 🚀 The Solution
**Pipeline-Sentinel** is a Python-based honeypot that mimics a Programmable Logic Controller (PLC). It acts as a "digital decoy," luring attackers away from real pipeline coordinates and well-site data. 

By emulating an industrial device, it captures real-time threat intelligence, allowing security teams to see who is scanning their network and what commands they are trying to inject.

## 🛠️ Technical Features
- **TCP Socket Emulation:** Mimics the handshake and response behavior of a Siemens S7-200 PLC.
- **Protocol Analysis:** Captures raw Hex payloads from the Modbus protocol for deep packet analysis.
- **Threat Logging:** Generates `pipeline_attacks.log` with timestamps, attacker IPs, and full payload data.
- **Minimal Footprint:** Designed to run on low-power, "off-grid" hardware or as a lightweight virtualized container.

## 📂 Project Structure
* `honeypot.py`: The core engine that listens for and logs unauthorized connections.
* `pipeline_attacks.log`: (Generated) The database of captured threat intelligence.
* `.gitignore`: Ensures sensitive log data isn't accidentally pushed to production.

## 🚦 Getting Started

### Installation
1. Clone this repository:
   ```bash
   git clone [https://github.com/YOUR_USERNAME/Pipeline-Sentinel.git](https://github.com/YOUR_USERNAME/Pipeline-Sentinel.git)
