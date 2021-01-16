#!/usr/bin/env python 
# -*- coding:utf-8 -*-  
# @Author: suixin 
# @Company: Aerospace Shenzhou Intelligent System Technology Co., Ltd  
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2020-12-29 16:35:55 
# @Remark: Life is short, I use python！ 
# @Software: vscode 
# 参考链接(scrapy爬虫下载音频文件并储存到本地)：https://www.cnblogs.com/jaysonteng/p/12931775.html

import scrapy
from ..items import TingroomAudioItem
from urllib import parse
import time
from scrapy import Selector
from scrapy.utils.project import get_project_settings

class TingroomSpider(scrapy.Spider):
    name = 'tingroom'
    allowed_domains = ['www.tingroom.com']
    start_urls = ['http://www.tingroom.com/lesson/']             # 起始网页，通过起始网页解析获取更多url，然后直到解析到所需音频链接
    root_dir = get_project_settings().get('FILES_STORE') + '\\'  # 获取根目录，在setting文件中定义的变量

    def parse(self, response):
        # response.body  # 获取音频图片下载到的数据，以二进制写入文件的方式储存
        listenning_rts = response.xpath('/html/body/div[5]//ul[@id="line_01"]//a')
        for class1_rt in listenning_rts:
            class1_title = class1_rt.xpath('./text()').extract_first().strip()
            class1_path = self.root_dir + class1_title              # 判断title文件夹是否存在
            first_url = class1_rt.xpath('./@href').extract_first().strip()
            first_url = response.urljoin(first_url)                 # 类别1链接
            meta = {'result_path': class1_path} 
            print('first_url:', first_url)
            yield scrapy.http.Request(first_url, meta=meta, callback=self.listenningParse)  # 将获取到的连接传给listenningParse进行进一步解析，通过meta传递参数
            #break
        
    def listenningParse(self, response):        # 听力板块解析
        meta = response.meta                    # meta是字典若直接使用meta['']取值，若无会报错。采用get方法，若无数据不会报错，且返回None
        result_path = meta.get('result_path')   # 当前文件列表的目录
        
        # 获取下一页数据
        next_url = response.xpath('//div[@class="dede_pages"]//a[text()="下一页"]/@href')
        if next_url:
            next_url = next_url.extract_first()
            next_url = response.urljoin(next_url)                                           # 下一页链接，再调用自己处理数据
            yield scrapy.http.Request(next_url, meta=meta, callback=self.listenningParse)   # 调用自身，继续执行
        # 获取所有内容的标题和正文链接
        article_rts = response.xpath('//a[@class="goog"]')
        if article_rts:
            for article_rt in article_rts:
                article_url = article_rt.xpath('./@href').extract_first().strip()
                article_url = response.urljoin(article_url)
                article_title = article_rt.xpath('./text()')
                if article_title:
                    article_title = article_title.extract_first().strip().replace(':', '：').replace('/',
                        '_').replace('\\', '_').replace('*', '').replace('?', '？').replace('\"', '”').replace('|', 
                        '').replace('<', '《').replace('>', '》').replace(' ', '_')
                    meta['article_title'] = article_title
                    # 传给listenningArticlePage继续解析
                    yield scrapy.http.Request(article_url, meta=meta,callback=self.listenningArticlePage)  

    def listenningArticlePage(self, response):  # 进入正文
        # 获取参数    
        meta = response.meta      
        # 获取正文内容：文本，字幕
        rs_texts = response.xpath('//div[@class="content"]//text()').extract()
        rs_text = [i.strip().replace('\n', '').replace('\r', '').replace('\t', '').replace('\xa0', '') for i in
                   rs_texts]
        while '' in rs_text:
            rs_text.remove('')
        file_text = []
        for rs in rs_text:
            # 用于分割正文和单词
            if rs == '点击':
                rs = '\n' + '=' * 60 + '\n' + '\n重要词汇：'
            # 如果是纯数字，或其他字符串，就跳过
            elif 'google_ad_client' in rs or 'tingroom' in rs or '单词翻译:' in rs or '收听单词发音' == rs or rs.isdigit():
                continue
            file_text.append(rs + '\n')
        
        # 获取下载链接，返回给pipeline下载并储存文件
        download_rt = response.xpath('//param[@name="movie"]/@value')
        if download_rt:
            download_url = download_rt.re_first('http:.*')          # 下载链接
            file_type = download_rt.re_first('com.*(\..*)')         # 根据下载链接，获取下载文件类型，有的是mp3，有的是rm等
            if not file_type:
                return
            file_name = meta.get('article_title') + file_type
            file_path = meta.get('result_path') + '\\' + file_name  # 文件储存目录 + 名称
            text_path = meta.get('result_path') + '\\' + meta.get('article_title') + '.txt'  # 文本储存目录 + 名称

            item = TingroomAudioItem()          # item中定义的字段，此处通过其建立对象
            item['file_text'] = file_text       # 通过字典方法，存入数据
            item['text_path'] = text_path       # 文本路径 + 文件名，用于存储。因为是自定义储存，所以文本路径是绝对路径
            item['file_paths'] = [file_path]    # 音频储存路径，因为是scrapy储存，所以可以是相对路径，可以是绝对路径。
            item['file_urls'] = [download_url]  # 音频下载链接
            yield item                          # 此处，会将下载链接等信息传给pipeline，pipeline里面配置好，会自动下载并储存文件