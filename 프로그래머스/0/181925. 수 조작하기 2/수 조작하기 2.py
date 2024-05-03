def solution(numLog):
    answer = ''
    for x in range(0, len(numLog) - 1):
        diff = numLog[x + 1] - numLog[x]
        if diff == 1:
            answer += 'w'
        elif diff == -1:
            answer += 's'
        elif diff == 10:
            answer += 'd'
        else : answer += 'a'
    return answer