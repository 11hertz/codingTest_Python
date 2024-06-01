def solution(balls, share):
    def fact(num):
        res = 1
        for x in range(1, num + 1):
            res *= x
        return res
    
    return fact(balls) / (fact(balls - share) * fact(share))