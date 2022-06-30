# 다중 상속
# 예제 1

class Person:
    def greeting(self):
        print('안녕하세요.')

class University:
    def manage_credit(self):
        print('학점관리')

class Undergraduate(Person, University):
    def study(self):
        print('공부하기')

# person1 = Undergraduate()
# person1.greeting()
# person1.manage_credit()
# person1.study()


# 예제 2

class Person:
    def sleep(self):
        print('sleep')

class Student(Person):
    def study(self):
        print('Study hard')

    def play(self):
        print('play with friends')

class Worker(Person):
    def work(self):
        print('work hard')

    def play(self):
        print('drinks alone')

# 다중 상속
class PartTimer(Student, Worker):
    def find_job(self):
        print('Find a job')


parttimer1 = PartTimer()
parttimer1.study()
parttimer1.work()
parttimer1.play()                   # 부모 클래스에 동일한 메소드나 속성이 있을 경우 왼쪽에서부터 우선권 부여

