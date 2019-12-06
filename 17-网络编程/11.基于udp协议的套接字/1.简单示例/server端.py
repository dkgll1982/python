from socket import *

server = socket(AF_INET,SOCK_DGRAM)
server.bind(('127.0.0.1',8081))

while True:
    data,clientaddr = server.recvfrom(1024)
    print(data.decode('gbk'),clientaddr)

    server.sendto('第一条：'.encode('gbk')+data,clientaddr)
    server.sendto('第二条：'.encode('gbk')+data,clientaddr)

server.close()