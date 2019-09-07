from tkinter import *

fruits = ["芒果",'苹果','香蕉',]

root = Tk()
root.title('删除指定索引项')
root.geometry('350x250')

#lb = Listbox(root,selectmode=MULTIPLE)      #建立可以多选项的listbox
lb = Listbox(root,selectmode=EXTENDED)       #可以用拖拽的方式选择区间多个项目

for fruit in fruits:
    lb.insert(END,fruit)

lb.insert(ACTIVE,'桔子','菠萝','椰子','榴莲','山竹')   

# 顺序依次：'桔子','菠萝','椰子','榴莲','山竹'，"芒果",'苹果','香蕉'
lb.pack(pady=10) 
#删除区间元素
lb.delete(1,2) 
lb.delete(4,6) 
# 第一次删除后：'桔子','榴莲','山竹'，"芒果",'苹果','香蕉'
# 第二次删除后：'桔子','榴莲','山竹'，"芒果"

#size：传回列表项目的数量
#curselection：传回选取项目的索引
print('Listbox选项的数量：%d，当前选中的数量：%s,分别选中的是第%s项'%(lb.size(),len(lb.curselection()),lb.curselection()))
root.mainloop()
