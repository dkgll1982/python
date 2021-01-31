#!/usr/bin/env python 
# -*- coding:utf-8 -*-  
# @Author: suixin 
# @Company: Aerospace Shenzhou Intelligent System Technology Co., Ltd  
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2021-01-25 20:40:02 
# @Remark: Life is short, I use python！ 
# @Software: vscode 
# 参考链接：https://www.cnblogs.com/bk9527/p/10504883.html

from selenium import webdriver
from selenium.webdriver.chrome.options import Options    # 使用无头浏览器
import scrapy 
from ..items import WangyiItem

#无头浏览器设置
chorme_option = Options()
# chorme_options.add_argument("--headless")
# chorme_options.add_argument("--disable-gpu")
chorme_option.add_argument('--disable-infobars')     # 去掉提示：Chrome正收到自动测试软件的控制
chorme_option.add_experimental_option("excludeSwitches", ["enable-automation"])
chorme_option.add_experimental_option('useAutomationExtension', False)
chorme_option.add_argument('--start-maximized')      # 最大化运行（全屏窗口）,不设置，取元素会报错

class WangyiSpider(scrapy.Spider):
    name = 'wangyi'
    # allowed_domains = ['wangyi.com']   # 允许爬取的域名
    start_urls = ['https://news.163.com/']

    # 实例化一个浏览器对象
    def __init__(self):
        self.browser = webdriver.Chrome(chrome_options=chorme_option) 

    def start_requests(self):
        url = "https://news.163.com/"
        response = scrapy.Request(url,callback=self.parse_index)
        yield response

    # 整个爬虫结束后关闭浏览器
    def close(self,spider):
        self.browser.quit()

    # 访问主页的url, 拿到对应板块的response
    def parse_index(self, response):
        div_list = response.xpath("//div[@class='ns_area list']/ul/li/a/@href").extract()
        index_list = [3,4,6,7]
        for index in index_list:
            response = scrapy.Request(div_list[index],callback=self.parse_detail)
            yield response

    # 对每一个板块进行详细访问并解析, 获取板块内的每条新闻的url
    def parse_detail(self,response):
        div_res = response.xpath("//div[@class='data_row news_article clearfix ']")
        # print(len(div_res))
        title = div_res.xpath(".//div[@class='news_title']/h3/a/text()").extract_first()
        pic_url = div_res.xpath("./a/img/@src").extract_first()
        detail_url = div_res.xpath("//div[@class='news_title']/h3/a/@href").extract_first()
        infos = div_res.xpath(".//div[@class='news_tag//text()']").extract()
        info_list = []
        for info in infos:
            info = info.strip()
            info_list.append(info)
        info_str = "".join(info_list)
        item = WangyiItem()

        item["title"] = title
        item["detail_url"] = detail_url
        item["pic_url"] = pic_url
        item["info_str"] = info_str
        
        #此处detail_url如果为空则报错，可以加以判断
        # 通过 参数meta 可以将item参数传递进 callback回调函数,再由 response.meta[...]取出来
        yield scrapy.Request(url=detail_url,callback=self.parse_content,meta={"item":item})   
        
    # 对每条新闻的url进行访问, 并解析
    def parse_content(self,response):
        item = response.meta["item"]    # 获取从response回调函数由meta传过来的 item 值
        content_list = response.xpath("//div[@class='post_text']/p/text()").extract()
        content = "".join(content_list)
        item["content"] = content
        yield item