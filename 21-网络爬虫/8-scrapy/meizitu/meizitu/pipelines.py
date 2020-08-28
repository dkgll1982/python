# -*- coding: utf-8 -*-
import hashlib
import re
from scrapy.pipelines.images import ImagesPipeline
from scrapy import Request
from scrapy.utils.python import to_bytes

class PicscrapyPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        url = item['image_urls']
        # 做了一下判断，排除一些无效链接
        if re.match(r'http', url):
            self.name = item['category']
            yield Request(url)

    # 重新定义了一下存储路径，默认情况下是存在一个full文件夹里面
    def file_path(self, request, response=None, info=None):
        if not isinstance(request, Request):
            url = request
        else:
            url = request.url
        image_guid = self.name + '_'+ hashlib.sha1(to_bytes(url)).hexdigest()  # change to request.url after deprecation
        return '%s.jpg' % image_guid