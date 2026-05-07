# 🔍 Net-Scanner-Tool (ARP Reconnaissance)

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Scapy](https://img.shields.io/badge/Scapy-Gry-004088?style=for-the-badge)
![Security](https://img.shields.io/badge/Security-Pentest-red?style=for-the-badge)

## 📖 Description
**Net-Scanner-Tool** is a network reconnaissance script developed in Python using the **Scapy** library. It discovers all active devices on a local network by leveraging the **ARP** (Address Resolution Protocol) protocol.

> This project was developed as part of my Cybersecurity training at **EPITA** to demonstrate my understanding of the OSI model's lower layers.

---

## 🛠️ How it works
The script operates at Layer 2 (Data Link) of the OSI model:
1. It generates an **Ethernet frame** with a "Broadcast" destination address (`ff:ff:ff:ff:ff:ff`).
2. It encapsulates an **ARP request** asking for the identity of every IP in the specified range.
3. It parses the responses to extract and display the **IP Address / MAC Address** pairs.



---

## 🚀 Installation & Usage

### 1. Prerequisites
You need Python 3 and the Scapy library installed:
```bash
pip install scapy

---
git clone [https://github.com/yanisdardaz/Net-Scanner-Tool.git](https://github.com/yanisdardaz/Net-Scanner-Tool.git)
cd Net-Scanner-Tool
---
sudo python3 scanner.py -t 192.168.1.0/24
