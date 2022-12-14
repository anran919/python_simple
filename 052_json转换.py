# _*_ coding : utf-8 _*_
# @Time: 2022/12/13 9:59 PM
# @Author : 张安然
# @File : '052_json转换
# @Project : python_space

import json

t_list = [{'name': '张大仙', 'age': 19}, {'name': '王大锤', 'age': 3}, {'name': '吕德华', 'age': 99}]

j_list = json.dumps(t_list, ensure_ascii=False)
print(j_list, type(j_list))

t_list2 = json.loads(j_list)
print(t_list2, type(t_list2))
