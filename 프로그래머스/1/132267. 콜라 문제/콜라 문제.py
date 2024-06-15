def solution(a, b, n):
    answer = 0;
    coke = n;
    
    while a <= coke:
        answer += int(coke / a) * b;
        res = coke % a;
        coke = int(coke / a) * b + res;
    
    return answer