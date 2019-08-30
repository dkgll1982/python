import threading
from tkinter import *  
# 引入字体模块
import tkinter.font as tkFont
import sys,os  
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))   
from singlewindow  import *

root = Tk() 
var = StringVar()

index = 0

slist ={    \
    "top":"默认值,由上往下排列", \
    "bottom":"由下往上排列", \
    "left":"由左往右排列",   \
    "right":"由右往左排列"
    }

var.set("当前label标签的布局：pack(side=%s)『%s』"%('top',slist["top"]))
window.show(root)   

frm = Frame(root,height=300,bg='LIGHTPINK')
frm.pack(fill=X)
 
lbl1 = Label(frm,text="①华中科技大学",bg = 'lightyellow',height=2,width=20) 
lbl2 = Label(frm,text="②武汉大学",bg = 'lightgreen',height=2,width=20) 
lbl3 = Label(frm,text="③中南财经大学中南校区",bg = 'lightblue',height=2,width=20) 
lbl4 = Label(frm,text="④华中农业大学",bg = 'PowderBlue',height=2,width=20) 
lbl5 = Label(frm,text="⑤湖北财经商贸大学",bg = 'Salmon',height=2,width=20) 

lbl1.pack(pady=3,padx =5)
lbl2.pack(pady=3,padx =5)
lbl3.pack(pady=3,padx =5)
lbl4.pack(pady=3,padx =5) 
lbl5.pack(pady=3,padx =5)


lbl6 = Label(root,textvariable=var,fg='red',bg='lightyellow')
lbl6.pack(fill=X,padx=5,pady=5)

def changeside():
    global index
    index=index+1
    di = 'top'
    if index==1:
        di = 'bottom'
    if index==2:
        di = 'left'
    if index==3:
        di = 'right'
    if index==4:       #==两个等号是判断是否相等，一个等号代表的含义是赋值
        di = 'top'
        index=0    
    for lbl in (lbl1,lbl2,lbl3,lbl4,lbl5):
        lbl.pack(side = di)
        
        var.set("当前label标签的布局：pack(side=%s)『%s』"%(di,slist[di]))

btn = Button(root,text="改变side位置",command=changeside)
btn.pack(pady=5)

root.mainloop() 