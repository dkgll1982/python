
#显示手柄和分割线
from tkinter import *
from tkinter import ttk
 
#设置分割线的样式

#默认值是FLAT

#另外你还可以设置SUNKEN，RAISED，GROOVED或RIDGE 
m1 = PanedWindow(showhandle=True, sashrelief=RIDGE ,handlepad=23,handlesize=23,sashwidth=9)  #默认是左右分布的
m1.pack(fill=BOTH, expand=1)
 
left = Label(m1, text='left pane')
m1.add(left)
 
#窗格的分布方式：HORIZONTAL（横向分布）和VERTICAL（纵向分布） 
m2 = PanedWindow(orient=VERTICAL, showhandle=True, sashrelief=RAISED,handlepad=43,handlesize=33)
m1.add(m2)
 
top = Label(m2, text='top pane')
m2.add(top)

center = Label(m2, text='center pane')
m2.add(center)
 
bottom = Label(m2, text='bottom pane') 
#before:添加新的子组件到指定子组件前边
m2.add(bottom,height=81,width=200,minsize=100,before=top)

#--删除一个子组件
m2.forget(center)
#m2.remove(center)

#重新添加自组件
m2.add(center)

print("bottom-before:",m2.panecget(bottom,'before'))
print("bottom-height:%d,maxsize:%d"%(m2.panecget(bottom,'height'),m2.panecget(bottom,'minsize'))) 

print('identify坐标所在的组件:',m2.identify(111,211))

mainloop()
#分割线上的类似正方形的东西就是handle 

'''
参数
PanedWindow(master=None, **options)(class)
master--父组件

**options--组件选项，下方详细列举了各个选项的具体含义和用法

选项	含义
background	设置背景颜色
bg	跟background一样
borderwidth	设置边框宽度
bd	跟borderwidth一样
cursor	
指定当鼠标在PanedWindow上飘过的时候的鼠标样式

默认值由系统指定

handlepad	
调节“手柄”的位置

例如orient=VERTICAL，则handlepad选项表示“分割线”上的手柄与左端的距离

默认值是8像素

handlesize	
设置“手柄”的尺寸（由于“手柄”必须是一个正方形，所以是设置正方形的边长）

默认值是8像素

height	
设置PanedWindow的高度

如果忽略该选项，则高度由子组件的尺寸决定

opaqueresize	
该选项定义了用户调整窗格尺寸的操作

如果该选项的值为True（默认），窗格的尺寸随用户鼠标的拖拽而改变

如果该选项的值为False，窗格的尺寸在用户释放鼠标的时候才更新到新的位置

orient	
指定窗格的分布方式

可以是HORIZONTAL（横向分布）和VERTICAL（纵向分布）

relief	
指定边框样式

默认值是FLAT

另外你还可以设置SUNKEN，RAISED，GROOVED或RIDGE

sashpad	设置每一条分割线到窗格间的间距
sashrelief	
设置分割线的样式

默认值是FLAT

另外你还可以设置SUNKEN，RAISED，GROOVED或RIDGE

sashwidth	设置分割线的宽度
showhandle	
设置是否显示调节窗格的手柄

默认值为False

width	
设置PanedWindow的宽度

如果忽略该选项，则高度由子组件的尺寸决定

 

方法
add(child, **options)
--添加一个新的子组件到窗格中

--下方表格列举了各个 options 选项的具体含义

选项	含义
after	添加新的子组件到指定子组件后边
before	添加新的子组件到指定子组件前边
height	指定子组件的高度
minsize	
该选项控制窗格不得低于的值

如果orient=HORIZONTAL，表示窗格的宽度不得低于该选项的值

如果orient=VERTICAL，表示窗格的高度不得低于该选项的值

padx	指定子组件的水平间距
pady	指定子组件的垂直间距
sticky	
当窗格的尺寸大于子组件时，该选项指定子组件位于窗格的位置

可选的值有：E、S、W、N（东南西北）以及他们的组合值

width	指定子组件的宽度
 

forget(child)
--删除一个子组件

 

identify(x, y)
--给定一个坐标 (x, y)，返回该坐标所在的元素名称

--如果该坐标位于子组件上，返回空字符串

--如果该坐标位于分割线上，返回一个二元组 (n, 'sash')，n 为 0 表示第一个分割线

--如果该坐标位于手柄上，返回一个二元组 (n, 'handle')，n 为 0 表示第一个手柄

 

panecget(child, option)
--获得子组件指定选项的值

 

panecget(child, option)
--获得子组件指定选项的值

 

paneconfig(child, **option)
--设置子组件的各种选项

--下面列举了各个 options 选项具体含义

after：添加新的子组件到指定子组件后边

before：添加新的子组件到指定子组件前边

height：指定子组件的高度 

'''