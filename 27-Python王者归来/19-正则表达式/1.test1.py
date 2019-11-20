import re

match = re.match(r'\Aabc', 'abc')
print('匹配结果：',match)

match = re.match(r'\A(0[0-9]|1[0-9]|2[0,3])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])$','19:52:03')
print('匹配结果：',match)

#flags标志位：用于控制正则表达式的匹配方式，如：是否区分大小写，多行匹配等等。
search = re.match(r'[a-zA-Z]','W123Eeewwee', flags=re.I)
print('匹配结果：',search)

print('-'*60)

class Seq():
    def __init__(self,index):
        self.__index__=index
    def __iter__(self):
        return self
    def __next__(self):
        self.__index__+=1
        return self.__index__
s = Seq(24) 
# re.match 尝试从字符串的起始位置匹配一个模式，如果不是起始位置    . 匹配除换行符（\n）以外的任意字符
print(str(s.__next__())+":",re.match(r".*\bname\b.*","my name is guojun"))
print(str(s.__next__())+":",re.match(".","Ab"))
print(str(s.__next__())+":",re.match(".","8"))
print(str(s.__next__())+":",re.match(".","-"))
print(str(s.__next__())+":",re.match("^((?!\_$).)*$","_33333——_"))
print(str(s.__next__())+":",re.match(".","10086"))        # 注意，只匹配第一个字符  
print(str(s.__next__())+":",re.match(".*","10086"))       # *表示匹配0到多个字符
print(str(s.__next__())+":",re.match(r"(\d?)(\d?)\1-\2","121-2286"))     # *表示匹配1到多个字符
print(str(s.__next__())+":",re.match("\d+","e10086"))     # *表示匹配1到多个字符
print(str(s.__next__())+":",re.match("\d+","10086e"))     # *表示匹配1到多个字符
print(str(s.__next__())+":",re.match(".?","10086"))       # *表示匹配0到1个字符
print(str(s.__next__())+":",re.match(".","\n10086"))      # 注意，在正则中\n(换行键是无法匹配的) 
print(str(s.__next__())+":",re.match(".?\d\d\d","\t10086"))     
print(str(s.__next__())+":",re.match("(.*)\\bgood\\b(.*)","today is a good day")) 
print(str(s.__next__())+":",re.match(".*(\\bgood\\b).*","today is a good day").group(1)) 
print(str(s.__next__())+":",re.match("[123456789]","6这个真是一个悲伤的故事 "))       
print(str(s.__next__())+":",re.match("[0-9]","6这个真是一个悲伤的故事 "))       
print(str(s.__next__())+":",re.match("[a-z\s]+","this is good day"))                           #\s为匹配空格
print(str(s.__next__())+":",re.match("[a-z0-9A-Z王小明]","小this is good day")) 
print(str(s.__next__())+":",re.match("[\u4e00-\u9fa5]+","大幅的发生"))                          #汉字。匹配中文字符的正则表达式： [\u4e00-\u9fa5]

s = Seq(47) 
#1、一个正则表达式，只含有汉字、数字、字母、下划线不能以下划线开头和结尾：
#?!表示之后的字符串内容需要不匹配表达式才能成功，即字符串不能等于后边的内容
print(str(s.__next__())+":",re.match("^(?!_)(?!.*?_$)[a-zA-Z0-9_\u4e00-\u9fa5]+$","大幅的发生"))   
print(str(s.__next__())+":",re.match("我今年\d*岁了","我今年5岁了")) 
print(str(s.__next__())+":",re.match("我今年\d+岁了","我今年5岁了")) 
print(str(s.__next__())+":",re.match("我今年\d?岁了","我今年5岁了")) 
print(str(s.__next__())+":",re.match("我今年\d{0,10}岁了","我今年5岁了")) 

s = Seq(56) 
#字符转义
#print(str(s.__next__())+":",re.match("c:\\","c:\\a\\b"))     # error 报错，因为\\转义后就变成了\了 
print(str(s.__next__())+":",re.match("c:\\\\","c:\\a\\b"))    #正确 
print(str(s.__next__())+":",re.match(r"c:\\","c:\\a\\b"))     # 正确，在前面加“r”表示匹配的字符不进行转义，以后匹配符不要再写出上面的的转义了
print(str(s.__next__())+":",re.match(".*\\bliu\\b","i is liu fas fsa5 662 2a"))  # 注意为什么使用点  
print(str(s.__next__())+":",re.match(r".*\bliu","i is liu fas fsa5 662 2a"))   #结果同上      

