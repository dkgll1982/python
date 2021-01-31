# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class JczlItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    id = scrapy.Field()
    placeName = scrapy.Field()
    oldPlaceName = scrapy.Field()
    placeAddr = scrapy.Field()
    areaName = scrapy.Field()
    safeType = scrapy.Field()
    placeTypeName = scrapy.Field()
