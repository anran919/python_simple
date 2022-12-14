# _*_ coding : utf-8 _*_
# @Time: 2022/12/14 10:42 AM
# @Author : 张安然
# @File : '054_类的基本概念
# @Project : python_space
from typing import Type


# 创建学生类
class Student:
    name = None
    gender = None
    nationality = None
    native_place = None

    def say_hi(self, msg):
        print(f'hi ,大家好,我是 {self.name},{msg}')


# 创建学生对象
s1 = Student()

# 赋值
s1.name = '加州招待所'
s1.gender = 1
s1.nationality = 'US'
s1.native_place = '加利福利亚'

# 获取对象的信息

print('111', s1.native_place)
s1.say_hi(msg=None)
s1.say_hi(msg="12333")
