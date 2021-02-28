import requests
import json
from urllib.parse import quote

api = "https://jd.spacecig.com/zhzlbackend/realPerson/person/familyPersons1?keyword=&personType=&dwdm=null&name=&cardNum=&gender=&maritalStatus=&politicalStatus=&education=&startBirthdayDate=&endBirthdayDate=&focusService=&focusControl=&isActualAddr=&death=&offset=0&limit=500&orderby=&ordertype="
lua_script = '''
    function main(splash)
        -- 自定义请求头
        splash:set_custom_headers({
            ["Cookie"] = "passport=2b86f8a1-53a4-4ae1-9503-afdfadcc4391; CIGToken=22c054d7-8f42-454f-ab04-d7ad9bf8a325; CIGUsername=%E7%AE%A1%E7%90%86%E5%91%98; CIGUserid=ADMIN; true=qhTBW2JkaCeFpP0KAAA3"
        })
        splash:go("https://jd.spacecig.com/zhzl-frames/main2.html")
        splash:wait(5) 
        return {
            html = splash:html(), 
        } 
    end
 '''
splash_url = 'http://10.21.197.162:8050/execute?lua_source='+quote(lua_script)
print(splash_url)

headers = { 
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36',
    'cookie': 'passport=2b86f8a1-53a4-4ae1-9503-afdfadcc4391; CIGToken=22c054d7-8f42-454f-ab04-d7ad9bf8a325; CIGUsername=%E7%AE%A1%E7%90%86%E5%91%98; CIGUserid=ADMIN; true=rTdDhhvWSnGIBGbvAAAz',
} 
response = requests.get(splash_url, headers = headers)

with open(r'backup\爬虫\jczl.html', 'w',encoding='utf-8') as f: 
    f.write(response.content.decode('unicode_escape'))
    #json.dump(response.json(),f,indent=2,ensure_ascii=False) 