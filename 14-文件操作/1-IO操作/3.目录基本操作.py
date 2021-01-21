import os,time
import shutil

# 查看当前目录的绝对路径:
print(os.path.abspath('.'))
#'/Users/michael'
# 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来:
print(os.path.join(r'backup', 'testdir'))
#'/Users/michael/testdir'

dir = r'backup\txt' 
# 然后创建一个目录:
if not os.path.exists(dir): 
    os.mkdir(r'backup\txt')
else:
    print('%s已存在！'%dir)

# os.makedirs（）函数创建多级目录。
subdir = r'backup\txt\subtxt\subsubtxt'
if not os.path.exists(subdir): 
    os.makedirs(subdir)
else:
    print('%s已存在！'%subdir) 

time.sleep(2)

# 删掉一个目录:
#os.rmdir(r'backup\txt')
# 注意：要删除的目录必须是空目录，,
#os.removedirs(path)   #删除空文件夹
shutil.rmtree(os.path.join(dir,'subtxt'))

print('*'*40)

def get_file_path(root_path,file_list,dir_list):
    #获取该目录下所有的文件名称和目录名称
    dir_or_files = os.listdir(root_path)
    for dir_file in dir_or_files:
        #获取目录或者文件的路径
        dir_file_path = os.path.join(root_path,dir_file)
        #判断该路径为文件还是路径
        if os.path.isdir(dir_file_path):
            dir_list.append(dir_file_path)
            #递归获取所有文件和目录的路径
            get_file_path(dir_file_path,file_list,dir_list)
        else:
            file_list.append(dir_file_path)
 
if __name__ == "__main__":
    #根目录路径
    root_path = r"backup"
    #用来存放所有的文件路径
    file_list = []
    #用来存放所有的目录路径
    dir_list = []
    get_file_path(root_path,file_list,dir_list)
    print(file_list)
    print(dir_list)