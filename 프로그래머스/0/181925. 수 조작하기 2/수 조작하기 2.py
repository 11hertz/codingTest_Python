def solution(numLog):
    answer = ''
    for x in range(0, len(numLog) - 1):
        if numLog[x + 1] - numLog[x] == 1:
            answer += 'w'
        elif numLog[x + 1] - numLog[x] == -1:
            answer += 's'
        elif numLog[x + 1] - numLog[x] == 10:
            answer += 'd'
        else : answer += 'a'
    return answer