# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy 

class qiantuwangItem(scrapy.Item):
    author = scrapy.Field()     #作者
    theme = scrapy.Field()      #主题 
