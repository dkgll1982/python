scrapy pipeline中自定义的spider_opened和spider_closed没有被调用，如何解决无法调用问题
参考链接： https://blog.csdn.net/x947096828/article/details/104681266

1.问题
我想要的信息正在从网站上正确地爬出，并且process_item方法能够正确调用。但是，不会调用spider_opened和spider_closed方法。
我尝试在spider_closed中添加端点，但debug过程没有运行到端点，一直没办法实现spider_closed函数

class MyPipeline(object):

    def __init__(self):
        log.msg("Initializing Pipeline")
        self.conn = None
        self.cur = None

    def spider_opened(self, spider):
        log.msg("Pipeline.spider_opened called", level=log.DEBUG)

    def spider_closed(self, spider):
        log.msg("Pipeline.spider_closed called", level=log.DEBUG)

    def process_item(self, item, spider):
        log.msg("Processsing item " + item['title'], level=log.DEBUG)


无论是__init__和process_item日志消息持续显示在日志中，但spider_open和spider_close日志消息都没有。

最后找了很久终于找到了解决办法

2.解决办法：
必须添加：

dispatcher.connect(self.spider_opened, signals.spider_opened)
dispatcher.connect(self.spider_closed, signals.spider_closed)
在__init__函数中，否则它永远不会接收到信号叫它。

3.示例代码：
from scrapy.xlib.pydispatch import dispatcher
from scrapy import signals
import json
import codecs

class PipelineToJson(object):
    def __init__(self):
        dispatcher.connect(self.spider_opened, signals.spider_opened)
        dispatcher.connect(self.spider_closed, signals.spider_closed)

    def spider_opened(self, spider):
        """
        打开文件
        """
        self.file = codecs.open("article.json", 'w', encoding='utf-8')
        self.file.write('[')

    def process_item(self, item, spider):
        """
        ensure_ascii=False 防止中文等编码错误
        """
        if spider.name == "myspider":
            lines = json.dumps(dict(item), ensure_ascii=False) + ',\n'
            self.file.write(lines)
            return item
        else:
            print('-' * 50 + "该爬虫无任何操作" + '-' * 50)
            return item

    def spider_closed(self, spider):
        """
        关闭文件
        """
        self.file.write(']')
        self.file.close()

作用：监控spider启动和关闭。
可以使用它们将对文件进行创建与关闭、打开和关闭与数据库的连接
