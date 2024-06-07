import math
def solution(n):
    answer = 0
    
    def isPrime(x):
        for i in range (2, int(math.sqrt(x) + 1)):
            if x % i == 0:
                return False
        return True
                    
    for x in range(2, n + 1):
        if isPrime(x) : answer += 1
    
    return answer