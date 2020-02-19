import re

#‘.’用于匹配除换行符（\n）之外的所有字符。
#‘^’用于匹配字符串的开始，即行首。
#‘$’用于匹配字符串的末尾（末尾如果有换行符\n，就匹配\n前面的那个字符），即行尾。
#‘*’用于将前面的模式匹配0次或多次（贪婪模式，即尽可能多的匹配）
#‘+’用于将前面的模式匹配1次或多次（贪婪模式）
#‘？’用于将前面的模式匹配0次或1次（贪婪模式）
#‘{m,n}’用于将前面的模式匹配m次到n次（贪婪模式），即最小匹配m次，最大匹配n次。
#‘*？，+？，？？’即上面三种特殊字符的非贪婪模式（尽可能少的匹配）。
s1=re.findall(r'\D+\d+','abc123456');print(1,s1)              #1次或多次,结果为:['abc123456']
s2=re.findall(r'\D+\d+?','abc123456');print(2,s2)             #结果为:['abc1']

s2=re.findall(r'\D+\d*','abc123456');print(3,s2)              #0次或多次,结果为:['abc123456']
s2=re.findall(r'\D+\d*?','abc123456');print(4,s2)             #结果为:['abc']

s2=re.findall(r'\D+\d{2,4}','abc123456');print(5,s2)          #m次到n次,结果为:['abc1234']
s2=re.findall(r'\D+\d{2,4}?','abc123456',re.I);print(6,s2)    #结果为:['abc12']

s2=re.findall(r'\D+\d?','abc123456',re.I);print(7,s2)         #0次或1次,结果为:['abc1']
s2=re.findall(r'\D+\d??','abc123456',re.I);print(8,s2)        #结果为:['abc'] 

#\b：表示字母数字与非字母数字（如！，空格，逗号之类）的边界，      非字母数字与字母数字的边界。
print(re.split(r'123\b','123!! abc123. 123. 123abc. 123'))    #['', '!! abc', '. ', '. 123abc. ', '']  
print(re.findall(r'\d+\b','010-22-22-334--32324'))

s = '<html><head><title>Title</title></head></html>'
print(re.findall('<[\w]+>', s))

print(re.findall(r'(?P<name>\d+)','987java678abc891abe2345stu2454dy'))#结果是:['987', '678', '891', '2345', '2454']
print(re.findall(r'(?P<name>\D+)','java678abc891abe2345stu2454dy'))

print(re.findall(r'[\s|\S]+?','ads fvsdd gfdgd fgdg d'))
print(re.findall(r'\S+','ads fvsdd gfdgd fgdg d'))