# _*_ coding : utf-8 _*_
# @Time: 2022/12/14 2:26 PM
# @Author : 张安然
# @File : '056_魔术方法
# @Project : python_space


class Student:
    def __init__(self, name, gender, nationality, native_place) -> None:
        self.name = name
        self.gender = gender
        self.nationality = nationality
        self.native_place = native_place

    def __str__(self):
        # str 魔术方法
        return f'Student : name ={self.name} gender = {self.gender} nationality = {self.nationality}' \
               f' native_place = {self.native_place} '

    def __lt__(self, other):
        # lt 小于,魔术方法
        return self.gender < other.gender

    def __le__(self, other):
        # le 小于等于,魔术方法
        return self.gender >= other.gender

    def __eq__(self, other):
        # eq ,比较相等的魔术方法
        return self.name == other.name


s1 = Student('魔术方法', 1, 'Python', 'Python')
s2 = Student('重写比较方法', 2, 'lt', '比较大小')

print('魔术方法 lt', s1)
print('魔术方法 le', s1 >= s2)
print('魔术方法 eq', s1 == s2)
