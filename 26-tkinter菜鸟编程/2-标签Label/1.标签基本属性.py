
from tkinter import *  
# 引入字体模块
import tkinter.font as tkFont
import sys,os 
 
# __file__ 为当前文件
curr_dir = os.path.dirname(__file__)  #返回当前文件所在的目录  
#获得curr_dir所在的目录,即curr_dir的父级目录   
parent_dir = os.path.dirname(curr_dir) 
sys.path.append(parent_dir)   

#sys.path.append(os.path.dirname(os.path.dirname(__file__)))   
from singlewindow  import *

root = Tk()
window.show(root) 

#设置字体
font = tkFont.Font(family='Fixdsys', 
    size=16, 
    weight=tkFont.BOLD,         #加粗
    slant=tkFont.ITALIC,        #斜体
    underline=True,             #下划线
    overstrike=True             #删除线
)

# justify与anchor的区别：
# justify用于控制多行的对齐；
# anchor用于控制整个文本块在Label中的位置

#compound 选项支持如下属性值：
#None：图片覆盖文字。默认值
#LEFT 常量（值为‘left’字符串）：图片在左，文本在右。
#RIGHT 常量（值为‘right’字符串）：图片在右，文本在左。
#TOP 常量（值为‘top’字符串）： 图片在上，文本在下。
#BOTTOM 常量（值为‘bottom’字符串）：图片在底，文本在上。
#CENTER 常量（值为‘center’字符串）：文本在图片上方。\

#需要指定image或者bitmap属性，然后再使用width, height来控制。
#默认的Label、button是text类型, width, heigth表示字符个数和行数，指定image或者bitmap属性后，意义就从字符数变成像素。
lbl = Label(root,
    text = "I love tkinter",
    fg = "blue",
    bg = "yellow",
    height = 156,               #字符高度或者像素，定义image或者bitmap属性就变成像素
    width = 242,                #字符宽度或者像素，定义image或者bitmap属性就变成像素
    wraplength = 80,            #标签文字达到多少像素进行换行输出
    anchor = 'center',          #整个文本块在Label中的位置
    justify = "left",           #控制多行文本的对齐方式
    #font = font,
    bitmap="hourglass",         #图标，如hourglass 为沙漏形状的图标
    compound="bottom"
)

#增加配置管理
lbl.configure(font=font)
lbl.pack()

root.mainloop()