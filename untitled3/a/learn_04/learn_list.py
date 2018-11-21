"""list的学习,要获取序列长的某个元素，就用下标；要获取某个子集，就用切片"""

c = [1, 2, 3, 4, 5]
d = ['aaa', 'bbb', 'ccc']
e = [1, 'hello', [3, 'world']]
print(type(c), type(d), type(e))
print(len(c))
f = c[0]
print(f)
m = c[1:4:2]
print(m)
n = e[1]
print(n)
t = e[1:3]
print(t)
o = e[2][1]
print(o)
print(e[1:3][0] + ' ' + e[1:3][1][1])

""" list 也可以逆向取值"""
u =["apple", 'pear', 8]
print(u[2:3])
print(u[-1:])
print(u[1:3])
print(u[-2:])

# 空的list
print(type([]))

# list 是可以改变的
p =[1, 2, 3]
p[1] = 5
print(p)
p.append(4)
print(p)

#list 的元素可以是任意类型。
print(type([1,'AA', [1,2], (1,), {1,3}, {1:"1"}]))







