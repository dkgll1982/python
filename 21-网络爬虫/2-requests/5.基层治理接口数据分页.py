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
        
class JczlSpider(object):    
    def __init__(self,url):    
        self.file_name = r'backup\接口.json'
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
    def send_request(self,url,header,params):
        response = self.session.get(url = url,headers = header,params = params) 
        if response.status_code == 200:
            return response.json()
        else:
            print('URL：{}，状态码：{}'.format(url, response.status_code))
    
    def start(self): 
        params = self.query
        self.pagelen = 1024000                          #设置单次取数据字节限制1mb
        params["offset"] = '0'
        params["limit"] = '1'        
        
        #先查询总数
        res = self.send_request(self.base_url,self.header,params)
        if res:
            size = len(str(res["data"]["rows"]))        #查询单行记录长度
            total = res["data"]["total"]                #查询记录总数
            page_num = math.ceil(1024000/size)          #每页数据行数
            page_size = math.ceil(total/page_num)       #总页数,接口调用次数
            
            open(self.file_name, 'w').close()           #先清空文本内容
            
            for index in range(page_size):
                params["offset"] = index * page_num
                params["limit"] = page_num 
                
                #分页查询数量
                res2 = self.send_request(self.base_url,self.header,params)  
                if res2:       
                    json_append(file_name = self.file_name,json_data = res2["data"]["rows"])
                    print(f"全部记录：{total}条，当前第{index+1}/{page_size}次查询：{index * page_num}到{index * page_num + page_num}条记录完毕！")
 
if __name__=='__main__':
    #接口地址
    url = 'http://huzhou-jczl-wx.spacecig.com/zhzlbackend/check/safeCheckList?1=1&offset=0&limit=10&orderby=&ordertype=&keyword=&gid=&name=&num=&checker=&illegal=&startTime=&endTime=&startDate=&endDate=&userId='
    jczls  = JczlSpider(url)
    jczls.start()