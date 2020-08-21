# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import json

class ItcastteacherPipeline:
    #主要初始化打开一个文件夹，并表示将要向其中输入数据。只执行一次
    def __init__(self):
        self.file = open("detail.json",'w')
        
    #主要用于把json格式转化为unicode编码，并把数据写入文件中。    
    def process_item(self, item, spider):
        content = json.dumps(dict(item),ensure_ascii=False) + ',\n'
        self.file.write(content)
        return item
    
    # 关闭爬虫时执行，只执行一次。 (如果爬虫中间发生异常导致崩溃，close_spider可能也不会执行)    
    def close_spider(self,spider):
        self.file.close()
