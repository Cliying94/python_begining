name = 'python'
age = 27

# 印出 "我是python,今年27歲了"

new_str = "我是" + name + "," + "今年" + str(age) + "歲了"
new_str1 = '我是%s,今年%d歲了' % (name, age)
new_str2 = "我是{},今年{}歲了".format(name, age)
new_str3 = "我是{name},今年{age}歲了".format(
    name='aaa', age="bbb"
)
new_str4 = f"我是{name},今年{age}歲了"

print(new_str)
print(new_str1)
print(new_str2)
print(new_str3)
print(new_str4)

# ---------- Quiz1
print("Quiz1")
x = "hello world"
y = x.split(' ')
print(f'{y},{type(y)}')

z = ' '.join(["hello", "world"])
print(z)

# ---------- Quiz1
print("Quiz2")

s1 = "hello-world"
l1 = s1.split("-")
print(f'{l1}')

s2 = 'A new version of    python'
l2 = s2.split()

print(f'{l2}')  # 默認無參數就會按照空格(不計數)
