import socket
def banner(ip, port):
    s = socket.socket()
    s.connect((ip, int(port)))
    print(s.recv(1024))

def main():
    ip = input("Please eneter your ip: ")
    port = str(input("Please enter your port: "))
    banner(ip,port)

main()

