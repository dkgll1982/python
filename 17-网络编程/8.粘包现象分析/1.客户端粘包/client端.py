import socket
import time
 
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
 
client.connect(('127.0.0.1',9904))
 
 
client.send('hello'.encode('utf-8'))
#client.recv(1)

#送端需要等缓冲区满才发送出去，造成粘包（发送数据时间间隔很短，数据量很小，TCP优化算法会当做一个包发出去，产生粘包）
#此处采用sleep间隔发送就不会产生粘包现象
#time.sleep(0.00001)
client.send('world'.encode('utf-8'))
client.send('！'.encode('utf-8'))
client.send('！'.encode('utf-8'))
client.send('！'.encode('utf-8'))
