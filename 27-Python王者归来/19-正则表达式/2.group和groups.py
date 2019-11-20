import re

# group和groups是两个不同的函数。

# 一般，m.group(N) 返回第N组括号匹配的字符。
# 而m.group() == m.group(0) == 所有匹配的字符，与括号(用来分组的)无关，这个是API规定的。

# m.groups() 返回所有括号匹配的字符，为tuple格式。如果没有括号分组m.groups()就没有返回值
#m.groups() == (m.group(1), m.group(2), ...)

# 或者m.groups()[0] == m.group(1)，m.groups()[1] == m.group(2)

print(re.match(r"(\d?)(\d?)\1-\2", "121-2286"))     # *表示匹配1到多个字符
print(re.match(r"(\d?)(\d?)\1(-)\2", "121-221212"))
print(re.match(r"(\d?)(\d?)\1\2\1\2", "12121212"))
print(re.match(r"(\d?)(\d?)\2(-)\1\2\1\2", "122-121212"))
print(re.match(r"\d{3}\d{3}", "221221286").groups())  # 没有括号分组，返回元组为空()
print(re.match(r"(\d{3})(\d{3})", "221221286").groups())
print(re.match(r"(\d{3})\1", "221221286").groups())
print(re.match(r"(\d{3})(\1)", "221221286").groups())
print(re.match(r"<(a>)\w+(</)\1", "<a>这是一个正确的链接</A>", flags=re.I))
print(re.match(r"<(a>)\w+(</)\1", "<a>这是一个错误的链接</b>", flags=re.I))

# 如果整个字符串string都匹配RE表达式，就返回对应的match object，如果不匹配就返回None；
# 再次提示：返回长度为0与None的意义截然不同。
print(re.fullmatch(r"[a-zA-Z0-9-]+", "121-2286"))     # *表示匹配1到多个字符
