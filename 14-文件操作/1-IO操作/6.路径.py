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

print('*'*40) 

print('***获取当前目录***')
print(os.getcwd())
print(os.path.abspath(os.path.dirname(__file__)))

print('***获取上级目录***')
print(os.path.abspath(os.path.dirname(os.path.dirname(__file__))))
print(os.path.abspath(os.path.dirname(os.getcwd())))
print(os.path.abspath(os.path.join(os.getcwd(), "..")))

print('***获取上上级目录***')
print(os.path.abspath(os.path.join(os.getcwd(), "../..")))