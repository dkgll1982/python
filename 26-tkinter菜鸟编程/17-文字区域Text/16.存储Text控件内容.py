from tkinter import *

def saveFile():
    textcontent = text.get('1.0',END)
    filename = r"26-tkinter菜鸟编程\17-文字区域Text\savetext.txt"
    with open(filename,'w') as output:
        output.write(textcontent)
        root.title(filename)
        
root = Tk()
root.title('存储文本')
root.geometry("400x300+300+200")

menubar = Menu(root)            #建立最上层菜单
#建立菜单类别对象,并将此菜单命名为File
filemenu = Menu(menubar,tearoff=False)
menubar.add_cascade(label='File',menu=filemenu)
#在File菜单内建立菜单列表
filemenu.add_command(label='Save',command=saveFile)
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
text.insert(END, 'COMMENT ON COLUMN CIGPROXY SPT_PUSH_RE嗯嗯TRY_TASK IS_SUCCESS IS  是否成功推送 \n')
text.insert(END, 'COMMENT ON COLUMN CIGPROXY SPT_PUSH_RETRY_TASK ERR_LOG IS  出错日志 \n')
text.insert(END, 'COMMENT ON TABLE CIGPROXY SPT_PUSH_RETRY_TASK  IS  省平台数据采集推送重试任务表 \n') 

root.mainloop()