#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: 航天神舟智慧系统技术有限公司 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2019-10-17 20:38:25 
# @Last Modified by: guojun 
# @Last Modified time: 2019-10-17 20:38:25 
# @Software: vscode  

import cx_Oracle
import os
import urllib.request 
from 坐标转换 import bd09_to_wgs84,bdapi 
import threading,time,datetime
import urllib.request
import json 
from tkinter import *
from tkinter import ttk,filedialog, messagebox    
# 引入字体模块
import tkinter.font as tkFont
from db import *            #连接实体类
import dbconfig             #连接配置文件 
from DataManage import * 

#百度ak,sk
ak = "LKnE67ysMkrG0LHwyG2GHPlc00LtMfSW"
sk = "3hPe7iy3Ydq003v6wYbKn6pq7sHgGCRj"  

#线程数量
threadcount = 10
#数据分段区间
pagecount = 5000
#每次取数据行数
rowcount = 100

# 大致计算公式如下
# 公式1：线程循环次数 = 数据分段区间/每次取数据行数，如5000/100=50，即需要约50次循环才能跑完区间的所有的数据 
# 公式2：最终处理数据量 = 线程数量*数据分段区间，如20*5000=100000
# 由公式1也可得公式3：最终处理数据量 = 线程数量*每次取数据行数*线程循环次数，如20*100*50=100000

#调用api返回json数据
def request_data(urt):
    #测试发现：Accept、User-Agent这俩必不可少
    head={
        #'Host':'jczl.giscloud.cx',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
        #'Accept-Language':'zh-CN,zh;q=0.9,und;q=0.8,en;q=0.7',
        #'Accept-Encoding':'gzip, deflate', 
        #'Connection':'keep-alive',
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3'
        #'Cookie':"passport=34672dc8-12f7-46e2-ad36-a0f7de5f4e7c; CIGUserid=ADMIN; true=SpwLpmOm8qrd8f0YAAA6"
    }      
    request = urllib.request.Request(url=urt,headers=head) 
    response = urllib.request.urlopen(request)
    s = response.read().decode('utf-8')  #一定要解码！！！！ 
    #jsonData = json.loads(s)
    return s 

