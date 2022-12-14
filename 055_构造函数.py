# _*_ coding : utf-8 _*_
# @Time: 2022/12/14 2:24 PM
# @Author : 张安然
# @File : '055_构造函数
# @Project : python_space


class Student:
    def __init__(self, name, gender, nationality, native_place) -> None:
        super().__init__()
        self.name = name
        self.gender = gender
        self.nationality = nationality
        self.native_place = native_place


# 使用构造方法
# name, gender, nationality, native_place
s2 = Student("吕德华", 1, '中国', '广东')
print(s2.name)
