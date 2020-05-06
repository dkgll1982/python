# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from mingyan.settings import DATA_DIR
from urllib import parse

class MingyanPipeline:
    def __init__(self):
        super().__init__()
        self.path = DATA_DIR    #文件目录
        
    def process_item(self, item, spider): 
        print(type(item),item)
        #下边存储数据的操作交由pipeline
        with open(item["fileName"], "a+") as f:
            f.write(item["text"])
            f.write('\n')
            f.write('标签：' + item["tags"])
            f.write('\n-------\n')
            f.close()
