from tkinter import *
# 导入ttk
from tkinter import ttk
class App:
    def __init__(self, master):
        self.master = master
        self.initWidgets()
    def initWidgets(self):
        # 创建第一个Text组件
        text1 = Text(self.master, height=27, width=32)
        # 创建图片
        book = PhotoImage(file=r'backup\image\2-1Z226140142564.png')
        text1.bm = book
        text1.insert(END,'\n')
        # 在结尾处插入图片
        text1.image_create(END, image=book)
        text1.pack(side=LEFT, fill=BOTH, expand=YES)
        # 创建第二个Text组件
        text2 = Text(self.master, height=33, width=50)
        text2.pack(side=LEFT,  fill=BOTH, expand=YES)
        self.text = text2
        # 创建Scrollbar组件，设置该组件与text2的纵向滚动关联
        scroll = Scrollbar(self.master, command=text2.yview)
        scroll.pack(side=RIGHT, fill=Y)
        # 设置text2的纵向滚动影响scroll滚动条
        text2.configure(yscrollcommand=scroll.set)
        # 配置名为title的样式
        text2.tag_configure('title', font=('楷体', 20, 'bold'),
            foreground='red', justify=CENTER, spacing3=20)
        text2.tag_configure('detail', foreground='darkgray',
            font=('微软雅黑', 11, 'bold'),
            spacing2=10, # 设置行间距
            spacing3=15) # 设置段间距
        text2.insert(END,'\n')
        # 插入文本内容，设置使用title样式
        text2.insert(END,'C语言中文网\n', 'title')
        # 创建图片
        star = PhotoImage(file=r'backup\image\2-1Z226140142564.png')
        text2.bm = star
        details = ('C语言中文网成立于 2012 年初，目前已经运营了将近 5 年，' +\
            '我们致力于分享精品教程，帮助对编程感兴趣的读者。\n' ,
        '我们一直都在坚持的是：认认真真、一丝不苟、以工匠的精神来打磨每一套教程，让读者感受到作者的用心，以及默默投入的时间，由衷地心动和点赞。\n',
        '这样的教程是一件作品，而不是呆板的文字！\n')
        # 采用循环插入多条介绍信息
        for de in details:
            text2.image_create(END, image=star)
            text2.insert(END, de, 'detail')
        url =['http://vip.biancheng.net/','http://c.biancheng.net/']
        name =['VIP会员', 'C语言中文网']
        m=0
        for each in name:
            # 为每个链接创建单独的配置
            text2.tag_configure(m, foreground='blue', underline=True,
                font=('微软雅黑', 13, 'bold'))
            text2.tag_bind(m, '<Enter>', self.show_arrow_cursor)
            text2.tag_bind(m, '<Leave>', self.show_common_cursor)
            # 使用handlerAdaptor包装,将当前链接参数传入事件处理函数
            text2.tag_bind(m, '<Button-1>', self.handlerAdaptor(self.click, x = url[m]))
            text2.insert(END, each + '\n', m)
            m += 1
    def show_arrow_cursor(self, event):
        # 光标移上去时变成箭头
        self.text.config(cursor='arrow')
    def show_common_cursor(self, event):
        # 光标移出去时恢复原样
        self.text.config(cursor='xterm')
    def click(self, event, x):
        import webbrowser
        # 使用默认浏览器打开链接
        webbrowser.open(x)
    def handlerAdaptor(self, fun,**kwds):
        return lambda event, fun=fun, kwds=kwds: fun(event,**kwds)
root = Tk()
root.title("Text测试")
App(root)
root.mainloop()