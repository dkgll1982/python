from tkinter import *
import tkinter

top = tkinter.Tk()
top.geometry('500x400+300+300')
#Tkinter Bitmaps: 使用这个属性显示一个位图。有以下类型的可用位图

bitmaplist=(
    "error",
    "gray75",
    "gray50",
    "gray25",
    "gray12",
    "hourglass",
    "info",
    "questhead",
    "question",
    "warning"
)

for x in bitmaplist:
    tkinter.Button(top, 
        text =x, 
        relief=RAISED,
        bitmap=x,
        compound='left',
        width=120,
        anchor='w', #内部文字在区域内输出位置的设置
        padx =10
    ).pack(pady=5) 

top.mainloop()