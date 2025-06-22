import socket

# calls on socket class

# AF_INET specifies 1pv4 protocol SOCK_STREAM specifies connection 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(10)

host = input("Please enter the ip address you want to scan: ")
port = int(input("Enter the port number you want to scan: "))

# preforms scan

def portScanner(port):
    # connect_ex return error codes
    if s.connect_ex((host,port)):
        print("The port is closed")
    else:
        print("The port is open")

portScanner(port)