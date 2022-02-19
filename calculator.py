import socket
import math

num1=0
num2=0

print()

print("      Hi "+ socket.gethostname())

print("*** Calculator ***")
print()

num1=int(input("Enter First Number:"))
num2=int(input("Enter Second Number:"))
choice=input("Choice:")

if(choice=="a"):
    print(num1+num2)

if(choice=="s"):
    print(num1-num2)

if(choice=="m"):
    print(num1*num2)

if(choice=="d"):
    print(num1/num2)

