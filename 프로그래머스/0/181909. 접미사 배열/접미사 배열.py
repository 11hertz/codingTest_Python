def solution(my_string):
    answer = []
    for x in range(len(my_string)):
        answer.append(my_string[x:])
    answer.sort()
    return answer