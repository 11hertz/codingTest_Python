def solution(price):
    discountedPrice = [0.8, 0.9, 0.95]
    if price >= 500000:
        return int(price * discountedPrice[0])
    elif price >= 300000:
        return int(price * discountedPrice[1])
    elif price >= 100000:
        return int(price * discountedPrice[2])
    else:
        return int(price)