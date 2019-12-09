import socket
import sys
 
HOST, PORT = "localhost", 9000 
 
# Create a socket (SOCK_STREAM means a TCP socket)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Connect to server and send data
sock.connect((HOST, PORT))

while True: 
    cmd = input('=>')
    if not cmd:continue
    if cmd=="quit":break
    sock.sendall(bytes(cmd + "\n", "gbk"))
    # Receive data from the server and shut down
    received = str(sock.recv(1024), "gbk")
    
    print("Sent:     {}".format(cmd))
    print("Received: {}".format(received))
sock.close()