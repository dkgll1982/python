# 5号词云：乡村振兴战略中央文件（词云）
# B站专栏：同济子豪兄 2019-5-23

# 导入词云制作库wordcloud和中文分词库jieba
import jieba
import wordcloud 
import sys
import os 

# 获取文件当前所在的目录，并返回完整文件全路径 
def realpath(filebame):
    return os.path.join(os.path.dirname(os.path.realpath(__file__)), filebame)

# 对来自外部文件的文本进行中文分词，得到string
f = open(realpath('关于实施乡村振兴战略的意见.txt'),encoding='utf-8')
txt = f.read()

# 构建并配置词云对象w
w = wordcloud.WordCloud(width=1000,
                        height=700,
                        background_color='white',
                        font_path='msyh.ttc')
 
txtlist = jieba.lcut(txt)
string = " ".join(txtlist)

# 将string变量传入w的generate()方法，给词云输入文字
w.generate(string)

# 将词云图片导出到当前文件夹
w.to_file(realpath('img\output5-village.png'))