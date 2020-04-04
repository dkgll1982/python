from pyecharts import options as opts
from pyecharts.charts import Pie
from pyecharts.faker import Faker
import sys,os  

#获取文件当前所在的目录，并返回完整文件全路径
def realpath(filebame):
    return os.path.join(os.path.dirname(os.path.realpath(__file__)),filebame)   

c = (
    Pie()
    .add(
        "",
        [
            list(z)
            for z in zip(
                Faker.choose() + Faker.choose() + Faker.choose(),
                Faker.values() + Faker.values() + Faker.values(),
            )
        ],
        center=["40%", "50%"],
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title="Pie-Legend 滚动"),
        legend_opts=opts.LegendOpts(type_="scroll", pos_left="80%", orient="vertical"),
    )
    .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
    .render(realpath("pie_scroll_legend.html"))
)
