import threading
from tkinter import *  
# 引入字体模块
import tkinter.font as tkFont
import sys,os  
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))   
from singlewindow  import *

root = Tk()   
window.show(root)   
 
lbl1 = Label(root,text="①华中科技大学",bg = 'lightyellow',height=2) 
lbl2 = Label(root,text="②武汉大学",bg = 'lightgreen',height=2) 
lbl3 = Label(root,text="③中南财经大学中南校区",bg = 'lightblue',height=2) 
lbl4 = Label(root,text="④华中农业大学",bg = 'PowderBlue',height=2) 
lbl5 = Label(root,text="⑤湖北财经商贸大学",bg = 'Salmon',height=2) 

lbl1.pack(pady=3,ipadx=50)
lbl2.pack(pady=3,ipadx=50)
lbl3.pack(pady=3,ipadx=50)
lbl4.pack(pady=3,padx=111,fill=X) 
lbl5.pack(pady=3,padx=50) 
 
root.mainloop() 