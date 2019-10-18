from tkinter import *
from tkinter import ttk
from DataManage import *
 
# 动态添加g:\fk_ext路径作为模块加载路径
sys.path.append(r'E:\100-航天智慧\2-源码库\python\26-tkinter菜鸟编程\24-数据查询器\Model')  
from Db  import *

root =  Tk() 
w = 1080
h =650
wx = (root.winfo_screenwidth()-w)/2
wy = (root.winfo_screenheight()-h)/2  
root.geometry('%dx%d+%d+%d'%(w,h,wx,wy))
root.title('数据查询器')

#全局变量
bl = False
status = StringVar()
db = Db()

#获取数据库连接配置参数
def _getdb(): 
    global db 
    db.userid = entuser.get()
    db.pwd = entpwd.get()
    db.ip = entip.get()
    db.port = entport.get()
    db.sid = entsid.get() 

#连接
def _getconn(event):
    global bl
    _getdb()
    bl = getconn(db) 
    if(bl):
        status.set("数据库连接成功！！！")
        lblstatus.config(fg="blue")
    else:
        status.set("数据库连接失败！！！")
        lblstatus.config(fg="red")
    

#查询数据
def _getdata(event):
    _getconn(event)
    if(bl):
        sqltext = sqltxt.get('1.0',END)
        if(sqltext is not None): 
            data = get_data(db,sqltext)
        
            #将查询出的数据渲染导表格
            setgrid(lrm3,data) 

#设置数据库连接配置
def _setconfig(parent):
    lbluser=Label(parent,text='用户名：',width=8)
    lbluser.grid(column=0,row=0)

    entuser = Entry(parent,width=20)
    entuser.grid(column=1,row=0,pady=5)
    entuser.insert(END,'cigproxy')

    lblpwd=Label(parent,text='密码：',width=8)
    lblpwd.grid(column=2,row=0)

    entpwd = Entry(parent,width=20,show='*')
    entpwd.grid(column=3,row=0,pady=5)
    entpwd.insert(END,'cigproxy')

    lblip=Label(parent,text='主机IP：',width=8)
    lblip.grid(column=4,row=0)

    entip = Entry(parent,width=20)
    entip.grid(column=5,row=0,pady=5)
    entip.insert(END,'172.21.188.219')

    btnconn =ttk.Button(parent,text="连接",width=12,cursor='heart')
    btnconn.grid(column=6,row=0,padx=10)

    btnclr =ttk.Button(parent,text="清除",width=12,command = lambda:sqltxt.delete(0.0,END))
    btnclr.grid(column=7,row=0)

    lblport=Label(parent,text='端口：',width=8)
    lblport.grid(column=0,row=1)

    entport = Entry(parent,width=20)
    entport.grid(column=1,row=1,pady=5)
    entport.insert(END,'15223')

    lblsid=Label(parent,text='SID：',width=8)
    lblsid.grid(column=2,row=1)

    entsid = Entry(parent,width=20)
    entsid.grid(column=3,row=1,pady=5) 
    entsid.insert(END,'orcl')

    btnexec =ttk.Button(parent,text="执行SQL语句",width=12)
    btnexec.grid(column=6,row=1,padx=10)

    btncancle =ttk.Button(parent,text="取消",width=12)
    btncancle.grid(column=7,row=1)

    btnconn.bind('<Button-1>',_getconn) 
    btnexec.bind('<Button-1>',_getdata) 

#将查询结果以列表的形式展现在界面
def setgrid(frm,data): 
    # 删除原节点
    for widget in frm.winfo_children():
        widget.destroy()

    #建立Treeview组件
    #show = "tree", 第一列也会被显示出来
    #也可用show = "headings" 把第一列隐藏起来 
    #for x in data[0]:
        # 如果该菜单是顶层菜单的一个菜单项，则它添加的是下拉菜单的菜单项。
    #    fmenu1.add_command(label=item) 
    tree = ttk.Treeview(frm,column=(data[0]))
    index = 1
    tree.heading('#0',text='序号')
    tree.column('#0',width=3)
    for x in data[0]: 
        #建立栏目标题
        tree.heading('#'+str(index),text=x)
        #格式化栏位 
        tree.column('#'+str(index),anchor=W,width=1)
        index+=1  

    #格式栏位
    tree.tag_configure('evenColor',background='lightblue')   #设置标签  
    
    index = 0
    for x in data:
        if index!=0:
            #建立内容
            if (index%2==0):
                tree.insert("",index=END,text=index,values=x,tags=('evenColor'))
            else:
                tree.insert("",index=END,text=index,values=x)  
        index+=1   

    tree.pack(side = LEFT,fill = BOTH,expand = True)
    
    yscrollbar = Scrollbar(frm)                            #y轴滚动条对象    
    yscrollbar.pack(fill = BOTH,side = LEFT)               #y轴滚动条包装
    yscrollbar.config(command = tree.yview)                #y轴滚动条设置
    tree.config(yscrollcommand = yscrollbar.set)                 

#顶部框架：数据库连接信息
lrm1 = LabelFrame(root,text="数据库连接信息",height=200 )
lrm1.pack(fill=X,padx=10)

_setconfig(lrm1)

#中间框架：SQL语句
lrm2= LabelFrame(root,text="SQL语句",height=12)
lrm2.pack(fill=X,padx=10,pady=10)

sqltxt = Text(lrm2,height=12,fg='blue')
sqltxt.pack(side=LEFT,fill=BOTH,expand=True)

#SQL语句
sqltxt.insert(END, '''select card_num,name,to_char(birth_date,'yyyy-mm-dd') birth_date,decode(gender,'1','男','2','女') sex,
    r_addr,displayname,to_char(create_date,'yyyy-mm-dd') create_date,create_user
from cigproxy.zz_person ta join a4_sys_department tb on ta.g_id = tb.departmentid
    where create_user is not null and create_date is not null and g_id is not null and rownum<=100''')

#底部框架：执行结果（如果执行的是查询语句，返回查询结果，如果执行的是非查询语句，返回命令行参数）
lrm3 = LabelFrame(root,text="执行结果")
lrm3.pack(fill=BOTH,expand=True,padx=10)  

#状态栏：
lrm4 = Frame(root)
lrm4.pack(fill=X)

lblstatus = Label(lrm4,textvariable = status) 
lblstatus.pack(side=LEFT,padx=10)
 
root.mainloop()