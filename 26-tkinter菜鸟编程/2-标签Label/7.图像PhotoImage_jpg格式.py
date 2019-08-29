
from tkinter import *  
# 引入字体模块
import tkinter.font as tkFont
import sys,os  
sys.path.append(os.path.dirname(os.path.dirname(__file__)) )   
from singlewindow  import *

root = Tk() 

window.show(root)   

root.geometry('1300x600+90+90')

# 早期的图片只支持gif文件格式，目前已经可以支持png格式了
img1 = PhotoImage(file=r'images\miaomiao.png')  

from PIL import Image,ImageTk

jpg = Image.open(r'images\jpg\timg.jpg')
img2 = ImageTk.PhotoImage(jpg)

lbl =Label(root,image=img1,width=630,height=550)
lbl.pack(side=LEFT)
lbl2 =Label(root,image=img2,width=630,height=550)
lbl2.pack(side=LEFT,padx=20)



root.mainloop()