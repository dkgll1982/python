import jieba
import jieba.posseg
import sys
import os 

# 获取文件当前所在的目录，并返回完整文件全路径 
def realpath(filename):
    return os.path.join(os.path.dirname(os.path.realpath(__file__)), filename)

txt = open(realpath("三国演义.txt"), "r").read()
 
counts = {}                 # 通过键值对的形式存储词语及其出现的次数
 
for key,tag in jieba.posseg.lcut(txt):
    if  len(key) > 1 and tag == 'nr':           # 单个词语不计算在内,nr表示人名
        counts[key] = counts.get(key, 0) + 1    # 遍历所有词语，每出现一次其对应的值加 1 
        
items = list(counts.items())                    #将键值对转换成列表
items.sort(key=lambda x: x[1], reverse=True)    # 根据词语出现的次数进行从大到小排序

for i in range(15):
    word, count = items[i]
    print("{0:<5}{1:>5}".format(word, count))