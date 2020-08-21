import re
import json
import os 

# 获取文件当前所在的目录，并返回完整文件全路径 
def realpath(filename):
    return os.path.join(os.path.dirname(os.path.realpath(__file__)), filename)
  
# file = open(realpath("test.txt"), "r",encoding='utf8')
# txt = file.read()
txt = '''
  <script type="text/data" id="initData">{"ch":"photography","src":"","cid":"%E8%87%AA%E7%84%B6","tid":"","data":{"end":false,"count":30,"lastid":30,"prevsn":"0","list":[{"id":"66d00a646ec25e6e71d6d89e3307b7e2","index":1,"grpmd5":"de9b538d211fe97499272a37a104ea12","grpseq":"1","grpcnt":"1","imgkey":"t01a9e11720c9189b04.jpg","width":"1001","height":"799","title":"\u5b89\u5409\u6df1\u6eaa\u5ce1\u8c37\u6f02\u6d41","imgurl":"http:\/\/m.tuniucdn.com\/filebroker\/cdn\/olb\/15\/4b\/154b6f68f10fedea03a44db34487664d_w1001_h801_c1_t0.jpg","purl":"http:\/\/www.tuniu.com\/guide\/v-shenxipiaoliu-39835\/tupian\/","site":"www.tuniu.com","imgsize":"0","label":"","sitename":"www.tuniu.com","siteid":"1225387127","src":"0","fnum":"0","qhimg_thumb_width":200,"qhimg_thumb_height":160,"qhimg_downurl":"https:\/\/dl.image.so.com\/d?imgurl=https%3A%2F%2Fp0.ssl.qhimgs1.com%2Ft01a9e11720c9189b04.jpg&purl=https%3A%2F%2Fimage.so.com%2F%3Fsrc%3Ddl.image&key=5ffbc4a78d","qhimg_url":"https:\/\/p0.ssl.qhimgs1.com\/t01a9e11720c9189b04.jpg","qhimg_thumb":"https:\/\/p0.ssl.qhimgs1.com\/sdr\/200_200_\/t01a9e11720c9189b04.jpg","qhimg_qr_key":"a6b0ea2a14","tag":"0","rdate":"1373385600","ins_time":"2013-07-10 00:00:00","dsptime":"","summary":[],"pic_desc":" \u5b89\u5409\u6df1\u6eaa\u5ce1\u8c37\u6f02\u6d41"}]}}</script>'''

json_str = re.findall(r'.*?<script.*id="initData">(.*?)</script>',txt)
data = json.loads(json_str[0])
print(data['data']['list'])