#分组
s = Seq(63) 
print(str(s.__next__())+":",re.match("100|[1-9][0-9]|[0-9]","2"))            # 匹配100以内的数
print(str(s.__next__())+":",re.match("0|100|[1-9]?\d$","22"))                #[1-9]?\d$匹配的是1位数或2位数，不含0，因此加上0和100两组
print(str(s.__next__())+":",re.match("\d+(183|192|168)\.(li|wang|liu)","452168.wang").groups()) #groups()返回一个包含所有分组字符串的元组。

s = 'abc.|123'
s1 = r'abc\.\|123'
s2 = r'abc\1\3|123'
print(re.escape(s),re.escape(s1),re.escape(s2)) 

s = Seq(77) 
# re.search 扫描整个字符串并返回第一个成功的匹配，如果匹配失败search()就返回None。
# re.match方法与re.search方法的区别
# re.match只匹配字符串的开始，如果字符串开始不符合正则表达式， 则匹配失败，并返货None； 
# re.search匹配整个字符串， 直到找到一个匹配，如果整个字符串都没匹配到，则返回None。
print(str(s.__next__())+":",re.search("\d+","10086d0f8g6233fd234fdds23fddsf"))     
print(str(s.__next__())+":",re.search("\d?","10086d0f8g6233fd234fdds23fddsf"))         
print(str(s.__next__())+":",re.search("\d*","10086d0f8g6233fd234fdds23fddsf"))         
print(str(s.__next__())+":",re.search("\d{1,2}","10086d0f8g6233fd234fdds23fddsf"))        
print(str(s.__next__())+":",re.findall("\d{1,2}","10086d0f8g6233fd234fdds23fddsf"))       
print(str(s.__next__())+":",re.findall("[^\d]{1,2}","10086d0f8g6233fd234fdds23fddsf")) 
print(str(s.__next__())+":",re.search('4[^369]*[369]','24dfvea3142459').group())                #search匹配是从整体里找符合条件的
print(str(s.__next__())+":",re.findall('4[^369]*[369]','24dfvea3142459'))   
#实例: 匹配邮箱：首字母不能为_，中间可以为任意字符，@符号前可以为4-20个字符。邮箱前缀为163、qq等，后缀为com、cn等
print(str(s.__next__()+1)+":",re.match(r'^[a-zA-Z0-9]\w{3,19}@(163|263|sina|google|sohu|qq|myspace).(com|cn|edu|cx|net|cy|tr)','a_949978171@QQ.com',flags=re.I))

#实例：匹配电话号码
mylist = ['010-8989345','020-321532','0103425431','0111-3713456','03743713456']        #匹配显示   区号与号码
for i in mylist:
    a = re.match('(?P<G1>0[1-9][0-9]{1,2})-?(?P<G2>\d{6,8})',i)        #（）表示分组，分组的编码是从1开始,也可以自定义分组?P<G1>
    if a:
        print('95：区号：%s,号码：%s'%(a.group('G1'),a.group('G2')))    #表示分组1的内容 
    else:
        print('没有找到') 

s = Seq(99) 
#用空格分割
print(str(s.__next__())+":",re.split(r'\s+', 'a b   c'))
print(str(s.__next__())+":",re.split(r'([\s\,\|])+', 'a,b, c | d'))


'''
正则一般是用来匹配，比如电话号码和人匹配
'''

