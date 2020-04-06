#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: Aerospace Shenzhou Intelligent System Technology Co., Ltd 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2020-04-05 15:42:09 
# @Remark: 人生苦短，我用python！
# 参考链接：https://blog.csdn.net/weixin_30596343/article/details/101925994?depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromBaidu-3&utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromBaidu-3

import jieba
import sys
import os 

# 获取文件当前所在的目录，并返回完整文件全路径 
def realpath(filename):
    return os.path.join(os.path.dirname(os.path.realpath(__file__)), filename)

# 注意到，古明地觉四个字被进行了切割，可以如果我想让它作为整体出现呢
# jieba分词会使用一个词典，根据词典里面的词进行分词，如果像人名之类的，不再jieba使用的词典里，那么分词就会出现不预期之内的结果
sentence = "古明地觉来自于东方地灵殿,是一个超级可爱的女孩"
print(jieba.lcut(sentence))  # ['古明', '地觉', '来自', '于', '东方', '地灵', '殿', ',', '是', '一个', '超级', '可爱', '的', '女孩']

jieba.load_userdict(realpath("自定义词典.txt"))
print(jieba.lcut(sentence))  # ['古明地觉', '来自', '于', '东方地灵殿', ',', '是', '一个', '超级', '可爱', '的', '女孩']
# 可以看到，在将我们自定义的词典load进去之后，就能分出我们想要的结果了
# 因为jieba使用词典里的单词，词性标注，词频等等来切割单词
# 但如果词不在里面的话，就不行了，因此我们可以自己定义告诉结巴，'古明地觉'和'东方地灵殿'都是一个整体，不要进行切割
 
# jieba分词中cut和lcut的区别
# jieba.cut生成的是一个生成器，generator，也就是可以通过for循环来取里面的每一个词。 
# word_list= [word for word in jieba.cut(text)]
# jieba.lcut 直接生成的就是一个list