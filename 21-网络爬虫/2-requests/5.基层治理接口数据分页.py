#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: Aerospace Shenzhou Intelligent System Technology Co., Ltd 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2020-07-08 15:37:52 
# @Remark: 人生苦短，我用python！
# 参考链接：（将URL按一定的格式进行拆分）https://www.cnblogs.com/fanjc/p/9910292.html

import requests 
import json
from urllib import parse
import math 
from threading import Thread
import time
import pandas as pd

#json数据追加
def json_append(file_name,json_data,key = 'data'):  
    with open(file_name,'a+',encoding="utf-8") as f:
        # 因为是追加方式打开，默认偏移量再最后面，我们调整到开头
        f.seek(0)                       
        # 判断是否为空，如果为空的话创建一个新的字典格式 
        if f.read() =='':              
            data = {}
        else:
            f.seek(0)
            data = json.load(f) 
        if data != {}:  
            data[key][len(data[key]):len(data[key])] = json_data 
        else:
            data[key] = json_data         
        # 设置文件当前位置 0代表开始处 其实有两个参数 offset,whence （whence常用有三个参数0，1，2；0 代表从文件开头开始算起，1 代表从当前位置开始算起，2 代表从文件末尾算起。）
        f.seek(0)                       
        # 如果操作成功，则返回新的文件位置，如果操作失败，则函数返回 -1。
        # 从开头截断，截断文件为size个字符，无参代表 从当前位置截断，截断之后后面的所有字符都被删除
        f.truncate()                    
        json.dump(data,f,indent=2,ensure_ascii=False)

#json数据转化为excel        
def json_excel(json_file,excel_file):    
    data = []           # 用于存储每一行的Json数据
    j = json.load(open(json_file, 'r', encoding='utf-8')) 
    data.append(j)
    df = pd.DataFrame() # 最后转换得到的结果
    for line in data:
        for i in line:  
            df1 = pd.DataFrame([i])
            df = df.append(df1)

    # 在excel表格的第1列写入, 不写入index
    df.to_excel(excel_file, sheet_name='Data', startcol=0, index=False)

class JczlSpider(object):    
    def __init__(self,url):    
        self.file_name = r'backup\js\接口_{}.{}' 
        self.session = requests.Session()
        parse_list = list(parse.urlparse(url)) 
        self.host = parse_list[0] + '://' + parse_list[1]
        #提取url中的参数，即url中?后的内容
        self.query = parse.parse_qs(parse_list[4])      
        self.login_url = parse.urljoin(self.host,'/iam/saml/login')
        self.base_url = parse.urljoin(self.host, parse_list[2])
        self.header = {
            "Content-type":"application/json;charset=UTF-8",
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.100 Safari/537.36"
        }
        self.param = {
            "userid":"admin", 
            "password":"DFYOPS1RrpdVlu2U"
        }  
        self.session.post(self.login_url,data = self.param) 
    
    #发送请求
    def send_request(self,url,header,params,file_name=None):
        response = self.session.get(url = url,headers = header,params = params) 
        if response.status_code == 200:
            try:        
                if file_name is not None:                           #测试返回数据是否解析json异常,便于事后进行分析
                    self.write_content(file_name,response.url+'\r\n'+response.text)     
                return response.json()
            except Exception as e: 
                print('JSON解析错误：{}'.format(e))    
                self.write_content(r'backup\js\error.txt',response.url+'\r\n'+response.text,mode='w')
        else:
            print('URL：{}，状态码：{}'.format(url, response.status_code))    
    
    #获取每页的数据
    def get_pagerows(self,total,page_size,index,page_num,retry_count=0):    
        params = self.query
        params["offset"] = index * page_num
        params["limit"] = page_num 
        next_index = index * page_num + page_num
        if next_index > total:
            next_index = total
                
        #分页查询数据 
        res2 = self.send_request(self.base_url,self.header,params,self.file_name.format(index+1,'html'))  
        if res2:   
            try:    
                #html_file = self.file_name.format(index+1,'html')       #html文件
                json_file = self.file_name.format(index+1,'json')       #json文件
                excel_file = self.file_name.format(index+1,'xlsx')      #excel文件
                
                if 'data' in res2:              #判断返回的JSON是否包含data属性               
                    json_content = json.dumps(res2["data"]["rows"], indent=4, ensure_ascii=False)     
                    
                    #self.write_content(html_file,json_content)                           
                    self.write_content(json_file,json_content)
                    json_excel(json_file,excel_file)
                    
                    print(f"线程{index+1}/{page_size}查询(记录总数:{total})第{index * page_num}到{next_index}条记录完毕！")  
                elif retry_count == 0:          #如果接口返回数据有误，重试且只重试一次 
                    self.get_pagerows(total,page_size,index,page_num,1)                         
            except Exception as e: 
                self.write_content(self.file_name.format(index+1,'txt'),'请求出错，错误原因：%s,%s'%(e,json.dumps(res2, indent=4, ensure_ascii=False))) 
    #写入文件
    def write_content(self,filename,content,mode='w'):
        with open(filename, mode=mode,encoding="utf-8") as f:
            f.write(content)
        
    def start(self): 
        params = self.query
        pagelen = 512000                                #设置单次取数据字节限制500kb
        params["offset"] = '0'
        params["limit"] = '1'        
        
        #先查询总数
        res = self.send_request(self.base_url,self.header,params)
        if res:
            size = len(str(res["data"]["rows"]))        #查询单行记录长度
            total = res["data"]["total"]                #查询记录总数
            page_num = math.ceil(pagelen/size)          #每页数据行数
            page_size = math.ceil(total/page_num)       #总页数,接口调用次数
                        
            #2020-07-09测试例子：单线程需要80秒，多线程9秒，多线程效率高很多！
            ThreadList = []
            
            for index in range(page_size):
                ThreadList.append(Thread(target = self.get_pagerows, args=(total,page_size,index,page_num,)))
 
            for tr in ThreadList:
                tr.start()

            for tr in ThreadList:
                tr.join()

if __name__=='__main__': 
    start = time.time()
        
    #接口地址
    url = 'http://huzhou-jczl-wx.spacecig.com/zhzlbackend/check/safeCheckList?1=1&offset=0&limit=10&orderby=&ordertype=&keyword=&gid=&name=&num=&checker=&illegal=&startTime=&endTime=&startDate=&endDate=&userId='
    jczls  = JczlSpider(url)
    jczls.start()

    end = time.time() 
    print("查询数据完成！！！""总耗时：%0.2fs"%(end -start)); 
    