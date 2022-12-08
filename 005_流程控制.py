# _*_ coding : utf-8 _*_
# @Time: 2022/12/8 9:37 AM
# @Author : 张安然
# @File : '005_流程控制
# @Project : python_space

if True:
    print('hello')

if 19 > 18:
    print('python')

age = input('输入你的年龄!')
if int(age) > 18:
    print('你可以去网吧了')
else:
    print('好好上学吧你')

if int(age) <= 1:
    print('你是小孩子!')
elif int(age) <= 6:
    print('你可以上小学了')
elif int(age) <= 15:
    print('你在上初中了')
else:
    print('我懒得写了,高中或者大学吧')

s = 'python'
for i in s:
    print(i)

for i in range(5):
    print(i)

for i in range(1, 5):
    print(i)
# 三个参数分别是(起始,结束,步长)
for i in range(1, 10, 2):
    print(i)

# 遍历数组
authors = ['伍佰', '李宗盛', '王菲']
for v in authors:
    print(v)

# 遍历下标
# 获取数组长度
print(len(authors))
for i in range(len(authors)):
    print(authors[i])
