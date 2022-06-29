# 문제 6-3
#
# 아래의 Stock 클래스에 대해 2개의 인스턴스를 생성했을 때 클래스와 a와 b 인스턴스의 네임스페이스를 그려보세요.
class Stock:
    market = "kospi"

a = Stock()
b = Stock()

# Stock(class object) {'market': "kospi"}
# a(instance), b(instance)


# 문제 6-4
#
# 문제 6-3의 코드에서 추가로 아래와 같은 코드를 수행했을 때 '???'로 표시된 부분의 결괏값을 적어보세요.

print(a.market)             #kospi
# ???
print(b.market)             #kospi
# ???
print(Stock.market)         #kospi
# ???
a.market = "kosdaq"
b.market = "nasdaq"
print(a.market)             #kosdaq
# ???
print(b.market)             #nasdaq
# ???
print(Stock.market)         #kospi
# ???


# 문제 6-5
#
# 문제 6-3, 문제 6-4의 코드가 모두 수행된 후의 Stock 클래스, a 인스턴스와 b 인스턴스의 네임스페이스를 그려보세요.

# Stock(class object) {'market': "kospi"}
# a(instance) {'market': "kosdaq"}
# , b(instance) {'market': "nasdaq"}