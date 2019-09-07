from tkinter import *
from tkinter.ttk import *

root = Tk()
root.geometry('300x140')
root.title('进度条的基本应用')

#使用默认设置创建进度条
pb = Progressbar(root)
pb.pack(pady=20)

pb['maximum'] = 100
pb['value'] = 23

#mode:进度条的工作模式
#determinate：确定模式，从起点移动到终点。一般用于知道工作时间时使用此模式
#indeterminate：不确定模式，指针在起点和重点间来回移动
pb2 = Progressbar(root,orient=HORIZONTAL,length=200,mode='indeterminate')
pb2.pack(pady=20)

pb2['maximum'] = 100            #进度条的最大值
pb2['value'] = 50               #进度条的目前值

root.mainloop()
