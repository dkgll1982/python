#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: 航天神舟智慧系统技术有限公司 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2019-12-05 16:51:39 
# @Last Modified by: guojun 
# @Last Modified time: 2019-12-05 16:51:39 
# @Software: vscode 
# 参考链接：https://blog.csdn.net/guddqs/article/details/53810886?utm_source=blogxgwz5
# 此处演示：客户端从服务端下载文件功能。

'''
    规定:
    服务器接受客户端请求,得知要发送文件了(实际就得知该发送哪个)
    向其发送文件,然后不停的发送(大文件分段发送),此处我还要接受客户端的接受成功消息
'''


import socket

BUF_SIZE = 1024
server_addr = ('127.0.0.1',8888)

#socket的类型是socket.SOCK_DGRAM(udp使用的)
server = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

#服务端照例绑定地址
server.bind(server_addr)

#循环接受客户端发送数据,并将数据发回

count=0
flag=1
f=open(r'backup\zipfile.zip','rb')
while True:
    if count==0:
        print ("Are You Ready?")
        data,client_addr = server.recvfrom(BUF_SIZE)
        print ('来自',client_addr,' 的数据是: ',data.decode('utf-8'))

    data=f.read(BUF_SIZE)
    if str(data)!="b''":
        server.sendto(data,client_addr)
        print(data)                                         #此处打印注意被刷屏,仅测试用
    else:
        server.sendto('end'.encode('utf-8'),client_addr)    #此处为文件结束,发送结束通知给客户端
        break

    data,client_addr = server.recvfrom(BUF_SIZE)
    print ('接受自 ',client_addr,' 收到数据为 : ',data.decode('utf-8'))
    count+=1
print('循环了'+str(count))
server.close()

