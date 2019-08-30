import threading
from tkinter import *  
# 引入字体模块
import tkinter.font as tkFont
import sys,os  
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))   
from singlewindow  import *

root = Tk()   
window.show(root)    

frm =Frame(root,bg='lightpink',padx=10,pady=10)
frm.pack()
 
Label(frm,text='列',width=76).grid(columnspan=11,column=0,row=0)
Label(frm,text='行',height=15,pady=4).grid(rowspan=10,column=0,row=1)
for row in range(10):
    for column in range(10):
        Label(frm,text='%dX%d'%(row+1,column+1),width=6).grid(row=row+1,column=column+1,padx=2,pady=2)

root.mainloop()