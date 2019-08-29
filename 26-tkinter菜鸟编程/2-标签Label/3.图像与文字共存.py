
from tkinter import *  
# 引入字体模块
import tkinter.font as tkFont
import sys,os  
sys.path.append(os.path.dirname(os.path.dirname(__file__)) )   
from singlewindow  import *

root = Tk() 

window.show(root)  

title = "当前选中的图像与文字共存模式："

var = StringVar() 
var.set(title+"bottom")

lbl = Label(root,
    text = "I love tkinter",
    fg = "blue",
    bg = "yellow",
    height = 156,               #字符高度或者像素，定义image或者bitmap属性就变成像素
    width = 242,                #字符宽度或者像素，定义image或者bitmap属性就变成像素
    wraplength = 80,            #标签文字达到多少像素进行换行输出
    anchor = 'center',          #整个文本块在Label中的位置
    justify = "left",           #控制多行文本的对齐方式
    #font = font,
    bitmap="hourglass",         #图标，如hourglass 为沙漏形状的图标
    compound="bottom"
)

index = 0
clist=["none","left","right","top","bottom","center"]
def changelabel():
    global index
    lbl.configure(compound=clist[index])
    var.set(title+clist[index])
    index+=1
    if index==6:
        index=0

#增加配置管理 
lbl.pack()

Label(root,textvariable = var,fg = "red",bg = "pink").pack()

btn = Button(root,text="改变图像显示",command=changelabel)
btn.pack()

root.mainloop()