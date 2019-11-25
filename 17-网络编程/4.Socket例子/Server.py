#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: 航天神舟智慧系统技术有限公司 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2019-11-23 17:14:53 
# @Last Modified by: guojun 
# @Last Modified time: 2019-11-23 17:14:53 
# @Software: vscode
#参考链接：https://segmentfault.com/a/1190000016606175

import socket
server = socket.socket()
server.bind(('',8900))
#调用 listen() 方法开始监听端口， 传入的参数指定等待连接的最大数量
server.listen(4)
serObj,address = server.accept()
#当有客户端访问时，实现两边的交流，如果有一方退出，整个程序退出。
#服务器程序通过一个永久循环来接受来自客户端的连接
#这里虽然给出最大连接数为4，但单线程程序也只会响应一个连接
while True:
#建立连接后，服务端等待客户端发送的数据，实现通信
    re_data = serObj.recv(1024).decode('utf-8')
    print('client>>',re_data)
    if re_data == 'quit':
        break
    send_data = input('server>>')
    serObj.send(send_data.encode('utf-8'))
    if send_data == 'quit':
        break
serObj.close()
server.close()