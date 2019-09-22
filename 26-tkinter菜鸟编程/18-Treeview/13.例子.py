import tkinter
from tkinter import ttk

win = tkinter.Tk()
win.title("yudanqu")
win.geometry("400x400+200+50")

tree = ttk.Treeview(win,show='tree')
tree.pack()

# 添加一级树枝,第一个参数值为空表示根节点
treeF1 = tree.insert("",0,"中国",text= "中国Chi", values=("F1"))
treeF2 = tree.insert("",1,"美国",text= "美国USA", values=("F1"))
treeF3 = tree.insert("",2,"英国",text= "英国UK", values=("F1"))

# 二级树枝
treeF1_1 = tree.insert(treeF1,0,"黑龙江",text="中国黑龙江",values=("F1_1"))
treeF1_2 = tree.insert(treeF1,1,"吉林",text="中国吉林",values=("F1_2"))
treeF1_3 = tree.insert(treeF1,2,"辽宁",text="中国辽宁",values=("F1_3"))

treeF2_1 = tree.insert(treeF2,0,"华盛顿",text="华盛顿",values=("F2_1"))
treeF2_2 = tree.insert(treeF2,1,"纽约",text="纽约",values=("F2_2"))
treeF2_3 = tree.insert(treeF2,2,"底特律",text="底特律",values=("F2_3"))

# 三级树枝
treeF1_1_1 = tree.insert(treeF1_1,0,"哈尔滨",text="黑龙江哈尔滨")
treeF1_1_2 = tree.insert(treeF1_1,1,"五常",text="黑龙江五常")

win.mainloop()