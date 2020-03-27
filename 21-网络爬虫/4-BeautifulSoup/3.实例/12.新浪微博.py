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

class WeiBoSpider():
    def __init__(self):
        super().__init__()
        self.url = 'https://s.weibo.com/weibo?q=%E6%88%90%E9%83%BD%E4%B8%83%E4%B8%AD%E7%BE%8E%E9%A3%9F&Refer=SWeibo_box'
        self.base_dir = r'backup/爬虫/微博'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36',
            'Cookie': 'SINAGLOBAL=3141108771060.63.1553863967185; UM_distinctid=16e88aa439529a-00db7a6cc5b9e6-7711439-144000-16e88aa43961ae; _s_tentry=www.baidu.com; Apache=2775841346126.4995.1585024132452; ULV=1585024132491:46:2:1:2775841346126.4995.1585024132452:1584718911865; login_sid_t=662130e3fdfa40e5398d791ace11dd1a; cross_origin_proto=SSL; WBtopGlobal_register_version=3d5b6de7399dfbdb; UOR=,,www.sina.com.cn; un=dkgll; wvr=6; SCF=Akw6l0ddwQgGEnkzbbUnAm3ALPNZ7pGVsWUJLLEjSLXhPOcPxcjDl_7ZK_UezieNS0QunCCtnzgsPDBKUFPZCMo.; SUB=_2A25zfcxoDeRhGedO7FEZ9S_MzD2IHXVQCrqgrDV8PUNbmtAfLUqjkW9NXP80YGpoFZu8AennUCo51DTP2t0VCrtE; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWCdf6o_QAvdcfTjm28zmwZ5JpX5K2hUgL.Fo27S0eRSK27S022dJLoIEBLxKqL1hnL1K2LxKqLB-eLBozLxK.L1-2L12qLxK-LB.qL1het; SUHB=0pHgRwrWQfI9jJ; ALF=1616572342; SSOLoginState=1585036344; webim_unReadCount=%7B%22time%22%3A1585036469638%2C%22dm_pub_total%22%3A2%2C%22chat_group_client%22%3A0%2C%22allcountNum%22%3A69%2C%22msgbox%22%3A0%7D; WBStorage=42212210b087ca50|undefined'
        }
        self.form_data={
            'q':'成都七中美食',
            'Refer':'SWeibo_box'
        }
        if not os.path.exists(self.base_dir):
            os.mkdir(self.base_dir)
    
    def send_request(self,url):
        response = requests.get(url = url,headers = self.headers)
        if response.status_code == 200:
            return response
        else:
            print('URL：{}，状态码：{}'.format(url,response.status_code))
    
    def parse_content(self,response):
        #html = etree.HTML(response.content)
        self.write_content(self.base_dir+'/weibo.html',response.text)
        
    def write_content(self,path,content):
        with open(path,'w',encoding = 'utf-8') as f:
            f.write(content)
    
    def start(self):
        response = self.send_request(self.url)
        if response:
            self.parse_content(response)
        
if __name__ == "__main__":
    start = time.time()
    wbs = WeiBoSpider()
    wbs.start()
    end = time.time()
    print('爬取新浪微博完成，耗时%.2fs'%(end-start))