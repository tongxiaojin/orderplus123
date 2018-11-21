""" dict 的学习 """
#dict 是key:value的形式，且key 必须是不可变的类型，int,str,tuple,value 可以是任意类型。

a = {1:'a', 2:'b', 3:'c', 4:'d'}
print(type(a))

b ={'A':'applle'}
print(b['A'])

c = {(1,2):[3,4]}
print(c[(1,2)])

#key 不能重复
d = {1:'apple',2:'pear', 1:'banana'}
print(d)
#value可以是任意值
e = {1:2,'a':'apple',(3,4):(5,6),'b':[7,8,9],3:{'people', 'pet'},9:{'t':888}}
print(type(e))
print(e[9])
print(e[9]['t'])

#空dict
{}
print(type({}))
print(type(set()))