'''

re.match函数                            #match   ：re.match 尝试从字符串的起始位置匹配一个模式，如果不是起始位置
函数语法：
re.match(pattern, string, flags=0)


re.search函数                           #search ：re.search 扫描整个字符串并返回第一个成功的匹配。      
函数语法：
re.search(pattern, string, flags=0)


pattern 匹配的正则表达式
string  要匹配的字符串。
flags   标志位，用于控制正则表达式的匹配方式，如：是否区分大小写，多行匹配等等。参见：正则表达式修饰符 - 可选标志


pattern:
^   匹配字符串的开头
$  匹配字符串的末尾。
.   匹配任意字符，除了换行符，当re.DOTALL标记被指定时，则可以匹配包括换行符的任意字符。
[...]   用来表示一组字符,单独列出：[amk] 匹配 'a'，'m'或'k'
[^...]  不在[]中的字符：[^abc] 匹配除了a,b,c之外的字符。
re* 匹配0个或多个的表达式。
re+ 匹配1个或多个的表达式。
re? 匹配0个或1个由前面的正则表达式定义的片段，非贪婪方式
re{ n}  精确匹配 n 个前面表达式。例如， o{2} 不能匹配 "Bob" 中的 "o"，但是能匹配 "food" 中的两个 o。
re{ n,} 匹配 n 个前面表达式。例如， o{2,} 不能匹配"Bob"中的"o"，但能匹配 "foooood"中的所有 o。"o{1,}" 等价于 "o+"。"o{0,}" 则等价于 "o*"。
re{ n, m}   匹配 n 到 m 次由前面的正则表达式定义的片段，贪婪方式
a| b    匹配a或b
(re)    匹配括号内的表达式，也表示一个组
(?imx)  正则表达式包含三种可选标志：i, m, 或 x 。只影响括号中的区域。
(?-imx) 正则表达式关闭 i, m, 或 x 可选标志。只影响括号中的区域。
(?: re) 类似 (...), 但是不表示一个组
(?imx: re)  在括号中使用i, m, 或 x 可选标志
(?-imx: re) 在括号中不使用i, m, 或 x 可选标志
(?#...) 注释.
(?= re) 前向肯定界定符。如果所含正则表达式，以 ... 表示，在当前位置成功匹配时成功，否则失败。但一旦所含表达式已经尝试，匹配引擎根本没有提高；模式的剩余部分还要尝试界定符的右边。
(?! re) 前向否定界定符。与肯定界定符相反；当所含表达式不能在字符串当前位置匹配时成功
(?> re) 匹配的独立模式，省去回溯。
\w  匹配字母数字及下划线
\W  匹配非字母数字及下划线
\s  匹配任意空白字符，等价于 [\t\n\r\f].
\S  匹配任意非空字符
\d  匹配任意数字，等价于 [0-9].
\D  匹配任意非数字
\A  匹配字符串开始
\Z  匹配字符串结束，如果是存在换行，只匹配到换行前的结束字符串。
\z  匹配字符串结束
\G  匹配最后匹配完成的位置。
\b  匹配一个单词边界，也就是指单词和空格间的位置。例如， 'er\b' 可以匹配"never" 中的 'er'，但不能匹配 "verb" 中的 'er'。
\B  匹配非单词边界。'er\B' 能匹配 "verb" 中的 'er'，但不能匹配 "never" 中的 'er'。
\n, \t, 等.  匹配一个换行符。匹配一个制表符。等
\1...\9 匹配第n个分组的内容。
\10 匹配第n个分组的内容，如果它经匹配。否则指的是八进制字符码的表达式。


flags : 可选，表示匹配模式，比如忽略大小写，多行模式等，具体参数为：
re.I 忽略大小写
re.L 表示特殊字符集 \w, \W, \b, \B, \s, \S 依赖于当前环境
re.M 多行模式
re.S 即为 . 并且包括换行符在内的任意字符（. 不包括换行符）
re.U 表示特殊字符集 \w, \W, \b, \B, \d, \D, \s, \S 依赖于 Unicode 字符属性数据库
re.X 为了增加可读性，忽略空格和 # 后面的注释


正则表达式实例:
实例:           描述:
[Pp]ython        匹配 "Python" 或 "python"
rub[ye]          匹配 "ruby" 或 "rube"
[aeiou]          匹配中括号内的任意一个字母
[0-9]            匹配任何数字。类似于 [0123456789]
[a-z]            匹配任何小写字母
[A-Z]            匹配任何大写字母
[a-zA-Z0-9]     匹配任何字母及数字
[^aeiou]        除了aeiou字母以外的所有字符
[^0-9]          匹配除了数字外的字符

————————————————
版权声明：本文为CSDN博主「sui_yi123」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/sui_yi123/article/details/81875913

'''