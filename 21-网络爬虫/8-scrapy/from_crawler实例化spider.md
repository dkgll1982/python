参考链接：https://blog.csdn.net/qq_27056805/article/details/86262685

1. from_crawler()函数
#@classmethod表示该方法输入该类，可以直接由类名调用，不必通过对象调用
#即Spider.from_crawler(crawler)即可调用该函数。在Crawler类中，Crawler通过
#传入一个Spider类作为参数初始化该Crawler，这个Spider类直接调用该from_crawler()
#函数从而实现Spider的初始化。
@classmethod
    def from_crawler(cls, crawler, *args, **kwargs): #cls参数就是Spider类本身，crawler是Crawler类对象
        spider = cls(*args, **kwargs)   #spider对象就是由这句初始化的，里面的参数会传递给__init__()并调用该函数实现初始化。
        spider._set_crawler(crawler)    #用来设置spider对象的crawler属性和settings属性
        return spider#返回spider对象

2. _set_crawler()函数
#这个函数在from_crawler中被调用，用来初始化crawler和settings对象。这两个属性是spider对象产生后又添加的，即它们二者不是在__init__中被赋值的。
 def _set_crawler(self, crawler):
        self.crawler = crawler # 这个属性可以访问其它的components，非常有用
        self.settings = crawler.settings #这个属性可以访问公共配置变量，self.settings.get()，也很有用。
        crawler.signals.connect(self.close, signals.spider_closed)

3. init_()函数
#这个函数就是实例化Spider类最终函数，由上述cls()调用
def __init__(self, name=None, **kwargs):
        if name is not None:
            self.name = name
        elif not getattr(self, 'name', None):
            raise ValueError("%s must have a name" % type(self).__name__)
        self.__dict__.update(kwargs)
        if not hasattr(self, 'start_urls'):
            self.start_urls = []

