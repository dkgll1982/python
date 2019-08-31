from tkinter import *

def cal(name,index,mode):
    xl.set(xe.get())
    print("name=%r,index=%r,mode=%r"%(name,index,mode))

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