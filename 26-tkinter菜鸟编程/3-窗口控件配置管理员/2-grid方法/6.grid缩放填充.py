import threading
from tkinter import *  
# 引入字体模块
import tkinter.font as tkFont
import sys,os  
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))   
from singlewindow  import *

root = Tk()   
window.show(root)    

for row in range(10):
    root.rowconfigure(row,weight=1)
    for column in range(10):
        root.columnconfigure(column,weight=1)
        Label(root,text='%dX%d'%(row,column),width=6).grid(row=row+1,column=column+1,padx=2,pady=2,ipady=12)

root.mainloop()