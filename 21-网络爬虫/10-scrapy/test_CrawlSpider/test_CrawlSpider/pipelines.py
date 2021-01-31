# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import json

class TestCrawlspiderPipeline:
    def __init__(self):
        self.file = open('dongguan.json','w')
        
    def process_item(self, item, spider):
        content = json.dumps(dict(item),ensure_ascii=False).encode('utf-8') + '\n'
        self.file.write(content)
        return item
    
    def closespider(self):
        self.file.close()
