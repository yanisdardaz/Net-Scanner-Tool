# Net-Scanner-Tool 🔍

A professional network reconnaissance script built with **Python** and **Scapy**. This tool performs an ARP scan to discover all active devices within a specific network range.

## 🛠️ How it works
The scanner sends **ARP (Address Resolution Protocol)** requests across the local network. 
1. It creates an Ethernet broadcast frame.
2. It embeds an ARP request asking "Who has this IP?".
3. It captures and parses the responses to map **IP addresses** to **MAC addresses**.

## 🚀 Installation & Usage
### Prerequisites
- Python 3.x
- Scapy library: `pip install scapy`

### Run the scanner
You must run the script with **root privileges** to allow raw socket manipulation:
```bash
sudo python3 scanner.py -t 192.168.1.0/24
