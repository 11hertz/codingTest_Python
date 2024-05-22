def solution(my_str, n):
    return [my_str[x : x + n] for x in range(0, len(my_str), n)]