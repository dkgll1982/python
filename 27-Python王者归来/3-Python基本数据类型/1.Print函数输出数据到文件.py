fsstream1 = open(r'C:\Users\dkgll\Desktop\1.txt',mode='w')
print('test output',file=fsstream1)
fsstream1.close()

fsstream2 = open(r'C:\Users\dkgll\Desktop\1.txt',mode='a')
print('append output',file=fsstream2)
fsstream2.close()

import sys 
#在Python 3+中，__builtin__模块被命名为builtins
for x in dir(sys.modules['builtins']):
    print(x)