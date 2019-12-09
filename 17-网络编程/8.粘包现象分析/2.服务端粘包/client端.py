import socket
import time
 
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
 
client.connect(('127.0.0.1',9905))
 
 
client.send('hello'.encode('utf-8'))
#client.recv(1)
client.send('world'.encode('utf-8'))
