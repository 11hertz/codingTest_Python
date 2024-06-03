def solution(t, p):
    answer = 0

    for x in range(len(t)):
        num = t[x : len(p) + x]
        if len(num) == len(p) and int(p) >= int(num): answer += 1

    return answer