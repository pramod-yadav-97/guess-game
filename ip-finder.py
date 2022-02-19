import socket
url=input()
IP_addres = socket.gethostbyname(url)
print("IP Address is:" + IP_addres)
