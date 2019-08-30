import threading
from tkinter import *  
# 引入字体模块
import tkinter.font as tkFont
import sys,os  
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))   
from singlewindow  import *

root = Tk()  
window.show(root)   

lbl = Label(root,
        text = 'OK',
        font = 'Times 20 bold',
        fg = 'white',
        bg = 'blue'
        )
lbl.pack(anchor=S,side=RIGHT,padx=110,pady=10)

lbl2 = Label(root,
        text = 'NO RESULTS',
        font = 'Times 20 bold',
        fg = 'white',
        bg = 'red'
        )
lbl2.pack(anchor=S,side=RIGHT,padx=10,pady=10)
 
root.mainloop() 