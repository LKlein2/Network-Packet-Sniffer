import textwrap

Tab = ['\t - ', '\t\t - ', '\t\t\t - ', '\t\t\t\t - ']
DataTab = ['\t ', '\t\t ', '\t\t\t ', '\t\t\t\t ']


#formats multi-line string
def format_multi_line(prefix, string, size=80):
    size -= len(prefix)
    if isinstance(string, bytes):
        string = ''.join(r'\x{:02x}'.format(byte) for byte in string)
        if size % 2:
            size -= 1
    return '\n'.join([prefix + line for line in textwrap.wrap(string, size)])

#returns the MAC Address in conventional form AA:BB:CC:DD:EE:FF
def get_mac_address(address):
   str_byte = map('{:02x}'.format, address)
   macAddress = ':'.join(str_byte).upper()
   return macAddress

#return IPv4 address in standard form 122.0.0.1
def ipv4(address):
    return '.'.join(map(str, address))