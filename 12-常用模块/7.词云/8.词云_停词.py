# 8号词云：《三国演义》词云（stopwords参数去除“曹操”和“孔明”两个词）
# B站专栏：同济子豪兄 2019-5-23

# 导入词云制作库wordcloud和中文分词库jieba
import jieba
import wordcloud
import sys
import os
# 导入imageio库中的imread函数，并用这个函数读取本地图片，作为词云形状图片
import imageio

# 获取文件当前所在的目录，并返回完整文件全路径
def realpath(filebame):
    return os.path.join(os.path.dirname(os.path.realpath(__file__)), filebame)

mk = imageio.imread(realpath("img\chinamap.jpg"))

# 构建并配置词云对象w，注意要加stopwords集合参数，将不想展示在词云中的词放在stopwords集合里，这里去掉“曹操”和“孔明”两个词
# 设置中文停词
stopwords = set('')
stopwords.update(['曹躁','孔明','玄德','将军'])
w = wordcloud.WordCloud(width=1000,
                        height=700,
                        background_color='white',
                        font_path='msyh.ttc',
                        mask=mk,
                        scale=15,
                        max_words = 200,        # 最多词个数
                        stopwords = stopwords)  # stopwords参数去除词

# 对来自外部文件的文本进行中文分词，得到string
f = open(realpath("三国演义.txt"), "r")
txt = f.read()
txtlist = jieba.lcut(txt)
string = " ".join(txtlist)

# 将string变量传入w的generate()方法，给词云输入文字
w.generate(string)

# 将词云图片导出到当前文件夹
w.to_file(realpath('img\output8-threekingdoms.png'))
