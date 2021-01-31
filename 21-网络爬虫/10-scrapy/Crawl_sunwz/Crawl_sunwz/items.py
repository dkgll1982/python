import scrapy


class SunproItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    new_num = scrapy.Field()
    new_title = scrapy.Field()
    pass

class DetailproItem(scrapy.Item):
    new_content = scrapy.Field()