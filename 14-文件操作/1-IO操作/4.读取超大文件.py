#参考链接：https://blog.csdn.net/qq_38882327/article/details/89207026
#参考链接：https://www.cnblogs.com/wenBlog/p/8441231.html

import time

print("开始处理...")
start = time.time()
#file = r'14-文件操作\1-IO操作\测试.txt'
file = r'backup\stus.txt'

# with open(file,'r', encoding='UTF-8') as f:
#     for line in f:
#         print(line)

with open(file, 'rb') as f: 	#rb方式最快
	for line in f:li = line.strip();lin = str(li).lstrip("b");print(lin)

end = time.time()
shi = end - start
print("已完成！总耗时%s秒！" % shi)