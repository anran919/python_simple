# _*_ coding : utf-8 _*_
# @Time: 2022/12/14 5:53 PM
# @Author : 张安然
# @File : '__init__.py
# @Project : python_space
from typing import List

from pyecharts.charts import Bar
from pyecharts.globals import ThemeType
from pyecharts.options import TitleOpts, LabelOpts, InitOpts

from file_define import TextFileReader, JsonFileReader
from data_define import Record

# 处理数据

if __name__ == '__main__':
    tfr = TextFileReader("../json/063_销售数据分析2月.text")
    record_list_2: List[Record] = tfr.read_file()
    trj = JsonFileReader("../json/063_销售数据分析1月.json")
    record_list_1: List[Record] = trj.read_file()
    all_list: List[Record] = record_list_1 + record_list_2
    data_dict = {}
    for record in all_list:
        if record.date in data_dict.keys():
            data_dict[record.date] += record.money
        else:
            data_dict[record.date] = record.money
    print(data_dict)
    bar = Bar(init_opts=InitOpts(theme=ThemeType.LIGHT))
    bar.add_xaxis(list(data_dict.keys()))
    bar.add_yaxis('销售额', list(data_dict.values()), label_opts=LabelOpts(is_show=False))
    bar.set_global_opts(
        title_opts=TitleOpts(title='每日销售额')
    )
    bar.render("每日销售份额柱状图.html")
