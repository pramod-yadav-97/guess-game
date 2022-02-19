import socket
import sys
url = sys.stdin.readline()
IP_addres = socket.gethostbyname(url)
print("IP Address is:" + IP_addres)
