from  socket import *

client = socket(AF_INET,SOCK_DGRAM)

client.sendto(b'hello',('127.0.0.1',8081))
client.sendto(b'word',('127.0.0.1',8081))

data, serveraddr = client.recvfrom(1024)
print(data.decode('gbk'), serveraddr)

data, serveraddr = client.recvfrom(1024)
print(data.decode('gbk'), serveraddr)

client.close()

