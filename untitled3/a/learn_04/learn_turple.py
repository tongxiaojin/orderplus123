""" tuple学习 """
# tuple 的操作
a = (1, 'apple', [1, 'pear'], (2, 3))
print(type(a))
print(len(a))
print(a[1])
print(a[2:4])
print(a[-1: ])
b = (1,)
print(type(b))

# tuple 是不可改变的

a[1] = 'banana'
print(a)

