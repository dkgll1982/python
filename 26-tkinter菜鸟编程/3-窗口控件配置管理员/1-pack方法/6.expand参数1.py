import threading
from tkinter import *  
# 引入字体模块
import tkinter.font as tkFont
import sys,os  
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))   
from singlewindow  import *

root = Tk()   
window.show(root)   
 
lbl1 = Label(root,text="①华中科技大学",bg = 'lightyellow') 
lbl2 = Label(root,text="②武汉大学",bg = 'lightgreen')  
lbl5 = Label(root,text="⑤湖北财经商贸大学",bg = 'Salmon') 

lbl1.pack(fill=X)
lbl2.pack(fill=BOTH,expand=Y)
lbl5.pack(fill=BOTH)

 
root.mainloop() 