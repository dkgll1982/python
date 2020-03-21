#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: 航天神舟智慧系统技术有限公司 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2020-02-21 19:20:37 
# @Last Modified by: guojun 
# @Last Modified time: 2020-02-21 19:20:37 
# @Software: vscode 
# @Describe：健康码查询

from urllib import request
import http.cookiejar as cookielib
import urllib
import json
import urllib.parse
import os,cx_Oracle,sys
import threading,time,datetime
import hashlib
import xlrd,xlsxwriter 
import math

class JKMSpider():
    def __init__(self,file_name):
        os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
        self.dbuser = 'cigproxy'
        self.dbpwd = 'cigproxy'
        self.dbserver = '172.21.246.244:15211/xe'
        self.datatype = 'jkm_person'
        self.city = '杭州市'
        self.file_name = file_name  
        self.file_md5 = self.getfilemd5()
        
        self.pagecount = 9000        #每次取数据行数
        self.totalcount = 0          #总行数
        
        self.collist = '' 
        self.key_column = ''
        
        host = 'http://jczl.giscloud.cx/'
        login_url = host + "iam/saml/login"
        self.inter_url = host + "healthWeb/front/index/healthQuery"
        userpwd = {"userid":"admin", "password":"DFYOPS1RrpdVlu2U"}  
        
        # 通过CookieJar()类构建一个cookieJar()对象，用来保存cookie的值
        cookie = cookielib.CookieJar()
        # 通过HTTPCookieProcessor()处理器类构建一个处理器对象，用来处理cookie
        # 参数就是构建的CookieJar()对象
        cookie_handler = request.HTTPCookieProcessor(cookie)
        opener = request.build_opener(cookie_handler)

        # 自定义opener的addheadders的参数，可以赋值HTTP报头参数
        opener.addheaders = [("Content-type","application/json;charset=UTF-8"),("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.100 Safari/537.36")]
  
        # 通过urlencode()转码
        postdata = urllib.parse.urlencode(userpwd).encode('utf8')

        # 构建Request请求对象，包含需要发送的用户名和密码
        req = request.Request(login_url, data = postdata)

        # 通过opener发送这个请求，并获取登录后的Cookie值，
        response = opener.open(req)  

        # 可以按标准格式将保存的Cookie打印出来
        cookieStr = ""
        for item in cookie:
            cookieStr = cookieStr + item.name + "=" + item.value + ";"

        # 舍去最后一位的分号(此处取到cookie值)
        self.cookieStr = cookieStr[:-1]   
        
    def send_request(self,data):  
        headers = {
            "Host":'jczl.giscloud.cx',
            "Content-type":"application/json;charset=UTF-8",
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.100 Safari/537.36",
            "Cookie":self.cookieStr
        } 
 
        form_data = bytes(json.dumps(data), 'utf8')
 
        req = request.Request(self.inter_url,headers = headers, method='POST')
        response = urllib.request.urlopen(req,data = form_data)

        return response.read().decode('utf-8')  
    
    #获取文件md5值
    def getfilemd5(self): 
        md5 = ''
        if os.path.isfile(self.file_name):
            with open(self.file_name,'rb') as f:
                contents = f.read()
                f.close()
                md5 = hashlib.md5(contents).hexdigest()
        return md5 
    
    #读取excel，保存到db
    def savedb(self):  
        filemd5 = self.getfilemd5()
        # 1. 打开文件
        work_book = xlrd.open_workbook(self.file_name) 

        # 2 通过sheet页索引创建sheet页对象
        work_sheet = work_book.sheet_by_index(0)

        # 3.获取excel文件sheet页 行列数
        self.totalcount = work_sheet.nrows
        num_cols = work_sheet.ncols
        num_collist = work_sheet.row_values(0)
        
        print("导入的Excel文件(md5值:{})的列为:{}".format(self.file_md5,num_collist)) 

        db_conn=cx_Oracle.connect(self.dbuser, self.dbpwd, self.dbserver,encoding="UTF-8")
        db_cursor = db_conn.cursor()

        letter = 'ABCDEFGHIJKLMNOPQRSTUVWXY'    #excel_table的列为A,B,C,D这样的形式
        for x in range(len(num_collist)): 
            cname = num_collist[x].strip().replace('\n', '').replace('\r', '').replace('（','').replace('）','')[0:8] #oracle列名暂定8个汉字，25个英文字母的长度
            self.collist =  self.collist + 'ta.{} as "{}",'.format(letter[x],cname) 
            if '身份证' in cname:               #身份证号码作为关联列进行匹配    
                self.key_column = letter[x] 
                     
        col = ''
        for l in letter[0:num_cols]: 
            col = col +',:' + l
        col = ':XH,:TYPE,:Z' + col   
        
        sql_del = "delete from excel_table where type='{}' and z='{}'".format(self.datatype,self.file_md5)
        sql_cmd = 'insert into excel_table({}) values ({})'.format(col.replace(':',''),col)
        db_cursor.execute(sql_del) 

        rn = 0 
        for curr_row in range(self.totalcount):
            rn = rn + 1
            row = work_sheet.row_values(curr_row)
            row.insert(0,rn) 
            row.insert(1,self.datatype)
            row.insert(2,self.file_md5) 
            db_cursor.execute(sql_cmd, row) 
            if rn%1000 == 0:            #每1000次提交一次结果
                db_conn.commit() 

        db_conn.commit() 
        db_cursor.close()
        db_conn.close() 
     
    #查询人口数据，调用接口 
    def get_data(self): 
        conn = cx_Oracle.connect(self.dbuser, self.dbpwd, self.dbserver,encoding="UTF-8") 
        cursor = conn.cursor()  
        
        #查询人口数据
        sql1 = """with T as (
            select {} sfzh from excel_table where type='{}' and z='{}' and exists(select * from excel_table where {} LIKE '%身份证%' )    
        ) 
        select sfzh,mzt,mffd FROM (  
            select DISTINCT replace(replace(trim(replace(replace(replace(replace(sfzh,chr(10)),CHR(32)),chr(13),chr(9)),' ')),'	'),'	') sfzh, '绿码' mzt,'{}' mffd from T 
            where sfzh NOT IN (
                select A from excel_table where TYPE='jkm' --and to_date(c,'YYYY-MM-DD HH24')>sysdate-0.25
            )  
        ) where LENGTH(SFZH)=18 and ROWNUM<""".format(self.key_column,self.datatype,self.file_md5,self.key_column,self.city) + str(self.pagecount) 
        sql2 = "" 
        
        cursor.execute(sql1)  
        rows = cursor.fetchall()  # 得到所有数据集
        rowindex = 0
        for row in rows:  
            rowindex = rowindex + 1  
            data = {"sfzh":row[0],"mzt":row[1],"mffd":row[2]}
            jsonstr = self.send_request(data)
            print('获取第%d条身份证：%s健康码（%s）成功!'%(rowindex,row[0],row[1]))
            sql2 = "INSERT INTO excel_table(TYPE,A,B,C,D) VALUES('jkm','%s','%s','%s','%s')"%(row[0],jsonstr,datetime.datetime.now().strftime('%Y-%m-%d %H'),row[1])
            cursor.execute(sql2)
          
        conn.commit() 
        cursor.close()
        conn.close()  
    
    #导出结果到Excel
    def imp_excel(self):
        file_name = '健康码查询结果{}'.format(datetime.datetime.now().strftime('%Y%m%d%H%M'))
        conn = cx_Oracle.connect(self.dbuser, self.dbpwd, self.dbserver,encoding="UTF-8") 
        cursor = conn.cursor()  
        
        #查询结果
        sql = """select distinct ta.xh,{}
            TO_SINGLE_BYTE(JSON_VALUE(tb.b,'$.data.mzt' )) 健康码状态,
            TO_SINGLE_BYTE(JSON_VALUE(tb.b,'$.data.hmcmyy' )) 红黄码原因,
            TO_SINGLE_BYTE(JSON_VALUE(tb.b,'$.data.scsqsj' )) 首次申请时间,
            TO_SINGLE_BYTE(JSON_VALUE(tb.b,'$.data.scffsj' )) 首次发放时间,
            TO_SINGLE_BYTE(JSON_VALUE(tb.b,'$.data.scffsj' )) 最近更新时间
        from excel_table ta 
        join ( 
            select a,b from (
                select a,b,c,row_number() over (partition by a order by to_date(c,'YYYY-MM-DD HH24') desc) rn from excel_table where type='jkm'
            ) where rn=1
        ) tb on ta.{}=tb.a and ta.TYPE='{}' and ta.z='{}' 
        order by ta.xh""".format(self.collist,self.key_column,self.datatype,self.file_md5)
         
        cursor.execute(sql)  
        rows = cursor.fetchall()  # 得到所有数据集 
        
        book = xlsxwriter.Workbook(file_name+'.xlsx') 
        sheet = book.add_worksheet('sheet1')

        # Write some data headers. 带自定义粗体blod格式写表头
        bold = book.add_format({'bold': True})
    
        #获取表的列名
        title = [i[0] for i in cursor.description]   
        sheet.write_row('A1',title)  
              
        rn = 1     
        for row in rows: 
            rn += 1
            sheet.write_row('A%d'%rn,row) 
            
        book.close()
        print('导出%s完成！'%(file_name))
        #打开文件
        os.startfile(file_name+'.xlsx') 
        cursor.close()
        conn.close()  
        
if __name__ == '__main__': 
    args = sys.argv 
    if len(args) > 1: 
        file_name = args[1]
        if os.path.isfile(file_name): 
            print("主线程(%s)启动"%(threading.current_thread().name))
            start = time.time()  
            
            jkm = JKMSpider(file_name)  
            jkm.savedb()  
            pagesize = math.ceil(jkm.totalcount/jkm.pagecount)+1
            for x in range(1,2): 
                jkm.get_data()
                print('第%d遍查询完毕！'%(x+1))
                
            # jkm.imp_excel()
                
            end = time.time()
            print("主线程(%s)结束,总耗时：%0.6f秒"%(threading.current_thread().name,end-start)) 
        else:
            print('Waring!!!,excel file path is not exist.') 
    else:
        print('Erorr!!!,please enter excel file path.') 
            