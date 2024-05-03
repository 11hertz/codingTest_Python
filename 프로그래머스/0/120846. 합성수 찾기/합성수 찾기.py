def solution(n):
    answer = 0
    
    def getDivisor(num):
        count = 0
        for x in range(1, num + 1):
            if num % x == 0 : count += 1
        return count
    
    for x in range(1, n + 1):
        if getDivisor(x) >= 3 : answer += 1
        
    return answer