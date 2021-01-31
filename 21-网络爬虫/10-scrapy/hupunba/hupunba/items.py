# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class HupunbaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    
    #球队
    playerteam = scrapy.Field() 
    #球员照片
    playerimg = scrapy.Field() 
    #球员姓名
    playername = scrapy.Field() 
    #球员号码
    playernumber = scrapy.Field() 
    #球员位置
    playerjob = scrapy.Field() 
    #球员身高
    playertall = scrapy.Field() 
    #球员体重
    playerweight = scrapy.Field() 
    #球员生日
    playerbirthday = scrapy.Field() 
    #球员合同
    playercont = scrapy.Field() 
    #球员年薪
    playersal = scrapy.Field ()
