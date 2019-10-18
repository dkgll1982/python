import threading
from tkinter import *  
# 引入字体模块
import tkinter.font as tkFont
import sys,os  
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))   
from singlewindow  import *

root = Tk()   
window.show(root)    

# sticky=W表示label需要贴着西面(左侧)
# N/S/E/W，分别代表上对齐/下对齐/左对齐/右对齐，可以单独使用N/S/E/W，也可以上下和左右组合使用，达到不同的对齐效果

# sticky=N/S/E//W:顶端对齐/底端对齐/右对齐/左对齐
# sticky=N+S：拉伸高度，使其在水平方向上顶端和底端都对齐
# sticky=E+W，拉伸宽度，使其在垂直方向上左边界和右边界都对齐
# sticky=N+S+E:拉伸高度，使其在水平方向上对齐，并将控件放在右边（当两个控件放在同一行同一列时效果明显）

# padx 设置文本与按钮边框x的距离，还有pady;
lbl1 = Label(root,text="明志工专",relief='raised', anchor='w',padx=8)  #指定按钮上文本的位置
lbl2 = Label(root,bg="yellow",width=20)
lbl3 = Label(root,text="武汉科技大学")
lbl4 = Label(root,bg="aqua",width=20,pady=15) 
lbl5 = Label(root,text="理工大", anchor='e',padx=6)
lbl6 = Label(root,bg="pink",width=20) 

lbl1.grid(row=0,column=0,padx=5,pady=5 ) 
lbl2.grid(row=0,column=1,padx=5,pady=5) 
lbl3.grid(row=1,column=0,padx=5)  
lbl4.grid(row=1,column=1,padx=5)   
lbl5.grid(row=2,column=0,padx=5,pady=5,sticky=W+E)
lbl6.grid(row=2,column=1,padx=5,pady=5)  

root.mainloop()