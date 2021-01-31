# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
 
class TingroomAudioItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 左边是字段名，右边是item对象。item是字典类型数据，字段通过item['file_text']方式提取数据。
    file_text = scrapy.Field()  
    text_path = scrapy.Field()
    file_paths = scrapy.Field()
    file_urls = scrapy.Field()
