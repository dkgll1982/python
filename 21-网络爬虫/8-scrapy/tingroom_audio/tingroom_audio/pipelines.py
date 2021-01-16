# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from .items import TingroomAudioItem  # 如果需要判断不同的item，需要导入item，用isinstance(item, item_name)来判断
from scrapy.pipelines.files import FilesPipeline
from scrapy.http import Request

class TingroomAudioPipeline(FilesPipeline):
    def get_media_requests(self, item, info):                     # 获取item中的url，用于下载文件
        file_url = item['file_urls'][0]
        yield Request(file_url, meta=item)

    def file_path(self, request, response=None, info=None):       # 通过request匹配设置文件路径
        meta = request.meta
        file_path = meta.get('file_paths')[0]                     # 自动储存。相对路径（相对setting.py中的FILES_STORE），或绝对路径
        return file_path

    def item_completed(self, results, item, info):
        with open(item['text_path'], 'w', encoding='utf8') as f:  # 自己写入文本内容到对应路径下，同样通过item传入数据（路径 + 文本内容）
            f.writelines(item['file_text'])
        print(f'{item["file_paths"][0]}下载完成！\n{"*" * 50}\n')
        return item