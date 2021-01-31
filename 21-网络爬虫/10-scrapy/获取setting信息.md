Scrapy进阶知识点总结（五）——Settings：https://www.cnblogs.com/fengf233/p/11400262.html

1：在spider中通过self.settings获取
class MySpider(scrapy.Spider):
    name = 'myspider'
    start_urls = ['http://example.com']

    def parse(self, response):
        print("Existing settings: %s" % self.settings.attributes.keys())

2：通过from_crawler类方法获取scrapy.crawler.Crawler.settings 中的属性
class MyExtension(object):
    def __init__(self, log_is_enabled=False):
        if log_is_enabled:
            print("log is enabled!")

    @classmethod
    def from_crawler(cls, crawler):
        settings = crawler.settings
        return cls(settings.getbool('LOG_ENABLED'))
可以在spider类、middleware类、pipeline类以及extension使用from_crawler方法

总结
1.settings.py中的设置是针对整个项目的，可以添加对整个spiders通用的设置
2.custom_settings是spider单独的设置，比如可以设置每个spider用不同的中间件或管道
3.命令行中的设置，最高的优先级，应用场景比如，cmd多开的时候使用不同配置去跑spider，不过一些配置可能会出问题

--------------------------------------------------------------------------------------------------

Scrapy 从 settings 中获得配置属性的方法：https://blog.csdn.net/xiaoyu_wu/article/details/102533513
1. get(name, default=None)

2. getbool(name, default=False)
    1, '1', True 和 'True' 返回 True， 当0, '0', False, 'False' 和 None 时，返回 False

3. getint(name, default=0)
    a = settings.getint('CONCURRENT_REQUESTS')       # 获取配置的值
    b = settings.getint("CONCURRENT_REQUESTS", 16)   # 获取配置的值，如果没有这个配置，则设置默认值为16

4. getfloat(name, default=0.0)

5. getlist(name, default=None)
    获取一个为 list 的 setting 的值。如果原值就是 list，则按原则返回；如果原值是 string，则会被 "," 分割；
    例如，'one,two' ，会被返回成为 ['one', 'two']。

6. getdict(name, default=None)