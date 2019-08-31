from tkinter import * 
from tkinter.colorchooser import *

def bgUpdate():
    '''更改窗口背景颜色'''
    myColor = askcolor()                          #列出颜色对话框
    print(type(myColor),myColor)
    root.config(bg=myColor[1])

root =Tk()
root.title('色彩对话框')
root.geometry('500x300+200+200') 
btn = Button(root,text='Select Color',command=bgUpdate)
btn.pack(pady=5)

root.mainloop()
