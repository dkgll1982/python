import threading
from tkinter import *  
# 引入字体模块
import tkinter.font as tkFont
import sys,os  
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))   
from singlewindow  import *

root = Tk() 
var = StringVar()  
sep = 200 
step = 1

var.set("当前pady的值：pack(pady=%d)"%(sep))
window.show(root)   
 
lbl1 = Label(root,text="①华中科技大学",bg = 'lightyellow',height=2) 
lbl2 = Label(root,text="②武汉大学",bg = 'lightgreen',height=2) 
lbl3 = Label(root,text="③中南财经大学中南校区",bg = 'lightblue',height=2) 
lbl4 = Label(root,text="④华中农业大学",bg = 'PowderBlue',height=2) 
lbl5 = Label(root,text="⑤湖北财经商贸大学",bg = 'Salmon',height=2) 

lbl1.pack(fill=X,pady=3,padx =sep)
lbl2.pack(fill=X,pady=3,padx =sep)
lbl3.pack(fill=X,pady=3,padx =sep)
lbl4.pack(fill=X,pady=3,padx =sep) 
lbl5.pack(fill=X,pady=3,padx =sep) 

lbl6 = Label(root,textvariable=var,fg='red',bg='lightyellow')
lbl6.pack(fill=X,padx=5,pady=5)

def changepad(stp):
    global step
    step = stp; 
    def change():
        global sep
        sep=sep+stp 
        lbl1.pack(ipadx =sep)
        lbl2.pack(padx =sep)
        lbl3.pack(padx =sep)
        lbl4.pack(padx =sep) 
        lbl5.pack(padx =sep)
        var.set("当前pady的值：pack(pady=%d)"%(sep))  
        global task 
        #开启定时循环   
        task = root.after(100,change)
        if sep>=350 or sep<=20:
            root.after_cancel(task)
    change()    

frm =Frame(root,bg='lightgray')    
frm.pack()   

btn = Button(frm,text="增加padx值",command=lambda:changepad(1))
btn.pack(side=LEFT,pady=5,padx=20)
btn = Button(frm,text="减小padx值",command=lambda:changepad(-1))
btn.pack(side=LEFT,pady=5)

root.mainloop() 