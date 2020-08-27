# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class DoubanBookItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()               #书名
    author = scrapy.Field()             #作者
    price = scrapy.Field()              #价格
    edition_time = scrapy.Field()       #出版时间
    publisher = scrapy.Field()          #出版社
    ratings = scrapy.Field()            #评分