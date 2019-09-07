from tkinter import *

root = Tk()
root.title('插入子控件')

pw = PanedWindow(orient=HORIZONTAL)
pw.pack(fill=BOTH,expand=True)

ent = Entry(pw,bd=3)
pw.add(ent)                              

scale = Scale(pw,orient=HORIZONTAL)
pw.add(scale)                          

root.mainloop()