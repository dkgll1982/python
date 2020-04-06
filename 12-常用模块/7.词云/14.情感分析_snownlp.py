#中文文本分析库snownlp
#snownlp的语料库是淘宝等电商网站的评论，所以对购物类的文本情感分析准确度很高。
import snownlp 

print('\n')
text1 = '中华民族伟大复兴'
print('{:-^50}'.format('测试文本：'+text1))
s = snownlp.SnowNLP(text1)
print('\n')
print('情感分析',s.sentiments)
print('\n')
print('中文分词',s.words)
print('\n')
print('转成拼音',s.pinyin)
print('\n')
print('词频',s.tf)
print('\n')
print('提取三个关键词',s.keywords(3))
print('\n')

text2 = '快递慢到死，客服态度不好，退款！'
print('{:-^50}'.format('测试文本：'+text2))
s = snownlp.SnowNLP(text2)
print('\n')
print('情感分析',s.sentiments)
print('\n')
print('中文分词',s.words)
print('\n')
print('转成拼音',s.pinyin)
print('\n')
print('词频',s.tf)
print('\n')
print('提取三个关键词',s.keywords(3))