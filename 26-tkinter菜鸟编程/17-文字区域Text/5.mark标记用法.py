# from tkinter import *

# root = Tk()
# text = Text(root,width = 30,height = 5) 
# text.pack()
# text.insert(INSERT,'I love python.')
# text.mark_set('mark',1.2) #标记mark(这个名字随意起)在l之前
# text.insert('mark','插')#‘插’出现在l之前
# text.insert('mark','入')#‘入’出现在l之前
# text.insert('mark','python ')#‘python ’出现在l之前  不管怎么插入，始终在l之前 
# text.insert('mark','kang')
# text.mark_unset('mark') #解除MArk标记 

# text.mark_set('mark',1.6) #标记mark(这个名字随意起)在l之前
# text.insert('mark','python')

# mainloop()
 
'''另外，一般插入的字符在标记的左边，如何插入标记的右边呢?
使用mark_gravity()方法。'''
from tkinter import *
root = Tk()
text = Text(root,width = 30,height = 5) 
text.pack()
text.insert(INSERT,'I love python.')
text.mark_set('mark',1.2)
text.mark_gravity('mark',LEFT)
 
# 设置 tag
# Text 组件的 insert() 方法有一个可选的参数，用于指定一个或多个“标签”（标签用于设置文本的格式，请参考下方【Tags 用法】）到新插入的文本中：
text.tag_config("tag_1", backgroun="yellow", foreground="red")

text.insert('mark','插', "tag_1") 
text.insert('mark','入', "tag_1")

print(text.get('mark','end'))
mainloop() 