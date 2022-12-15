# _*_ coding : utf-8 _*_
# @Time: 2022/12/15 11:50 AM
# @Author : 张安然
# @File : '069_设计模式_工厂模式
# @Project : python_space

class Person:
    pass


class Student(Person):
    pass


class Teacher(Person):
    pass


class Worker(Person):
    pass


class PersonFactory:
    def get_person(self, type: str):
        if type == 's':
            return Student()
        elif type == 't':
            return Teacher()
        elif type == 'w':
            return Worker()
        else:
            return Person()


factory = PersonFactory()
w = factory.get_person('w')
print(w)
s = factory.get_person('s')
print(s)
