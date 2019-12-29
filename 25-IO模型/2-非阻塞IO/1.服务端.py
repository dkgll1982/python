#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: 航天神舟智慧系统技术有限公司 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2019-12-28 17:47:01 
# @Last Modified by: guojun 
# @Last Modified time: 2019-12-28 17:47:01 
# @Software: vscode 

from socket import *
from time import ctime

HOST = ''
PORT = 8083
BUFSIZ = 1024
ADDR = (HOST,PORT)

tcpSerSock = socket(AF_INET,SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)
tcpSerSock.setblocking(False)
print('starting...')

rlist = []
wlist = []
while True:
    try:
        conn, addr = tcpSerSock.accept()        #IO操作 
        rlist.append(conn)
        print(rlist)
    except BlockingIOError:
        del_list = []
        #收消息
        for conn in rlist:
            try:
                data = conn.recv(1024)          #IO操作 
                if not data:
                    del_list.append(conn)
                    continue 
                wlist.append((conn,data.upper()))
            except BlockingIOError:
                continue
            except Exception:
                conn.close()
                del_list.append(conn)

        #发消息
        del_wlist = []
        for item in wlist:
            try:
                conn = item[0]
                data = item[1]
                conn.send(data)
                del_wlist.append(item)
            except BlockingIOError:
                pass

        for conn in del_wlist:  
            wlist.remove(conn)

        for conn in del_list: 
            rlist.remove(conn)
            
tcpSerSock.close()