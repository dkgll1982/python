# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from .items import SunproItem,DetailproItem

class SunproPipeline(object):
    def process_item(self, item, spider):
        if isinstance(item,DetailproItem):
            print('DetailproItem:{}'.format(item['new_content']))
        else:
            print('SunproItem:{}:{}'.format(item['new_num'],item['new_title']))
        return item