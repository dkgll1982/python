# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import os

class XiaoshuoPipeline:
    #接收管道流的数据，写入对应目录文件里
    def process_item(self, item, spider): 
      curPath = 'data'  
      tempPath = str(item['name'])
      targetPath = curPath + os.path.sep + tempPath
      if not os.path.exists(targetPath):
          os.makedirs(targetPath) 
      filename_path = curPath + os.path.sep + str(item['name']) + os.path.sep + str(item['chapter_name']) + '.txt' 
      with open(filename_path, 'w', encoding='utf-8') as f:
          f.write(item['chapter_content'] + "\n")
          f.close()
      return item