a = [1, 2, 3]
a[2] = 4            #[1, 2, 4]
a[1:2] = ['a', 'b', 'c']    #[1, 'a', 'b', 'c', 4]
a[1:3] =[]          #[1, 'c', 4]
del a[1]            #[1, 4]

a.append(2)
print(a)

a.sort()
a.reverse()          #a = [4, 2, 1]
print(a.index(4))    #0

a.insert(0, 4)       #a = [5, 4, 2, 1]
a.remove(4)
print(a)
a.pop(1)
print(a)

a.extend([5, 6])
print(a)             #[4, 1, 5, 6]

#리스트 복사(1)
# b = a
# a[1] = 2
# print(a)
# print(b)

#리스트 복사(2)
# b = a[:]
# a[1] = 2
# print(a)
# print(b)

#리스트 복사(3) == (2)
from copy import copy
b = copy(a)
a[1] = 2
print(a)
print(b)

print(b is a)

#tuple
t1 = (1, 2, 'a', 'b')
print("=====tuple=====")
print(t1)
