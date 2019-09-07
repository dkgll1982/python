from tkinter import *
from tkinter.ttk import *

def treeview_sortColumn(col):
    global reverFlag                            #定义排序排序标识全局变量
    lst = [(tree.set(st,col),st)                
            for st in tree.get_children("")]
    print(lst)                                  #打印列表
    lst.sort(reverse=reverFlag)                 #排序列表
    print(lst)                                  #打印列表
    for index,item in enumerate(lst):           #重新移动排序项目
        tree.move(item[1],"",index)           

    reverFlag = not reverFlag                   #更改排序标识符

root = Tk()
root.title('排序')

reverFlag  = False

myStates = {"illinois","california",'Texas',"Washington","Jiangsu","shandong",'GuangDong'}
tree = Treeview(root,columns=('states'),show='headings')
yscrollbar = Scrollbar(root)
yscrollbar.pack(side=RIGHT,fill=Y)
tree.pack()

yscrollbar.config(command=tree.yview)
tree.config(yscrollcommand=yscrollbar.set)

tree.heading('states',text='State')

for state in myStates:
    tree.insert('',index=END,values=(state,))

tree.heading('#1',text='State',command=lambda c="states":treeview_sortColumn(c))

root.mainloop()
