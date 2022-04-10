# Create a dictionary

a = {
    1: 'a',
    2: 'b',
    '3': 'c'
}

#  key需為不可改變的數據類型ㄝ, ex: 不可為list，但可為tuple

l1 = ['a', 'b', 'c']
t1 = (1, 2, 3)
c = {
    t1: l1
}
print(c)

# 通過dict函數創建字典

d = dict()
print(d)

# 透過dict函數初始化一個字典
e = dict(a=1, b=2, c='a')
print(e)

# read dictionary

print(e['a'])

# dictionary can be edited
e['d'] = 123
print(e)

# 因為字典是可以被改變的，所以一個字典不可成為另一個字典的key

