from tkinter import *

root = Tk()
root.title()
root.geometry('300x100+200+200')

def printInfo():            #打印显示的值
    print(spin.get())

spin = Spinbox(root,from_=10,to=30,increment=0.2,command = printInfo)
spin.pack(pady=20,padx=20)

root.mainloop()