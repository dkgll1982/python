from  socket import *

client = socket(AF_INET,SOCK_DGRAM)

while True:
    inp = input('->').strip()
    client.sendto(inp.encode('gbk'),('127.0.0.1',8081))

    data,serveraddr = client.recvfrom(1024)
    print(data.decode('gbk'),serveraddr)
    
    data,serveraddr = client.recvfrom(1024)
    print(data.decode('gbk'),serveraddr)

client.close()

