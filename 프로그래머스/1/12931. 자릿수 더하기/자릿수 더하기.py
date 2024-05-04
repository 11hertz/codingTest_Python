def solution(n):
    answer = 0

    while(True) :
        answer += n % 10
        n //= 10
        if n == 0 : break
        
    return answer