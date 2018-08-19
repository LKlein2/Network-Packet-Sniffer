import struct
from utilities import *

class ICMP:
    def __init__(self,data):
        self.type, self.code, self.checksum = struct.unpack('! B B H',data[:4])
        self.data = data[4:]

    def __str__(self):
        print(Tab[0] + 'ICMP Packet:')
        print(Tab[1] + 'Type: {}, Code: {}, Checksum: {}'.format(self.type, self.code, self.checksum))
        print(Tab[1] + 'Data: ')
        return (format_multi_line(DataTab[2], self.data))