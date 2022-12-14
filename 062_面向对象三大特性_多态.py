# _*_ coding : utf-8 _*_
# @Time: 2022/12/14 5:09 PM
# @Author : 张安然
# @File : '062_面向对象_多态
# @Project : python_space
class Animal:
    pass


class Dog(Animal):
    name = 'dog'

    def speak(self):
        print(self.name, '旺旺旺')


class Cat(Animal):
    name = 'cat'

    def speak(self):
        print(self.name, '喵喵喵')

    name = 'dog'


def make_noise(animal: Animal):
    animal.speak()


dog = Dog()
cat = Cat()

make_noise(dog)
make_noise(cat)


# 抽象类
class AC:
    def cool(self):
        """制冷"""
        pass

    def hot(self):
        """制热"""
        pass

    def swing(self):
        """吹风"""
        pass


class Midea_AC(AC):
    name = '美的空调'

    def cool(self):
        print(self.name, 'cool....')


class Gree_AC(AC):
    name = '格力空调'

    def cool(self):
        print(self.name, 'cool....')


def make_cool(ac: AC):
    ac.cool()


gree = Gree_AC()
midea = Midea_AC()
make_cool(gree)
make_cool(midea)
