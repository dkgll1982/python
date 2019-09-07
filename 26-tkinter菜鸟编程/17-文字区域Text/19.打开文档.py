from tkinter import *
from tkinter.filedialog import *

def newFile():
    text.delete('1.0',END)
    root.title('Untitled')

def openFile():
    global filename 
    #读取打开的文档
    filename = askopenfilename(initialdir = r'C:\Users\dkgll\Desktop',
                                title='打开文本文件', 
                                filetypes=[('*.TXT', '*.txt'), ('All Files', '*')])
    if filename == "":                     #如果没有选择文档
        return 
    with open(filename,'r') as fileobj:    #打开文档
        content = fileobj.read()           #读取文档内容
    text.delete('1.0',END)                 #删除Text控件文本内容
    text.insert(END,content)               #插入所读取的文档
    root.title(filename)                   #更改窗口标题

def saveasFile():
    global filename
    textcontent = text.get('1.0',END)
    #开启"另存为"对话框，所输入的文档路径回传会给filename，默认所存储的文档扩展名为.txt
    
    filename = asksaveasfilename(initialdir = r'C:\Users\dkgll\Desktop',
                                title='另存为',
                                defaultextension='.txt') 
    if filename == "":                     #如果没有输入文件名
        return 
    with open(filename,'w') as output:
        output.write(textcontent)
    root.title(filename)
        
filename=r'C:\Users\dkgll\Desktop\mydict.txt'        
root = Tk()
root.title(filename)
root.geometry("400x300+300+200")

menubar = Menu(root)            #建立最上层菜单
#建立菜单类别对象,并将此菜单命名为File
filemenu = Menu(menubar,tearoff=False)
menubar.add_cascade(label='File',menu=filemenu)
#在File菜单内建立菜单列表
filemenu.add_command(label='New File',command=newFile)
filemenu.add_command(label='Open File',command=openFile)
filemenu.add_command(label='Save as',command=saveasFile)
filemenu.add_command(label='Exit',command=root.destroy)
root.config(menu=menubar)       #显示菜单对象
 
#建立Text
text = Text(root,undo=True)
text.pack(fill=BOTH,expand=True)

text.insert(END, 'COMMENT ON COLUMN\n')
text.insert(END, 'COMMENT ON COLUMN CIGPROXY SPT_PUSH_RETRY_TASK SEND_URL IS  推送调用省平台接口url \n')
text.insert(END, 'COMMENT ON COLUMN CIGPROXY SPT_PUSH_RETRY_TASK METHOD_NAME IS  推送调用方法名 \n')
text.insert(END, 'COMMENT ON COLUMN CIGPROXY SPT_PUSH_RETRY_TASK BIZ_CONTENT IS  推送内容 \n')
text.insert(END, 'COMMENT ON COLUMN CIGPROXY SPT_PUSH_RETRY_TASK ERR_COUNT IS  重试次数 \n')
text.insert(END, 'COMMENT ON COLUMN CIGPROXY SPT_PUSH_RETRY_TASK IS_SUCCESS IS  是否成功推送 \n')
text.insert(END, 'COMMENT ON COLUMN CIGPROXY SPT_PUSH_RETRY_TASK ERR_LOG IS  出错日志 \n')
text.insert(END, 'COMMENT ON TABLE CIGPROXY SPT_PUSH_RETRY_TASK  IS  省平台数据采集推送重试任务表 \n') 

root.mainloop()