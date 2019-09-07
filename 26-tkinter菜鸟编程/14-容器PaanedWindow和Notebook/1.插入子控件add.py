from tkinter import *

root = Tk()
root.title('插入子控件')

pw = PanedWindow(orient=VERTICAL)
pw.pack(fill=BOTH,expand=True)

top = Label(pw,text='Top pane')
pw.add(top)                             #top标签插入PanedWindow

bottom = Label(pw,text='Bottom pane')
pw.add(bottom)                          #bottom标签插入PanedWindow

root.mainloop()