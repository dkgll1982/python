import threading
from tkinter import *  
# 引入字体模块
import tkinter.font as tkFont
import sys,os  
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))   
from singlewindow  import *

root = Tk()   
window.show(root)    

lbl1 = Label(root,text="标签1",relief='solid')
lbl2 = Label(root,text="标签2",relief='solid')
lbl3 = Label(root,text="标签3",relief='solid')
lbl4 = Label(root,text="标签4",relief='solid')
lbl5 = Label(root,text="标签5",relief='solid')
lbl6 = Label(root,text="标签6",relief='solid')
lbl7 = Label(root,text="标签7",relief='solid')
lbl8 = Label(root,text="标签8",relief='solid')

lbl1.grid(row=0,column=0) 
lbl2.grid(row=0,column=1,rowspan=2,columnspan=2) 
lbl3.grid(row=0,column=3)  
lbl5.grid(row=1,column=0)  
lbl7.grid(row=1,column=3)  

root.mainloop()