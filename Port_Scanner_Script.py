#!usr/bin/python

# IMPORT STATEMENTS
import socket
from termcolor import colored

# WELCOME STATEMENT
print("Welcome to the Port Scanning Tool")
print("Please start by entering the following information")
print("Type 0 to exit the Tool")

# INIT VARIABLES
target_host = str(input("\nHost: "))   # Target Host, www.example.com
target_ip = socket.gethostbyname(target_host)     # Resolve t_host to IPv4 address

# Print the IP address
print("\nIP Address: ", target_ip)


while 1:
    target_port = int(input("\nPort Number: "))       # Enter the port to be scanned
    if target_port == 0:
        print("-- Port Scanning Ended --\n")
        exit()
    try:
        sock = socket.socket()
        res = sock.connect((target_ip, target_port))
        print("Port ", target_port, ": Open")
        sock.close()
    except:
        print("Port ", target_port, ": Closed")
    
print("\nPort Scanning complete")
