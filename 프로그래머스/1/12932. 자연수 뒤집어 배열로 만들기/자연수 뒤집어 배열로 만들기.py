def solution(n):
    answer = []
    
    while(True) :
        answer.append(n % 10)
        n //= 10
        if n == 0 : break
    
    return answer