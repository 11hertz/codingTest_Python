def solution(order):
    answer = 0
    threesixnine = ['3', '6', '9']
    for x in list(str(order)) :
        if x in threesixnine : answer += 1
    return answer