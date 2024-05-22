def solution(left, right):
    answer = 0
    
    def countFactors(num):
        count = 0
        for x in range(1, num + 1):
            if num % x == 0 : count += 1 
        return count
    
    for x in range(left, right + 1):
        target = countFactors(x)
        if target % 2 == 0 : answer += x
        else : answer -= x
    
    return answer