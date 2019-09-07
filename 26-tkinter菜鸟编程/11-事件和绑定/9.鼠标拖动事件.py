
#鼠标事件

# <ButtonPress-n>     <Button-n>      <n>                         鼠标按钮n被按下，n为1左键，2中键，3右键
# <ButtonRelease-n>                                               鼠标按钮n被松开
# <Double-Button-n>                                               鼠标按钮n被双击
# <Triple-Button-n>                                               鼠标按钮n被三击
# <Motion>                                                        鼠标被按下，同时，鼠标发生移动
# <Bn-Motion>                                                     鼠标按钮n被按下，同时，鼠标发生移动
# <Enter>                                                         鼠标进入
# <Leave>                                                         鼠标离开
# <MouseWheel>                                                    鼠标滚轮滚动

#键盘事件
# <Any-KeyPress>      <KeyPress>      <Key>                       任意键按下
# <KeyRelease>                                                    任意键松开
# <KeyPress-key>      <Key-key>       <key>                       特定键按下
# <KeyRelease-key>                                                特定键松开
# <Control-Shift-Alt-KeyPress-key>    <Control-Shift-Alt-key>     组合键按下（Alt，Shift，Control任选一到三个）

import tkinter

win = tkinter.Tk()
win.title("鼠标拖动事件")
win.geometry("800x600+600+100")

#<B1-Motion> 拖动左键触发事件
#<B2-Motion> 拖动中键触发事件
#<B3-Motion> 拖动右键触发事件

label=tkinter.Label(win,text="red orange yellow green cyan blue violet拖动鼠标打印",height=3,width=50,bg='lightblue')
label.pack()
def func(event):
    print(event.x,event.y)
label.bind("<B1-Motion>",func)

win.mainloop()
