import struct
from utilities import *
class IPv4:
    def __init__(self,data):
        version_header_length = data[0]
        self.version = version_header_length >> 4
        self.headerLen = (version_header_length & 15) * 4
        self.ttl, self.protocal, src, dest = struct.unpack('! 8x B B 2x 4s 4s', data[:20])
        self.sourceIP = ipv4(src)
        self.destinationIP = ipv4(dest)
        self.data = data[self.headerLen:]




    def __str__(self):
        print(Tab[0] + 'IPv4 Packet:')
        print(Tab[1] + 'Version: {}, Header Length: {}, Time to live: {}'.format(self.version, self.headerLen, self.ttl))
        return (Tab[1] + 'Protocal: {}, Source: {}, Target: {}'.format(self.protocal,self.sourceIP, self.destinationIP))