"""
Cosnulta: Generate a code in python3 to send a character per character 
of string in ping to loopback using scapy with not null hex id, 
increasing sequence number start in 0, had this sequences of hex bits 
in payload 
6327c4a3000eb9xx08090a0b0c0d0e0f101112131415161718191a1b1c1d1e1f202122232425262728292a2b2c2d2e2f3031323334353637 
and replacing xx for a hex value of character to send
"""

from scapy.all import *

def ping(text):
    # Define the packet payload
    string = '6427c4a3000eb9{}08090a0b0c0d0e0f101112131415161718191a1b1c1d1e1f202122232425262728292a2b2c2d2e2f3031323334353637'
    # Send ping packets to the loopback interface
    for i in range(len(text)):
        # Define the packet payload
        char = str(format(ord(text[i]), "x"))
        payload = bytes.fromhex(string.format(char))

        # Define the ICMP packet with the ping format of macOS
        packet = IP(dst='127.0.0.1')/ICMP(type=8, code=0, id=0x1234, seq=i)/payload
        
        # Send the packet and wait for the response
        reply = sr1(packet, timeout=1, verbose=0)

if __name__ == '__main__':
    # Read input arguments from the command line
    text = " ".join(sys.argv[1:])

    ping = ping(text)
