def solution(n):
    answer = [[0] * n for x in range(n)]
    
    for x in range(n) : answer[x][x] = 1
    
    return answer