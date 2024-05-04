def solution(n):
    divisorList = []
    for x in range(1, n + 1):
        if(n % x == 0) : divisorList.append(x)
        
    return sum(divisorList)