def solution(my_string, s, e):
    answer = ''.join(list(my_string[0 : s: 1])) + ''.join(reversed(list(my_string[s : e + 1: 1]))) + ''.join(list(my_string[e + 1::]))
    
    
    return answer