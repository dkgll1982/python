from fontTools.ttLib import TTFont
import re
 
font = TTFont(r'12-常用模块\ZWgWmrNR.ttf')  #打开本地的ttf文件
# 保存为xml文件：
font.saveXML('local_fonts.xml')

#获取cmap节点code与name值映射, 返回为字典：
bestcmap = font['cmap'].getBestCmap()
print(bestcmap) 
#获取getGlyphOrder节点的name值，返回为列表：
print(font.getGlyphNames(),font.getGlyphOrder())

print('----------------------------------------------------------------')
 
# font = TTFont(r'C:\Users\dkgll\Downloads\fonteditor (2).ttf')  #打开本地的ttf文件
# bestcmap = font['cmap'].getBestCmap()
# print('黑体:',bestcmap)
 

font = TTFont(r'12-常用模块\xNmnLMXp.ttf')  #打开本地的ttf文件
bestcmap = font['cmap'].getBestCmap()
print(bestcmap)

print('----------------------------------------------------------------')

font = TTFont(r'c:\windows\Fonts\teamviewer14.otf')  #打开本地的ttf文件
bestcmap = font['cmap'].getBestCmap()
print(bestcmap)

print('----------------------------------------------------------------')

font = TTFont(r'c:\windows\Fonts\iqiyi_logov5.ttf')  #打开本地的ttf文件
bestcmap = font['cmap'].getBestCmap()
print(bestcmap)

# 链接：http://fontstore.baidu.com/static/editor/doc/index.html
# 字形信息
# 一个ttf字体文件包含多个字形，单个字形包含以下信息：

# 字形轮廓，单个轮廓由线段和二次贝塞尔曲线组成，多个轮廓组成一个字形。
# unicode，码元，一个字形可以对应多个unicode码元，但一个unicode码元只能对应一个字形
# name，字形名称
# leftSideBearing，左边距，字形左侧的留白
# rightSideBearing，右边距，字形右侧的留白