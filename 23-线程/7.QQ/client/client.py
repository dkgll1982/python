#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: 航天神舟智慧系统技术有限公司 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2019-08-17 19:32:34 
# @Last Modified by: guojun 
# @Last Modified time: 2019-08-17 19:32:34 
# @Software: vscode  

import tkinter
import threading
import socket

win = tkinter.Tk()
win.title("QQ客户端")
win.geometry("400x400+200+20")
 
ck = None

def getinfo():
    while True:
        data = ck.recv(1024)
        text.insert(tkinter.INSERT,data.decode("utf-8"))

#连接服务器
def connectServer(): 
    global ck
    ipStr = eip.get()
    portStr =eport.get()

    userStr = euser.get()
    #创建一个socket
    client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client.connect((ipStr,int(portStr)))
    client.send(userStr.encode("utf-8"))

    ck = client

    #等待接收数据
    t = threading.Thread(target = getinfo)
    t.start()

#发送好友消息
def sengmsg():
    friend = efriend.get()
    sendStr = esend.get()

    sendStr = friend + ":" + sendStr
    ck.send(sendStr.encode("utf-8"))

lableuser = tkinter.Label(win,text = "user").grid(row=0,column=0)
lableIp = tkinter.Label(win,text = "ip").grid(row=1,column=0)
lablePort = tkinter.Label(win,text = "port").grid(row=2,column=0)

euser = tkinter.Variable()
eip = tkinter.Variable()
eport = tkinter.Variable()

entryUser = tkinter.Entry(win,textvariable = euser).grid(row=0,column=1)
entryIp = tkinter.Entry(win,textvariable = eip).grid(row=1,column=1)
entryPort = tkinter.Entry(win,textvariable = eport).grid(row=2,column=1)

button = tkinter.Button(win,text = "链接",command = connectServer).grid(row=3,column=0)

text = tkinter.Text(win,width=30,height=6)
text.grid(row=4,column=0) 

#lablesend = tkinter.Label(win,text = "send message").grid(row=5,column=0)
esend = tkinter.Variable()
entrysend = tkinter.Entry(win,textvariable = esend).grid(row=5,column=0)

efriend =  tkinter.Variable()
entryfriend = tkinter.Entry(win,textvariable = efriend).grid(row=6,column=0)
 
button2 = tkinter.Button(win,text = "发送",command = sengmsg).grid(row=6,column=1)

win.mainloop()