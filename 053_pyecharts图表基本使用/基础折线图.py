# _*_ coding : utf-8 _*_
# @Time: 2022/12/13 10:40 PM
# @Author : 张安然
# @File : '基础折线图
# @Project : python_space

from pyecharts.charts import Line
from pyecharts.options import TitleOpts,LegendOpts,ToolboxOpts,VisualMapOpts

if __name__ == '__main__':
    line = Line()
    line.set_global_opts(
        # 表头
        title_opts=TitleOpts(title='DGP折线图', pos_left='center',pos_top= '10% '),
        # 图例
        legend_opts=LegendOpts(is_show=True),
        toolbox_opts=ToolboxOpts(is_show=True),
        visualmap_opts=VisualMapOpts(is_show=True)
    )
    line.add_xaxis(["中国", '美国', '俄罗斯'])
    line.add_yaxis("GDP", [30, 20, 10])
    line.render(path='基础折线图.html')
