# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter 
from .items import XimalayaMusicItem  # 如果需要判断不同的item，需要导入item，用isinstance(item, item_name)来判断
from scrapy.pipelines.files import FilesPipeline
from scrapy.exceptions import DropItem
from scrapy.http import Request 
from os.path import basename, dirname, join

class XimalayaMusicPipeline(FilesPipeline): #继承FilesPipeline类
    # def process_item(self, item, spider):
    #     return item

    def get_media_requests(self, item, info):                     # 获取item中的url，用于下载文件
        file_url = item['file_urls'][0]
        yield Request(file_url, meta = item)
    
    # 当一个单独项目中的所有图片请求完成时（要么完成下载，要么因为某种原因下载失败）， ImagesPipeline.item_completed() 方法将被调用。
    # 其中的results参数是get_media_requests()函数请求下载后返回的结果 
    def item_completed(self, results, item, info):
        file_urls = [x['path'] for ok, x in results if ok]
        if not file_urls:
            raise DropItem("Item contains no files")
        item['file_urls'] = file_urls
        return item

    def file_path(self, request, response = None, info = None):       # 通过request匹配设置文件路径
        item = request.meta
        file_path = join(item.get('file_type'),item.get('file_name')+'.m4a')     
        return file_path
