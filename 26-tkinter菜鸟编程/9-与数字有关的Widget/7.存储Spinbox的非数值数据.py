from tkinter import *

root = Tk()
root.title()
root.geometry('300x100+200+200')

def printInfo():            #打印显示的值
    print(spin.get())

spin = Spinbox(root,values=(10,20,324,64,'非数字也能存储',23,54,234,75,24,724),command = printInfo)  #以元组形式存储数值
spin.pack(pady=20,padx=20)

root.mainloop()