class Smartphone:
    """
    Smartphone Class
    """
    # 클래스 변수
    smartphone_count = 0

    def __init__(self, brand, infomations):
        #인스턴스 변수
        self._brand = brand
        self._infomations = infomations
        Smartphone.smartphone_count += 1

    def __str__(self):
        return f'str : {self._brand} - {self._infomations}'

    def __repr__(self):
        return f'repr : {self._brand} - {self._infomations}'

    def detail_info(self):
        print(f'Current Id : {id(self)}')
        print(f'Smartphone Detail Info : {self._brand} {self._infomations.get("price")}')

    def get_price(self):
        return f'Before Smartphone Price -> brand: {self._brand}' \
               f', price: {self._infomations.get("price")}'

    def get_price_culc(self):
        return f'After Smartphone Price -> brand: {self._brand}' \
               f', price: {self._infomations.get("price")* Smartphone.price_per_raise}'

    @classmethod
    def raise_price(cls, per):
        if per <= 1:
            print('Please Enter 1 or More')
            return
        cls.price_per_raise = per
        return 'Succeed! Price increased.'

    @staticmethod
    def is_iphone(inst):
        if inst._brand == 'Iphone':
            return f'OK! This Smartphone is {inst._brand}.'
        return 'Sorry. This Smartphone is not Iphone.'

    def __del__(self):
        Smartphone.smartphone_count -= 1


Smartphone1 = Smartphone('Iphone', {'color': 'White', 'price': 10000})
Smartphone2 = Smartphone('Galaxy', {'color': 'Black', 'price': 8000})

# print(Smartphone.__dict__)
# print(Smartphone1.__dict__)
# print(Smartphone2.__dict__)
# print(dir(Smartphone1))
#
# print(Smartphone1.smartphone_count)
# print(Smartphone.smartphone_count)

# 기본 정보
print(Smartphone1)
print(Smartphone2)

Smartphone1.detail_info()
Smartphone2.detail_info()

print(Smartphone1.get_price())
print(Smartphone2.get_price())

# 가격 인상(클래스 메소드 미사용)
# 직접 접근(좋지 않음)
Smartphone.price_per_raise = 1.2

# 가격 정보
print(Smartphone1.get_price_culc())
print(Smartphone2.get_price_culc())

def is_iphone(inst):
    if inst._brand == 'Iphone':
        return f'OK! This Smartphone is {inst._brand}.'
    return 'Sorry. This Smartphone is not Iphone.'

print(is_iphone(Smartphone2))

print('Static: ', Smartphone.is_iphone(Smartphone1))
print('Static: ', Smartphone.is_iphone(Smartphone2))