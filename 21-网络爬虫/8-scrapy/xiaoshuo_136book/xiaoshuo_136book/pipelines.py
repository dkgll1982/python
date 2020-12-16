# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import codecs, sys

class Xiaoshuo136BookPipeline:
            
    def process_item(self, item, spider):
        item = dict(item)
        # 自定义目录，保存到本地
        for i in range(len(item["title"])): 
            path = r'backup\爬虫\小说\花千骨\\' + item["title"][i]
            self.file = open(path, "wb", encoding="utf-8")
            for j in item["text"]:
                self.file.write(j)

    def close_spider(self,spider):
        self.file.close()