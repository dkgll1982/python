# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter 
import codecs,json
from .items import PageItem,DetailItem

class CrawlSjwzPipeline:
    def __init__(self):
        self.filename = codecs.open(r'data\data.json', 'w', encoding='utf-8')
        
    def process_item(self, item, spider):
        html = json.dumps(dict(item), ensure_ascii=False)
        self.filename.write(html + '\n')
        return item
    
    def spider_closed(self, spider):
        self.filename.close()
        

class CrawlSjwz2Pipeline:
    def __init__(self):
        self.filename1 = codecs.open(r'data\data2.json', 'w', encoding='utf-8')
        self.filename2 = codecs.open(r'data\data3.json', 'w', encoding='utf-8')
        
    def process_item(self, item, spider):
        html = json.dumps(dict(item), ensure_ascii=False)
        if not isinstance(item,DetailItem):                #判断item是否为PageItem类型
            self.filename1.write(html + '\n')
        else:
            self.filename2.write(html + '\n')
        return item
    
    def spider_closed(self, spider):
        self.filename1.close()
        self.filename2.close()