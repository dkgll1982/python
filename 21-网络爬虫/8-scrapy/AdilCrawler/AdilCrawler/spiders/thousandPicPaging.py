# -*- coding: utf-8 -*-
import scrapy
# 导入链接规则匹配类，用来提取符合规则的连接
from scrapy.linkextractors import LinkExtractor
# 导入CrawlSpider类和Rule
from scrapy.loader import ItemLoader
from scrapy.spiders import CrawlSpider, Rule
import AdilCrawler.items as items

class ThousandpicpagingSpider(CrawlSpider):
    name = 'thousandPicPaging'
    allowed_domains = ['www.58pic.com']
    # 修改起始页地址
    start_urls = ['http://www.58pic.com/c/']

    # Response里链接的提取规则，返回的符合匹配规则的链接匹配对象的列表
    # http://www.58pic.com/c/1-0-0-03.html  根据翻页连接地址，找到 相应的 正则表达式   1-0-0-03  -> \S-\S-\S-\S\S  而且 这里使用 allow
    # 不能使用 restrict_xpaths ，使用 他的话，正则将失效
    page_link = LinkExtractor(allow='http://www.58pic.com/c/\S-\S-\S-\S\S.html', allow_domains='www.58pic.com')

    rules = (
        # 获取这个列表里的链接，依次发送请求，并且继续跟进，调用指定回调函数处理
        Rule(page_link, callback='parse_item', follow=True),  # 注意这里的 ',' 要不会报错
    ) 

    # 加上这个 方法是为了 解决 parse_item() 不能抓取第一页数据的问题 parse_start_url 是 CrawlSpider() 类下的方法，这里重写一下即可
    def parse_start_url(self, response):
        i = ItemLoader(item = items.AdilcrawlerItem(),response = response )
        i.add_xpath('author',"//span[@class='usernameColor']/text()")
        i.add_xpath('theme',"//span[@class='fl info-h1']/text()")
        yield i.load_item()

    # 指定的回调函数
    def parse_item(self, response):
        self.parse_start_url(response)