def solution(numLog):
    answer = ''
    for x in range(0, len(numLog) - 1):
        calc = numLog[x + 1] - numLog[x]
        if calc == 1:
            answer += 'w'
        elif calc == -1:
            answer += 's'
        elif calc == 10:
            answer += 'd'
        else : answer += 'a'
    return answer