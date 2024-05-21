def solution(emergency):
    answer = [1 for x in range(len(emergency))]
    
    for x in range(len(emergency)):
        for y in range(x, len(emergency)):
            if x == y : continue
            if emergency[x] > emergency[y] : answer[y] += 1
            else : answer[x] += 1

    return answer