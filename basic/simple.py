# languages = ['python', 'perl', 'c', 'java']
#
# for lang in languages:
#     if lang in ['python', 'perl']:
#         print("%6s need interpreter" % lang)
#     elif lang in ['c', 'java']:
#         print("%6s need compiler" % lang)
#     else:
#         print("should not reach here")
#
# multiline = """
# Life is too short
# You need python\b
# """
#
# print(multiline)
#
# a = [1, 2, 3, 4]
# while a:
#     print(a.pop())
#
# if[]:
#     print("True")
# else:
#     print("False")
#
# if[1, 2, 3]:
#     print("True")
# else:
#     print("False")

import sys

print(sys.getrefcount(3))

a = 3
print(sys.getrefcount(3))
b = 3
print(sys.getrefcount(3))
c = 3
print(sys.getrefcount(3))

# a, b = 'python', 'life'           #튜플 형식으로 변수 생성
[a, b] = ['python', 'life']         #리스트 형식으로 변수 생성
# a = b = 'python'

print(a, b)

a, b = b, a
print(a, b)

#메모리에 생성된 변수 삭제
del(a)
del(b)