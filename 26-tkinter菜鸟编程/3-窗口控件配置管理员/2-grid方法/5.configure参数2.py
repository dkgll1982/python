import threading
from tkinter import *  
# 引入字体模块
import tkinter.font as tkFont
import sys,os  
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))   
from singlewindow  import *

root = Tk()   
window.show(root)     

root.rowconfigure(1,weight=1)
root.columnconfigure(0,weight=1)

lbl = Label(root,text="Label 1",bg='pink')
lbl.grid(row=0,column=0,padx=5,pady=5,stick=W+E) 

lb2 = Label(root,text="Label 2",bg='lightblue')
lb2.grid(row=0,column=1,padx=5,pady=5) 

lb3 = Label(root,bg='yellow')
lb3.grid(row=1,column=0,columnspan=2,padx=5,pady=5,
        sticky=N+S+W+E) 

root.mainloop()