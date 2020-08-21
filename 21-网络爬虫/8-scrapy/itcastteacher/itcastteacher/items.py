# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ItcastteacherItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    
    name = scrapy.Field()       #教师姓名
    title = scrapy.Field()      #教师职位
    info = scrapy.Field()       #教师简介信息
