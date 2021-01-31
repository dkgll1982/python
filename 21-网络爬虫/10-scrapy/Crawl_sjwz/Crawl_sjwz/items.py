# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CrawlSjwzItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pindex = scrapy.Field()
    name = scrapy.Field()
    image = scrapy.Field()
    link = scrapy.Field()
    content = scrapy.Field()

# 列表页
class PageItem(scrapy.Item):
    pindex = scrapy.Field()
    name = scrapy.Field()
    image = scrapy.Field()
    link = scrapy.Field()

# 详情页（后期用link项作为纽带进行关联）    
class DetailItem(PageItem): 
    content = scrapy.Field()
    