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

lbl1.pack(side=BOTTOM,fill=X)                 #从左往右配置时，配置管理员配置的空间是Y轴的空间，从上往下配置时，配置的空间是X轴的空间
lbl2.pack(side=LEFT,fill=BOTH,expand=YES)
lbl5.pack(side=LEFT,fill=BOTH)

 
root.mainloop() 