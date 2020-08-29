# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class XiaoshuoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #小说名称
    name = scrapy.Field()
    #小说章节名字
    chapter_name = scrapy.Field()
    #小说章节内容
    chapter_content = scrapy.Field()