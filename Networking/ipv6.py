from socket import *
import ipaddress


class IPv6:

	def __init__(self, data, addr):

		self.ipv6data = data[:40]
		#shift to Right by 4 bits
		self.version = self.ipv6data[0] >> 4

		#shift to left by 4 bits (| means or) shift to Right by 4 bits
		self.class_trafic = self.ipv6data[0] << 4 | self.ipv6data[1] >> 4

		# 11111111 = 0x00FF
		# bits self.ipv6data[1] over 11111111 combination
		# shift to left 16 bits bitwise
		# shift to left 8 bits
		self.flow_label = ((self.ipv6data[1] & 0x00FF) << 16) | (self.ipv6data[2] << 8) | self.ipv6data[3]

		#Shift to left 8 bits or check 5 bit
		self.payload = (self.ipv6data[4]  << 8) | self.ipv6data[5]

		#Get the next header but only shows the first one
		self.next_header = self.ipv6data[6]
		self.hlimit = self.ipv6data[7]

		#bits from source address
		self.source = ipaddress.IPv6Address(self.ipv6data[8:24])
		#bits from destination address
		self.destination = ipaddress.IPv6Address(self.ipv6data[24:40])

		self.data = data[40:]

	def __str__(self):
	
		print('IPV6 VERSIOM: {}'.format(self.version))
		print('FLOW_LABEL: {}, PAYLOAD: {}'.format(self.flow_label, self.payload))
		print('NEXT HEADER: {}, HOP: {}'.format(self.next_header, self.hlimit))
		print('SOURCE: {}'.format(self.source))
		print('DESTINATION: {},'.format(self.destination))
		
		return ('')
