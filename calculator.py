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

if(choice=="Add"):
    print(num1+num2)

if(choice=="Sub"):
    print(num1-num2)

if(choice=="Mul"):
    print(num1*num2)

if(choice=="Div"):
    print(num1/num2)

