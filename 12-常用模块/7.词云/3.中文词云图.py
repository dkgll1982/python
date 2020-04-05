from wordcloud import WordCloud
import jieba
import matplotlib.pyplot as plt
import sys
import os

# 获取文件当前所在的目录，并返回完整文件全路径 
def realpath(filebame):
    return os.path.join(os.path.dirname(os.path.realpath(__file__)), filebame) 

text = ''
with open(realpath('lagou-job1000-ai-details.txt'), 'r',encoding='utf8') as f:
    text = f.read()
 
words = jieba.lcut(text)
cuted = ' '.join(words)
print(cuted[:100])

fontpath = r'font\SourceHanSerifSC-Regular.otf'

wc = WordCloud(font_path=fontpath,      # 设置字体
               background_color="white",# 背景颜色
               max_words=1000,          # 词云显示的最大词数
               max_font_size=500,       # 字体最大值
               min_font_size=20,        # 字体最小值
               random_state=42,         # 随机数
               collocations=False,      # 避免重复单词
               # 图像宽高，字间距，需要配合下面的plt.figure(dpi=xx)放缩才有效
               width=1600,
               height=1200,
               margin=10,
               )
wc.generate(cuted)

plt.figure(dpi=100)       # 通过这里可以放大或缩小
plt.imshow(wc, interpolation='catrom', vmax=1000)
plt.axis("off")             # 隐藏坐标
