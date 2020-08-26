# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

# 为增强可读性，直接以中文作为变量名,实际应用中不要这么干
class LianjiaershouItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    标题 = scrapy.Field()
    小区 = scrapy.Field()
    区域 = scrapy.Field()
    户型_室 = scrapy.Field()
    户型_厅 = scrapy.Field()
    面积 = scrapy.Field()
    朝向 = scrapy.Field()
    装修 = scrapy.Field()
    楼层 = scrapy.Field()
    建成年份 = scrapy.Field()
    建筑结构 = scrapy.Field()
    关注人数 = scrapy.Field()
    已发布日 = scrapy.Field()
    总价 = scrapy.Field()
    单价 = scrapy.Field()
    满二 = scrapy.Field()
    满五 = scrapy.Field()
    近地铁 = scrapy.Field()
