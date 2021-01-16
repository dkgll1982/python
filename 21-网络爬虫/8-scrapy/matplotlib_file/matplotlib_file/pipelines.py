# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class MatplotlibFilePipeline:
    def process_item(self, item, spider):
        return item
    
from scrapy.pipelines.files import FilesPipeline
from scrapy.exceptions import DropItem
from urllib.parse import urlparse
from os.path import basename, dirname, join
import scrapy

# os.path.dirname()方法　去掉文件名，返回目录
# os.path.basename()方法　返回path最后的文件名

class MyFilesPipeline(FilesPipeline):  
    # 此函数中需要把 file_url 取出并构建为 scrapy.Request 请求对象并返回，每一个请求都将触发一次下载图片的操作。
    def get_media_requests(self, item, info):
        for file_url in item['file_urls']:
            yield scrapy.Request(file_url)

    # 当一个单独项目中的所有图片请求完成时（要么完成下载，要么因为某种原因下载失败）， ImagesPipeline.item_completed() 方法将被调用。
    # 其中的results参数是get_media_requests()函数请求下载后返回的结果 
    def item_completed(self, results, item, info):
        file_urls = [x['path'] for ok, x in results if ok]
        if not file_urls:
            raise DropItem("Item contains no files")
        item['file_urls'] = file_urls
        return item
    
    # 可以通过get_media_requests()函数,在每一个Request请求中加入meta参数将item中的信息传入file_path进行文件重命名。         
    # file_path()参数中的request就是get_media_requests()发出的请求            
    def file_path(self, request, response=None, info=None):
        path = urlparse(request.url).path
        return join(basename(dirname(path)), basename(path))
