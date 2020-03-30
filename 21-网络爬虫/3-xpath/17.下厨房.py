#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: Aerospace Shenzhou Intelligent System Technology Co., Ltd 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2020-03-21 21:33:17 
# @Remark: 人生苦短，我用python！

import time
import requests
from lxml import etree
import os 
from urllib import parse
import emoji
import re
import json

#返回的内容带有emoji表情，需要过滤
def filter_emoji(desstr,restr=''):
    '''
    过滤表情
    '''
    try:
        co = re.compile(u'[\U00010000-\U0010ffff]')
    except re.error:
        co = re.compile(u'[\uD800-\uDBFF][\uDC00-\uDFFF]')
    return co.sub(restr, desstr)

class XiaChuFangSpider(object):
    def __init__(self):
        super().__init__()
        self.host = "http://www.xiachufang.com"
        self.url = self.host + "/category/40076/?page={}"
        self.headers = {     
            "user_agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'         
        }    
    
    def send_request(self,page_num):
        response = requests.get(self.url.format(page_num),headers = self.headers)
        if response.status_code == 200:
            return response
    
    def parse_request(self,response):
        html = etree.HTML(response.content)
        li_list = html.xpath("//div[@class='recipe recipe-215-horizontal pure-g image-link display-block']")
        cai = {}
        for li in li_list:
            cai['name'] = li.xpath('..//div[@class="info pure-u"]/p[1]/a[1]/text()')[0].replace('\n','').replace(' ','')
            cai['href'] = parse.urljoin(self.host,li.xpath('..//div[@class="info pure-u"]/p[1]/a[1]/@href')[0])
            cai['zuoliao'] = ','.join(li.xpath('..//div[@class="info pure-u"]/p[2]/a/text()'))
            cai['pingjia'] = ''.join(li.xpath('..//div[@class="info pure-u"]/p[@class="stats"]//text()')).replace('\n','').replace(' ','').replace('\xa0','')
            self.parse_detail(cai) 
        
    def parse_detail(self,dict):
        url = dict["href"]
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            html = etree.HTML(response.content)
            dict["desc"] = "".join(html.xpath('//div[@class="desc mt30"]//text()')).replace('\n','').replace(' ','').replace('\xa0','')
            
            #如果字典内容带有emoji表情，可能导致输出内容不正常
            dict["desc"] = filter_emoji(dict["desc"])   
            
            tr_list = html.xpath("//tr[contains(@itemprop,'recipeIngredient')]")
            all_zl = ''
            for tr in tr_list:
                zl = tr.xpath('./td//text()')
                all_zl += "".join(zl).replace('\n', "").replace(" ", "")
                all_zl += ","
            dict["yongliao"] = all_zl.rsplit(',', 1)[0]   
            dict["step"] = "".join(html.xpath('//li[@class="container"]//text()')).replace('\n', "").replace(" ", "").replace('\xa0','')  
            self.write_content(dict)      
    
    def write_content(self,content):
        with open(r'backup/爬虫/菜谱/caipu.json','a',encoding="utf-8") as f: 
            json.dump(content,f,indent=2,ensure_ascii=False)

    def start(self):
        for x in range(1,50):
            response = self.send_request(x)
            if response:
                self.parse_request(response)
                print('爬取第%d页成功！'%x)
    
if __name__ == "__main__":
    start = time.time()
    xcfs = XiaChuFangSpider()
    xcfs.start()
    end = time.time()
    
    print('爬取数据完成，耗时%.2fs!'%(end-start))