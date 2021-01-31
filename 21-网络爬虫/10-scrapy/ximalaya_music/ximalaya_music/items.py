# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class XimalayaMusicItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 左边是字段名，右边是item对象。item是字典类型数据。
    file_type = scrapy.Field()      # 歌曲类型
    file_name = scrapy.Field()      # 歌曲名称 
    #抓取一个项目，把其中文件的URL放入 file_urls 组内。该字段的值必须是一个列表
    file_urls = scrapy.Field()      # 歌曲文件链接
