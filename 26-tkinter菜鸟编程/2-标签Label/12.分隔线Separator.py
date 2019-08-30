from tkinter import *  
from tkinter import ttk

# 引入字体模块
import tkinter.font as tkFont
import sys,os  
sys.path.append(os.path.dirname(os.path.dirname(__file__)) )   
from singlewindow  import *

root = Tk() 
window.show(root)  

myTitle = '一个人的极境旅行'
myContent = '''一个人的旅行，你会恍然发现，世界真的很奇妙，你真的很勇敢。其实，没有你做不到的事情，只有你不敢去做的事情。这个世界真的很大，翻山越岭后你才会知道山的那边还是山。这个世界也很巧，巧得我们都有同一个浪迹天涯的梦想。

1、 人生，需要一场说走就走的旅行。

2、 这里的风景美不胜收，真让人流连忘返。

3、 如果你不出去走走，你就会以为这就是世界。

4、 一辈子是场修行，短的是旅行，长的是人生。

5、 当遗忘变成另一种开始，我踏出了旅途的第一步！'''

lbl = Label(root,text = myTitle,font ="Helvetic 20 bold")
lbl.pack(padx=10,pady=10)

sep = ttk.Separator(root,orient = HORIZONTAL)
sep.pack(fill=X,padx=5)

lbl = Label(root,text = myContent,wraplength=760,width=1000,justify='left')
lbl.pack(padx=10,pady=10) 

root.mainloop()