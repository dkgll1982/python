import threading
from tkinter import *  
# 引入字体模块
import tkinter.font as tkFont
import sys,os  
sys.path.append(os.path.dirname(os.path.dirname(__file__)) )   
from singlewindow  import *
from PIL import Image,ImageTk
import Pmw

root = Tk()   
window.show(root)    
labl = Label(root)

def showmsg():
    labl["text"]="I Love Python!!!"
    labl['bg']='lightyellow'
    labl['fg']='blue'
    labl.config(width=20,height=2,padx=6)
    labl.pack()

btn1 = Button(root,text="打印消息",width=15,command=showmsg)
btn2 = Button(root,text="结束",width=15,command=root.destroy,padx=5,state=DISABLED)


btn1.pack(side=LEFT,anchor=S,pady=10,padx=10)
btn2.pack(side=LEFT,anchor=S,pady=10)

ballon = Pmw.Balloon(root)
ballon.bind(btn1,'这是一个按钮撒')

root.mainloop()