# _*_ coding : utf-8 _*_
# @Time: 2022/12/14 10:41 PM
# @Author : 张安然
# @File : '066_闭包
# @Project : python_space

# 内部函数使用外部变量

def outer(lang):
    def inner(msg):
        # 需要修改外部函数传入的变量需要使用nonlocal修饰,不需要修改则不需要修饰
        nonlocal lang
        lang = f'##{lang}##'
        print(f'<{lang}>{msg}<{lang}>')

    return inner


o = outer('Java')
o("你好啊")
o = outer('Python')
o("你好啊")


def account_create(init_account=0):
    def atm(num, deposit=True):
        # 需要修改外部函数传入的变量需要使用nonlocal修饰,不需要修改则不需要修饰
        nonlocal init_account
        if deposit:
            init_account += num
            print(f'存入了{num}元')
        else:
            init_account -= num
            print(f'取出了{num}元')

    return atm


fn = account_create(100)
fn(333, True)
fn(333, False)
