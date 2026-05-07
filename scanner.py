#!/usr/bin/env python3
from scapy.all import ARP, Ether, srp
import sys
import argparse

def scan(ip_range):
    """
    Sends ARP requests to a given IP range and returns a list of discovered devices.
    """
    # Create ARP request packet
    # pdst is the destination IP range
    arp_request = ARP(pdst=ip_range)
    
    # Create Ethernet frame to broadcast the ARP request
    # dst="ff:ff:ff:ff:ff:ff" ensures it's sent to everyone on the local segment
    broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")
    
    # Stack layers: Ethernet / ARP
    packet = broadcast / arp_request

    # Send packet and receive response (srp = Send and Receive Packets at layer 2)
    # timeout=2: wait 2 seconds for answers
    answered_list = srp(packet, timeout=2, verbose=False)[0]

    clients_list = []
    for element in answered_list:
        client_dict = {"ip": element[1].psrc, "mac": element[1].hwsrc}
        clients_list.append(client_dict)
    
    return clients_list

def print_result(results_list):
    print("IP Address\t\tMAC Address")
    print("-----------------------------------------")
    for client in results_list:
        print(f"{client['ip']}\t\t{client['mac']}")

if __name__ == "__main__":
    # Setup command line arguments
    parser = argparse.ArgumentParser(description="Simple ARP Network Scanner")
    parser.add_argument("-t", "--target", help="Target IP range (e.g. 192.168.1.0/24)")
    args = parser.parse_args()

    if not args.target:
        print("[-] Please specify a target range. Use --help for more info.")
        sys.exit()

    try:
        scan_result = scan(args.target)
        print_result(scan_result)
    except KeyboardInterrupt:
        print("\n[!] Scan stopped by user.")
    except PermissionError:
        print("[!] Error: You must run this script with sudo (Root privileges required for Scapy).")
