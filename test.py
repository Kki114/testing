#!/usr/bin/python
# Testing some scapy functionality

from scapy.all import srp1, sr1, Ether, IP, ICMP, ARP
import time

x = time.time()
pkt = Ether()/ARP(op="who-has", pdst="192.168.1.1", hwlen=6, plen=4, psrc="192.168.1.102", hwdst="ff:ff:ff:ff:ff:ff")
#pkt.show()
# Copies broadcast address into "broadcast" variable
broadcast = pkt[ARP].hwdst
#print(broadcast)

# Next line breaks code when attempting to send packet
ARP.show()
send = sr1(ARP)
send.show()

router_mac = send[ARP].hwsrc
router_ip = send[ARP].psrc
print(f"Program took {time.time() - x} seconds to get response for ARP message.")

ping_pkt = Ether(dst=router_mac)/IP(dst=router_ip)/ICMP()/b"Message Confirmation"
ping_pkt.show()
send1 = sr1(ping_pkt)
if send1 is not None:
    send1.show()
