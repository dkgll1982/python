# 2号词云：面朝大海，春暖花开
# B站专栏：同济子豪兄 2019-5-23 

import wordcloud
import sys
import os 

# 获取文件当前所在的目录，并返回完整文件全路径 
def realpath(filename):
    return os.path.join(os.path.dirname(os.path.realpath(__file__)), filename)

# 构建词云对象w，设置词云图片宽、高、字体、背景颜色等参数
w = wordcloud.WordCloud(width=1000,
                        height=700,
                        background_color='white',
                        font_path='msyh.ttc')

# 调用词云对象的generate方法，将文本传入
w.generate('从明天起，做一个幸福的人。喂马、劈柴，周游世界。从明天起，关心粮食和蔬菜。我有一所房子，面朝大海，春暖花开')

# 将生成的词云保存为output2-poem.png图片文件，保存到当前文件夹中
w.to_file(realpath('img\output2-poem.png'))

# 参数详解：
#     font_path：字体路径，就是绘制词云用的字体，比如monaco.ttf
#     width：输出的画布宽度，默认400像素
#     height：输出的画布宽度，默认200像素
#     margin：画布偏移，默认2像素
#     prefer_horizontal : 词语水平方向排版出现的频率，默认0.9，垂直方向出现概率0.1
#     mask：如果参数为空，则使用二维遮罩绘制词云。如果 mask 非空，设置的宽高值将
#           被忽略，遮罩形状被 mask，除全白（#FFFFFF）的部分将不会绘制，其余部分会用于绘制词云。
#           如：bg_pic = imread('读取一张图片.png')，背景图片的画布一定要设置为白色（#FFFFFF），
#           然后显示的形状为不是白色的其他颜色。可以用ps工具将自己要显示的形状复制到一个纯白色
#           的画布上再保存，就ok了。
#     scale：按照比例进行放大画布，如设置为1.5，则长和宽都是原来画布的1.5倍
#     color_func：生成新颜色的函数，如果为空，则使用 self.color_func
#     max_words：显示的词的最大个数
#     min_font_size：显示的最小字体大小
#     stopwords：需要屏蔽的词(字符串集合)，为空使用内置STOPWORDS
#     random_state：如果给出了一个随机对象，用作生成一个随机数
#     background_color：背景颜色，默认为黑色
#     max_font_size：显示的最大的字体大小
#     font_step：字体步长，如果步长大于1，会加快运算但是可能导致结果出现较大的误差
#     mode：当参数为"RGBA"，并且background_color不为空时，背景为透明。默认RGB
#     relative_scaling：词频和字体大小的关联性，默认5
#     regexp：使用正则表达式分隔输入的文本
#     collocations：是否包括两个词的搭配
#     colormap：给每个单词随机分配颜色，若指定color_func，则忽略该方法
#     normalize_plurals：是否删除尾随的词语 
    
#常用的几个方法：
#     fit_words(frequencies) //根据词频生成词云
#     generate(text) //根据文本生成词云
#     generate_from_frequencies(frequencies[, ...]) #根据词频生成词云
#     generate_from_text(text) #根据文本生成词云
#     process_text(text) #将长文本分词并去除屏蔽词
#     （此处指英语，中文分词还是需要自己用别的库先行实现，使用上面的 fit_words(frequencies) ）
#     recolor([random_state, color_func, colormap]) #对现有输出重新着色。重新上色会比重新生成整个词云快很多。
#     to_array() #转化为 numpy array
#     to_file(filename) #输出到文件

# 作者：coder_pig
# 链接：http://www.imooc.com/article/50612?block_id=tuijian_wz
# 来源：慕课网
# 本文原创发布于慕课网 ，转载请注明出处，谢谢合作