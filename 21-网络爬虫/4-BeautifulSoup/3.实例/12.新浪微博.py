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
            'Cookie': 'SINAGLOBAL=3141108771060.63.1553863967185; UM_distinctid=16e88aa439529a-00db7a6cc5b9e6-7711439-144000-16e88aa43961ae; un=dkgll; wvr=6; UOR=,,www.baidu.com; login_sid_t=2abc3f4284d18af3a44480575e6a2d88; cross_origin_proto=SSL; _s_tentry=www.baidu.com; Apache=8075098235356.297.1585409863467; ULV=1585409863476:48:4:3:8075098235356.297.1585409863467:1585191715647; SCF=Asm90sASrBEdSoAUTl_xQ4mG-rF2FWxpJMzIoK33r9V9mXlrtpWb660mYCe1mYwWpj13TixYHyscSVOVVPU7r4I.; SUB=_2A25zex8EDeRhGedO7FEZ9S_MzD2IHXVQ8XfMrDV8PUNbmtAfLRfYkW9NXP80YHq-2wWl0gsjfOh276oZwwrX8qfy; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWCdf6o_QAvdcfTjm28zmwZ5JpX5K2hUgL.Fo27S0eRSK27S022dJLoIEBLxKqL1hnL1K2LxKqLB-eLBozLxK.L1-2L12qLxK-LB.qL1het; SUHB=0WGN35qa2WUtkR; ALF=1616945875; SSOLoginState=1585409876; webim_unReadCount=%7B%22time%22%3A1585409892308%2C%22dm_pub_total%22%3A2%2C%22chat_group_client%22%3A0%2C%22allcountNum%22%3A72%2C%22msgbox%22%3A0%7D'
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