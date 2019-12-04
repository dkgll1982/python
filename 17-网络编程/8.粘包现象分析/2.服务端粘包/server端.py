import socket
import time
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(('127.0.0.1',9905)) #0-65535:0-1024给操作系统使用
server.listen(5)
 
 
conn,   addr=server.accept()
print('connect by ',addr)
#接收方不及时接收缓冲区的包，造成多个包接收（客户端发送了一段数据，服务端只收了一小部分，服务端下次再收的时候还是从缓冲区拿上次遗留的数据，产生粘包）　
res1 = conn.recv(2)#第一没有接收完整
print('第一次',res1)
time.sleep(6)
res2=conn.recv(10)# 第二次会接收旧数据，再收取新的
print('第二次', res2)
res3=conn.recv(10)# 第二次会接收旧数据，再收取新的
print('第二次', res3)