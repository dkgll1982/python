from tkinter import *
import Pmw

root = Tk()
root.geometry('300x300')

lab = Label(root,text="别惹我")
lab.pack()

ballon = Pmw.Balloon(root)
ballon.bind(lab,'点你妹啊')

root.mainloop()