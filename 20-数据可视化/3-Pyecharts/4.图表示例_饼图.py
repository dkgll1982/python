#导入柱状图-Bar
from pyecharts import options as opts
from pyecharts.charts import Pie
from pyecharts.faker import Faker 
import sys,os  

#获取文件当前所在的目录，并返回完整文件全路径
def realpath(filename):
    return os.path.join(os.path.dirname(os.path.realpath(__file__)),filename)   

c = (
    Pie()
    .add(
        "",
        [list(z) for z in zip(Faker.choose(), Faker.values())],
        center=["35%", "50%"],
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title="Pie-调整位置"),
        legend_opts=opts.LegendOpts(pos_left="15%"),
    )
    .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
    .render(realpath("pie_position.html"))
)
