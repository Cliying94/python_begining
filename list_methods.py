list1 = [9, 1, -4, 3, 11, 987, 3, 3]

print('list的長度為', len(list1))

print('list中的最大值為', max(list1))

print('list中的最小值為', min(list1))

print('在list中3這個元素一共出現了{}次'.format(list1.count(3)))

list2 = ['a', 'c', 'd']
print('list2-', list2)
list2.append('e')
print('list2=', list2)

list2.insert(1, 'b')
print('list2=', list2)

list2.remove('b')
print('list2=', list2)

list2[0] = '1'
print('list2=', list2)

a = '1234'
# a[0] = 'a'  #TypeError: 'str' object does not support item assignment
print('a=', a)
a = 'abc'
print('a=', a)


list3 = [1, 2, 3]
list3.reverse()
print(list3)

list4 = [9, 1, -4, 3, 7, 11, 3]
list4.sort()
print('list4=', list4)
list4.sort(reverse=True)
print('list4=', list4)
