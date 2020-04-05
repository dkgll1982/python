from pyecharts.charts import Bar
from pyecharts import options as opts
import sys
import os
# 内置主题类型可查看 pyecharts.globals.ThemeType
from pyecharts.globals import ThemeType
from pyecharts.commons.utils import JsCode

# 获取文件当前所在的目录，并返回完整文件全路径 
def realpath(filebame):
    return os.path.join(os.path.dirname(os.path.realpath(__file__)), filebame)


color_function = """
        function (params) {
            if (params.value > 0 && params.value < 50) {
                return 'green';
            } else if (params.value > 50 && params.value < 100) {
                return 'orange';
            }
            return 'red';
        }
        """

# V1 版本开始支持链式调用
# 你所看到的格式其实是 `black` 格式化以后的效果
# 可以执行 `pip install black` 下载使用
bar = (
    Bar(
        # 初始化配置项
        init_opts=opts.InitOpts(
            theme=ThemeType.VINTAGE,
            width="1400px",
            height="800px",
            # 动画效果
            animation_opts=opts.AnimationOpts(
                animation_delay=1000, animation_easing="elasticOut"
            )
        ),
    )
    .add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子", "避孕套", "口香糖"])
    .add_yaxis("商家A", [111, 20, 36, 10, 75, 90, 110, 75],
                # 系列配置项:此处采用自定义函数控制颜色
                itemstyle_opts = opts.ItemStyleOpts(color = JsCode(color_function),
                                                 # 图形透明度。支持从 0 到 1 的数字，为 0 时不绘制该图形。
                                                 opacity = 0.6)

               )
    .add_yaxis("商家B", [15, 10, 26, 30, 45, 120, 40, 46],
               itemstyle_opts=opts.ItemStyleOpts(color = "lightblue")
               )
    .add_yaxis("商家C", [35, 21, 46, 10, 63, 40, 120, 45],
               itemstyle_opts=opts.ItemStyleOpts(color = "pink")
               )
    .set_global_opts(title_opts = opts.TitleOpts(title="商家货物数量", subtitle="商家A(<50:绿,<100:黄,>100:红)"))
    # 或者直接使用字典参数
    # .set_global_opts(title_opts={"text": "主标题", "subtext": "副标题"})
)
bar.render(realpath("render.html"))

# 不习惯链式调用的开发者依旧可以单独调用方法
# bar = Bar()
# bar.add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
# bar.add_yaxis("商家A", [5, 20, 36, 10, 75, 90])
# bar.set_global_opts(title_opts=opts.TitleOpts(title="主标题", subtitle="副标题"))
# bar.render(realpath("render.html"))
