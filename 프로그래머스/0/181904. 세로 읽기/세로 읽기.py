def solution(my_string, m, c):
    answer = ''
    for x in range(c - 1, len(my_string)):
        if x % m - c + 1 == 0 : answer += my_string[x]
    return answer