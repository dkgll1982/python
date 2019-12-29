# encoding:utf-8
import sys
import requests 

appid = '9897191'
ak = 'fZGH6al0ADgaxgabRlf8aGFX'
sk = 'AdGjnwvasv7pofwflH9Bf3ipGVnZ2Z7d'
token = '25.25aa0b56369713cbedfc57787792ca8a.315360000.1887630192.282335-9897191'
# client_id 为官网获取的AK， client_secret 为官网获取的SK
host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=%s&client_secret=%s'%(ak,sk)
# response = requests.get(host)
# if response:
#     print(response.json())

from aip import AipOcr
 
config = {
    'appId': appid,
    'apiKey': ak,
    'secretKey': sk
}
 
client = AipOcr(**config)
 
def get_file_content(file):
    with open(file, 'rb') as fp:
        return fp.read()
 
def img_to_str(image_path):
    image = get_file_content(image_path)
    # 通用文字识别（可以根据需求进行更改）
    result = client.basicGeneral(image)
    print(result)
    return result    

if __name__=='__main__':
    filename = r'backup\3.jpg'
    img_to_str(filename)

#参考链接：https://blog.csdn.net/apollo_miracle/article/details/99056926    