# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import json

class AdilcrawlerPipeline: 
    '''
        保存item数据
    '''
    def __init__(self):
        self.filename = open('thousandPic.json','w', encoding='utf-8')
        
    def process_item(self, item, spider):
        #  ensure_ascii=False 可以解决 json 文件中 乱码的问题。
        #  这里是一个字典一个字典存储的，后面加个 ',\n' 以便分隔和换行。
        text = json.dumps(dict(item) , ensure_ascii=False) + ',\n'  
        self.filename.write(text)

        return item 

    def close_spider(self,spider):
        self.filename.close()
