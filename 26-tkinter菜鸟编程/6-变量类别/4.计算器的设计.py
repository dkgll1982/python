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
equ = StringVar()
equ.set("0")

def calculate():
    if '=' not in (equ.get()):
        result = eval(equ.get())
        equ.set(equ.get()+'=\n'+str(result))

def show(buttonstring):
    content = equ.get()
    if content == '0':
        content = ""
    if not(buttonstring =='.' and '.' in content):
        equ.set(content+buttonstring)

def backspace():
    equ.set(str(equ.get()[:-1]))         #删除前一个字符

def clear():
    equ.set('0')                         #清除显示区,放置0

labl = Label(root,textvariable=equ,bg="yellow",anchor=W,height=2)
labl.grid(row=0,column=0,columnspan=4,sticky=W+E,padx=5,pady=5)

clearbtn = Button(root,text='C', height=2,fg='blue',command=clear)
clearbtn.grid(row=1,column=0,padx=5,sticky=W+E)
Button(root,text='DEL',width=8,height=2,command=backspace,font='blod').grid(row=1,column=1)
Button(root,text='%',width=8,height=2,command=lambda:show("%"),font='blod').grid(row=1,column=2)
Button(root,text='/',width=8,height=2,command=lambda:show("/"),font='blod').grid(row=1,column=3)

Button(root,text='7',width=8,height=2,command=lambda:show("7"),font='blod').grid(row=2,column=0,padx=5,pady=3)
Button(root,text='8',width=8,height=2,command=lambda:show("8"),font='blod').grid(row=2,column=1,padx=5,pady=3)
Button(root,text='9',width=8,height=2,command=lambda:show("9"),font='blod').grid(row=2,column=2,padx=5,pady=3)
Button(root,text='*',width=8,height=2,command=lambda:show("*"),font='blod').grid(row=2,column=3,padx=5,pady=3)

Button(root,text='4',width=8,height=2,command=lambda:show("4"),font='blod').grid(row=3,column=0,padx=5,pady=3)
Button(root,text='5',width=8,height=2,command=lambda:show("5"),font='blod').grid(row=3,column=1,padx=5,pady=3)
Button(root,text='6',width=8,height=2,command=lambda:show("6"),font='blod').grid(row=3,column=2,padx=5,pady=3)
Button(root,text='-',width=8,height=2,command=lambda:show("-"),font='blod').grid(row=3,column=3,padx=5,pady=3)

Button(root,text='1',width=8,height=2,command=lambda:show("1"),font='blod').grid(row=4,column=0,padx=5,pady=3)
Button(root,text='2',width=8,height=2,command=lambda:show("2"),font='blod').grid(row=4,column=1,padx=5,pady=3)
Button(root,text='3',width=8,height=2,command=lambda:show("3"),font='blod').grid(row=4,column=2,padx=5,pady=3)
Button(root,text='+',width=8,height=2,command=lambda:show("+"),font='blod').grid(row=4,column=3,padx=5,pady=3)

Button(root,text='0',width=8,height=2,command=lambda:show("0"),font='blod').grid(row=5,column=0,padx=5,pady=3,columnspan=2,sticky=W+E)
Button(root,text='.',width=8,height=2,command=lambda:show("."),font='blod').grid(row=5,column=2,padx=5,pady=3)
Button(root,text='=',height=2,command=calculate).grid(row=5,column=3,padx=5,pady=3,sticky=W+E) 

root.mainloop()