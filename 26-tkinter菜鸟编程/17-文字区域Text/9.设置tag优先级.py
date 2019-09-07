#可以使用 tag_raised() 和 tag_lower() 方法来提高和降低某个 Tag 的优先级。
from tkinter import *
 
root = Tk()
 
text = Text(root, width=30, height=5)
text.pack()
 
text.tag_config('tag2', foreground='blue')  #设置tag的选项时，如果没有该tag，则会新建一个
text.tag_config('tag1', background='yellow', foreground='red') #此时这个就是新建的Tag的顺序
#到这里是黄底红字的
 
text.tag_lower('tag1')
#到这里就成了黄底蓝字
 
text.insert(INSERT,'I love Python！！！\r\n')
text.insert(INSERT,'I love Node.js！！！\r\n','tag2')
text.insert(INSERT, 'I love study very well\r\n', ('tag2', 'tag1'))  #和这里的tag选项的顺序无关。这样Tag加入的是整个文本
text.insert(INSERT,'I love C#！！！','tag1')

mainloop()