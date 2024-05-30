def solution(price, money, count):
    totalMoney = sum(x * price for x in range(1, count + 1))
    return 0 if totalMoney - money <= 0 else totalMoney - money

