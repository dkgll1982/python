from tkinter import *
from tkinter import ttk,filedialog, messagebox 
from DataManage import * 
import os 
# 动态添加g:\fk_ext路径作为模块加载路径
sys.path.append(r'26-tkinter菜鸟编程\24-数据查询器\Model')  
from Db  import *
import threading,time,datetime

class MyWindow(Tk):   
    def __init__(self):
        super().__init__()
        self._set_window_()  
        self.bl = False
        self.status = StringVar()
        self.db = Db() 
        self._create_body()
        self.rowindex = 0

    # 设置初始窗口的属性
    def _set_window_(self):
        self.title("数据查询器")
        
        w = 1080
        h =650
        wx = (self.winfo_screenwidth()-w)/2
        wy = (self.winfo_screenheight()-h)/2  
        self.geometry('%dx%d+%d+%d'%(w,h,wx,wy)) 
        self.protocol('WM_DELETE_WINDOW', self.exit_Window) 
  
    #获取数据库连接配置参数
    def _getdb(self):  
        self.db.userid = self.entuser.get()
        self.db.pwd = self.entpwd.get()
        self.db.ip = self.entip.get()
        self.db.port = self.entport.get()
        self.db.sid = self.entsid.get() 

    #连接
    def _getconn(self,event=None): 
        self._getdb()
        self.bl = getconn(self.db) 
        if(self.bl):
            self.status.set("数据库连接成功！！！")
            self.lblstatus.config(fg="blue")
        else:
            self.status.set("数据库连接失败！！！")
            self.lblstatus.config(fg="red")  

    #执行非查询的SQL语句返回命令行参数
    def _execsql(self,event=None): 
        self._getconn()
        if(self.bl):
            sqltext = self.sqltxt.get('0.0',END)
            if(sqltext is not None): 
                os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
                conn = cx_Oracle.connect(self.db.userid,self.db.pwd,self.db.ip+':'+self.db.port+'/'+self.db.sid)
                cursor = conn.cursor()  

                sqllist = sqltext.replace('\r','').replace('\n','').split(';')
                self.entresult.insert(END,'开始时间：%s，执行非查询的SQL语句！\r\n\r\n'%(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]))
                self.entresult.update()
                for sql in sqllist: 
                    if sql is not None and sql != '':
                        row  = cursor.execute(sql)  
                        self.entresult.insert(END,'开始时间：%s，执行SQL:%s成功！\r\n'%(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3],sql)) 
                        self.entresult.update()

                        txt = self.entresult.get('0.0',END)
                        if(len(txt)>5000):
                            self.entresult.delete('0.0',END) 

                self.entresult.insert(END,'\r\n结束时间：%s，执行结束！\r\n'%(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]))
                self.entresult.update()
                conn.commit() 
                cursor.close()
                conn.close()   

    #设置数据库连接配置
    def _setconfig(self):
        parent = self.lrm1

        lbluser=Label(parent,text='用户名：',width=8)
        lbluser.grid(column=0,row=0)

        self.entuser = Entry(parent,width=20)
        self.entuser.grid(column=1,row=0,pady=5)
        self.entuser.insert(END,'cigproxy')

        lblpwd=Label(parent,text='密码：',width=8)
        lblpwd.grid(column=2,row=0)

        self.entpwd = Entry(parent,width=20,show='*')
        self.entpwd.grid(column=3,row=0,pady=5)
        self.entpwd.insert(END,'cigproxy')

        lblip=Label(parent,text='主机IP：',width=8)
        lblip.grid(column=4,row=0)

        self.entip = Entry(parent,width=20)
        self.entip.grid(column=5,row=0,pady=5)
        self.entip.insert(END,'172.21.188.219')

        btnconn =ttk.Button(parent,text="连接",width=12,cursor='heart')
        btnconn.grid(column=6,row=0,padx=10)

        btnclr =ttk.Button(parent,text="清除",width=12,command = lambda:self.sqltxt.delete(0.0,END))
        btnclr.grid(column=7,row=0)

        lblport=Label(parent,text='端口：',width=8)
        lblport.grid(column=0,row=1)

        self.entport = Entry(parent,width=20)
        self.entport.grid(column=1,row=1,pady=5)
        self.entport.insert(END,'15223')

        lblsid=Label(parent,text='SID：',width=8)
        lblsid.grid(column=2,row=1)

        self.entsid = Entry(parent,width=20)
        self.entsid.grid(column=3,row=1,pady=5) 
        self.entsid.insert(END,'orcl')

        btnexec =ttk.Button(parent,text="执行SQL语句",width=12)
        btnexec.grid(column=6,row=1,padx=10)

        btncancle =ttk.Button(parent,text="取消",width=12)
        btncancle.grid(column=7,row=1) 

        btnconn.bind('<Button-1>',self._getconn)  
        btnexec.bind('<Button-1>',self._execsql)  

    def _create_body(self):
        #顶部框架：数据库连接信息
        self.lrm1 = LabelFrame(self,text="数据库连接信息",height=200 )
        self.lrm1.pack(fill=X,padx=10) 

        self._setconfig()

        #中间框架：SQL语句
        self.lrm2= LabelFrame(self,text="SQL语句",height=12)
        self.lrm2.pack(fill=X,padx=10,pady=10)

        self.sqltxt = Text(self.lrm2,height=12,fg='blue')
        self.sqltxt.pack(side=LEFT,fill=BOTH,expand=True)

        sqltext = '''INSERT INTO EXCEL_TABLE(XH,A,B,C,TYPE) VALUES(SEQUENCE1.nextval,2,3,4,'测试插入');\r\n'''
        #SQL语句
        self.sqltxt.insert(END, sqltext*100) 

        #底部框架：执行结果（如果执行的是查询语句，返回查询结果，如果执行的是非查询语句，返回命令行参数）
        self.lrm3 = LabelFrame(self,text="执行结果")
        self.lrm3.pack(fill=BOTH,expand=True,padx=10)  
        self.entresult = Text(self.lrm3)
        self.entresult.pack(side=LEFT,fill=BOTH,expand=True)
        
        yscrollbar = Scrollbar(self.lrm3)                               #y轴滚动条对象    
        yscrollbar.pack(fill = BOTH,side = LEFT)                        #y轴滚动条包装
        yscrollbar.config(command = self.entresult.yview)               #y轴滚动条设置
        self.entresult.config(yscrollcommand = yscrollbar.set)         

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
