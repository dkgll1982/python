import requests
from urllib.parse import quote

#此页面是通过js动态加载的直接请求无法获取渲染后的数据
url = 'http://www.300600900.cn/'
# response = requests.get(url)

# with open(r'backup/爬虫/cpml.html','w') as f:
#     f.write(response.text)

lua_script = '''
    function main(splash,args)
        splash:go("http://www.300600900.cn/")
        splash:wait(3)
        return {
            html = splash:html(),
        }
    end
'''

lua_url = "http://10.21.197.162:8050/execute?lua_source="+quote(lua_script)
response = requests.get(lua_url)

with open(r'backup/爬虫/cpml.html','w',encoding='utf-8') as f:
    f.write(response.content.decode('unicode_escape'))
