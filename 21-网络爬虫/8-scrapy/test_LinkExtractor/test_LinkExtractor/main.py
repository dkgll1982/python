from scrapy import cmdline
import os

#获取当前目录
path = os.path.dirname(os.path.realpath(__file__))
#设置当前目录为工作目录
os.chdir(path)
#cmdline.execute("scrapy crawl jianshu".split())
cmdline.execute("scrapy crawl jianshu_Crawl".split())