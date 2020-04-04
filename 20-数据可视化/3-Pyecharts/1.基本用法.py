from pyecharts.charts import Bar 
from pyecharts.render import make_snapshot
# 使用 snapshot-selenium 渲染图片
from snapshot_selenium import snapshot
import sys,os  

#获取文件当前所在的目录，并返回完整文件全路径
def realpath(filebame):
    return os.path.join(os.path.dirname(os.path.realpath(__file__)),filebame)  
  
bar = Bar()
bar.add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
bar.add_yaxis("商家A", [5, 20, 36, 10, 75, 90])
# render 会生成本地 HTML 文件，默认会在当前目录生成 render.html 文件
# 也可以传入路径参数，如 bar.render("mycharts.html")
bar.render(realpath("render.html"))
make_snapshot(snapshot, bar.render(), realpath("bar.png"))