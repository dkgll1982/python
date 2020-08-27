from  scrapy import cmdline
import sys
import os 

#获取当前目录
path = os.path.dirname(os.path.realpath(__file__))
#设置当前目录为工作目录
os.chdir(path)
# 输出未过滤的页面信息
#cmdline.execute('scrapy crawl douban_spider -o movielist.csv'.split())
#cmdline.execute('scrapy crawl douban_spider -o movielist.json'.split())
#保存monogo
cmdline.execute('scrapy crawl douban_spider'.split())