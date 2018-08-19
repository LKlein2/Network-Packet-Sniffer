import struct
import socket
from utilities import *

class EthernetFrame:
    def __init__(self,data):
        dest, src, protocal  = struct.unpack('! 6s 6s H', data[:14])
        self.destinationMac = get_mac_address(dest)
        self.srcMac = get_mac_address(src)
        self.protocal = socket.htons(protocal)
        self.data = data[14:]


    def __str__(self):
        print('\nEthernet Frame:')
        return (Tab[0] + 'Destination: {}, Source: {}, Protocol: {}'.format(self.destinationMac, self.srcMac, self.protocal))


