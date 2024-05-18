def solution(i, j, k):
    totalStr = ''
    
    for x in range(i, j + 1):
        totalStr += str(x)
    
    count = 0
    for x in range(len(totalStr)):
        if totalStr[x] == str(k): count += 1
        
    return count