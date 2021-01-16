import os
print(os.path,os.path.abspath('.'),os.path.abspath('..'))
print(os.path.relpath(r'E:\\'))
print(os.getcwd())
print(os.curdir)

print(os.listdir(os.path.abspath('.')))

os.chdir('D:\\')

print('-'*40)

print(os.listdir(os.getcwd()))

#basename用法是去掉目录路径，单独返回文件名 
print(os.path.basename("C:/Users/top/PycharmProjects/untitled4/venv/a_4.py"))

#dirname：去掉文件名，单独返回目录路径 
print(os.path.dirname("C:/Users/top/PycharmProjects/untitled4/venv/a_4.py"))