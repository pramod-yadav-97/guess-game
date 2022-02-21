import socket
import sys

hname = socket.gethostname()
IP_addres = socket.gethostbyname(hname)

print()
print("Hostname is: " + hname)
print("IP Address is: " + IP_addres)
