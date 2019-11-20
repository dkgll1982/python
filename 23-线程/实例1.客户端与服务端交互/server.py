#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: 航天神舟智慧系统技术有限公司 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2019-08-11 23:13:47 
# @Last Modified by: guojun 
# @Last Modified time: 2019-08-11 23:13:47 
# @Software: vscode 

import socket,threading

#创建一个socket
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#绑定IP端口
server.bind(('127.0.0.1',8081))
#监听
server.listen(5)
print("服务器启动成功,等待连接......")

def run(ck):
    data = clientSocket.recv(1024)
    print("客户端说："+data.decode("utf-8"))
    #senData = input("输入返回给客户端的数据：")
    clientSocket.send("sunck is a good man".encode("utf-8"))

while True: 
    #等待链接
    clientSocket,clientAddress = server.accept()
    t = threading.Thread(target=run,args=(clientSocket,))
    t.start()
    #print("%s --  %s 连接成功" %(str(clientSocket),clientAddress))