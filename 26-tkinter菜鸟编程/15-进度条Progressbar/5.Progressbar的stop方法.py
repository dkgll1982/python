from tkinter import *
from tkinter.ttk import *
import time

def runing():
    pb.start() 

def stop(): 
    value =pb.cget('value')
    pb.stop()
    print(pb["value"])
    #停止后进度被清0，此时手动绑定停止前一刻的进度值
    pb["value"] = value

root = Tk()
root.title('start方法')

var =StringVar()
var.set('进度：0%')

pb = Progressbar(root,length=200,mode = 'indeterminate',orient=HORIZONTAL)
pb.pack(padx=10,pady=10)
pb['maximum'] = 100
pb['value'] = 0
 
btn = Button(root,text='Run',command=runing)
btn.pack(side=LEFT,pady=10,padx=10) 

btn2 = Button(root,text='Stop',command=stop)
btn2.pack(side=LEFT,pady=10) 

root.mainloop()
