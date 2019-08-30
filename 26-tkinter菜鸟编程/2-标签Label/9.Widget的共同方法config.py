import threading
from tkinter import *  
# 引入字体模块
import tkinter.font as tkFont
import sys,os  
sys.path.append(os.path.dirname(os.path.dirname(__file__)) )   
from singlewindow  import *
import datetime

root = Tk() 

window.show(root)   

counter = 0                                         #计数的全局变量

def run_counter1(digit):                            #数字变量内容的更新
    def counting():                                 #更新数字方法
        global counter                              #定义全局变量
        global task1
        counter+=1  
        digit.config(text='计数：'+str(counter))    #列出数字内容
        task1 = digit.after(1000,counting)          #隔1秒执行调用couting
    counting()                                      #调用方法

def run_counter2(digit):                            #数字变量内容的更新
    def counting():                                 #更新数字方法
        global task2
        day20 = datetime.datetime.strptime('2019-09-08 0:0:0','%Y-%m-%d %H:%M:%S')
        now = datetime.datetime.today()
        delta = day20 - now
        day = delta.days
        hour = int(delta.seconds/60/60)
        minutes = int((delta.seconds-hour*60*60)/60)
        seconds = delta.seconds-hour*60*60-minutes*60
        mseconds = delta.microseconds 

        digit.config(text='距离开始:'+ ''+str(day)+''+'天'+''+str(hour)+''+'时'+''+str(minutes)+''+'分'+''+str(seconds)+'.'+str(mseconds)[0:4]+'秒') 
        task2 = digit.after(10,counting)                  
    counting()           

def stop():
    #关闭定时循环
    root.after_cancel(task1)
    root.after_cancel(task2)

def restart():
    run_counter1(digit1)
    run_counter2(digit2)

digit1 = Label(root,bg='yellow',
            fg ="blue",height=3,
            width=10,
            font = "Helvetic 20 bold"
        )
digit2 = Label(root,bg='pink',
            fg ="blue",height=3,
            width=30,
            font = "Helvetic 20 bold", 
        ) 

digit1.pack()
digit2.pack(pady = 10)
run_counter1(digit1)
run_counter2(digit2)

btn = Button(root,text = "停止计时",command = stop)
btn.pack();        
btn = Button(root,text = "继续计时",command = restart)
btn.pack(pady=10);        

root.mainloop();