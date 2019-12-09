#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: 航天神舟智慧系统技术有限公司 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2019-10-18 23:13:44 
# @Last Modified by: guojun 
# @Last Modified time: 2019-10-18 23:13:44 
# @Software: vscode 
 
import tkinter as tk
from tkinter import ttk
 
import re
import time
 
#固定
pattern = '{"排名": "(.*?)", "片名": "(.*?)", "主演": "(.*?)", "上映时间": "(.*?)", "评分": "(.*?)"}\n'
patch = re.compile(pattern)
 
 
class info():
    def __init__(self,):
        self.root = tk.Tk()
        self._setpage()       
        
    def _setpage(self,):
        start= time.time()
        
        self.scrollbar = tk.Scrollbar(self.root,command=self.moveScroll)
        self.scrollbar.bind("<MouseWheel>",self.moveScroll)
        self.scrollbar.pack(side=tk.RIGHT,fill=tk.Y)
    
        
        title=['1','2','3','4','5',]
        self.box = ttk.Treeview(self.root,columns=title,
                                yscrollcommand=self.scrollbar.set,
                                show='headings')
        self.box.bind("<MouseWheel>",self.moveScroll)
        
        self.box.column('1',width=50,anchor='center')
        self.box.column('2',width=200,anchor='center')
        self.box.column('3',width=300,anchor='center')
        self.box.column('4',width=150,anchor='center')
        self.box.column('5',width=50,anchor='center')
        
        self.box.heading('1',text='Range')
        self.box.heading('2',text='Flim Name')
        self.box.heading('3',text='Actor')
        self.box.heading('4',text='Time')
        self.box.heading('5',text='Score')
        
        #对象处理
        self.op = self.readdata()
        self.dealline(self.op)
        
        self.scrollbar.config(command=self.box.yview)
        self.box.pack()
 
        end=time.time()
        tk.Label(self.root,text=end-start,fg='red').pack()
        tk.Button(self.root,text='Look',bg='green',command=self.turn).pack()
        
        
    #翻页模式，每点击一次，加载多10条数据
    def turn(self):
#        self.scrollbar.set(0.89,0.99)    
#        print(self.scrollbar.get())
 
        self.dealline(self.op)
        
    #鼠标滚动模式，下滑时加载数据
    def moveScroll(self,event):
        if event.delta < 0:
            self.dealline(self.op)
               
    def dragScroll(self):
        #未实现
        pass
    
    def readdata(self,):    
        """逐行读取文件"""    
        
        #读取gbk编码文件，需要加encoding='utf-8'
        f = open(r'26-tkinter菜鸟编程\18-Treeview\result.txt','r',encoding='utf-8')
        line = f.readline()
        while line:
            yield line
            line = f.readline()
            
        f.close()
       
    def dealline(self,op):
        self.cal = 0
        while 1:
            try:
                line = next(op)
            except StopIteration:
                break
            else:
                result = patch.match(line)
                self.box.insert('','end',values=[result.group(i) for i in range(1,6)])
                
                self.cal +=1
                if self.cal == 10:
                    break
 
 
 
if __name__ == '__main__':
    op = info()
    op.root.mainloop()