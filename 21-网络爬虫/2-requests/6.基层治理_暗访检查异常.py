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
import tablib

def json_append(file_name,key,json_data):  
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

        #print('{}添加后的值：{}'.format(key,data))
        
        # 设置文件当前位置 0代表开始处 其实有两个参数 offset,whence （whence常用有三个参数0，1，2；0 代表从文件开头开始算起，1 代表从当前位置开始算起，2 代表从文件末尾算起。）
        f.seek(0)                       
        # 如果操作成功，则返回新的文件位置，如果操作失败，则函数返回 -1。
        # 从开头截断，截断文件为size个字符，无参代表 从当前位置截断，截断之后后面的所有字符都被删除
        f.truncate()                    
        json.dump(data,f,indent=4,ensure_ascii=False)

# json数据转化为excel 
# json.text文件的格式： [{"a":1},{"a":2},{"a":3},{"a":4},{"a":5}]       
def json_excel(json_file,excel_file):    
    # 获取json数据
    with open(json_file, 'r',encoding='utf-8',errors='ignore') as f:
        rows = json.load(f).get('data')
        # 将json中的key作为header, 也可以自定义header（列名）
        header = tuple([ i for i in rows[0].keys()])
        data = []
        # 循环里面的字典，将value作为数据写入进去
        for row in rows:
            body = []
            for v in row.values():
                body.append(v)
            data.append(tuple(body))
        #将含标题和内容的数据放到data里
        data = tablib.Dataset(*data,headers=header)
        #写到桌面
        open(excel_file, 'wb').write(data.xls) 
            
class AnFangSpider(object):    
    def __init__(self,url):     
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
            "userid":"wxcs", 
            "password":"DFYOPS1RrpdVlu2U"
        }  
        self.session.post(self.login_url,data = self.param) 
    
    #发送请求
    def send_request(self,url,header,params,file_name=None):
        response = self.session.get(url = url,headers = header,params = params) 
        if response.status_code == 200:
            try:         
                return response.json()
            except Exception as e: 
                print('JSON解析错误：{}'.format(e))     
        else:
            print('URL：{}，状态码：{}'.format(url, response.status_code))        

    #解析请求
    def parse_request(self,response):
        total = response.get('data')["total"]
        rows = response.get('data')["rows"]
        for index,row in enumerate(rows,start=1):
            unit = [{
                "id": row["id"], 
                "placeName": row["placeName"],
                "oldPlaceName": row["oldPlaceName"], 
                "placeAddr": row["placeAddr"],   
                "isKeyPlace": row["isKeyPlace"],
                "displayName": row["displayName"],
                "checkDate": row["checkDate"],
                "checkLevel": row["checkLevel"],
                "RN": row["RN"],
                "safeType": row["safeType"],
                "task_num":[],
                "checkUserName":[],
                "description":[],
                "ill_list":[]
            }]
            place_id = row["id"]
            task_url = f"http://huzhou-jczl-wx.spacecig.com/zhzlbackend/anfang/anfangCheck/anfangCheckQuery?offset=0&limit=10&orderby=&ordertype=&dateFrom=2020-09-01&dateTo=2020-09-30&placeId={place_id}&status=2&departmentId=&issuePlaceQuery=1"
            task_res = self.send_request(task_url,self.header,None)              #获取任务列表
            if task_res:
                task_rows = task_res.get('data')["rows"]
                for task_row in task_rows:
                    task_id = task_row["id"]
                    
                    unit[0]["task_num"].append(task_row["num"])
                    unit[0]["checkUserName"].append(task_row["checkUserName"])
                    unit[0]["description"].append(task_row["description"]) 
                    
                    check_url = f"http://huzhou-jczl-wx.spacecig.com/zhzlbackend/anfang/anfangCheck/detail?id={task_id}"
                    check_res = self.send_request(check_url,self.header,None)·     #获取暗访检查信息
                    if check_res:
                        check_rows = check_res.get('data')["items"][0]["items"]
                        for check_row in check_rows:
                            if "select_value" in check_row:
                                select_value = check_row["select_value"]
                                if select_value == '是':    #异常项
                                    text = check_row["text"]
                                    opinion = check_row["opinion"]
                                    if opinion:
                                        text = text + '备注：' + opinion
                                    unit[0]["ill_list"].append(text) 
            json_append(r'backup\爬虫\暗访.json','data',unit)
            print(f'查询第{index}条记录成功...')
        
    #写入文件
    def write_content(self,filename,content):
        with open(filename,'w') as f:
            f.write(json.dumps(content,ensure_ascii=False))
        
    def start(self):    
        params = self.query
        params["offset"] = 0
        params["limit"] = 2000 
                
        #分页查询数据 
        res = self.send_request(self.base_url,self.header,params)
        if res:
            self.parse_request(res)
        
        #將json数据写入excel文件
        json_excel(r'backup\爬虫\暗访.json',r'backup\爬虫\暗访.xlsx') 

if __name__=='__main__': 
    start = time.time()
        
    #接口地址
    url = 'http://huzhou-jczl-wx.spacecig.com/zhzlbackend/anfang/anfangCheck/anfangPlaceQuery?offset=0&limit=2000&orderby=&ordertype=&issuePlaceQuery=1&departmentId=1125899906842624&startTime=2020-09-01&endTime=2020-09-30&dataFromType=report&visitSit=1&isCZW=&keyword='
    af  = AnFangSpider(url)
    af.start()

    end = time.time() 
    print("查询数据完成！！！""总耗时：%0.2fs"%(end -start)); 
    