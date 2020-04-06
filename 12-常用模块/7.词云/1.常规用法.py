import wordcloud
import sys
import os 

# 获取文件当前所在的目录，并返回完整文件全路径 
def realpath(filename):
    return os.path.join(os.path.dirname(os.path.realpath(__file__)), filename)

# 创建词云对象，赋值给w，现在w就表示了一个词云对象
w = wordcloud.WordCloud()
# 调用词云对象的generate方法，将文本传入
w.generate("Python and WordCloud")
# 将生成的词云保存为pywordcloud.png图片文件，保存出到当前文件夹中
w.to_file(realpath("img\pywordcloud.png"))
