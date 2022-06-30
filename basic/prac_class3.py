# 예제 1
class Book:
    def __init__(self, bookName):
        self.name = bookName
        print("객체가 생성되었습니다.")
        print("책의 이름은 " + bookName + "입니다.")

# objectBook = Book("뇌를 자극하는 파이썬")


#############################################################################
# 예제 2
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def aboutMe(self):
        print("제 이름은 " + self.name + "이며, " + str(self.age) + "살 입니다.")


adult = Person('홍길동', 20)
# adult.aboutMe()


#############################################################################
# 예제 3
class IceCream:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        print(name + "의 가격은 " + str(price) + "원 입니다.")

    def __del__(self):
        print(self.name + " 객체가 소멸합니다.")


# ice_cream1 = IceCream('부라보콘', 1000)
# del ice_cream1
# ice_cream = IceCream('구구콘', 2000)

#############################################################################
# 예제 4
from time import ctime


class Student:
    # 생성자
    def __init__(self, name = 'noname'):
        print('{0}에 객체가 생성되었습니다.' .format(ctime()))
        self.name = name

    schoolname = 'SeoKyeong'
    def setName(self, name):
        self.name = name
    def getName(self):
        return self.name

    def __del__(self):
        print('{0}에 객체가 소멸되었습니다.' .format(ctime()))

# stu1 = Student("yeji")
# stu2 = Student()
#
# print("stu1의 이름: {0}" .format(stu1.getName()))
# print("stu2의 이름: {0}" .format(stu2.getName()))
#
# del stu1
# del stu2


#############################################################################
# 예제 4
class BusinessCard:
    def __init__(self, name, email, addr):
        self.name = name
        self.email = email
        self.addr = addr

    def print_info(self):
        print("-------------------------------")
        print("Name       : ", self.name)
        print("Email      : ", self.email)
        print("address    : ", self.addr)
        print("-------------------------------")


member1 = BusinessCard("yeji kim", "yejikim@test.com", "Seoul")
member1.print_info()
