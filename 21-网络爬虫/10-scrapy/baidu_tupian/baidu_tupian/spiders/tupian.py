#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: Aerospace Shenzhou Intelligent System Technology Co., Ltd 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2020-08-29 14:50:53 
# 参考链接：https://blog.csdn.net/ck784101777/article/details/105466589

import scrapy
import json
from urllib import parse
from ..items import BaiduTupianItem

class TupianSpider(scrapy.Spider):
    name = 'tupian'
    allowed_domains = ['image.baidu.com']
    
    word_origin = input("请输入搜索关键字：")
    word = parse.quote(word_origin)
    
    #图片查询页面
    url = "https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord="+word+"&cl=2&lm=-1&hd=0&latest=0&copyright=0&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=0&ic=0&word="+word+"&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&fr=&pn={}&rn=30&gsm=186&1598686624425="

    #重写start_requests方法，构造新的请求地址
    def start_requests(self):
        #页数可调整，开始页30,每次递增30
        for x in range(30,180,30):
            url = self.url.format(x)
            yield scrapy.Request(url = url,callback = self.parse)
   
    def parse(self, response): 
        dict_img = json.loads(response.text)    #json转换成字典
        for index,img in enumerate(dict_img['data'],start = 1):
            item = BaiduTupianItem()
            item['image_url'] = img["thumbURL"]
            #将搜索内容赋值给item,创建文件夹会用到
            item['word'] = self.word_origin
            item['name'] = self.word_origin + "_" + str(index)
            yield item