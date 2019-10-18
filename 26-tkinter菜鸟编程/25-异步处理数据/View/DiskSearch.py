import time
from tkinter import *

def run():
    index = 0
    while index<100:
        txt.insert(END,'...')
        txt.update()#我指的是加这句代码。
        #下面两句，回复显示后对不齐，请注意，与上面两句平行 
        time.sleep(0.3)
        index+=1

root = Tk()
txt = Text(root)
txt.pack()
Button(root,text='Run',command = run).pack()
root.mainloop()