# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class TestCrawlspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 每页的帖子链接
    url = scrapy.Field()
    # 帖子标题
    title = scrapy.Field()
    # 帖子编号
    number = scrapy.Field()
    # 帖子内容
    content = scrapy.Field()