#Item Exporters用法：https://blog.csdn.net/mashaokang1314/article/details/82770456

from scrapy.exporters import JsonLinesItemExporter

class WxappPipeline:
    def __init__(self):
        self.fp = open('wx.json', 'wb')
        self.exporter = JsonLinesItemExporter(self.fp, ensure_ascii = False, encoding = 'utf-8')
        
    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item
    
    def close_spider(self, spider):
        self.fp.close()
