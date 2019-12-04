import socket
import time
 
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(('127.0.0.1',9904)) #0-65535:0-1024给操作系统使用
server.listen(5)
 
 
conn,   addr=server.accept()
print('connect by ',addr)
res1 = conn.recv(100)
print('第一次',res1.decode('utf-8'))
res2=conn.recv(110)
print('第二次', res2.decode('utf-8'))
res3=conn.recv(110)
print('第三次', res3.decode('utf-8'))