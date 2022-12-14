# _*_ coding : utf-8 _*_
# @Time: 2022/12/8 2:53 PM
# @Author : 张安然
# @File : '011_文件的读写
# @Project : python_space

import json

# f = open('data.json', 'w')

s = 'hello'
# 覆盖写入
# f.write((s+'\n')*5)
# 追加写入 'a'
# f = open('data.json', 'a')

# 默认一字节一字节的读
f = open('data.json', 'r')
# r = f.read()
# print(r)
# 一行一行读.每次只能读取一行
# rl = f.readline()
# print("readline:", rl)


# readlines
# rls = f.readlines()
# print("readlines():", rls)

# 序列化
# f = open('data.json', 'w')
r = open('data.json', 'r')
dog = {
    "name": 'tome',
    "age": 19,
    "color": "yellow"
}
# 写入序列化后的字符串
# 方式一
# f.write(json.dumps(dog))
# 方式二
# json.dump(dog, f)

# 反序列化
# 方式一 loads
# content = r.read()
# print(json.loads(content))
# 方式二 load
content = json.load(r)
print(content)
r.close()

# 循环读取每一行
rf = open('data.json', 'r', encoding='utf-8')
for line in rf:
    print('循环读取', line)
rf.close()

# with open 语法,不需要手动关闭
with open('data.json', 'r', encoding='utf-8') as f:
    for line in f:
        print('循环读取', line)
