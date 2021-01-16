#!/usr/bin/env python 
# -*- coding:utf-8 -*-  
# @Author: suixin 
# @Company: Aerospace Shenzhou Intelligent System Technology Co., Ltd  
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2021-01-10 11:04:00 
# @Remark: Life is short, I use python！ 
# @Software: vscode 

import scrapy,json
from scrapy.http import Request
from ..items import XimalayaMusicItem

class MusicSpider(scrapy.Spider):
    name = 'music'
    host = "www.ximalaya.com"
    allowed_domains = [host] 
    start_urls = [f'https://{host}/yinyue/liuxing/p1']

    def parse(self, response):
        # 第一步：获取节目列表
        item_urls = response.xpath("//div[@class='content']/ul/li/div/a/@href").extract()
        
        #item_urls = [item_urls[0]]  #测试取第一条
        for url in item_urls:
            #第二步：循环跳转到每个节目的详情页      
            url = response.urljoin(url)      
            yield Request(url = url, callback = self.music_parse)
        
        #爬取10页
        for x in range(2,11):
            next_page = f'https://{self.host}/yinyue/liuxing/p{x}'
            yield Request(url = next_page, callback=self.parse)
    
    #解析节目里的音乐详情
    def music_parse(self,response):
        print('-'*40,'进入调试!')
        
        # 歌曲类型
        file_type = self.replace_str(response.xpath("//h1[@class='title vA_']/text()").get())
        # 第三步：获取音乐列表
        music_list = response.xpath('//div[@class="text lF_"]')
        
        #music_list = [music_list[0]]
        for music in music_list:
            #第四步：获取音乐名称和链接地址
            file_name = self.replace_str(music.xpath("a/span[@class='title lF_']/text()").get())
            
            #调取此链接获取文件的真实地址
            music_link = f"https://{self.host}/revision/play/v1/audio?id=" + music.xpath("a/@href").get().split('/')[-1] + "&ptype=1"
            
            #第五步：获取音乐的真实链接地址
            yield Request(url = music_link, callback = self.real_musci_parse,meta = {'file_type':file_type,"file_name":file_name}, dont_filter = True)
            
    #获取音乐的真实链接地址        
    def real_musci_parse(self,response): 
        item = XimalayaMusicItem()
        # 提取每次Response的meta数据
        item["file_type"] = response.meta['file_type']
        item["file_name"] = response.meta['file_name']
        #返回json,转化python字典类型
        data = json.loads(response.text) 
        item["file_urls"] = [data["data"]["src"]]
        yield item 
    
    def replace_str(self,repstr):
        return repstr.replace('|','').replace(' ', '').replace('-','_').replace('(','').replace(')','') \
                     .replace('（','').replace('）','').replace('~','').replace('`','').replace('【','') \
                     .replace('】','').replace('[','').replace(']','').replace(':','').replace('：','') \
                     .replace('&','').replace('、','').replace('\\','').replace('/','').replace('$','') \
                     .replace(',','').replace('，','').replace('《','').replace('》','').replace('！','') \
                     .replace(',','').replace('，','').replace('《','').replace('》','').replace('<','') \
                     .replace('>','').replace('?','').replace('？','')        