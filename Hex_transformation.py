import socket
import struct

class transformation(object):
    def ip2hex (self,ip):
        return hex(struct.unpack("!I", socket.inet_aton(ip))[0])

    def ip2long (self,ip):
        return struct.unpack("!I", socket.inet_aton(ip))[0]

    def long2ip (self,lint):
        return socket.inet_ntoa(struct.pack("!I", lint))

a=transformation()
b=a.ip2long("100.100.100.100")
print b