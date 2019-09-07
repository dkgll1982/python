from tkinter import *

def spellingCheck():
    text.tag_remove('spellErr',"1.0",END)               #删除标签但是不删除标签定义
    textwords = text.get("1.0",END).split()             #Text控件的文字
    print ("字典内容\n",textwords)                       #打印字典内容

    startChar = ("(")                                   #可能的起始字符
    endChar = (".",",",":",";","?","!",")")             #可能的终止符
     
    start =  "1.0"                                      #检查起始索引位置
    for word in textwords:
        if word[0] in startChar:                        #是否含非字母的起始字符
            word = word[1:]                             #删除非字母的起始字符
        if word[-1] in endChar:                         #是否含非字母的终止符
            word = word[-1:]                            #删除非字母的终止符
        #if str(dicts).find(word)!=-1 and str(dicts).find(word.lower())!=-1 :
        if word not in dicts and word.lower() not in dicts:
            print("error", word)
            pos = text.search(word, start,END) 
            text.tag_add("spellErr",pos,"%s+%dc" %(pos,len(word)))
            pos = "%s+%dc" %(pos,len(word))

def clrText():
    text.tag_remove("spellErr","1.0",END)

root = Tk()
root.title('拼写检查')
root.geometry("400x300+300+200")

#建立工具栏
toolbar = Frame(root,relief=RAISED,borderwidth=1)
toolbar.pack(side=TOP,fill=X,padx=2,pady=1)

#建立Button
chkbtn = Button(toolbar,text='拼写检查',command=spellingCheck)
clrBtn = Button(toolbar,text='清除',command=clrText)
chkbtn.pack(side=LEFT,pady=2)
clrBtn.pack(side=LEFT,pady=2)

#建立Text
text = Text(root,undo=True)
text.pack(fill=BOTH,expand=True)

text.insert(END, 'COMMENT ON COLUMN\n')
text.insert(END, 'COMMENT ON COLUMN CIGPROXY SPT_PUSH_RETRY_TASK SEND_URL IS  推送调用省平台接口url \n')
text.insert(END, 'COMMENT ON COLUMN CIGPROXY SPT_PUSH_RETRY_TASK METHOD_NAME IS  推送调用方法名 \n')
text.insert(END, 'COMMENT ON 24234dg CIGPROXY SPT_PUSH_RETRY_TASK BIZ_CONTENT IS  推送内容 \n')
text.insert(END, 'COMMENT ON COLUMN CIGPROXY SPT_PUSH_RETRY_TASK ERR_COUNT IS  重试次数 \n')
text.insert(END, 'COMMENT ON COLUMN CIGPROXY SPT_PUSH_RETRY_TASK IS_SUCCESS IS  是否成功推送 \n')
text.insert(END, 'COMMENT ON COLUMN CIGPROXY SPT_PUSH_RETRY_TASK ERR_LOG IS  出错日志 \n')
text.insert(END, 'COMMENT ON TABLE CIGPROXY SPT_PUSH_RETRY_TASK  IS  省平台数据采集推送重试任务表 \n')

text.tag_config('spellErr',background='red')
with open(r"26-tkinter菜鸟编程\17-文字区域Text\mydict.txt",'r') as dictobj:
    dicts = dictobj.read().split('\n')

print('dicts-------',dicts)

root.mainloop()