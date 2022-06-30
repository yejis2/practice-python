# 추상 클래스

from abc import *

class AbstractCountry(metaclass=ABCMeta):
    name = '국가명'
    population = '인구'
    capital = '수도'

    def show(self):
        print('국가 클래스의 메소드입니다.')

    @abstractmethod
    def show_capital(self):
        super().show_capital()

class Korea(AbstractCountry):
    def __init__(self, name, population, capital):
        self.name = name
        self.population = population
        self.capital = capital

    def show_name(self):
        print("국가    이름:", self.name)

    def show_capital(self):
        print("{0} 수도: {1}" .format(self.name, self.capital))


a = Korea("대한민국", 50000000, "서울")
a.show_name()
a.show_capital()

