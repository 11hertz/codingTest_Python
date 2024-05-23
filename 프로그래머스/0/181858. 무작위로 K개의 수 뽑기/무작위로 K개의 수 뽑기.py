def solution(arr, k):
    answer = [-1 for x in range(k)]
    setArr = []
    
    for x in arr :
        if x not in setArr : setArr.append(x)
    
    setArr = setArr[:k]

    for idx, val in enumerate(setArr):
        answer[idx] = val
        
    return answer