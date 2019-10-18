from tkinter import *
from tkinter import ttk 

root = Tk()
root.geometry('400x300+300+200')
style = ttk.Style() 
 
#获取所有支持的主题
print(style.theme_names())  
#获取当前使用的主题
print(style.theme_use())

var =StringVar()
var.set('按钮的风格：'+style.theme_use())

index = 0
def set_theme():
    global index
    #切换主题
    style.theme_use(themename=style.theme_names()[index])
    var.set('按钮的风格：'+style.theme_names()[index])
    #获取当前使用的主题
    print("当前主题切换为：%s"%style.theme_use())
    index+=1
    if index>6:
        index=0

ttk.Button(root,text='按钮',command=set_theme,width=12).pack()  
ttk.Label(root,textvariable=var).pack()  

root.mainloop();