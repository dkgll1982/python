# 9号词云：哈姆雷特（勾勒轮廓线）
# B站专栏：同济子豪兄 2019-5-23

# 导入词云制作库wordcloud
import wordcloud
import sys
import os
# 导入imageio库中的imread函数，并用这个函数读取本地图片，作为词云形状图片
import imageio

# 获取文件当前所在的目录，并返回完整文件全路径
def realpath(filebame):
    return os.path.join(os.path.dirname(os.path.realpath(__file__)), filebame)
 
# 将外部文件包含的文本保存在string变量中
string = open(realpath('hamlet.txt'),'r',encoding='utf-8').read()

mk = imageio.imread(realpath(r"img\alice.png"))

# 构建词云对象w，注意增加参数contour_width和contour_color设置轮廓宽度和颜色
w = wordcloud.WordCloud(background_color="white",
                        font_path='msyh.ttc',
                        mask=mk,
                        contour_width=1,
                        contour_color='steelblue')

# # 将string变量传入w的generate()方法，给词云输入文字
w.generate(string)

# 将词云图片导出到当前文件夹
w.to_file(realpath("img\output9-contour.png"))