def solution(n):
    answer = [[0 for y in range(n)] for x in range(n)]
    
    for x in range(n):
        for y in range(n):
            if(x == y) : answer[x][y] = 1
    
    return answer