import os
print(os.path,os.path.abspath('.'),os.path.abspath('..'))
print(os.path.relpath(r'E:\\100-航天智慧\\2-源码库\\'))
print(os.getcwd())
print(os.curdir)

print(os.listdir(os.path.abspath('.')))

os.chdir('D:\\')

print('-'*40)

print(os.listdir(os.getcwd()))