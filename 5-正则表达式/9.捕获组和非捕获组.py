import re

#(?=...)
# 前向肯定断言。如果当前包含的正则表达式（这里以 ... 表示）在当前位置成功匹配，则代表成功，否则失败。
# 一旦该部分正则表达式被匹配引擎尝试过，就不会继续进行匹配了；剩下的模式在此断言开始的地方继续尝试。
#(?!...)
#前向否定断言。这跟前向肯定断言相反（不匹配则表示成功，匹配表示失败）。
print(re.match('([abc])+', 'abcabc').groups())
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
