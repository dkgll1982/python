import re
# 参考链接：https://www.cnblogs.com/cute/p/9186208.html
# 参考链接：https://www.cnblogs.com/zsvslx/p/10536893.html

# (?=pattern)前向肯定断言的语法|(?<=pattern)后向肯定断言的语法：
# 需要注意的是，如果在匹配的过程中，需要同时用到前向肯定断言和后向肯定断言，
# 那么必须将后向肯定断言写在正则语句的前面，前向肯定断言写在正则语句的后面，表示后向肯定模式之后，前行肯定模式之前。
s1='''char *a="hello world"; char b='c'; /* this is comment */ int c=1; /* t
his is multiline comment */'''
print(re.findall( r'(?<=/\*).+?(?=\*/)' , s1 ,re.M|re.S))

#(?=...)
# 前向肯定断言。如果当前包含的正则表达式（这里以 ... 表示）在当前位置成功匹配，则代表成功，否则失败。
# 一旦该部分正则表达式被匹配引擎尝试过，就不会继续进行匹配了；剩下的模式在此断言开始的地方继续尝试。
#(?!...)
#前向否定断言。这跟前向肯定断言相反（不匹配则表示成功，匹配表示失败）。

#提取不以数字开头不以py结尾的文件
print('----',re.findall(r'^(?!\d+).+?\..*$(?<!py$)','test.p2y'))

print(re.match('[abc]*', 'abcabc') )
print(re.match('([abc])', 'abcabc').groups())
print(re.match('([abc])+', 'abcabcd').groups())
print(re.match('(?:[abc])+', 'abcabc').groups())
print(re.findall(r'a(?=bcd)', 'aebcd'))
print(re.findall(r'a(?!bcd)', 'aebcd'))
print(re.findall(r'a(?=bcd)', 'abcd')),
print(re.findall(r'a(bcd)', 'abcd'))

print(re.findall(r'(\d{3,4}-)?(\d{7,8})', '020-82228888,0357-4227865')) 
print(re.findall(r'(\d{3,4}-)?\d{7,8}', '020-82228888,0357-4227865')) 
print(re.findall(r'(?:\d{3,4}-)?\d{7,8}', '020-82228888,0357-4227865')) 
print(re.findall(r'(?:\d{3,4}-)?\d{7,8}','020-82228888,4227865'))
print(re.findall(r'.*[.](?!bat$|exe$).*$', 'dgdg.exe')) 
