scrapy中Request方法中的meta参数有什么用，怎么用。
参考链接：https://blog.csdn.net/wumxiaozhu/article/details/81368689

初学scrapy可能会有点蒙圈，今天和大家分享下scrapy中Request方法中meta参数的用法
首先我们要知道meta是一个字典，它的主要作用是用来传递数据的，meta = {'key1':value1}，如果想在下一个函数中取出value1, 只需得到上一个函数的meta['key1']即可， 因为meta是随着Request产生时传递的，下一个函数得到的Response对象中就会有meta，即response.meta.
请瞧下面的简单例子更好的帮助理解。

#在items模块中有下面三个参数：
import scrapy
class TextItem(spider.Item):
    title = scrapy.Field()
    price = scrapy.Field()
    image = scrapy.Field()
#在spider爬虫中：
class TaobaoSpider(scrapy.Spider):
    name = ['taobao']
    allowed_domains = ['www.taobao.com']
    def parse1(self,response):
        '''
        需要知道的是item是一个字典
        '''
        item = TextItem()
        for product in response.css('......').extract():
            item['title'] = product.css('......').extract_first()
            item['price'] = product.css('......').extract_first()
            url = product.css('......').extract_first()
            yield = scrapy.Request(url=url, meta={'item':item} callback=self.parse2)
            '''
            比如我们要爬取淘宝上的商品，我们在第一层爬取时候获得了标题(title)和价格(price)，
            但是还想获得商品的图片，就是那些点进去的大图片，假设点进去的链接是上述代码的url，
            利用scrpy.Request请求url后生成一个Request对象，通过meta参数，把item这个字典赋值给meta字典的'item'键，
            即meta={'item':item}，这个meta参数会被放在Request对象里一起发送给parse2()函数。

            '''
    def parse2(self,response):
        item = response.meta['item']
        for product in response.css('......').extract():
            item[imgae] = product.scc('......').extract_first()
        return item
        '''
        这个response已含有上述meta字典，此句将这个字典赋值给item，完成信息传递。
        这个item已经和parse中的item一样了
        之后我们就可以做图片url提取的工作了，
        数据提取完成后return item ，这样就完成了数据抓取的任务了。

        '''



