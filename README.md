# 🔍 Net-Scanner-Tool — ARP Network Reconnaissance
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Scapy](https://img.shields.io/badge/Scapy-004088?style=for-the-badge)
![Security](https://img.shields.io/badge/Security-Pentest-red?style=for-the-badge)

## 📖 Description
**Net-Scanner-Tool** est un outil de reconnaissance réseau développé en Python utilisant **Scapy**. Il permet d’identifier tous les appareils actifs sur un réseau local grâce au protocole **ARP**.  
> Projet réalisé dans le cadre de ma formation en Cybersécurité à **EPITA**, illustrant la compréhension des couches basses du modèle OSI.

## 🛠️ Fonctionnement
Le script opère au niveau de la **couche 2 (Liaison de données)** du modèle OSI :
1. Création d’une **trame Ethernet** en broadcast (`ff:ff:ff:ff:ff:ff`)
2. Envoi d’une **requête ARP** vers chaque IP de la plage ciblée
3. Réception et parsing des réponses pour afficher les couples **IP / MAC**

## 🚀 Installation, Clonage & Exécution

### 1. Installer les dépendances:
```bash
pip install scapy
```
### 2. Cloner le dépot:
```bash
git clone https://github.com/yanisdardaz/Net-Scanner-Tool.git
```
### 3. Entrer dans le dossier:
```bash
cd Net-Scanner-Tool
```
### 4.  Exécuter le scanner:
```bash
sudo python3 scanner.py -t 192.168.1.0/24
```

