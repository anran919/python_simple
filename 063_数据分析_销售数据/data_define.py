# _*_ coding : utf-8 _*_
# @Time: 2022/12/14 5:53 PM
# @Author : 张安然
# @File : 'data_define
# @Project : python_space
"""数据处理的的类"""


class Record:
    def __init__(self, date, order_id, money, province):
        self.date = date
        self.order_id = order_id
        self.money = money
        self.province = province

    def __str__(self):
        return f'Record : {self.date}, {self.order_id}, {self.money}, {self.province},'
