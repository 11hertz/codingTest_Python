def solution(intStrs, k, s, l):
    answer = []
    
    for x in intStrs:
        slicedStr = int(x[s : s + l])
        if slicedStr > k : answer.append(slicedStr)
    
    return answer