import threading
from tkinter import *  
# 引入字体模块
import tkinter.font as tkFont
import sys,os  
sys.path.append(os.path.dirname(os.path.dirname(__file__)) )   
from singlewindow  import *
from PIL import Image,ImageTk

root = Tk()   
window.show(root)     
root.title("简易计算器")
labl = Label(root,text="",bg="yellow",anchor=W,height=2)
btn7 = Button(root,text='7',width=8,height=2)
btn8 = Button(root,text='8',width=8,height=2)
btn9 = Button(root,text='9',width=8,height=2)
btnM = Button(root,text='*',width=8,height=2)
btn4 = Button(root,text='4',width=8,height=2)
btn5 = Button(root,text='5',width=8,height=2)
btn6 = Button(root,text='6',width=8,height=2)
btnS = Button(root,text='-',width=8,height=2)
btn1 = Button(root,text='1',width=8,height=2)
btn2 = Button(root,text='2',width=8,height=2)
btn3 = Button(root,text='3',width=8,height=2)
btnP = Button(root,text='+',width=8,height=2)
btn0 = Button(root,text='0',width=8,height=2)
btnD = Button(root,text='.',width=8,height=2)
btnE = Button(root,text='=',width=8,height=2) 

labl.grid(row=0,column=0,columnspan=4,sticky=W+E)
btn7.grid(row=1,column=0,padx=5,pady=3)
btn8.grid(row=1,column=1,padx=5,pady=3)
btn9.grid(row=1,column=2,padx=5,pady=3)
btnM.grid(row=1,column=3,padx=5,pady=3)
btn4.grid(row=2,column=0,padx=5,pady=3)
btn5.grid(row=2,column=1,padx=5,pady=3)
btn6.grid(row=2,column=2,padx=5,pady=3)
btnS.grid(row=2,column=3,padx=5,pady=3)
btn1.grid(row=3,column=0,padx=5,pady=3)
btn2.grid(row=3,column=1,padx=5,pady=3)
btn3.grid(row=3,column=2,padx=5,pady=3)
btnP.grid(row=3,column=3,padx=5,pady=3)
btn0.grid(row=4,column=0,padx=5,pady=3,columnspan=2,sticky=W+E)
btnD.grid(row=4,column=2,padx=5,pady=3)
btnE.grid(row=4,column=3,padx=5,pady=3) 

root.mainloop()