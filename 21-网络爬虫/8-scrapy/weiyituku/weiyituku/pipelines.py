# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter 

class WeiyitukuPipeline:
    def process_item(self, item, spider):        
        return item


from scrapy.pipelines.images import ImagesPipeline
import scrapy

class ImagePipeline(ImagesPipeline):
    # 接收item对象并将获取item对象中的url发送请求
    def get_media_requests(self, item, info): 
        # 这里把item传过去，因为后面需要用item里面的信息做为文件名的参考
        yield scrapy.Request(item["img_url"] , meta = {'item': item })

    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:     #如果其中没有图片，我们将丢弃项目                  
            raise DropItem('Image Downloaded Failed')  
        return item             #默认情况下，item_completed()方法返回项目。   
    
    #定义下载图片存储的路径，我们需要处理一下，以此把图片存储到我们想存储的地方
    def file_path(self, request, response=None, info=None):
        item = request.meta['item']
        # 图片路径
        url = request.url
        # 通过分割图片路径获取图片名字
        file_name = './{}/{}'.format(item['title'],item['name'].replace('/','_') + '_' + url.split('/')[-1])
        # 返回图片路径
        return file_name