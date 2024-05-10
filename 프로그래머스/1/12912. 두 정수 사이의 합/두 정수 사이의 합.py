def solution(a, b):
    step = 0
    if a < b : step = 1
    else : step = -1
    
    return sum(list(range(a, b + step, step)))