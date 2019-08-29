
from tkinter import *  
# 引入字体模块
import tkinter.font as tkFont
import sys,os  
sys.path.append(os.path.dirname(os.path.dirname(__file__)) )   
from singlewindow  import *

root = Tk() 

window.show(root)   

var = StringVar() 
var.set("当前标签padx:1,pady:1")

lbl = Label(root,
    text = "I love tkinter",
    fg = "blue",
    bg = "yellow", 
    height = 2,            
    width = 15,     
    relief = "flat",   #默认为flat，可不写
    padx = 1,
    pady = 1
)
 
def changelabel(step): 
    padx = lbl.cget('padx')+step
    pady = lbl.cget('pady')+step
    if padx<0:
        padx=0
    if pady<0:
        pady=0
    lbl.configure(padx=padx) 
    lbl.configure(pady=pady) 
    var.set("当前标签padx:%d,pady:%d"%(padx,pady)) 

#增加配置管理 
lbl.pack()

Label(root,textvariable = var,fg = "red",bg = "pink").pack(pady=5)

btn1 = Button(root,text="增加字间距",command=lambda:changelabel(1))
btn2 = Button(root,text="减小字间距",command=lambda:changelabel(-1))

btn1.pack(side=TOP,padx=5,pady=10)
btn2.pack(side=TOP,padx=5)

root.mainloop()