import urllib.request
import urllib.parse
import ssl
import json

ssl._create_default_https_context = ssl._create_unverified_context

class LaGouSpider():
    def __init__(self):
        self.url = "https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false"
        self.headers={
            "Referer":"https://www.lagou.com/jobs/list_python/p-city_0?&cl=false&fromSearch=true&labelWords=&suginput=",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36",
            "Cookie":'user_trace_token=20200209220610-d640ad4b-dc96-4a44-a56e-a89fe7792baa; _ga=GA1.2.708725097.1581257172; LGUID=20200209220610-2a3d95ce-4a21-453e-8d66-60924b3218a0; _ga=GA1.3.708725097.1581257172; index_location_city=%E5%85%A8%E5%9B%BD; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%221702a45e96b1cf-03f580ac9222ee-b383f66-1327104-1702a45e96c3dc%22%2C%22%24device_id%22%3A%221702a45e96b1cf-03f580ac9222ee-b383f66-1327104-1702a45e96c3dc%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D; JSESSIONID=ABAAAECAAHHAAFD86E225FC9F93A4D6AC644295D1B62A79; _gid=GA1.2.326010959.1581909570; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1581385909,1581386533,1581392974,1581909570; LGSID=20200217111931-350dcf5f-0370-42bb-845a-bf284cfc03e0; PRE_UTM=; PRE_HOST=; PRE_SITE=; PRE_LAND=https%3A%2F%2Fpassport.lagou.com%2Flogin%2Flogin.html%3Fsignature%3D864F92E08F534DAEE10239FFF5693601%26service%3Dhttp%25253A%25252F%25252Fwww.lagou.com%25252Fjobs%26action%3Dlogin%26serviceId%3Dlagou%26ts%3D1581909569497; X_MIDDLE_TOKEN=674b3a201dc0565b77b30a638dd6ec48; _gat=1; X_HTTP_TOKEN=cb9a9928d186223032201918518f96417862597a28; LGRID=20200217113032-577b11fc-f191-4bcf-90bb-44b5570ead08; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1581910232'
        }
        self.page = 1
    
    def send_request(self,form_data): 
        #创建请求
        request = urllib.request.Request(url =self.url,data=form_data,headers=self.headers)
        response = urllib.request.urlopen(request)
        content = response.read().decode('utf-8') 
        json_str = json.loads(content)
        print(json_str) 
        if json_str["msg"] is not None:
            print("错误消息：",type(json_str["msg"])) 
            ret = False
        else:
            job = json_str["content"]["positionResult"]["result"]
            self.write_content(job)
            ret = True
        return ret
            
    def write_content(self,content):
        with open(r'backup\爬虫\拉钩job.json','a',encoding='utf8') as f:
            f.write('\n'+str(content))     
    
    def start(self):    
        while True:
            self.page += 1    
            form_data={
                "first":'false',
                "pn":self.page,
                "kd":"python",
                "sid":'f4924ac6c3454447bd9a5ac884bfdb3d'
            }
            form_data = urllib.parse.urlencode(form_data).encode('utf8')
        
            ret = self.send_request(form_data)
            if not ret:
                break
            inp = input('继续按任意键，退出按q键：')
            if inp =='q':
                break 
            
if __name__ == "__main__":
    lgs = LaGouSpider()
    lgs.start()