# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter 
from scrapy.pipelines.images import ImagesPipeline
from scrapy import Request 

class TgbusPipeline:
    def process_item(self, item, spider):
        return item



# 自定义 创建下载及存储的特殊管道类
class MyImagePipeline(ImagesPipeline):
    # 接收item对象并将获取item对象中的url发送请求
    def get_media_requests(self, item, info):
        for image_url in item["image_urls"]:
            yield Request(image_url)

    # 指定文件存储路径
    def file_path(self, request, response=None, info=None):
        # 打印图片路径
        # print(request.url)
        # 通过分割图片路径获取图片名字
        img_name = request.url.split("/")[-1]
        return img_name

    # 返回item对象，给下一执行的管道类
    def item_completed(self, results, item, info):
        # 图片下载路径、url和校验和等信息
        print(results)
        return item