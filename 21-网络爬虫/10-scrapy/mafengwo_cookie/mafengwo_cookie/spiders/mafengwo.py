#!/usr/bin/env python 
# -*- coding:utf-8 -*-  
# @Author: suixin 
# @Company: Aerospace Shenzhou Intelligent System Technology Co., Ltd  
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2021-01-20 15:08:46 
# @Remark: Life is short, I use python！ 
# @Software: vscode 
# 参考链接：https://www.mubanjun.cn/8143.html

import scrapy
import re

class MafengwoSpider(scrapy.Spider):
    name = 'fw'
    allowed_domains = ['mafengwo.cn']
    #开始的url为我们个人主页
    start_urls = ['http://www.mafengwo.cn/u/53787390/note.html']
    def start_requests(self):
        #添加headers
        headers={
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9,am;q=0.8',
            'Connection': 'keep-alive',
            'Host': 'www.mafengwo.cn',
            'Referer': 'http://www.mafengwo.cn/u/53787390.html',
            'Upgrade-Insecure-Requests': 1,
            #可以添加UA，或者在settings更换
        }
        #我们手动登录马蜂窝，找到cookies，cookies格式 通过:分割，等号左边(key):等号右边(value)
        cookies='br-resp-key="g:21012014265153700000007006070e5738"; __jsluid_h=8f716362a9d028d315d435463ae8b127; __jsl_clearance=1611123688.532|0|cE%2BdJss4yhVa8AuAfiibZqog%2FUA%3D; PHPSESSID=9dvb4fdig8dn9pkr60giqefjv0; mfw_uuid=6007cbea-5fbe-0e77-c643-789ec74a265f; oad_n=a%3A3%3A%7Bs%3A3%3A%22oid%22%3Bi%3A1029%3Bs%3A2%3A%22dm%22%3Bs%3A15%3A%22www.mafengwo.cn%22%3Bs%3A2%3A%22ft%22%3Bs%3A19%3A%222021-01-20+14%3A21%3A30%22%3B%7D; __mfwc=direct; __mfwa=1611123691617.94047.1.1611123691617.1611123691617; __mfwlv=1611123691; __mfwvn=1; uva=s%3A91%3A%22a%3A3%3A%7Bs%3A2%3A%22lt%22%3Bi%3A1611123691%3Bs%3A10%3A%22last_refer%22%3Bs%3A23%3A%22http%3A%2F%2Fwww.mafengwo.cn%2F%22%3Bs%3A5%3A%22rhost%22%3BN%3B%7D%22%3B; __mfwurd=a%3A3%3A%7Bs%3A6%3A%22f_time%22%3Bi%3A1611123691%3Bs%3A9%3A%22f_rdomain%22%3Bs%3A15%3A%22www.mafengwo.cn%22%3Bs%3A6%3A%22f_host%22%3Bs%3A3%3A%22www%22%3B%7D; __mfwuuid=6007cbea-5fbe-0e77-c643-789ec74a265f; Hm_lvt_8288b2ed37e5bc9b4c9f7008798d2de0=1611123692; UM_distinctid=1771e7494fafa-0b780474633bb2-c791039-144000-1771e7494fc2fd; CNZZDATA30065558=cnzz_eid%3D1341152524-1611122278-http%253A%252F%252Fwww.mafengwo.cn%252F%26ntime%3D1611122278; c=07w7gWGQ-1611123920386-7d3a66a90fc7d21780133; _fmdata=B%2Fk8OnsoHjI1k76vkVAzwCC3SppzIwQOcEPDgkjybC1Q%2B6mo3IYVvv%2BaGEJrcPB22Q%2BUdM4GMsg6z5wuUPUA7zdQBT8vn4FsLA4RtC58mI4%3D; _xid=lTIfQUo4M3rGp2Pvp2aNXY4eOMhTxkT76JPkAYtuQxw29LJSSmor%2Ftid%2BAt2%2FkQROkoZ8CY%2FkhOqAtOzxyTTmg%3D%3D; login=mafengwo; mafengwo=280d682a266020aac615956f11056245_53787390_6007cd23df9a33.46061760_6007cd23df9a75.05918274; mfw_uid=53787390; __omc_chl=; __omc_r=; bottom_ad_status=0; uol_throttle=53787390; __mfwb=454d9f296ee2.10.direct; __mfwlt=1611124639; Hm_lpvt_8288b2ed37e5bc9b4c9f7008798d2de0=1611124640'
        cookies={i.split('=')[0]:i.split('=')[1] for i in cookies.split('; ')}
        yield scrapy.Request(
            self.start_urls[0],
            cookies=cookies,
            headers=headers,
            callback=self.parse,
        )
    def parse(self, response): 
        with open(r'data/myhome.html','w',encoding='utf8') as f:
            f.write(response.body.decode())