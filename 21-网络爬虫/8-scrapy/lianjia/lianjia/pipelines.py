# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import json

class LianjiaPipeline (object):
    # 打开文件
    def open_spider (self,spider):
        try:
            self.file = open('MyData.json ', "w", encoding="utf-8")
        except Exception as err:
            print(err)
    # 写入
    def process_item (self, item, spider):
        dict_item = dict (item)
        # 生成 json 串
        json_str = json.dumps(dict_item , ensure_ascii=False) + "\n" 
        self.file.write(json_str)
        return item
    # 关闭文件
    def close_spider (self,spider):
        self.file.close()