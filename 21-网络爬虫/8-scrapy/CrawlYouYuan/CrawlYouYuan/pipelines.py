import json
import codecs

class CrawlyouyuanPipeline(object): 
    def __init__(self):
        self.filename = codecs.open('content.json', 'w', encoding='utf-8')
    
    def process_item(self, item, spider):
        html = json.dumps(dict(item), ensure_ascii=False)
        self.filename.write(html + '\n')
        return item
    
    def spider_closed(self, spider):
        self.filename.close()