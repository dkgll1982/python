from tkinter import *

def cal():
    out.config(text="结果："+str(eval(entry.get())))

root = Tk()
root.geometry('200x120+400+100')

lb = Label(root,text='请输入数学表达式')
lb.pack()

entry = Entry(root)
entry.pack(pady=5)

out =Label(root)
out.pack()

btn =Button(root,text='计算',command=cal)
btn.pack()

root.mainloop()