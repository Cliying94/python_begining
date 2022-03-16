a = [1, 2, 3]

b = [1, 'abc', 2.0, ['a', 'b', 'c']]

print(a)
print(b)

print(a[0], a[1])  # result: 1 2, default seq = ' ' and default end = ''
print(a[0], a[1], sep='-', end='**\n')

# sublist
print(b[1], b[2])
c = b[1:3]  # [index:quantity = number - 1]
print(c, type(c))

s = 'abcedf'
print(s[1:3], s[-1])
print(b[-1])
