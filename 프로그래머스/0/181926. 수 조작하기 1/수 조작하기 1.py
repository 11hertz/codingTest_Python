def solution(n, control):
    answer = n
    dir = { 'w' : 1, 's' : -1, 'd' : 10, 'a' : -10}
    for x in control:
        answer += dir[x]
    return answer