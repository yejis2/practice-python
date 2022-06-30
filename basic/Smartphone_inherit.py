class Smartphone:
    def __init__(self, brand, price):
        self._brand = brand
        self._price = price

    def __str__(self):
        return f'str: {self._brand} - {self._price}'

class Galaxy(Smartphone):
    def __init__(self, brand, price, country):
        self._brand = brand
        self._price = price
        self._country = country

    def __str__(self):
        return f'str: {self.__class__.__name__} 스마트폰은 {self._brand}에서 출시되었고' \
               f', {self._country}에서 생산되었습니다. 가격은 {self._price}입니다.'


iphone = Smartphone('Iphone', 7000)
print(iphone)
galaxy = Galaxy('Galaxy', 5000, 'South Korea')
print(galaxy)