# 6号词云：乡村振兴战略中央文件（五角星形状）
# B站专栏：同济子豪兄 2019-5-23

# 导入词云制作库wordcloud和中文分词库jieba
import jieba
import wordcloud
import sys
import os 
# 导入imageio库中的imread函数，并用这个函数读取本地图片，作为词云形状图片
import imageio

# 获取文件当前所在的目录，并返回完整文件全路径 
def realpath(filename):
    return os.path.join(os.path.dirname(os.path.realpath(__file__)), filename)

mk = imageio.imread(realpath("img\wujiaoxing.jpg"))
w = wordcloud.WordCloud(mask=mk)

# 构建并配置词云对象w，注意要加scale参数，提高清晰度
w = wordcloud.WordCloud(width=1000,
                        height=700,
                        background_color='white',
                        font_path='msyh.ttc',
                        prefer_horizontal = 0.1,
                        max_words=100,                  #最大词数 默认200
                        stopwords={"python","java"},    #不显示的单词  
                        mask=mk,                        #面具模板， 指定词云形状图片，默认为矩形
                        scale=25)                       #Scale 默认值1。值越大，图像密度越大越清晰

# 对来自外部文件的文本进行中文分词，得到string
f = open(realpath('关于实施乡村振兴战略的意见.txt'),encoding='utf-8')
txt = f.read()
txtlist = jieba.lcut(txt)
string = " ".join(txtlist)

# 将string变量传入w的generate()方法，给词云输入文字
w.generate(string)

# 将词云图片导出到当前文件夹
w.to_file(realpath('img\output6-village.png'))