# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Wangzherongyao2Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    hero_name = scrapy.Field()      # 英雄名称
    pf_names = scrapy.Field()       # 皮肤名称
    image_urls = scrapy.Field()     # 项目的图像URL
    images = scrapy.Field()         # 有关下载图像的信息字段
