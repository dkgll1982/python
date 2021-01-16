#!/usr/bin/env python 
# -*- coding:utf-8 -*-  
# @Author: suixin 
# @Company: Aerospace Shenzhou Intelligent System Technology Co., Ltd  
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2021-01-07 14:30:13 
# @Remark: Life is short, I use python！ 
# @Software: vscode 

import scrapy 
from scrapy.http import Request
from ..items import MatplotlibFileItem
# 参考链接：https://blog.csdn.net/qq_43537354/article/details/88360636?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-1.control&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-1.control

# FilesPipeline的工作流如下：

# 1. 在spider中爬取要下载的文件链接，将其放置于item中的file_urls。
# 2. spider将其返回并传送至pipeline链。
# 3. 当FilesPipeline处理时，它会检测是否有file_urls字段，如果有的话，会将url传送给scarpy调度器和下载器。
# 4. 下载完成之后，会将结果写入item的另一字段files，files包含了文件现在的本地路径（相对于配置FILE_STORE的路径）、文件校验和checksum、文件的url

class ExampleSpider(scrapy.Spider):
    name = 'example'
    allowed_domains = ['matplotlib.org']
    start_urls = ['https://matplotlib.org/examples/index.html']

    def parse(self, response):
        #每一个例子的网址
        urls = response.xpath('//li[@class="toctree-l2"]/a/@href').extract()
        for url in urls:
            url = 'https://matplotlib.org/examples/' + url
            yield Request(url = url, callback = self.parse_example)

    def parse_example(self, response):
        #进入例子中的source code的网址
        href = response.xpath('//a[@class="reference external"]/@href').extract()[0]
        #构造完整的url
        url = response.urljoin(href)
        item = MatplotlibFileItem()
        
        # 在Spider解析一个包含文件下载链接的页面时，将所有下载的文件所需要的url地址收集到一个列表，赋给item的file_urls字段。
        # FilesPipeline在处理每一项item时，会读取item[‘file_urls’]，对其中的每一个url进行下载。注意！！！
        item['file_urls'] = [url]
        yield item