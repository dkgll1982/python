import threading
from tkinter import *  
# 引入字体模块
import tkinter.font as tkFont
import sys,os  
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))   
from singlewindow  import *

root = Tk()   
window.show(root)    

frm =Frame(root)
 
lbl1 = Label(root,text="①华中科技大学",bg = 'lightyellow',height=2) 
lbl2 = Label(frm,text="②武汉大学",bg = 'lightgreen',height=2) 
lbl3 = Label(frm,text="③中南财经大学中南校区",bg = 'lightblue',height=2) 
lbl4 = Label(frm,text="④华中农业大学",bg = 'lightpink',height=2) 
lbl5 = Label(root,text="⑤湖北财经商贸大学",bg = 'Salmon',height=2)  

lbl1.pack(side=LEFT,fill=Y)
frm.pack(side=LEFT,fill=BOTH,expand=Y) 
lbl2.pack(side=TOP,fill=X)
lbl3.pack(side=TOP,fill=BOTH,expand=Y)
lbl4.pack(side=TOP,fill=X)
lbl5.pack(side=RIGHT,fill=Y) 
 
print('执行后',root.pack_slaves())
 
root.mainloop()