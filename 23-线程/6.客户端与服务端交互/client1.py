#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: 航天神舟智慧系统技术有限公司 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2019-08-11 23:19:09 
# @Last Modified by: guojun 
# @Last Modified time: 2019-08-11 23:19:09 
# @Software: vscode 

import socket 

#创建一个socket
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(("127.0.0.1",8081))

while True:
    data =input("请输入发送给服务器的数据:")
    client.send(data.encode("utf-8"))
    info = client.recv(1024)
    print("服务器说：",info.decode("utf-8"))