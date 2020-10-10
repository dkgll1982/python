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

print('*'*40)

nstr = '''6GGGGG555
2aaaaa123
4bbbbb
ddddd
1cccc
3dddd
2eeee'''
pattern = r"^\d+\w+\n^\d+\w+\n^\d+\w+\n"  
print(re.match(pattern,nstr,flags = re.M|re.DOTALL))

# ^ 、\A 区别：只匹配字符串的起始位置。如果没有设置 MULTILINE 标志的时候，\A 和 ^ 的功能是一样的；
# 但如果设置了 MULTILINE 标志，则会有一些不同： \A 还是匹配字符串的起始位置，但 ^ 会对字符串中的每一行都进行匹配。
pattern = r"\A\d+\w+\n" 
#pattern = r"\A\d+\w+\n\A\d+\w+\n\A\d+\w+\n" 
print(re.match(pattern,nstr,flags = re.M|re.DOTALL))

# \Z对应$
# \Z匹配字符串结束位置，忽略多行模式
# $匹配结束位置，多行模式下匹配每一行的结束

# re.match与re.search的区别：
#re.match只匹配字符串的开始，如果字符串开始不符合正则表达式，则匹配失败，函数返回None；
# 而re.search匹配整个字符串，直到找到一个匹配。
pattern = r"^\D+\w+\n^\d+\w+\n^\d+\w+\n"  
print(re.search(pattern,nstr,flags = re.M|re.DOTALL))

phone = "2004-959-559 # 这是一个国外电话号码" 
# 删除字符串中的 Python注释 
num = re.sub(r'#.*$', "", phone)
print(f"电话号码是:[{num}]")
 
# 删除非数字(-)的字符串 
num = re.sub(r'\D', "", phone,count=6)
print(f"电话号码是:[{num}]")

# repl参数是一个函数的情况
# 将匹配的数字乘以 2
def double(matched):
    value = int(matched.group('value'))
    return str(value * 2)
 
s = 'A23G4HFD567'
print(re.sub('(?P<value>\d+)', double, s))

# findall:在字符串中找到正则表达式所匹配的所有子串，并返回一个列表，如果没有找到匹配的，则返回空列表。
# 注意:match和search是匹配一次findall 匹配所有。 
pattern = re.compile(r'\d+')   # 查找数字
result1 = re.findall('\d+','runoob 123 google 456')
result2 = pattern.findall('run88oob123google456', 0, 10)
print(result1)
print(result2)

result3 = pattern.finditer('run88oob123google456', 0, 10) 
for match in result3: 
    print('---->:',match.group() )
    
# re.split(pattern, string[, maxsplit=0, flags=0])
# maxsplit分隔次数，maxsplit=1 分隔一次，默认为 0，不限制次数 
result4 = pattern.split('run88oob123google456E',maxsplit=3) 
print(result4)