def solution(arr, flag):
    answer = []
    
    for x in range(len(flag)):
        if flag[x] : answer += [arr[x]] * (arr[x] * 2)
        else :
            for _ in range(arr[x]) : answer.pop()
    
    return answer