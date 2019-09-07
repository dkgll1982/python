from  tkinter import *

root = Tk()
root.title('删除和添加列表项')

root.geometry('400x330')

def itemadd():
    varadd= ent.get().strip()       #去掉首尾两端的空格 
    if (varadd==''):
        return
    lb.insert(END,varadd)
    ent.delete(0,END)

def itemdel():
    indexs = lb.curselection()      #选中一项或多项
    #这里多选删除是有问题的，因为当删除某一项时，列表索引会重排，例如删除指定项前，在其之后某一项的索引为3，删除后，索引会变为2，故需要改写以下多选删除功能
    #for ind in indexs: 
    #    lb.delete(ind)

    #根据以上注释，调整删除逻辑(循环每次删除一个元素，后面的所有项索引均减1)
    step = 0
    for ind in indexs:   
        lb.delete(ind-step)
        step+=1

ent = Entry(root)
ent.grid(row=0,column=0,padx=5,pady=5)

btnadd = Button(root,text='增加',width=10,command=itemadd)
btnadd.grid(row=0,column=1,padx=5,pady=5)

# takefocus： 指定该组件是否接受输入焦点（用户可以通过 tab 键将焦点转移上来）， 默认值是 True
# takefocus=False,则用tab切换时焦点会跳过Listbox
# exportselection： 指定选中的项目文本是否可以被复制到剪贴板，默认值是 True， 可以修改为 False 表示不允许复制项目文本。
lb = Listbox(root,selectmode=EXTENDED,takefocus=False,exportselection=False)
lb.grid(row=1,column=0,columnspan=2,padx=5,pady=5,sticky=W)

btndel= Button(root,text='删除',width=10,command=itemdel)
btndel.grid(row=2,column=0,padx=5,pady=5,sticky=W) 

# activate(index)：-- 将给定索引号对应的选项激活（在其文本下方画一条下划线）
# 删除激活选项
btndel= Button(root,text='删除激活选项',width=10,command=lambda x=lb:x.delete(ACTIVE))
btndel.grid(row=3,column=0,padx=5,pady=5,sticky=W) 

root.mainloop()