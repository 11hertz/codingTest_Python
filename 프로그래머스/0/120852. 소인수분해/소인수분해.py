def solution(n):
    answer = []
    count = 2
    
    while(True):
        if n % count == 0 : 
            answer.append(count)
            n = n // count
        else : count += 1
        if n == 1 : break
        
    
    return sorted(list(set(answer)))