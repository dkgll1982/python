import threading
from tkinter import *  
# 引入字体模块
import tkinter.font as tkFont
import sys,os  
sys.path.append(os.path.dirname(os.path.dirname(__file__)) )   
from singlewindow  import *

root = Tk() 

window.show(root)   

root.geometry('1300x650+90+90')

from PIL import Image,ImageTk

#bitmp参数和image参数不能共存，如果发生这种情况，bitmap参数不起作用
lbl =Label(root,bitmap='error',width=630,height=550)
lbl.pack(side=LEFT)
lbl2 =Label(root,bitmap='error',width=630,height=550)
lbl2.pack(side=LEFT,padx=20)
 
#目录下图像文件列表 
rootdir = r'images\jpg'
imagelist = os.listdir(rootdir) 
max1 = len(imagelist)
max2= max1//2
index1,index2=0,max2 


def run():  
    global index1,index2
    img1 = ImageTk.PhotoImage(Image.open(rootdir+'\\'+imagelist[index1])) 
    img2 = ImageTk.PhotoImage(Image.open(rootdir+'\\'+imagelist[index2])) 

    #暂时还未有设置图片的狂傲resize
    lbl.configure(image = img1)
    lbl2.configure(image = img2)
    lbl.image=img1                      #keep a reference
    lbl2.image=img2                     #keep a reference
    index1+=1
    index2+=1
    if index1==max2:
        index1=0
    if index2==max1:
        index2=max2

    global task 
    #开启定时循环   
    task = root.after(500,run)

def stop():
    #关闭定时循环
    root.after_cancel(task)

btn1 = Button(text="开启轮播",command=run)
btn2 = Button(text="停止轮播",command=stop)

btn1.place(x=580, y=610, anchor=NW)
btn2.place(x=650, y=610, anchor=NW)

#root.resizable(width = False, height = False) or resizable(0,0)
#或简单些，直接： 意思是窗口的大小在水平方向和垂直方向上都不能改变
root.resizable(False, False)
root.mainloop() 