import threading
from tkinter import *  
# 引入字体模块
import tkinter.font as tkFont
import sys,os  
sys.path.append(os.path.dirname(os.path.dirname(__file__)) )   
from singlewindow  import *
from PIL import Image,ImageTk

root = Tk()   
window.show(root)     

gif1 = PhotoImage(file = r'images\mao.gif')
gif2 = PhotoImage(file = r'images\remove.gif')
btn1 = Button(root,text="打印消息",width=85,image=gif1,height=24,compound=LEFT,anchor=W,cursor='star')
btn2 = Button(root,text="结束",width=55,image=gif2,height=24,command=root.destroy,compound=LEFT,anchor=W,cursor='question_arrow') 

btn1.pack(side=LEFT)
btn2.pack(side=LEFT,padx=10)
root.mainloop()