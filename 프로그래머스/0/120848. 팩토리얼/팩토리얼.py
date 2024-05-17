def solution(n):
    sum = 1
    count = 1
    
    while True:
        count += 1
        if sum > n : break
        sum *= count
        
    return count - 2