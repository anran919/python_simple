# _*_ coding : utf-8 _*_
# @Time: 2022/12/8 4:03 PM
# @Author : 张安然
# @File : '012_异常
# @Project : python_space
try:
    r = open('data.txt', 'r')
    print(r.read())
    r.close()
except FileNotFoundError:
    print("文件不存在")