class MyWindow(Tk):   
    def __init__(self):
        super().__init__() 
        self.db = server() 
        self.citylist = list(x['city'] for x in dbconfig.all)  #获取城市列表 
        self.bl = False
        self.status = StringVar()
        self.rowindex = 0
        #设置绑定变量
        self.city,self.url,self.userid,self.pwd,self.ip,self.port,self.sid = StringVar(),StringVar(),StringVar(),StringVar(),StringVar(),StringVar(),StringVar()
         
        self._set_window_()  
        self._create_body()
        self._changecity()   #给配置框默认值

    # 设置初始窗口的属性
    def _set_window_(self):
        self.title("地址网格计算器")        
        w = 1080
        h =650
        wx = (self.winfo_screenwidth()-w)/2
        wy = (self.winfo_screenheight()-h)/2  
        self.geometry('%dx%d+%d+%d'%(w,h,wx,wy)) 
        self.protocol('WM_DELETE_WINDOW', self.exit_Window) 
    
    #切换选择城市加载对应城市的连接配置
    def _changecity(self,event=None): 
        self.city.set(self.comb.get())         #当前选中城市
        for x in dbconfig.all:
            if x["city"] == self.city.get():
                self.url.set(x['url'])
                self.userid.set(x['userid'])
                self.pwd.set(x['pwd'])
                self.ip.set(x['ip'])
                self.port.set(x['port'])
                self.sid.set(x['sid'])

    #获取数据库连接配置参数
    def _getdb(self):  
        self.db.url = self.url.get()
        self.db.userid = self.userid.get()
        self.db.pwd = self.pwd.get()
        self.db.ip = self.ip.get()
        self.db.port = self.port.get()
        self.db.sid = self.sid.get()

    #测试连接
    def _getconn(self,event=None): 
        self._getdb()
        self.bl = getconn(self.db) 
        if(self.bl):
            self.status.set("数据库%s连接成功！！！"%self.db.ip)
            self.lblstatus.config(fg="blue")
        else:
            self.status.set("数据库%s连接失败！！！"%self.db.ip)
            self.lblstatus.config(fg="red")  

    #查询服务并更新坐标到数据表里
    def get_zb(self,index,cn,sThread,event):
        if(self.status.get() is None or self.status.get() ==''):    #先连接数据库
            self._getconn()
        if not event.is_set():
            if (self.bl):
                os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
                conn = cx_Oracle.connect(self.db.userid,self.db.pwd,self.db.ip+':'+self.db.port+'/'+self.db.sid)
                cursor = conn.cursor() 

                #取数据起始位置
                start = str(pagecount*(index-1))
                #取数据结束位置
                end = str(pagecount*(index))
                # if sThread:             #单线程
                #     start = '0'
                #     end = '100000000'
                #查询数据的sql
                sql1 =  ("select * from (select ADDR from BASE_ZB_WG where ADDR not in(select ADDR from TEMP_ZB_WG) and RESULT is null and rn<="+end+" and rn>"+start+") where rownum<="+str(rowcount))      
                sql2 = ""

                cursor.execute(sql1);    
                rows = cursor.fetchall()  # 得到所有数据集

                update_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                g = bdapi(ak,sk)
                for row in rows: 
                    url =g.get_url(self.city.get()+row[0]) 
                    try:
                        bd_zb = g.get_zb(url)                                                               #得到百度坐标
                        if bd_zb is not None:
                            wgs_zb =  bd09_to_wgs84(bd_zb[0], bd_zb[1])                                     #将百度坐标转为WGS84坐标                
                            bd_x,bd_y,wgs_x,wgs_y = str(bd_zb[0]),str(bd_zb[1]),str(wgs_zb[0]),str(wgs_zb[1])
                            geo = self.db.url+"?x="+wgs_x+"&y="+wgs_y
                            result = request_data(geo) 
                            cdate = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
                            self.txtresult.insert(END,"子线程(%s)处理——当前时间：%s,index:%d,循环次数：%d/%d,百度坐标：%s,WGS84坐标：%s\r\n"%(threading.current_thread().name,cdate,index,cn,self.xhcount,bd_zb,wgs_zb)) 
                            self.txtresult.update()
                            self.txtresult.see(END)
                            sql2 = "INSERT INTO TEMP_ZB_WG(ADDR,WGS_X,WGS_Y,BD_X,BD_Y,RESULT,UPDATE_DATE) VALUES('%s','%s','%s','%s','%s','%s',to_date('%s','YYYY-MM-DD HH24:MI:SS'))"%(row[0],wgs_x,wgs_y,bd_x,bd_y,str(result),update_date) 
                        else:       
                            sql2 = "INSERT INTO TEMP_ZB_WG(ADDR,UPDATE_DATE) VALUES('%s',to_date('%s','YYYY-MM-DD HH24:MI:SS'))"%(row[0],update_date)        
                        cursor.execute(sql2)
                    except Exception as e:
                        self.txtresult.insert(END,('Error:%s\r\n'%e))
                        self.txtresult.update()
                        self.txtresult.see(END)     #保持焦点始终在最底部
                    finally:
                        if(len(self.txtresult.get(0.0,END))>300000):
                            self.txtresult.delete(0.0,END)
                            self.update()
                conn.commit() 
                cursor.close()
                conn.close()    
                self.txtresult.insert(END,"子线程(%s)已处理完毕！！！\r\n"%(threading.current_thread().name),'highlight') 
                self.txtresult.update()
                self.txtresult.see(END)
            #event.wait()
        else:
            event.clear() 
   
    #调用服务(sThread=True是单线程，默认为多线程)
    def _callapi(self,sThread=False,event=None):
        self.txtresult.insert(END,"主线程(%s)启动\r\n"%threading.current_thread().name)
        self.txtresult.update()
        start = time.time()  
        self.xhcount = int(self.spin.get())  #循环调用线程次数

        for cn in range(self.xhcount):
            #任何进程默认就会启动一个线程，成为主线程，主线程就可以启动新的子线程
            #current_thread(): 返回当前线程的实例 
            ThreadList = []
            self.EventList = [] 
            #创建子线程
            for x in range(1 if sThread else threadcount):
                event = threading.Event()
                ThreadList.append(threading.Thread(target=self.get_zb,args=(x,cn+1,sThread,event)))
                self.EventList.append(event)   
            #启动子线程
            for thread in ThreadList:
                thread.setDaemon(True)      #守护线程  
                thread.start() 
            #等待线程结束
            #for thread in ThreadList:
            #    thread.join()              #线程阻塞，会卡死界面
            
            
        #end = time.time()
        #self.txtresult.insert(END,"主线程(%s)结束,总耗时：%0.6f秒\r\n"%(threading.current_thread().name,end-start)) 
        #self.txtresult.update()

    #暂停线程
    def _abortthread(self):
        self.__flag.clear()     # 设置为False, 让线程阻塞

    #终止线程
    def _stopthread(self):
        self.__flag.set()       # 将线程从暂停状态恢复, 如何已经暂停的话
        self.__running.clear()  # 设置为False 

    #恢复线程    
    def _resumethread(self):
        # 对应事件的set()方法将事件标志设置为True，则不阻塞线程 
        for event in self.EventList:
            event.set()

    #设置组件显示 
    def _create_body(self): 
        self.lrm0 = LabelFrame(self,text="地图服务配置",height=200 )
        self.lrm0.pack(fill=X,padx=10) 
        
        self.lrm1 = LabelFrame(self,text="数据库连接配置",height=200 )
        self.lrm1.pack(fill=X,padx=10)  
        
        lblcity = ttk.Label(self.lrm0,text='请选择区县：',width=12 ,foreground='red')
        lblcity.grid(column=0,row=0,padx=5)
        ft = tkFont.Font(size=12,weight=tkFont.BOLD)
        lblcity.configure(font=ft)

        self.comb = ttk.Combobox(self.lrm0,width=20,state='readonly')
        self.comb.grid(column=1,row=0,pady=5) 
        self.comb['value'] = self.citylist
        #默认选中第一条
        self.comb.current(0)  
        #虚拟ComboboxSelected事件：选中
        self.comb.bind('<<ComboboxSelected>>',self._changecity)   

        lblak=Label(self.lrm0,text='AK：',width=12)
        lblak.grid(column=2,row=0)

        self.entak = Entry(self.lrm0,width=35)
        self.entak.grid(column=3,row=0,pady=5)
        self.entak.insert(END,ak)

        lblsk=Label(self.lrm0,text='SK：',width=8)
        lblsk.grid(column=4,row=0)

        self.entsk = Entry(self.lrm0,width=35)
        self.entsk.grid(column=5,row=0,pady=5)
        self.entsk.insert(END,sk) 

        lblurl=Label(self.lrm0,text='网格服务地址：',width=12)
        lblurl.grid(column=0,row=1,padx=5)

        self.enurl = Entry(self.lrm0,width=72,textvariable=self.url)
        self.enurl.grid(column=1,row=1,pady=5,columnspan=3)  

        lbluser=Label(self.lrm1,text='用户名：',width=8)
        lbluser.grid(column=0,row=0,sticky=W)

        self.entuser = Entry(self.lrm1,width=22,textvariable=self.userid)
        self.entuser.grid(column=1,row=0,pady=5) 

        lblpwd=Label(self.lrm1,text='密码：',width=8)
        lblpwd.grid(column=2,row=0,sticky=W)

        self.entpwd = Entry(self.lrm1,width=22,show='*',textvariable=self.pwd)
        self.entpwd.grid(column=3,row=0,pady=5) 

        lblip=Label(self.lrm1,text='主机IP：',width=8)
        lblip.grid(column=4,row=0,padx=4,sticky=W)

        self.entip = Entry(self.lrm1,width=22,textvariable=self.ip)
        self.entip.grid(column=5,row=0,pady=5) 

        btnconn =ttk.Button(self.lrm1,text="测试连接",width=10,cursor='heart',command=self._getconn)
        btnconn.grid(column=6,row=0,padx=10)

        btnsing =ttk.Button(self.lrm1,text="单线程调用",width=10,command=lambda:self._callapi(True,None))
        btnsing.grid(column=7,row=0)
        
        btnclr =ttk.Button(self.lrm1,text="多线程调用",width=10,command=self._callapi)
        btnclr.grid(column=8,row=0,padx=10)

        lblport=Label(self.lrm1,text='端口：',width=8)
        lblport.grid(column=0,row=1,sticky=W)

        self.entport = Entry(self.lrm1,width=22,textvariable=self.port)
        self.entport.grid(column=1,row=1,pady=5) 

        lblsid=Label(self.lrm1,text='SID：',width=8)
        lblsid.grid(column=2,row=1,sticky=W)

        self.entsid = Entry(self.lrm1,width=22,textvariable=self.sid)
        self.entsid.grid(column=3,row=1,pady=5)  

        lblcn=Label(self.lrm1,text='循环次数：',width=8)
        lblcn.grid(column=4,row=1,padx=4,sticky=W)
 
        self.spin = Spinbox(self.lrm1,from_=1,to=20,increment=1,width=10)
        self.spin.grid(column=5,row=1,pady=5,sticky=W)  

        btnabort = ttk.Button(self.lrm1,text="暂停线程",width=10,command=self._abortthread)
        btnabort.grid(column=6,row=1,padx=10) 

        btnstop = ttk.Button(self.lrm1,text="终止线程",width=10,command=self._stopthread)
        btnstop.grid(column=7,row=1)

        btnclear = ttk.Button(self.lrm1,text="恢复线程",width=10,command=self._resumethread)
        btnclear.grid(column=8,row=1,padx=10)
 
        #底部框架：执行结果（如果执行的是查询语句，返回查询结果，如果执行的是非查询语句，返回命令行参数）
        self.lrm3 = LabelFrame(self,text="执行消息")
        self.lrm3.pack(fill=BOTH,expand=True,padx=10)  
        self.txtresult = Text(self.lrm3)
        self.txtresult.pack(side=LEFT,fill=BOTH,expand=True)
        self.txtresult.tag_config('highlight',background = 'yellow',foreground='red')
        
        yscrollbar = Scrollbar(self.lrm3)                               #y轴滚动条对象    
        yscrollbar.pack(fill = BOTH,side = LEFT)                        #y轴滚动条包装
        yscrollbar.config(command = self.txtresult.yview)               #y轴滚动条设置
        self.txtresult.config(yscrollcommand = yscrollbar.set)         

        #状态栏：
        self.lrm4 = Frame(self)
        self.lrm4.pack(fill=X)

        self.lblstatus = Label(self.lrm4,textvariable = self.status) 
        self.lblstatus.pack(side=LEFT,padx=10)    
            
    def exit_Window(self):
        if messagebox.askokcancel("退出?", "确定退出吗?"):
            self.destroy()

if "__main__" == __name__:
    app = MyWindow()
    app.mainloop() 