import jieba.posseg

sentence = "古明地觉是一个可爱的女孩子"
# 这里的tag表示单词的词性，nr表示人名
jieba.add_word("古明地觉", tag="nr")
for k, v in jieba.posseg.lcut(sentence):
    print(k, v)
"""
古明地觉 nr
是 v
一个 m
可爱 v
的 uj
女孩子 n
"""
# n: 名词  ns: 地名  vn: 名动词  v: 动词  nr: 人名，不在这里面的会被过滤掉