from scrapy import cmdline
import os

#获取当前目录
path = os.path.dirname(os.path.realpath(__file__))
#设置当前目录为工作目录
os.chdir(path)
area = 'haidian'
if os.path.exists("data/data_{}.csv".format(area)):
    os.remove("data/data_{}.csv".format(area))  # 为了防止文件已存在导致索引和数据重复，先删除将要生成的文件

cmdline.execute("scrapy crawl ershou -o data/data_{}.csv -t csv".format(area).split())

# 如果你不想以spider.py中area命名文件，请参考以下
'''
if os.path.exists("data/data.csv"):
    os.remove("data/data.csv")  # 为了防止文件已存在导致索引和数据重复，先删除将要生成的文件
cmdline.execute("scrapy crawl lianjiaershou -o data/data.csv -t csv".split())
'''