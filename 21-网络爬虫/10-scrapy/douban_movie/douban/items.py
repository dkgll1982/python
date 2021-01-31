# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    
    serial_number = scrapy.Field()  #排名
    movie_name = scrapy.Field()     #电影名称
    introduce = scrapy.Field()      #电影简介基本信息
    star = scrapy.Field()           #电影星级评分
    evaluate = scrapy.Field()       #电影评论人数
    describe = scrapy.Field()       #电影内容简介