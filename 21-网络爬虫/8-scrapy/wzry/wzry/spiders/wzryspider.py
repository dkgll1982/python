import scrapy
import re
from wzry.items import WzryItem 

class WzryspiderSpider(scrapy.Spider):
    name = 'wzryspider' 
    allowed_domains = ['pvp.qq.com']  #不能带https，会报错
    start_urls = ['https://pvp.qq.com/web201605/herolist.shtml']
 
    def parse(self, response):
        #//是相对路径，/是绝对路径
        hero_list=response.xpath("//ul[@class='herolist clearfix']//a")
        print('一共有'+str(len(hero_list))+'个英雄')
        for hero in hero_list:
            item=WzryItem()
            item['hero']=hero.xpath("./text()").extract()[0]
 
            number=hero.xpath("./img/@src").extract()[0][-7:-4]
            item['image_urls']="https://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/{0}/{0}-bigskin-".format(number) 
            url="https://pvp.qq.com/web201605/herodetail/"+number+".shtml"
 
            yield scrapy.Request(url=url,callback=self.parse_detail,meta={'item':item})
 
    def parse_detail(self,response):
        item=response.meta["item"]
 
        sample=r'[\u4E00-\u9FA5●]+'
        skins=response.xpath(".//ul[@class='pic-pf-list pic-pf-list3']/@data-imgname").extract()[0]
        item['skins']=re.findall(sample,skins)
 
        image_urls=item['image_urls']
        item['image_urls']=[]
        for i in range(1,len(item['skins'])+1):
            image_url=image_urls+str(i)+'.jpg'
            item['image_urls'].append(image_url)
 
        skills=response.xpath(".//p[@class='skill-name']/b/text()").extract()
        skills_detail=response.xpath(".//p[@class='skill-desc']/text()").extract()
        item['skill1']=skills[0]
        item['skill2']=skills[1]
        item['skill3']=skills[2]
        item['skill4']=skills[3]
        item['skill1_detail']=skills_detail[0]
        item['skill2_detail']=skills_detail[1]
        item['skill3_detail']=skills_detail[2]
        item['skill4_detail']=skills_detail[3]
        if len(skills)!=4:
            item['skill5']=skills[4]
            item['skill5_detail']=skills_detail[4]
        else:
            item['skill5']='null'
            item['skill5_detail']='null'
        print(item['hero']+"爬取成功！")
        yield item
