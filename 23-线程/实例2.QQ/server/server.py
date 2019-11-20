#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: 航天神舟智慧系统技术有限公司 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2019-08-12 23:07:52 
# @Last Modified by: guojun 
# @Last Modified time: 2019-08-12 23:07:52 
# @Software: vscode 

import tkinter
import threading
import socket

win = tkinter.Tk()
win.title("QQ服务器")
win.geometry("400x400+200+20")

users = {}

def run(ck,ca):
    print('*************') 
    usersName = ck.recv(1024)
    users[usersName.decode("utf-8")] = ck 
    print(users)

    while True:
        rData = ck.recv(1024)
        dataStr = rData.decode("utf-8")
        try:
            infolist = dataStr.split(":")
            users[infolist[0]].send((usersName.decode("utf-8")+":"+infolist[1]).encode("utf-8"))
        except:
            pass
        
def start():
    ipStr = eip.get()
    portStr = eport.get()
    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.bind((ipStr,int(portStr)))
    server.listen(10)
    printStr = "服务器启动成功"
    text.insert(tkinter.INSERT,printStr)
    while True:
        ck,ca=server.accept()
        t= threading.Thread(target = run,args=(ck,ca))
        t.start()

def startserver():
    s = threading.Thread(target = start)
    s.start() 

lableIp = tkinter.Label(win,text = "ip").grid(row=0,column=0)
lablePort = tkinter.Label(win,text = "port").grid(row=1,column=0)

eip = tkinter.Variable()
eport = tkinter.Variable()

entryIp = tkinter.Entry(win,textvariable = eip).grid(row=0,column=1)
entryPort = tkinter.Entry(win,textvariable = eport).grid(row=1,column=1)

button = tkinter.Button(win,text = "启动",command = startserver).grid(row=2,column=0)

text = tkinter.Text(win,width=30,height=10)
text.grid(row=3,column=0) 

win.mainloop()