# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class GithubFormrequestItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class CtoItem(scrapy.Item):
    title_url = scrapy.Field()
    title = scrapy.Field()
    fullname = scrapy.Field()
    