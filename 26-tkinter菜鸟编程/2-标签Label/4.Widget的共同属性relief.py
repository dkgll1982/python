
from tkinter import *  
# 引入字体模块
import tkinter.font as tkFont
import sys,os  
sys.path.append(os.path.dirname(os.path.dirname(__file__)) )   
from singlewindow  import *

root = Tk() 

window.show(root)  

title = "当前标签效果："

var = StringVar() 
var.set(title+"flat")

lbl = Label(root,
    text = "I love tkinter",
    fg = "blue",
    bg = "yellow", 
    height = 2,            
    width = 15,     
    relief = "flat"   #默认为flat，可不写
)

index = 1
clist=["flat","groove","raised","ridge","solid","sunken"]
def changelabel(): 
    global index
    lbl.configure(relief=clist[index]) 
    var.set(title+lbl.cget('relief'))
    index+=1
    if index==6:
        index=0

#增加配置管理 
lbl.pack()

Label(root,textvariable = var,fg = "red",bg = "pink").pack()

btn = Button(root,text="改变标签效果",command=changelabel)

for x in range(len(clist)):
    Label(root,
        text = title+clist[x],
        fg = "blue",
        bg = "yellow", 
        bd=5,
        height = 1,            
        width = 25,     
        relief = clist[x]  #默认为flat，可不写
    ).pack(pady=3,padx=2)

btn.pack(pady=10)

root.mainloop()