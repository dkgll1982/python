# 2号词云：面朝大海，春暖花开
# B站专栏：同济子豪兄 2019-5-23 

import wordcloud
import sys
import os 

# 获取文件当前所在的目录，并返回完整文件全路径 
def realpath(filebame):
    return os.path.join(os.path.dirname(os.path.realpath(__file__)), filebame)

# 构建词云对象w，设置词云图片宽、高、字体、背景颜色等参数
w = wordcloud.WordCloud(width=1000,
                        height=700,
                        background_color='white',
                        font_path='msyh.ttc')

# 调用词云对象的generate方法，将文本传入
w.generate('从明天起，做一个幸福的人。喂马、劈柴，周游世界。从明天起，关心粮食和蔬菜。我有一所房子，面朝大海，春暖花开')

# 将生成的词云保存为output2-poem.png图片文件，保存到当前文件夹中
w.to_file(realpath('img\output2-poem.png'))

# 常用参数
# width 词云图片宽度，默认400像素
# height 词云图片高度 默认200像素
# background_color 词云图片的背景颜色，默认为黑色
# background_color='white'
# font_step 字号增大的步进间隔 默认1号
# font_path 指定字体路径 默认None，对于中文可用font_path='msyh.ttc'
# mini_font_size 最小字号 默认4号
# max_font_size 最大字号 根据高度自动调节
# max_words 最大词数 默认200
# stop_words 不显示的单词 stop_words={"python","java"}
# Scale 默认值1。值越大，图像密度越大越清晰
# prefer_horizontal：默认值0.90，浮点数类型。表示在水平如果不合适，就旋转为垂直方向，水平放置的词数占0.9？
# relative_scaling：默认值0.5，浮点型。设定按词频倒序排列，上一个词相对下一位词的大小倍数。有如下取值：“0”表示大小标准只参考频率排名，“1”如果词频是2倍，大小也是2倍
# mask 指定词云形状图片，默认为矩形
# 通过以下代码读入外部词云形状图片（需要先pip install imageio安装imageio）