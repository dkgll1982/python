from tkinter import *
from tkinter.ttk import *
import time

root = Tk()
root.geometry('300x240+650+250')
root.title('进度动画效果')

# root.title('标题名')    　　 　 修改框体的名字,也可在创建时使用className参数来命名；
# root.resizable(0,0)   　　 　　 框体大小可调性，分别表示x,y方向的可变性；
# root.geometry('250x150')　　    指定主框体大小；
# root.quit()        　　　　 　　 退出；
# root.update_idletasks()
# root.update()        　　　　　  刷新页面；
def runing():
    for i in range(100):
        pb['value']=i
        pb.update()                 #刷新页面；
        time.sleep(0.02)

#使用默认设置创建进度条
pb = Progressbar(root)
pb.pack(pady=20)

pb['maximum'] = 100
pb['value'] = 0

#mode:进度条的工作模式
#determinate：确定模式，从起点移动到终点。一般用于知道工作时间时使用此模式
#indeterminate：不确定模式，指针在起点和重点间来回移动
pb2 = Progressbar(root,orient=HORIZONTAL,length=200,mode='indeterminate')
pb2.pack(pady=20)

pb2['maximum'] = 100            #进度条的最大值
pb2['value'] = 0                #进度条的目前值

btn = Button(root,text='Running',command=runing)
btn.pack(padx=10,pady=10)

root.mainloop()
