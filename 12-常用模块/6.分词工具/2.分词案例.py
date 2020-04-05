import jieba
 
# 可以使用jieba.cut进行分词
sentence = "失去恋人所带来的苦痛远远超过了他的承受范围"
"""
函数大致如下
jieba.cut(sentence, cut_all=False, HMM=True)
sentence：分词的句子
cut_all:是否使用全模式，默认是False，表示精准模式
HMM：是否使用隐藏马尔科夫模型，默认为True
"""
seg = jieba.cut(sentence)
# 得到的seg是一个生成器
print(list(seg))  # ['失去', '恋人', '所', '带来', '的', '苦痛', '远远', '超过', '了', '他', '的', '承受', '范围']
# 可以看到分的还是蛮准确的
 
# 如果使用全模式呢
seg = jieba.cut(sentence, cut_all=True)
print(list(seg))  # ['失去', '恋人', '所', '带来', '的', '苦痛', '远远', '远超过', '超过', '了', '他', '的', '承受', '范围']
# 默认一般都是用精准模式
# 除了jieba.cut之外还有一个jieba.lcut，两者之间功能一样，只不过后者会直接返回一个列表
# 搜索引擎模式
seg = jieba.cut_for_search(sentence)
print(list(seg))  # ['失去', '恋人', '所', '带来', '的', '苦痛', '远远', '超过', '了', '他', '的', '承受', '范围']
# 由于句子比较简单，导致和cut的结果是类似的
# 同理也有lcut_for_search，也是直接返回一个列表