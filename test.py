#!/usr/bin/python

from scapy.all import srp1, sr1, Ether, IP, ICMP, ARP, DHCP

pkt = ARP(op="who-has", pdst="192.168.128.1", hwdst="ff:ff:ff:ff:ff:ff")
#pkt.show()
broadcast = pkt[ARP].hwdst
send = sr1(pkt)
router_mac = send[ARP].hwsrc
router_ip = send[ARP].psrc

ping_pkt = Ether(dst=router_mac)/IP(dst=router_ip)/ICMP()/b"Message Received"
ping_pkt.show()
send1 = sr1(ping_pkt)
send1.show()