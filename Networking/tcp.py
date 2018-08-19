import struct
from utilities import *

class TCP:
    def __init__(self,data):
        self.sourcePort, self.destinationPort, self.sequenceNo, self.acknowledgmentNo, off_reserved_flag = struct.unpack('! H H L L H', data[:14])
        offset = (off_reserved_flag >> 12)*4
        self.flags = []

        '''
        flag[0]: URG
        flag[1]: ACK   
        flag[2]: PSH
        flag[3]: RST
        flag[4]: SYN
        flag[5]: FIN
        '''
        for i in range(6,0,-1):
            self.flags.append( (off_reserved_flag & (2 ** (i-1))) >> i-1 )

        self.data = data[offset:]

    def __str__(self):
        print(Tab[0] + 'TCP Segment')
        print(Tab[1] + 'Source Port: {}, Destination Port: {}'.format(self.sourcePort, self.destinationPort))
        print(Tab[1] + 'Sequence: {}, Acknowlegement: {}'.format(self.sequenceNo, self.acknowledgmentNo))
        print(Tab[1] + 'Flag:')
        print(Tab[2] + 'URG: {}, ACK: {}, PSH: {}'.format(self.flags[0], self.flags[1], self.flags[2]))
        return (Tab[2] + 'RST: {}, SYN: {}, FIN: {}'.format(self.flags[3], self.flags[4], self.flags[5]))
