from tkinter import *
from tkinter.ttk import *
from PIL import Image,ImageTk

def treeSelect(event):
    e = event.widget                        #取得控件
    itemselected = e.selection()[0]         #取得选项，通常也可称此所选的项目是iid，这是tkinter内部使用的id,调试可看出为I001,I002,I003....之类的格式
    #调用控件对象的Item方法
    col1 = e.item(itemselected,"text")      #取得图标栏内容 
    lw =  e.item(itemselected,'values')     #获取栏目内容
    if lw != '':
        col2 = lw[0]                        #取得第0索引栏位内容
        #str.format()，它增强了字符串格式化的功能。 
        #基本语法是通过 {} 和 : 来代替以前的 % 。 
        #format 函数可以接受不限个参数，位置可以不按顺序。
        #"{} {}".format("hello", "world")           # 不设置指定位置，按默认顺序
        #"{0} {1}".format("hello", "world")         # 设置指定位置
        #"{1} {0} {1}".format("hello", "world")     # 设置指定位置
        str = "{0},{1}".format(col2,col1)
        var.set(str)

root = Tk()
root.title('Select选项发生与事件触发')
root.geometry('800x650+400+30')

Style().configure('Treeview',rowheight=60) #格式化扩充row高度

#建立Treeview组件
#show = "tree", 第一列也会被显示出来
#也可用show = "headings" 把第一列隐藏起来 
tree = Treeview(root,column=('cities','populations'),selectmode=BROWSE)

#建立栏目标题
tree.heading('#0',text='品牌')
tree.heading('#1',text='国家')
tree.heading('#2',text='价格（万元）')

#建立id
id1 = tree.insert('',index=END,text='英国')
id2 = tree.insert('',index=END,text='德国')
id3 = tree.insert('',index=END,text='意大利')

#格式化栏位 
tree.column('#1',anchor=CENTER,width=250,minwidth=150)
tree.column('#2',anchor=CENTER,width=150)

#格式栏位
tree.tag_configure('evenColor',background='lightblue')   #设置标签 

#可以用元组或者列表方式设置栏目内容
t1 = ('意大利','800')
t2 = ['英国','4800']
t3 = ['意大利','3800']
t4 = ('德国','2800')
t5 = ('意大利','5800')
t6 = ('英国','6800')

#建立内容
#插入图像：需要考虑可能row的高度不足，必须增加高度
img1 = Image.open(r'images\ico\Alfa Romeo.ico') 
imgObj1 = ImageTk.PhotoImage(img1.resize((50, 50), Image.ANTIALIAS) )
tree.insert(id3,index=END,text="阿尔法罗密欧",image=imgObj1,values=t1,tags='evenColor')

img2 = Image.open(r'images\ico\Bugatti.ico')
imgObj2 = ImageTk.PhotoImage(img2.resize((50, 50), Image.ANTIALIAS) )
tree.insert(id1,index=END,text="布加迪",image=imgObj2,values=t2)

img3 = Image.open(r'images\ico\Ferrari.ico')
imgObj3 = ImageTk.PhotoImage(img3.resize((50, 50), Image.ANTIALIAS) )
tree.insert(id3,index=END,text="法拉利",image=imgObj3,values=t3)

img4 = Image.open(r'images\ico\Lamborghini.ico')
imgObj4 = ImageTk.PhotoImage(img4.resize((50, 50), Image.ANTIALIAS) )
tree.insert(id2,index=END,text="兰博基尼",image=imgObj4,values=t4)

img5 = Image.open(r'images\ico\Louts.ico')
imgObj5 = ImageTk.PhotoImage(img5.resize((50, 50), Image.ANTIALIAS) )
tree.insert(id3,index=END,text="路易斯",image=imgObj5,values=t5,tags='evenColor')

img6 = Image.open(r'images\ico\Maserati.ico')
imgObj6 = ImageTk.PhotoImage(img6.resize((50, 50), Image.ANTIALIAS) )
tree.insert(id1,index=END,text="玛莎拉蒂",image=imgObj6,values=t6,tags='evenColor')

#事件绑定
tree.bind('<<TreeviewSelect>>',treeSelect)              #Treeview控件Select事件发生
tree.pack(fill=BOTH,expand=TRUE,side=TOP,padx=10)

var = StringVar()
lbl = Label(root,textvariable=var,relief='groove')      #建立状态栏
lbl.pack(fill=BOTH,expand=True,side=BOTTOM,padx=10)

#以字典方式列出栏位的所有内容
print('cities:%r\npopulations:%r\n'%( tree.column('cities'), tree.column('populations')))

root.mainloop()