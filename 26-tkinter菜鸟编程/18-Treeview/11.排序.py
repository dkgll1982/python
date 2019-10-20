from tkinter import *
from tkinter.ttk import *

def treeview_sortColumn(col):
    global reverFlag                            #定义排序排序标识全局变量

    st =  tree.get_children("")                 #得到item的元组，如('I001', 'I002', 'I003', 'I004', 'I005', 'I006', 'I007') 
    print('col:%s,st:%r,st[0]:%s'%(col,st,st[0]))
    print('*'*20)
    print([(tree.set(st[0],col),st[0]),
        (tree.set(st[1],col),st[1]),
        (tree.set(st[2],col),st[2]),
        (tree.set(st[3],col),st[3]),
        (tree.set(st[4],col),st[4]),
        (tree.set(st[5],col),st[5]),
        (tree.set(st[6],col),st[6])])
    lst = [(tree.set(st,col),st)                
            for st in tree.get_children("")]
    print('*'*20)
    print(lst)                                  #打印列表
    lst.sort(reverse=reverFlag)                 #排序列表
    print('*'*20)
    print(list(enumerate(lst)))                       #打印列表
    for index,item in enumerate(lst):           #重新移动排序项目
        print('index:%r,item:%r'%(index,item))
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
