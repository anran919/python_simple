# _*_ coding : utf-8 _*_
# @Time: 2022/12/14 2:44 PM
# @Author : 张安然
# @File : '057_面向对象三大特性
# @Project : python_space

# 私有方法和私有属性
# 变量和方法前加__


class Student:

    def __init__(self, name, age) -> None:
        super().__init__()
        self.name = name
        self.__age = age

    def favorite(self):
        print('我的爱好是,不能随便告诉你', self.__age)


s = Student('张三', 999)
# __age为私有, 直接调用__age获取不到
# print(s.__age)
s.favorite()
