import scrapy
class WxappItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    author = scrapy.Field()
    pub_time = scrapy.Field()
    content = scrapy.Field()