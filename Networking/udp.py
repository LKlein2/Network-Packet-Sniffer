import struct
from utilities import *
class UDP:
    def __init__(self,data):
        self.sourcePort, self.destinationPort, self.size = struct.unpack('! H H 2x H',data[:8])
        self.data = data[8:]

    def __str__(self):
        print(Tab[0] + 'UDP Segment:')
        print(Tab[1] + 'Source Port: {}, Destination Port: {}, Length{}'.format(self.sourcePort, self.destinationPort, self.size))
        return(format_multi_line(DataTab[2], self.data))