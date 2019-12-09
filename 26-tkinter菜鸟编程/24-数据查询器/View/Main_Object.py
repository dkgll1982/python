from tkinter import *
from tkinter import ttk,filedialog, messagebox 
from DataManage import * 
import os 
# 动态添加g:\fk_ext路径作为模块加载路径
sys.path.append(r'26-tkinter菜鸟编程\24-数据查询器\Model')  
from Db  import *

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

    #查询数据
    def _getdata(self,event=None):
        self._getconn()
        if(self.bl):
            sqltext = self.sqltxt.get('1.0',END)
            if(sqltext is not None): 
                data = get_data(self.db,sqltext)
            
                #将查询出的数据渲染导表格
                self._setgrid(data) 

    #列排序
    def treeview_sort_column(self,tv, col, reverse):#Treeview、列名、排列方式
        print(tv.get_children(''))
        l = [(tv.set(k, col), k) for k in tv.get_children('')]
        print(l)
        l.sort(reverse=reverse)                 #排序方式
        # rearrange items in sorted positions
        for index, (val, k) in enumerate(l):    #根据排序后索引移动
            tv.move(k, '', index)
            #print(k)
        tv.heading(col, command=lambda: self.treeview_sort_column(tv, col, not reverse))  #重写标题，使之成为再点倒序的标题 

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

        btncancle =ttk.Button(parent,text="切换样式",width=12,command=self._change_style)
        btncancle.grid(column=8,row=0,rowspan=2,padx=5)

        btnconn.bind('<Button-1>',self._getconn) 
        btnexec.bind('<Button-1>',self._getdata) 

    #将查询结果以列表的形式展现在界面
    def _setgrid(self,data): 
        self.rowindex = 0
        frm = self.lrm3

        # 删除原节点
        for widget in frm.winfo_children():
            widget.destroy()

        #建立Treeview组件
        #show = "tree", 第一列也会被显示出来
        #也可用show = "headings" 把第一列隐藏起来 
        #for x in data[0]:
            # 如果该菜单是顶层菜单的一个菜单项，则它添加的是下拉菜单的菜单项。
        #    fmenu1.add_command(label=item) 
        self.tree = ttk.Treeview(frm,column=(data[0]), show="headings")
        index = 1
        self.tree.heading('#0',text = '序号')
        self.tree.column('#0',width = 3)
        for x in data[0]: 
            #建立栏目标题
            self.tree.heading('#'+str(index),text=x,command=lambda _col='#'+str(index):self.treeview_sort_column(self.tree, _col, False))
            
            #格式化栏位 
            if index == 1: 
                self.tree.column('#1',anchor=W,width=35,minwidth=35)
            else:
                self.tree.column('#'+str(index),anchor=W,width=105,)
            index+=1   

        #格式栏位
        self.tree.tag_configure('evenColor1', background='lightblue')     #设置标签  
        self.tree.tag_configure('evenColor2', background='white')         #设置标签  
        self.tree.tag_configure('evenColor3', background='#FF6347')       #设置标签  
        
        index = 0   
        for x in data:
            if index!=0:
                #建立内容
                if (index%2==0):
                    self.tree.insert("",index=END,text=index,values=x,tags=('evenColor1'))
                else:
                    self.tree.insert("",index=END,text=index,values=x,tags=('evenColor2'))
            index+=1   

        self.tree.pack(side = LEFT,fill = BOTH,expand = True)
        
        yscrollbar = Scrollbar(frm)                            #y轴滚动条对象    
        yscrollbar.pack(fill = BOTH,side = LEFT)               #y轴滚动条包装
        yscrollbar.config(command = self.tree.yview)           #y轴滚动条设置
        self.tree.config(yscrollcommand = yscrollbar.set)         

    #切换样式逐行变色
    def _change_style(self):
        def get_style(ind): 
            if (ind%2==0):
                self.tree.item(items[ind],tags=('evenColor2'))
            else:
                self.tree.item(items[ind],tags=('evenColor1')) 

        #遍历行记录
        items = self.tree.get_children() 
        self.tree.item(items[self.rowindex], tags=('evenColor3'))  
            
        if self.rowindex>0:
           get_style(self.rowindex-1)
        self.rowindex+=1 

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

        #SQL语句
        self.sqltxt.insert(END, '''select rownum as rn,card_num,name,to_char(birth_date,'yyyy-mm-dd') birth_date,decode(gender,'1','男','2','女') sex,
            r_addr,displayname,to_char(create_date,'yyyy-mm-dd') create_date,create_user
        from cigproxy.zz_person ta join a4_sys_department tb on ta.g_id = tb.departmentid
            where create_user is not null and create_date is not null and g_id is not null and rownum<=100''')

        #底部框架：执行结果（如果执行的是查询语句，返回查询结果，如果执行的是非查询语句，返回命令行参数）
        self.lrm3 = LabelFrame(self,text="执行结果")
        self.lrm3.pack(fill=BOTH,expand=True,padx=10)  

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
