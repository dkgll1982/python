from tkinter import *

def cal(*args):
    xl.set(xe.get())
    print("data changed:",xe.get())

root = Tk()
root.geometry('200x120+400+100')

xe = StringVar()
 
entry = Entry(root,textvariable=xe)
entry.pack(pady=5,padx=10)
xe.trace('w',cal)

xl = StringVar()
lbl =Label(root,textvariable=xl)
xl.set("同步显示")
lbl.pack(pady=5,padx=10)
root.mainloop()