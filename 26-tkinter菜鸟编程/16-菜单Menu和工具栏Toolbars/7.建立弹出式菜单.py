from tkinter import *
from tkinter import messagebox

#deiconify()
#--显示窗口
#--默认情况下新创建的窗口都会显示在屏幕上，但是用iconify()或withdraw()方法可以在屏幕上移除窗口
def minimizeIcon():
    root.iconify()              #缩小窗口为图标

def showPopumenu(event):
    popumenu.post(event.x_root,event.y_root)

root = Tk()
root.title('弹出式菜单')
root.geometry('300x100')

popumenu = Menu(root,tearoff = False)
#在弹出式菜单内建立两个指令列表
popumenu.add_command(label='Minimize',command=minimizeIcon)
popumenu.add_command(label='Exit',command=root.destroy)
#单击鼠标右键绑定显示弹出菜单
root.bind('<Button-3>',showPopumenu)

#显示菜单对象(此方法是显示在窗口顶部)
root.configure(menu=popumenu)

root.mainloop()