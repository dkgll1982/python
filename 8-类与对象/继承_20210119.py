#!/usr/bin/env python 
# -*- coding:utf-8 -*-  
# @Author: suixin 
# @Company: Aerospace Shenzhou Intelligent System Technology Co., Ltd  
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2021-01-19 14:07:44 
# @Remark: Life is short, I use python！ 
# @Software: vscode 


import scrapy

# 列表页
class PageItem(scrapy.Item):
    pindex = scrapy.Field()
    name = scrapy.Field()
    image = scrapy.Field()
    link = scrapy.Field()

# 详情页（后期用link项作为纽带进行关联）    
class DetailItem(PageItem): 
    content = scrapy.Field()     
    
class CrawlSjwzItem(DetailItem):
    pass
    
if __name__ == "__main__":
    item = CrawlSjwzItem()
    item["pindex"] = 1
    item["name"] = "李洁"
    item["image"] = "https://www.baidu.com/img/flexible/logo/pc/result@2.png" 
    item["content"] = '内容'
    print(item.keys())