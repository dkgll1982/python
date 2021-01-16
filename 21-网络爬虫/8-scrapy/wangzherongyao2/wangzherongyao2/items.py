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
     # 下载成功后返回有关images的一些相关信息
    images = scrapy.Field()         # 储存图片的相关信息(如：路径，下载的url，图片的效验码)  需要额外定义
