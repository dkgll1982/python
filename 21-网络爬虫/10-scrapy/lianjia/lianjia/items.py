# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class LianjiaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    resblock_type = scrapy.Field()
    sale_status = scrapy.Field()
    location0 = scrapy.Field()
    location1 = scrapy.Field()
    location2 = scrapy.Field()
    num_room = scrapy.Field()
    area = scrapy.Field()
    price_pre_spm = scrapy.Field()
    price_pre_suite = scrapy.Field()
