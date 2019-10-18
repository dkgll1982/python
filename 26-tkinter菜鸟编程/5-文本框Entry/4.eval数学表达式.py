from tkinter import *

def cal():
    out.config(text="结果："+str(eval(entry.get())))

root = Tk()
root.geometry('400x220+400+100')
root.title("计算数据表达式使用eval()")

lb = Label(root,text='输入数学表达式')
lb.pack()

# highlightthickness 这两个属性一起指定了控件如何绘制高亮区域. 
entry = Entry(root,highlightthickness=5,highlightcolor ="red")
entry.pack(pady=5)

out =Label(root)
out.pack()

btn =Button(root,text='计算',command=cal)
btn.pack()

root.mainloop()