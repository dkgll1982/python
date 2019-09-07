from tkinter import *
from tkinter import messagebox

def cutJob():
    copyJob()                                   #复制选取文字
    try:
        #Tkinter.SEL_FIRST：选中文本域的第一个字符，如果没有选中区域则会引发异常
        #Tkinter.SEL_LAST：选中文本域的最后一个字符，如果没有选中区域则会引发 异常
        text.delete(SEL_FIRST,SEL_LAST)         #删除选取文字
    except TclError:                            
        pass                                    #没有选中文本则跳过

def copyJob():
    try:
        #Tkinter.SEL_FIRST：选中文本域的第一个字符，如果没有选中区域则会引发异常
        #Tkinter.SEL_LAST：选中文本域的最后一个字符，如果没有选中区域则会引发 异常
        copyText = text.get(SEL_FIRST,SEL_LAST) #复制选取区域
        text.clipboard_clear()                  #清除剪贴板
        text.clipboard_append(copyText)         #写入剪贴板
    except TclError:
        print("没有选取")

def pasteJob():
    try:
        copyText = text.selection_get(selection='CLIPBOARD')    #读取剪贴板内容
        text.insert(INSERT,copyText)
    except TclError:
        print("剪贴板没有数据")

def showPopuMenu(event):
    # Menu 类里面有一个 post 方法，它接收两个参数，即 x 和y 坐标，它会在相应的位置弹出菜单。
    popumenu.post(event.x_root,event.y_root)

root = Tk()
root.title("剪切复制粘贴功能的例子")
root.geometry('300x200')

popumenu = Menu(root,tearoff=False) #建立弹出菜单
#在弹出菜单内建立三个命令列表(单击菜单项会触发相应事件)
popumenu.add_command(label='Cut',command=cutJob)
popumenu.add_command(label='Copy',command=copyJob)
popumenu.add_command(label='Paste',command=pasteJob)
#单击鼠标右键绑定显示弹出菜单
root.bind('<Button-3>',showPopuMenu)

#建立Text
text = Text(root)
text.pack(fill=BOTH,expand=True,padx=3,pady=2)
text.insert(END,'很多人其实都特别喜欢旅行，因为旅行对于一个人来说算得上是一种比较放松的方式了\n')
text.insert(END,'在结束了一段匆匆忙忙的工作之后选择这样一种方式让自己放松不也是很好的吗？\n')
text.insert(END,'但是现如今越来越多的人选择一个人去旅行，有的人可能觉得一个人的旅行太过孤独了\n')
text.insert(END,'因为一路上都只是跟自己作伴，没有一个人能够跟自己说话。')

root.mainloop()