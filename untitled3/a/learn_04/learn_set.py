"""set的学习"""
#set是一个无序且不重复的元素集合
a = {1, 2, 3}
b = {2, 1, 4}
c = {3, 2, 1}
d = {'orange', 'peach', 1, ('rose','daisy')}
#set 求差集
print(a-b)
print(b-a)
print(a-c)
#set 求并集
print(a | b)
print(a | c)
print(c | d)
#set 求交集
print(a & b)
print(c & d)
print(a & c)

#set常用的方法
print(type(d))
print(len(d))
print(max(a))
print(min(a))
x ={'a', 'b', 'c'}
print(max(x))
print(ord('c'))

#判断元素是否为此set的成员
print(1 in a)
print(2 not in b)

# 空的set
c = set()
print(type(c))




