# -*- coding: utf-8 -*-
import json

class TencentPipeline(object):
    def __init__(self):
        self.filename = open("tencent.json", "a")

    # 处理提取的数据(保存数据)
    def process_item(self, item, spider):
        text = json.dumps(dict(item), ensure_ascii = False) + ",\n"
        self.filename.write(text.encode("utf-8"))
        return item
    
    # 关闭爬虫时执行，只执行一次。 (如果爬虫中间发生异常导致崩溃，close_spider可能也不会执行)    
    def close_spider(self, spider):
        self.filename.close()