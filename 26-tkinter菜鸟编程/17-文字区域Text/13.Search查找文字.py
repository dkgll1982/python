from tkinter import *

def mySearch(): 
    #tag_remove(tagName, index1, index2=None)
    #-- 删除 index1 到 index2 之间所有的 tagName
    #-- 如果忽略 index2 参数，那么只删除 index1 指定的那个字符的 tagName（如果有的话） 
    #如果不加上text.tag_remove("found",'1.0',END)，则之前高亮显示的选中文字样式不会取消，加上后则每次高亮显示当前显示的文本
    text.tag_remove("found",'1.0',END)      #删除已应用该定义的标签高亮显示样式但不删除该标签定义
    start = '1.0'                           #设置查找起始位置
    key = entry.get()                       #读取查找关键字 
    if(len(key.strip())==0):                #没有输入
        return
    while True:
        pos = text.search(key,start,END)    #执行查找
        if(pos == ""):                      #找不到结束循环
            break
        #pos是加入标签的起始位置，标签的结束位置是一个索引的表达式，此处相当于是在pos的位置加上key关键词的长度
        #索引表达式的写法：text.tag_add("current_line", "insert linestart", "insert lineend+1c") 
        text.tag_add("found",pos,"%s+%dc" %(pos,len(key)))  #加入标签
        start = "%s+%dc" %(pos,len(key))                    #更新查找起始位置

root = Tk()
root.title("search查找文字")
root.geometry("400x300+300+200")

root.rowconfigure(1,weight=1)
root.columnconfigure(0,weight=1)

entry = Entry()
entry.grid(row=0,column=0,padx=5,sticky=W+E)

btn = Button(root,text='查找',command=mySearch)
btn.grid(row=0,column=1,padx=5,pady=5)

#建立Text
text = Text(root,undo=True)
text.grid(row=1,column=0,columnspan=2,padx=3,pady=5,sticky=N+S+W+E)
text.insert(END,'很多人其实都特别喜欢旅行，因为旅行对于一个人来说算得上是一种比较放松的方式了\n')
text.insert(END,'在结束了一段匆匆忙忙的工作之后选择这样一种方式让自己放松不也是很好的吗？\n')
text.insert(END,'但是现如今越来越多的人选择一个人去旅行，有的人可能觉得一个人的旅行太过孤独了\n')
text.insert(END,'因为一路上都只是跟自己作伴，没有一个人能够跟自己说话。')

text.tag_config('found',background='yellow')

root.mainloop()