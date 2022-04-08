tuple1 = (9, 1, -4, 3, 7, 11, 3)

print('tuple1的長度 =', len(tuple1))

print('tuple1裡的最大值 =', max(tuple1))

print('tuple1裡的最小值 =', min(tuple1))

print('tuple1裡3這個元素共出現了{}次'.format(tuple1.count(3)))

#  任何改變element都不能再tuple中執行，包含但不限於revserse()/sort()等

tuple1.index(9)