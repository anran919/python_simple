# _*_ coding : utf-8 _*_
# @Time: 2022/12/14 4:47 PM
# @Author : 张安然
# @File : '06_类型注解_union联合类型
# @Project : python_space

from typing import Union, List, Dict

# 混合类型.使用union表示可以有多种类型
m_list: List[Union[str, int, bool]] = [1, '联合', False]

print(m_list[0])

# 字典混合类型.使用union表示可以有多种类型
m_dict: Dict[str, Union[str, int, bool]] = {'name': 'jack', 'age': 19, 'is_show': False}

print(m_dict['name'])


# 联合类型注解在函数中使用

def add_list(a_list: List[Union[str, int, bool]], value: Union[str, int, bool]) -> None:
    return a_list.append(value)


add_list(m_list, '哈哈哈')
print('add_list', m_list)
