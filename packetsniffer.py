import socket
from utilities import *
from networking.ethernet import EthernetFrame
from networking.icmp import ICMP
from networking.ipv4 import IPv4
from networking.tcp import TCP
from networking.udp import UDP
from networking.http import HTTP

'''
Network Packet Sniffer
Requires admin user rights to run
In Linux terminal excecute following
sudo python3 packetsniffer.py
'''
def packet_sniffer():
    connection = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))
    while True:
        data, addr = connection.recvfrom(65535)
        ethernet_frame = EthernetFrame(data)
        print(ethernet_frame)

        #IPv4
        if ethernet_frame.protocal == 8:
            ipv4 = IPv4(ethernet_frame.data)
            print(ipv4)

            #ICMP
            if ipv4.protocal == 1:
                icmp = ICMP(ipv4.data)
                print(icmp)

            #TCP
            elif ipv4.protocal == 6:
                tcp = TCP(ipv4.data)
                print(tcp)

                if len(tcp.data) > 0:

                    #HTTP
                    if tcp.sourcePort == 80 or tcp.destinationPort == 80:
                        print(Tab[1] + 'HTTP Data:')
                        try:
                            http = HTTP(tcp.data)
                            http_info = str(http.data).split('\n')
                            for line in http_info:
                                print(DataTab[2] + line)
                        except:
                            print(format_multi_line(DataTab[2],tcp.data))
                    else:
                        print(Tab[1] + 'TCP Data:')
                        print(format_multi_line(DataTab[2],tcp.data))


            #UDP
            elif ipv4.protocal == 17:
                udp = UDP(ipv4.data)
                print(udp)

            #other IPv4 protocals
            else:
                print(Tab[0] + 'Other IPv4 Data:')
                print(format_multi_line(DataTab[0],ipv4.data))

        else:
            print('Ethernet Data:')
            print(format_multi_line(DataTab[0], ethernet_frame.data))

if __name__ == '__main__':
    packet_sniffer()
