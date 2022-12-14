# _*_ coding : utf-8 _*_
# @Time: 2022/12/14 4:38 PM
# @Author : 张安然
# @File : '60_类型注解_函数(方法)的类型注解
# @Project : python_space


def add(x: int, y: int) -> int:
    # 对形参注解,和对返回值注解
    return x + y


print(add(1, 2))
