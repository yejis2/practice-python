s1 = set([1, 2, 3])
print(s1)

s2 = set("Hello")
print(s2)

list1 = list(s1)
print(list1)

t1 = tuple(s1)
print(t1)
print(t1[0])

s3 = set([1, 2, 3, 4, 5, 6])
s4 = set([4, 5, 6, 7, 8, 9])

#교집합
print(s3 & s4)
print(s3.intersection(s4))

#합집합
print(s3 | s4)
print(s3.union(s4))

#차집합
print(s3 - s4)
print(s3.difference(s4))
print(s4 - s3)
print(s4.difference(s3))

#값 한개 혹은 여러개 추가
s1.add(4)
s1.update([4, 5, 6])
print(s1)

s1.remove(2)
print(s1)