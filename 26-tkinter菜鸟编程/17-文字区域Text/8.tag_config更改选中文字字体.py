from tkinter import *
from tkinter.ttk import *
from tkinter.font import Font

root = Tk()
root.title('更改选中文本字体')
root.geometry('500x400+600+150')

#Tags通常用于改变Text组件中内容的样式和功能，你可以修改文本的字体，尺寸和颜色。 另外Tags还允许你将文本、嵌入的组件和图片与键盘相关联，
# 除了user-defined tags(用户自定义的Tags)，还有一个预定义的特殊Tag：SEL
def sizeSelected(event): 
    f = Font(size=sizeVar.get()) 
    text1.tag_config(SEL,
                    font=f,
                    background='pink',
                    foreground='red',
                    underline=True
    )

#建立工具栏
toolbar = Frame(root,relief=RAISED,borderwidth=1)
toolbar.pack(side=TOP,fill=X,padx=2,pady=1)

#建立font size combobox
sizeVar = IntVar()
size = Combobox(toolbar,textvariable=sizeVar)
sizeFamliy = [x for x in range(8,30)]
size['value']=sizeFamliy
size.current(4)
size.bind('<<ComboboxSelected>>',sizeSelected)
size.pack() 

#字符串换行
txt1 = '小时候，总常常幻想着自己可以长大，可以独自一人去领略更多优美的风光。我们这一生，会有太多太多的梦想，要么就是用尽\
全力去实现他，要么就是永远沉积在自己的心中。我喜欢旅行，向往美丽的山、美丽的水，一见到大海和草原我就会心旷神怡，深陷其中。\
我期盼可以带着自己最爱的人去遨游世界，让他给自己拍上几张美美的照片。我想要开车或者走路去穿过每一个平淡的日子，只需要喜欢的\
人陪在身边，不谈什么理想目标，心中只有诗和远方。生活其实可以如此的平淡如此的美好，只需要有个人来陪着你一起记录。所以这就是\
最真实的。可能是缘分吧，我这一生注定过着漂泊的日子。幼年时期，因为各个方面的原因，我开始了我每天辛苦漂泊的日子，早就厌倦了\
这种生活。'

txt2='''

我以为长大后我会找一份稳定的工作，
在一个安静的环境里喝着一口清茶，
读上三两本书，
认真的过完这一生。
知道我真的成长了起来，
才发现这样的生活已经按捺不住我内心的浮躁，
所以我就决定，
这就是我再一次踏上征程的时候了。
于是，我就背上自己的小包，
装着我的期待，
一个人懵懵懂懂的踏上征途，
去看看这人人口中精彩的世界，
看看远方的太阳是不是更加的明媚。

'''

txt3='''经历过无数个日日夜夜，
白云日落沧海桑田，
这两年多的行程中，
我从出生的小草地走到了花海中，
从山涧穿越到了沙漠，
从大海游荡到平川。
这一路下来，
仿佛自己的心已经变年轻了十岁，
但是容颜却逝去。
我不敢确定我还会走多远的路，
还有走多久。
我很喜欢的一个诗人冰岛就写过这样的诗：
那时我们有梦,
关于文学，
关于爱情,
关于穿越世界的旅行。'''

#想显示X轴的滚动条必须设置warp='none'
text1 = Text(root,width=150,height=200,bg='lightgreen',fg='blue',padx=5,pady=5,wrap='none')

family = ("隶书","宋体","幼圆","隶书","楷体","魏碑","微软雅黑") 

init_font = Font(family=family[0],size=size.get())

#设置文本的初始字体为菜单列表默认选中的字体
text1.config(font=init_font)

#垂直滚动条
yscroll = Scrollbar(root,orient=VERTICAL)
yscroll.pack(side=RIGHT,fill=Y)             #窗口Y轴填满

#水平滚动条
xscroll = Scrollbar(root,orient=HORIZONTAL)
xscroll.pack(side=BOTTOM,fill=X)            #窗口底部X轴填满

xscroll.config(command=text1.xview)
text1.config(xscrollcommand=xscroll.set)

yscroll.config(command=text1.yview)
text1.config(yscrollcommand=yscroll.set)

#pack布局：注意先后顺序，此组件铺满除BOTTOM(xscroll)，RIGHT(yscroll)的剩余空间
text1.pack(fill=BOTH,expand=True)           #当窗口放大或缩小时，仍然随整个窗口铺满
#在结尾处添加文本内容
text1.insert(END,txt1)
text1.insert(END,'\r\n')
text1.insert(END,txt2)
text1.insert(END,'\r\n')
text1.insert(END,txt3)

text1.focus_set()       #设置什么控件获取到焦点，可以看到一个'|'标记在一闪一闪，一般我们用tab键能够切换焦点

root.mainloop()