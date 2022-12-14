# _*_ coding : utf-8 _*_
# @Time: 2022/12/14 2:44 PM
# @Author : 张安然
# @File : '059_类型注解_变量的类型注解
# @Project : python_space


from typing import List, Set, Tuple, Dict

# 变量类型注解
i: int = 10
ss: str = 'hello'

# 容器直接
books: list = ['三国演义', '水浒传']
my_set: set = {1, 2, 4}
my_tuple: tuple = ('他', '她', '它')
my_dict: dict = {"name": "tom", "age": 18}

# 容器详细注解
m_list: List[str] = ['三国演义', '水浒传']
m_set: Set[int] = {1, 2, 3}
m_tuple: Tuple[str, str, str] = ('他', '她', '它')
m_dict: Dict[str, int] = {"price": 999, "age": 18}

# 在注释中注解

c_list = [1, 'm']  # type: int ,str


def f1(data: set):
    # 变量类型注解
    print(data.append('122'))


class Student:
    msg: str = 'world'

    def say(self):
        print('hellow', self.msg)
