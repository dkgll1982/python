#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: 航天神舟智慧系统技术有限公司 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2019-11-23 17:14:59 
# @Last Modified by: guojun 
# @Last Modified time: 2019-11-23 17:14:59 
# @Software: vscode 

import socket
client = socket.socket()
client.connect(('127.0.0.1',8900))
while True:
    send_data = input("client>>")
    client.send(send_data.encode('utf-8'))
    if send_data == 'quit':
        break
    re_data = client.recv(1024).decode('utf-8')
    if re_data == 'quit':
        break
    print("server>>",re_data)

client.close()