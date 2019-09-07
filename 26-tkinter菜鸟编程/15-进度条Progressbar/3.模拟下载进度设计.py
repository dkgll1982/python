from tkinter import *
from tkinter.ttk import *
import time

root = Tk()
root.geometry('300x140+650+250')
root.title('模拟下载进度设计')
bytes = 0                       #设置初始值
maxbytes=10000                  #假设下载文件大小

def load():                     #仿真下载数据 
    global bytes
    bytes = 0
    btn.config(state='disabled')
    pb['value'] = 0 
    pb['maximum']=maxbytes
    loading()

def loading():
    global bytes

    # bytes += 50                    #模拟每次下载500B
    # pb['value'] = bytes            #设置指针
    # if bytes < maxbytes:
    #     pb.after(20,loading)       #经过0.5s继续执行loading
    # else: 
    #     btn.config(state='enabled') 
   
    #或者如下循环刷新页面
    for x in range(200):
        bytes += 50                    #模拟每次下载500B
        pb['value'] = bytes             #设置指针
        root.update()
        time.sleep(0.02)

    btn.config(state='enabled') 
 
pb = Progressbar(root,length=200,mode='determinate',orient=HORIZONTAL)
pb.pack(padx=10,pady=20) 
pb['value'] = 0  

btn = Button(root,text='Load',command=load)
btn.pack(padx=10,pady=10)

root.mainloop()
