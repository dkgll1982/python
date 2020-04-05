import wordcloud
import sys
import os 

# 获取文件当前所在的目录，并返回完整文件全路径 
def realpath(filebame):
    return os.path.join(os.path.dirname(os.path.realpath(__file__)), filebame)

w = wordcloud.WordCloud()
w.generate("Python and WordCloud")
w.to_file(realpath("pywordcloud.png"))
