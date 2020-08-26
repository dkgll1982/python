# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import os
import csv
import scrapy
from scrapy.pipelines.images import ImagesPipeline
from wzry.settings import IMAGES_STORE as images_store

class WzryPipeline:
    def __init__(self):
        #csv文件的位置，无需事先创建
        store_file=images_store+'/data.csv'
        print('****************************************************')
        #打开（创建）文件
        self.file=open(store_file,'w',newline='')
        #csv写法
        self.writer=csv.writer(self.file,dialect="excel")
        #写入第一行
        self.writer.writerow(['英雄','技能1','技能2','技能3','技能4','技能5','皮肤名'])
 
    def process_item(self,item,spider):
        #判断字段值不为空再写入文件
        if item['hero']:
            self.writer.writerow([item['hero'],item['skill1'],item['skill2'],item['skill3'],item['skill4'],item['skill5'],item['skins']])
            #以英雄名字创建文件夹
            isExist=os.path.exists(images_store+"/{}".format(item['hero']))
            if not isExist:
                os.mkdir(images_store+"/{}".format(item['hero']))
            try:
                with open(images_store+'/{}/技能.txt'.format(item['hero']),'w',encoding='gbk') as f:
                    f.write(item['skill1']+'\n'+item['skill1_detail']+'\n\n')      #写入技能详情
                    f.write(item['skill2']+'\n'+item['skill2_detail']+'\n\n')
                    f.write(item['skill3']+'\n'+item['skill3_detail']+'\n\n')
                    f.write(item['skill4']+'\n'+item['skill4_detail']+'\n\n')
                    if item['skill5'] is not'null':
                        f.write(item['skill5']+'\n'+item['skill5_detail']+'\n\n') 
            except Exception:
                raise
            print(item['hero']+"技能存储成功！")
        return item
 
    def close_spider(self,spider):
        #关闭爬虫时顺便将文件保存退出
        self.file.close()
 
class WzryImgPipeline(ImagesPipeline):
    #此方法是在发送下载请求之前调用，其实此方法本身就是去发送下载请求
    def get_media_requests(self,item,info):
        #调用原父类方法，发送下载请求并返回的结果（request的列表）
        request_objs=super().get_media_requests(item,info)
        #给每个request对象带上meta属性传入hero、name参数，并返回
        for request_obj,num in zip(request_objs,range(0,len(item['skins']))):
            request_obj.meta['hero']=item['hero']
            request_obj.meta['skin']=item['skins'][num]
        return request_objs
 
    #此方法是在图片将要被存储时调用，用来获取这个图片存储的全部路径
    def file_path(self,request,response=None,info=None):
        #获取request的meta属性的hero作为文件夹名称
        hero=request.meta.get('hero')
        #获取request的meta属性的skin并拼接作为文件名称
        image=request.meta.get('skin')+'.jpg'
        #获取IMAGES_STORE图片的默认地址并拼接！！！！不执行那一步
        hero_path=os.path.join(images_store,hero)
        #判断地址是否存在，不存在则创建
        if not os.path.exists(hero_path):
            os.makedirs(hero_path)
        #拼接文件夹地址与图片名存储的全部路径并返回！！！！原方法
        image_path=os.path.join(hero_path,image)
        return image_path