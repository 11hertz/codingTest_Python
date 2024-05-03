def solution(a, b, c):
    equals = len(set([a, b, c]))
    if equals == 1:
        return (a + b + c) * (a ** 2 + b ** 2 + c ** 2) * (a ** 3 + b ** 3 + c ** 3)
    elif equals == 2:
        return (a + b + c) * (a ** 2 + b ** 2 + c ** 2)
    elif equals == 3:
        return a + b + c
    