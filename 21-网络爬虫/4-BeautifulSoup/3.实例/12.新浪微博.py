#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: Aerospace Shenzhou Intelligent System Technology Co., Ltd 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2020-03-24 20:23:17 
# @Remark: 人生苦短，我用python！

import requests
from urllib import parse
import re
from lxml import etree
import os
import time
import cx_Oracle

os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'

class WeiBoSpider():
    def __init__(self):
        super().__init__()
        self.host = 'https://s.weibo.com'
        self.url = parse.urljoin(self.host,'/weibo')
        self.base_dir = r'backup/爬虫/微博'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36',
            'Cookie': 'SINAGLOBAL=3141108771060.63.1553863967185; UM_distinctid=16e88aa439529a-00db7a6cc5b9e6-7711439-144000-16e88aa43961ae; un=dkgll; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWCdf6o_QAvdcfTjm28zmwZ5JpX5K2hUgL.Fo27S0eRSK27S022dJLoIEBLxKqL1hnL1K2LxKqLB-eLBozLxK.L1-2L12qLxK-LB.qL1het; UOR=,,login.sina.com.cn; _s_tentry=login.sina.com.cn; Apache=2127291266101.1057.1586062059667; ULV=1586062059688:50:2:1:2127291266101.1057.1586062059667:1585969279494; WBStorage=42212210b087ca50|undefined; WBtopGlobal_register_version=3d5b6de7399dfbdb; SCF=AjShoweVB2eMIdWzoOQQ4HlW-oNrobjXx99gTO-x_uUce6YgVBpBAUgnL5cWnfuvijtgnplyZ3sbdQmyyYmHjgU.; SUB=_2A25zjRN4DeRhGedO7FEZ9S_MzD2IHXVQ-wOwrDV8PUNbmtAfLWvzkW9NXP80YKFCAbZ5p_AWcsI0-w7FbF0FCh3p; SUHB=0JvxupErcZ-_-4; ALF=1586666919; SSOLoginState=1586062120; un=dkgll'
        }
        if not os.path.exists(self.base_dir):
            os.mkdir(self.base_dir)
        self.page = None
        #ORACLE连接参数
        self.conn = cx_Oracle.connect('cigproxy','cigproxy','localhost/orcl')
        self.cursor = self.conn.cursor() 
        #建表语句
        # create table base_weibo_userinfo
        # (
        #   nickname varchar2(200),
        #   guanzhu number,
        #   fengsi number,
        #   weibo number
	    #   CREATE_DATE DATE DEFAULT sysdate
        # )

    
    #发送请求
    def send_request(self,url,params = None):
        response = requests.get(url = url,params = params,headers = self.headers)
        if response.status_code == 200:
            return response
        else:
            print('URL：{}，状态码：{}'.format(url,response.status_code))
    
    #解析请求
    def parse_content(self,response):
        html = etree.HTML(response.text)
        a_list = html.xpath("//div[@class='info']//a[@class='name']")
        for a in a_list:
            name = a.xpath('./text()')
            href = parse.urljoin(self.host,a.xpath('./@href')[0])
            #获取详情
            detail_res = self.send_request(href)
            if detail_res:
                self.parse_detail(detail_res) 
        if not self.page:
            self.page = len(html.xpath("//ul[@class='s-scroll']//li"))   #页数 

    #解析详情
    def parse_detail(self,response):
        content = response.text
        partten = re.compile('var url = "(.*)?"')
        #由于跳转后页面会重定向，此处获取重定向后的URL地址，再去请求
        real_url = re.search(partten,content).group(1)
        #获取用户的详细信息
        real_res = self.send_request(real_url)
        if real_res:
            self.parse_userinfo(real_res)
    
    #解析用户信息
    def parse_userinfo(self,response):
        content = response.text
        partten = re.compile('<h1 class=."username.">(.*?)<./h1>')
        name = re.search(partten,content).group(1)
        #反斜杠是转义字符，可以用'\\'代替
        partten = re.compile('<strong class=."W_f\d+.">(.*?)<./strong>')
        num = re.findall(partten,content)  
        params = {
            "1":'',
            "2":'',
            "3":'',
            "4":'',
        }
        params["1"] = name
        for x in range(len(num)):
            params["%d"%(x+2)] = num[x]            
        self.insert_record(params)
    
    # 执行添加记录的SQL    
    def insert_record(self,params):
        sql = "INSERT INTO base_weibo_userinfo(nickname,guanzhu,fengsi,weibo) values(:1,:2,:3,:4)" 
        self.cursor.execute(sql,params) 
    
    def start(self):        
        params = {
            'q':'双十一',   
            'Refer':'SWeibo_box'
        }
        response = self.send_request(self.url,params)
        if response:
            self.parse_content(response)        #首次调用并返回页码信息
            if self.page:
                for x in range(2,self.page+1):
                    params['page'] = x
                    response = self.send_request(self.url,params)
                    if response:
                        self.parse_content(response) 
                    print('爬取第{}页完成！'.format(x))
                    time.sleep(1) 
                    self.conn.commit()        
        self.conn.commit()
        self.cursor.close()
        self.conn.close()                  
        
if __name__ == "__main__":
    start = time.time()
    wbs = WeiBoSpider()
    wbs.start()
    end = time.time()
    print('爬取新浪微博完成，耗时%.2fs'%(end-start))