# #multistring
# print("=" * 50)
# print("My Program")
# print("=" * 50)
#
# #Indexing & Slicing String
# #0 <= a < 3
a = " Life is too short, You need Python "
# print(a[0:3])
#
# b = a[0] + a[1] + a[2] + a[3]
# print(b)
#
# #formatting
# num = 10
# day = "three"
# print("I ate %d apples. So I was sick for %s days." %(num, day))
#
# print("%-10sjane" %'hi')
# print("%10.4f" %3.42134234)

## 문자열 관련 함수
print(a.count('e'))
print(a.find('e'))
print(a.find('k'))
#index 함수는 find 와 달리 없는 문자 찾을 때 오류남
#print(a.index('k'))

#a,b,c,d
b = ','
print(b.join('abcd'))
print(a.upper())
print(a.lower())
print(a.lstrip())
print(a.rstrip())
print(a.replace("Life", "Your leg"))
print(a.split())
print("I eat {0} apples." .format(3))
print("I ate {number} apples. So I was sick for {day} days." .format(number = 10, day = 3))

#왼쪽, 오른쪽, 가운데 정렬
print("{0:<50}" .format(a))
print("{0:>50}" .format(a))
print("{0:^50}" .format(a))
#공백 채우기
print("{0:=^50}" .format(a))
print("{0:!^50}" .format(a))