from pyecharts.charts import Bar
from pyecharts import options as opts
import os,sys,random

# 获取文件当前所在的目录，并返回完整文件全路径 
def realpath(filename):
    return os.path.join(os.path.dirname(os.path.realpath(__file__)), filename) 

key = ['小米','三星','苹果','华为','oppo','vivo','一加','其他']
bar = (
    Bar()
    .add_xaxis(key)
    .add_yaxis("一季度", [random.randint(1,150) for x in range(8)],)
    .add_yaxis("二季度", [random.randint(1,150) for x in range(8)],)
    .add_yaxis("三季度", [111, 20, 36, 10, 75, 90, 110, 75],) 
    .set_global_opts(title_opts = opts.TitleOpts(title="出货量", subtitle="指标(<50:绿,<100:黄,>100:红)"))
)
bar.render(realpath("mobile.html"))

