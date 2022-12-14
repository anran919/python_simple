# _*_ coding : utf-8 _*_
# @Time: 2022/12/13 11:32 AM
# @Author : 张安然
# @File : '050_集合
# @Project : python_space

# 定义 set
no_st = {1, 1, 2}
no_st2 = {2, 4, 5}
card_set = set()
print(no_st)
print(type(card_set))

# 添加
card_set.add('F')
print(card_set)

# 移除
no_st.remove(2)
print(no_st)

# 清空集合
# no_st.clear()

# 取2个集合的差集
print(no_st.difference(no_st2))


# 合并
print(no_st.union(no_st2))
