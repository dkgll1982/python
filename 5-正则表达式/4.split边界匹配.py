import re

print(re.match(r'\d+?','1234'))   #1
print(re.match(r'\d*?','1234'))     
print(re.match(r'\d??','1234'))

#\b，\B是单词边界,不匹配任何实际字符,所以是看不到的;\B是\b的非(补)。 
#\b：表示字母数字与非字母数字的边界,非字母数字与字母数字的边界。 
#\B：表示字母数字与(非非)字母数字的边界,非字母数字与非字母数字的边界。
print(re.split(r'pyc#\B','1pycthon pyc#5 2pyc# 342 pyc1py2py4 pyp3 3pyc# pyc'))
print(re.split(r'pyc\B','1pycthon pyc#5 2pyc# 342 pyc1py2py4 pyp3 3pyc# pyc'))
print(re.split(r'\b123\b','123 ==123!! abc123.123.123abc.123'))
print(re.split(r'123\b','123 ==123!! abc123.123.123abc.123'))
print(re.split(r'123\b', '==123!! abc123. 123. 123abc. 123')) 
print(re.split(r'123\b', '==123!! abc123. 123\tabc 123'))
print(re.split(r'\b123\b', '123 ==123!! abc123.123.123abc.123'))
print(re.split(r'\b123=\b', '==123!! abc123,123,123=abc,123')) 
print(re.split(r'\b123a\b', '==123!! abc123,123,123a\nbc,123')) 
print(re.split(r'\b123=\b', '==123!! abc123,123,123==abc,123')) 
# \B
print(re.split(r'pyc\B', '1pycthon py5 2pyc342 pyc1py2pyr pyp3 3pyc# pyc'))
print(re.split(r'py=\B', '1py=cthon py5 2py=342 py==1py2py4 pyp3 3py- pyabc'))  
print(re.split(r'\b123=\B', '==123!! abc123,123,123==abc,123'))
