from pyecharts import options as opts
from pyecharts.charts import Bar
from pyecharts.faker import Faker
import sys,os  
import random

#获取文件当前所在的目录，并返回完整文件全路径
def realpath(filebame):
    return os.path.join(os.path.dirname(os.path.realpath(__file__)),filebame)  

c = (
    Bar()
    .add_xaxis(Faker.days_attrs)
    .add_yaxis("商家A", Faker.days_values)
    .add_yaxis("商家B", [random.randint(0, 50) for _ in range(30)])
    .set_global_opts(
        title_opts=opts.TitleOpts(title="Bar-DataZoom（slider-水平）"),
        datazoom_opts=opts.DataZoomOpts(),
    )
    .render(realpath("bar_datazoom_slider.html"))
)