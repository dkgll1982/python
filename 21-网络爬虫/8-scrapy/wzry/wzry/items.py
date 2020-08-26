# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class WzryItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    hero=scrapy.Field()
    skins=scrapy.Field()
 
    skill1=scrapy.Field()
    skill1_detail=scrapy.Field()
 
    skill2=scrapy.Field()
    skill2_detail=scrapy.Field()
 
    skill3=scrapy.Field()
    skill3_detail=scrapy.Field()
 
    skill4=scrapy.Field()
    skill4_detail=scrapy.Field()
 
    skill5=scrapy.Field()
    skill5_detail=scrapy.Field()
 
    image_urls=scrapy.Field()
