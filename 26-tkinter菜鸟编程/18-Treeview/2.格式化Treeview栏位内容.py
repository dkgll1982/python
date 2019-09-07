from tkinter import *
from tkinter.ttk import *

root = Tk()
root.title('格式化Treeview栏位内容')
root.geometry('700x300+400+100')

#建立Treeview组件
#show = "tree", 第一列也会被显示出来
#也可用show = "headings" 把第一列隐藏起来 
tree = Treeview(root,column=('cities','populations'))

#建立栏目标题
tree.heading('#0',text='State')
tree.heading('#1',text='City')
tree.heading('#2',text='populations')

#格式化栏位 
tree.column('#1',anchor=W,width=250,minwidth=150)
tree.column('#2',anchor=E,width=150)
#可以用元组或者列表方式设置栏目内容
t1 = ('黄陂','800')
t2 = ['洛阳','4800']
t3 = ['江都','3800']
t4 = ('长兴','2800')
t5 = ('玄武','5800')
t6 = ('昌平','6800')

#建立内容
tree.insert("",index=END,text='武汉',values=t1)
tree.insert("",index=END,text='随州',values=t2)
tree.insert("",index=END,text='扬州',values=t3)
tree.insert("",index=END,text='湖州',values=t4)
tree.insert("",index=END,text='南京',values=t5)
tree.insert("",index=END,text='北京',values=t6)

tree.pack()

#以字典方式列出栏位的所有内容
print('cities:%r\npopulations:%r\n'%( tree.column('cities'), tree.column('populations')))

root.mainloop()