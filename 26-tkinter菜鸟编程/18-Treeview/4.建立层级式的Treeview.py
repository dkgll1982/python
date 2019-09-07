from tkinter import *
from tkinter.ttk import *

root = Tk()
root.title('建立层级式的Treeview')
root.geometry('700x300+400+100')

#建立Treeview组件
#show = "tree", 第一列也会被显示出来
#也可用show = "headings" 把第一列隐藏起来 
tree = Treeview(root,column=('cities','populations'))

#建立栏目标题
tree.heading('#0',text='城市')
tree.heading('#1',text='区域')
tree.heading('#2',text='人均收入')

#建立id
id1 = tree.insert('',index=END,text='一线沿海')
id2 = tree.insert('',index=END,text='二线省会')
id3 = tree.insert('',index=END,text='三线市县')

#格式化栏位 
tree.column('#1',anchor=CENTER,width=250,minwidth=150)
tree.column('#2',anchor=CENTER,width=150)

#格式栏位
tree.tag_configure('evenColor',background='lightblue')   #设置标签 

#可以用元组或者列表方式设置栏目内容
t1 = ('黄陂','800')
t2 = ['洛阳','4800']
t3 = ['江都','3800']
t4 = ('长兴','2800')
t5 = ('玄武','5800')
t6 = ('昌平','6800')

#建立内容
tree.insert(id2,index=END,text='武汉',values=t1)
tree.insert(id3,index=END,text='随州',values=t2,tags=('evenColor'))
tree.insert(id3,index=END,text='扬州',values=t3)
tree.insert(id3,index=END,text='湖州',values=t4,tags=('evenColor'))
tree.insert(id2,index=END,text='南京',values=t5)
tree.insert(id1,index=END,text='北京',values=t6,tags=('evenColor'))

tree.pack()

#以字典方式列出栏位的所有内容
print('cities:%r\npopulations:%r\n'%( tree.column('cities'), tree.column('populations')))

root.mainloop()