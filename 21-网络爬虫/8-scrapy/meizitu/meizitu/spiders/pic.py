#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: Aerospace Shenzhou Intelligent System Technology Co., Ltd 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2020-08-28 11:04:34 
# 参考链接：https://www.jianshu.com/p/00c619939f66

from urllib.parse import urljoin
from scrapy.spiders import Spider
from scrapy.http import Request
from meizitu.items import PicscrapyItem
# 在你需要输出日志的地方设置，比如 your_spider.py
import logging

logger = logging.getLogger(__name__)
class PicSpider(Spider):
    name = "pic"  # 定义爬虫名，启动爬虫的时候用到
    start_url = 'http://www.win4000.com/wallpaper_2285_0_10_1.html'  # 爬虫入口
    # 设置爬虫的请求头，防止爬取失败
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 '
                      '(KHTML, like Gecko) Chrome/59.0.3071.104 Safari/537.36',
    }
    def start_requests(self):
        # 据观察，爬取的页面url是有规律的，后面的数字从1到167变化
        for i in range(1, 167):
            url = 'http://www.win4000.com/wallpaper_2285_0_10_%d.html' % i
            yield Request(url, headers=self.headers)

    def parse(self, response): 
        item = PicscrapyItem()
        # 获取页面所有的img标签地址，待下载
        # 注意：这里取得是全站的页面图片。粒度很粗，未做任何过滤，如果有些小图片或者某些类型图片不需要，最好是按照范围进行筛查 
        img_list = response.xpath('//img')
        for img in img_list:
            alt = img.xpath('./@alt').extract_first()   
            if alt:                         #没有标注图片名称的不进行爬取     
                item['image_urls'] = img.xpath('./@src').extract_first()
                item['category'] = alt
                logger.warning(item)        #打印日志
                yield item

        # 提取界面所有的url，待爬取
        all_urls = response.xpath('//a/@href').extract()

        # 遍历获得的url，如果满足条件，继续爬取
        for url in all_urls:
            url = urljoin(self.start_url, url)
            yield Request(url, callback=self.parse)