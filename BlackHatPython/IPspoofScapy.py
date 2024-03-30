from scapy.all import *

A = '192.168.1.54' # spoofed source IP address
B = '192.168.1.15' # destination IP address
C = 80 # source port
D = 80 # destination port
payload = "yada yada yada" # packet payload

spoofed_packet = IP(src=A, dst=B) / TCP(sport=C, dport=D) / payload
send(spoofed_packet)
