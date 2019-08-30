import threading
from tkinter import *  
# 引入字体模块
import tkinter.font as tkFont
import sys,os  
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))   
from singlewindow  import *

root = Tk()   
window.show(root)    

print("执行前",root.pack_slaves())

lbl = Label(root,text="OK",font='Times 20 bold',fg='white',bg='blue')
lbl.pack(anchor=S,side=RIGHT,padx=10,pady=10)

lbl2 = Label(root,text='NO',font='Times 20 bold',fg='white',bg='red')
lbl2.pack(anchor=S,side=RIGHT,pady=10)

print('执行后',root.pack_slaves())
print('标签lbl2属性:%s',lbl2.info())

def enable():
    lbl2.forget()
    lbl.forget()

def show():
    lbl.pack(anchor=S,side=RIGHT,padx=10,pady=10)
    lbl2.pack(anchor=S,side=RIGHT,pady=10)


btn = Button(root,text='隐藏标签',command=enable)
btn.pack()

btn2 = Button(root,text='标签复原',command=show)
btn2.pack() 

root.mainloop()