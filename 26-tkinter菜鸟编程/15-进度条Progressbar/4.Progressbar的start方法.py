from tkinter import *
from tkinter.ttk import *
import time

def runing():
    while pb.cget('value')<=pb['maximum']:
        pb.step(10)                             #滚动条每次增加步长
        root.update()                           #更新画面
        var.set('进度：%d%%'%pb.cget('value'))   #打印指针值
        time.sleep(1)

root = Tk()
root.title('start方法')

var =StringVar()
var.set('进度：0%')

pb = Progressbar(root,length=200,mode = 'determinate',orient=HORIZONTAL)
pb.pack(padx=10,pady=10)
pb['maximum'] = 100
pb['value'] = 0

style = Style()
style.configure("TLabel", foreground="green", background="pink",width=20) 

lbl = Label(root,textvariable=var,style='TLabel')
lbl.pack(padx=10,pady=10)

btn = Button(root,text='Running',command=runing)
btn.pack(pady=10) 

root.mainloop()
