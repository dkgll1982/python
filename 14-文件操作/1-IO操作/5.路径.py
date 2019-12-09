import os
print(os.path,os.path.abspath('.'),os.path.abspath('..'))
print(os.path.relpath(r'E:\\'))
print(os.getcwd())
print(os.curdir)

print(os.listdir(os.path.abspath('.')))

os.chdir('D:\\')

print('-'*40)

print(os.listdir(os.getcwd()))